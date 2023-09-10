import logging
from fastapi import APIRouter, FastAPI

from phex.image.model import Image

_logger = logging.getLogger(__name__)
router = APIRouter(prefix="/image")


@router.get("")
def read() -> Image:
    return Image(id="0edd52d6-da9c-4e42-a5a2-333ef0c2969c", name="Test", stored_at="/")


def setup(server: FastAPI) -> None:
    server.include_router(router)
    _logger.debug("Image router is set up.")
