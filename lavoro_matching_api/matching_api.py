from fastapi import APIRouter, FastAPI

from lavoro_matching_api.routers.application import router as application_router
from lavoro_matching_api.routers.matches import router as matches_router

app = FastAPI()


router = APIRouter()
router.include_router(application_router)
router.include_router(matches_router)

app.include_router(router)
