from core.settings.base import BackendBaseSettings
from core.settings.environment import Environment


class BackendProdSettings(BackendBaseSettings):
    DESCRIPTION: str | None = "Production Environment."
    ENVIRONMENT: Environment = Environment.PRODUCTION
