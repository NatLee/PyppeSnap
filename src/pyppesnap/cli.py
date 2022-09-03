import argparse
from pyppesnap import get_image_snapshot_by_url, get_pdf_snapshot_by_url

def get_parser():
    parser = argparse.ArgumentParser(description='PyppeSnap CLI')
    parser.add_argument('--url', type=str)
    parser.add_argument('--type', type=str, default='img')
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    url = args.url
    type_ = args.type.lower()
    print('------------- Parameters ---------------')
    print(f'URL: {url}')
    print(f'Type: {type_}')
    if not url:
        print('------------- ERROR ---------------')
        print('Please specific URL. Like `https://www.google.com`')
        parser.print_help()
        return

    if type_ != 'img' and type_ != 'pdf':
        print('------------- ERROR ---------------')
        print('Please select type `img` or `pdf`.')
        parser.print_help()
        return

    print('--------------- Base64 ------------------')
    if type_.lower() == 'img':
        print(get_image_snapshot_by_url(url))
    elif type_.lower() == 'pdf':
        print(get_pdf_snapshot_by_url(url))

    print('-------------------------------------')
    return