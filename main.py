#!/usr/bin/env python3

import logging
import os
import requests
import sys
from typing import List

# Change the current working directory to the directory where this script resides
os.chdir(os.path.dirname(os.path.abspath(__file__)))

log_level: str = os.getenv('LOG_LEVEL', 'INFO')

logging.basicConfig(
    format='%(asctime)s | %(filename)16s:%(lineno)-4d | %(levelname)-8s | %(message)s',
    level=logging._nameToLevel[log_level]
)

urls_filename: str = os.getenv('URLS_FILENAME', 'urls.txt')
urls_list: List[str] = list(
    map(lambda line: line.strip(), open(urls_filename).readlines()))


def main() -> int:
    for url_item in urls_list:
        logging.info(f'Check {url_item}')

        def url_exist(url: str) -> bool:
            try:
                response: requests.Response = requests.get(url, timeout=3)
                return response.status_code == 200
            except requests.exceptions.ReadTimeout:
                return False

        if url_exist(url_item):
            logging.info('Success')
        else:
            logging.error('Failed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
