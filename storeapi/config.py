from pydantic import BaseSettings
from typing import Optional

class BaseConfig(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

class GlobalConfig(BaseConfig):
    DATABASE_URL: Optional[str] = None
    DB_FORECE_ROLL_BACK: bool = False