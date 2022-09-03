import asyncio
from doctest import Example
from pyppeteer import launch

async def launch_ptppeteer_with_url(url:str, width:int, height:int, is_mobile:bool):
    options = {
        "headless": True,
        "args": [
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-dev-shm-usage",
            "--disable-accelerated-2d-canvas",
            "--no-zygote",
            "--disable-gpu",
        ],
    }
    browser = await launch(
        handleSIGINT=False, handleSIGTERM=False, handleSIGHUP=False, options=options
    )
    page = await browser.newPage()
    try:
        await page.setViewport(
            {
                "width": width,
                "height": height,
                "deviceScaleFactor": 1,
                "isMobile": is_mobile,
            }
        )
        await page.goto(url)
        data = await page.screenshot({"encoding": "base64"})
    except Exception as e:
        print(e)
    finally:
        await browser.close()
    return data


def get_snapshot_by_url(url:str, width=1600, height=900, is_mobile=False):
    coroutine = launch_ptppeteer_with_url(url, width, height, is_mobile)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    data = None
    try:
        data = loop.run_until_complete(coroutine)
    except Exception as e:
        print(e)
    finally:
        loop.close()
    return data
