from typing import Callable
import asyncio
import base64
from pyppeteer import launch

async def shot_with_image(page):
    return await page.screenshot({"encoding": "base64"})

async def shot_with_pdf(page):
    dimensions = await page.evaluate(
    """() => {
        return {
            width: document.scrollingElement.scrollWidth,
            height: document.documentElement.offsetHeight,
        }
    }"""
    )
    data = await page.pdf(
        {
            "printBackground": True,
            "width": dimensions["width"],
            "height": dimensions["height"] + 5
        }
    )
    return base64.b64encode(data)

async def launch_ptppeteer_with_url(url:str, width:int, height:int, is_mobile:bool, method:Callable):
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
        data = await method(page)
    except Exception as e:
        print(e)
    finally:
        await browser.close()
    return data

def get_snapshot_by_url(url:str, method:Callable, width=1600, height=900, is_mobile=False):
    coroutine = launch_ptppeteer_with_url(url, width, height, is_mobile, method)
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

def get_image_snapshot_by_url(url:str, width=1600, height=900, is_mobile=False):
    return get_snapshot_by_url(url=url, method=shot_with_image, width=width, height=height, is_mobile=is_mobile)

def get_pdf_snapshot_by_url(url:str, width=1600, height=900, is_mobile=False):
    return get_snapshot_by_url(url=url, method=shot_with_pdf, width=width, height=height, is_mobile=is_mobile)
