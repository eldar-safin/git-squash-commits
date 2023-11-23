#!/usr/bin/env python3

import logging
import os
import sys


log_level: str = os.getenv('LOG_LEVEL', 'INFO')
logging.basicConfig(
    level=logging._nameToLevel[log_level]
    )


def main():
    logging.info('main()')
    return 0

if __name__ == '__main__':
    sys.exit(main())

