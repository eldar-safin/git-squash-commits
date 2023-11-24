#!/usr/bin/env python3

import logging
import os
import sys
from typing import List

import requests

from settings import settings

# Change the current working directory to the directory where this script resides
os.chdir(os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(
    format="%(asctime)s | %(filename)16s:%(lineno)-4d | %(levelname)-8s | %(message)s",
    level=logging._nameToLevel[settings.log.level],
)

urls_list: List[str] = list(
    map(
        lambda line: line.strip(),
        open(settings.urls.filename).readlines(),
    )
)


def main() -> int:
    for url_item in urls_list:
        logging.info(f"Check {url_item}")

        def check_url(
            url: str,
        ) -> bool:
            try:
                response: requests.Response = requests.get(
                    url,
                    timeout=3,
                )
                return response.status_code == 200
            except (
                requests.exceptions.ReadTimeout,
                requests.exceptions.ConnectionError,
            ):
                return False

        if check_url(url_item):
            logging.info("Success")
        else:
            logging.error("Failed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
