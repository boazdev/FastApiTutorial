from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "Awesome API"
    jwt_key: str ="SECRET2"
    jwt_algorithm:str="HS256"
    db_url:str="mysql+pymysql://admin:admin@localhost:3306/factory_db"#mysql+pymysql://admin:admin@localhost:3306/factory_db"

    model_config = SettingsConfigDict(env_file=".env",extra="allow")

@lru_cache()
def get_settings():
    return Settings()

""" print("config.py called") """
settings= get_settings()


