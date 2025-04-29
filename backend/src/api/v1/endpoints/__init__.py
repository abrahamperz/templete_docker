from fastapi import APIRouter

from .health import router as health_router
from .whatsapp_messages import router as whatsapp_messages


router = APIRouter()

# Marked for removal
router.include_router(health_router, tags=["Health"])
router.include_router(whatsapp_messages, tags=["Messages"])

