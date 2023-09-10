from fastapi import APIRouter, FastAPI

from phex.photo.model import Photo

router = APIRouter(prefix="/photo")


@router.get("")
def read() -> Photo:
    return Photo(id="0edd52d6-da9c-4e42-a5a2-333ef0c2969c", name="Test")


def setup(server: FastAPI) -> None:
    server.include_router(router)
