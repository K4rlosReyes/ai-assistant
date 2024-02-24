import fastapi

from v1.endpoints.ask_model import router as ask_router

router = fastapi.APIRouter()
router.include_router(router=ask_router)
