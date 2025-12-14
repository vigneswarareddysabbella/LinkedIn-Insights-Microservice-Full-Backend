from fastapi import APIRouter
from app.api.v1.endpoints.page import router as page_router

router = APIRouter()
router.include_router(page_router, tags=["LinkedIn Pages"])
