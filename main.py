#!/usr/bin/env python3

import logging
import os
import sys


log_level: str = os.getenv('LOG_LEVEL', 'INFO')
logging.basicConfig(
    format='%(asctime)s | %(filename)16s:%(lineno)-4d | %(levelname)-8s | %(message)s',
    level=logging._nameToLevel[log_level]
)


def main():
    logging.info('main()')
    return 0


if __name__ == '__main__':
    sys.exit(main())
