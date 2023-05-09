from pydantic import BaseSettings

from affiliate_bypass.version import __version__


class Config(BaseSettings):
    title: str = "Affiliate Bypass"
    version: str = __version__

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
