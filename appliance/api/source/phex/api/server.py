import logging
import tomllib
from functools import cache
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Response

from phex.photo.router import setup as photo_setup
from phex.image.router import setup as image_setup


def create() -> FastAPI:
    logging.basicConfig()
    project = _project_information()
    server = FastAPI(
        debug=True,
        title=project["name"],
        version=project["version"],
        description=project["description"],
    )

    @server.get("/")
    def _() -> Response:
        return {
            "name": project["name"],
            "version": project["version"],
            "description": project["description"],
        }

    image_setup(server)
    photo_setup(server)

    return server


@cache
def _project_information() -> dict[str, Any]:
    return tomllib.loads((Path.cwd() / "pyproject.toml").read_text())["tool"]["poetry"]
