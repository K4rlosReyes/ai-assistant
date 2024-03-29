import logging
import pathlib

import pydantic
import pydantic_settings
from decouple import config

ROOT_DIR: pathlib.Path = pathlib.Path(
    __file__
).parent.parent.parent.parent.parent.resolve()


class BackendBaseSettings(pydantic_settings.BaseSettings):
    TITLE: str = "DAPSQL FARN-Stack Template Application"
    VERSION: str = "0.1.0"
    TIMEZONE: str = "UTC"
    DESCRIPTION: str | None = None
    DEBUG: bool = False

    SERVER_HOST: str = config("BACKEND_SERVER_HOST", cast=str)  # type: ignore
    SERVER_PORT: int = config("BACKEND_SERVER_PORT", cast=int)  # type: ignore
    SERVER_WORKERS: int = config("BACKEND_SERVER_WORKERS", cast=int)  # type: ignore
    API_PREFIX: str = "/api"
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: str = "/redoc"
    OPENAPI_PREFIX: str = ""

    OPENAI_KEY: str = config("OPENAI_KEY", cast=str)

    DB_POSTGRES_HOST: str = config("POSTGRES_HOST", cast=str)  # type: ignore
    DB_MAX_POOL_CON: int = config("DB_MAX_POOL_CON", cast=int)  # type: ignore
    DB_POSTGRES_NAME: str = config("POSTGRES_DB", cast=str)  # type: ignore
    DB_POSTGRES_PASSWORD: str = config("POSTGRES_PASSWORD", cast=str)  # type: ignore
    DB_POOL_SIZE: int = config("DB_POOL_SIZE", cast=int)  # type: ignore
    DB_POOL_OVERFLOW: int = config("DB_POOL_OVERFLOW", cast=int)  # type: ignore
    DB_POSTGRES_PORT: int = config("POSTGRES_PORT", cast=int)  # type: ignore
    DB_POSTGRES_SCHEMA: str = config("POSTGRES_SCHEMA", cast=str)  # type: ignore
    DB_TIMEOUT: int = config("DB_TIMEOUT", cast=int)  # type: ignore
    DB_POSTGRES_USERNAME: str = config("POSTGRES_USERNAME", cast=str)  # type: ignore

    IS_DB_ECHO_LOG: bool = config("IS_DB_ECHO_LOG", cast=bool)  # type: ignore
    IS_DB_FORCE_ROLLBACK: bool = config("IS_DB_FORCE_ROLLBACK", cast=bool)  # type: ignore
    IS_DB_EXPIRE_ON_COMMIT: bool = config("IS_DB_EXPIRE_ON_COMMIT", cast=bool)  # type: ignore

    API_TOKEN: str = config("API_TOKEN", cast=str)  # type: ignore
    AUTH_TOKEN: str = config("AUTH_TOKEN", cast=str)  # type: ignore
    JWT_TOKEN_PREFIX: str = config("JWT_TOKEN_PREFIX", cast=str)  # type: ignore
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)  # type: ignore
    JWT_SUBJECT: str = config("JWT_SUBJECT", cast=str)  # type: ignore
    JWT_MIN: int = config("JWT_MIN", cast=int)  # type: ignore
    JWT_HOUR: int = config("JWT_HOUR", cast=int)  # type: ignore
    JWT_DAY: int = config("JWT_DAY", cast=int)  # type: ignore
    JWT_ACCESS_TOKEN_EXPIRATION_TIME: int = JWT_MIN * JWT_HOUR * JWT_DAY

    IS_ALLOWED_CREDENTIALS: bool = config("IS_ALLOWED_CREDENTIALS", cast=bool)  # type: ignore
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:3000",  # React default port
        "http://0.0.0.0:3000",
        "http://127.0.0.1:3000",  # React docker port
        "http://127.0.0.1:3001",
        "http://localhost:5173",  # Qwik default port
        "http://0.0.0.0:5173",
        "http://127.0.0.1:5173",  # Qwik docker port
        "http://127.0.0.1:5174",
    ]
    ALLOWED_METHODS: list[str] = ["*"]
    ALLOWED_HEADERS: list[str] = ["*"]

    LOGGING_LEVEL: int = logging.INFO
    LOGGERS: tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    HASHING_ALGORITHM_LAYER_1: str = config("HASHING_ALGORITHM_LAYER_1", cast=str)  # type: ignore
    HASHING_ALGORITHM_LAYER_2: str = config("HASHING_ALGORITHM_LAYER_2", cast=str)  # type: ignore
    HASHING_SALT: str = config("HASHING_SALT", cast=str)  # type: ignore
    JWT_ALGORITHM: str = config("JWT_ALGORITHM", cast=str)  # type: ignore

    class Config(pydantic.BaseConfig):
        case_sensitive: bool = True
        env_file: str = f"{str(ROOT_DIR)}/.env"
        validate_assignment: bool = True

    @property
    def set_backend_app_attributes(self) -> dict[str, str | bool | None]:
        """
        Set all `FastAPI` class' attributes with the custom values defined in `BackendBaseSettings`.
        """
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "debug": self.DEBUG,
            "description": self.DESCRIPTION,
            "docs_url": self.DOCS_URL,
            "openapi_url": self.OPENAPI_URL,
            "redoc_url": self.REDOC_URL,
            "openapi_prefix": self.OPENAPI_PREFIX,
            "api_prefix": self.API_PREFIX,
        }
