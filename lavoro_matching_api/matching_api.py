from fastapi import APIRouter, FastAPI

from lavoro_matching_api.routers.matches import router as matches_router

app = FastAPI()


router = APIRouter()
router.include_router(matches_router)

app.include_router(router)
