from os import getenv


class LogSettings:
    level: str = getenv('LOG_LEVEL', 'INFO')


class UrlsSettings:
    filename: str = getenv('URLS_FILENAME', 'urls.txt')


class Settings:
    log: LogSettings = LogSettings()
    urls: UrlsSettings = UrlsSettings()


settings = Settings()
