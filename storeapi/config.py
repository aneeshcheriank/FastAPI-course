from pydantic import BaseSettings
from typing import Optional

class BaseConfig(BaseSettings):
    ENV_STATE: Optional[str] = None #what environment we are running (dev, test, prod)
    class Configuration:
        env_file = ".env"
        env_file_encoding = "utf-8"

class GlobalConfig(BaseConfig):
    DATABASE_URL: Optional[str] = None
    DB_FORCE_ROLL_BACK: bool = False

class DevConfig(GlobalConfig):
    class Configuration:
        env_prefix = "DEV_"

class TestConfig(GlobalConfig):
    # test db values are not secreat
    DATABASE_URL = "sqlite:///test.db"
    DB_FORCE_ROLL_BACK = True

    class Configuration:
            env_prefix = "TETST_"

class ProdConfig(GlobalConfig):
     class Configuration:
            env_prefix = "PROD_"