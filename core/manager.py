from functools import lru_cache

import decouple

from core.settings.base import BackendBaseSettings
from core.settings.development import BackendDevSettings
from core.settings.environment import Environment
from core.settings.production import BackendProdSettings
from core.settings.staging import BackendStageSettings


class BackendSettingsFactory:
    def __init__(self, environment: str):
        self.environment = environment

    def __call__(self) -> BackendBaseSettings:
        if self.environment == Environment.DEVELOPMENT.value:
            return BackendDevSettings()
        elif self.environment == Environment.STAGING.value:
            return BackendStageSettings()
        return BackendProdSettings()


@lru_cache()
def get_settings() -> BackendBaseSettings:
    return BackendSettingsFactory(
        environment=decouple.config("ENVIRONMENT", default="DEV", cast=str)
    )()  # type: ignore


settings: BackendBaseSettings = get_settings()
