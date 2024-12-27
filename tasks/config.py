from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    DEBUG: bool = Field(default=True, env="DEBUG")
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    DB_ENGINE: str = Field(
        default="django.db.backends.sqlite3", env="DB_ENGINE")
    DB_NAME: str = Field(default="db.sqlite3", env="DB_NAME")
    DB_USER: str = Field(default="", env="DB_USER")
    DB_PASSWORD: str = Field(default="", env="DB_PASSWORD")
    DB_HOST: str = Field(default="localhost", env="DB_HOST")
    DB_PORT: int = Field(default=5432, env="DB_PORT")

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()
