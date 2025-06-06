from fastapi import APIRouter

from .health import router as health_router


router = APIRouter()

# Marked for removal
router.include_router(health_router, tags=["Health"])

