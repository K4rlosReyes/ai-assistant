from core.settings.base import BackendBaseSettings
from core.settings.environment import Environment


class BackendDevSettings(BackendBaseSettings):
    DESCRIPTION: str | None = "Development Environment."
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.DEVELOPMENT
