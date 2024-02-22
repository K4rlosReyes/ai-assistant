import fastapi
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from core.manager import settings
from v1.api import router as api_endpoint_router


def initialize_backend_application() -> fastapi.FastAPI():
    app = fastapi.FastAPI(**settings.set_backend_app_attributes)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=settings.IS_ALLOWED_CREDENTIALS,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )

    app.include_router(router=api_endpoint_router, prefix=settings.API_PREFIX)

    return app


backend_app: fastapi.FastAPI = initialize_backend_application()

if __name__ == "__main__":
    uvicorn.run(
        app="main:backend_app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=True,
        workers=settings.SERVER_WORKERS,
        log_level=settings.LOGGING_LEVEL,
    )
