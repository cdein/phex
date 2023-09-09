import tomllib
from functools import cache
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Response


def create() -> FastAPI:
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

    return server


@cache
def _project_information() -> dict[str, Any]:
    return tomllib.loads((Path.cwd() / "pyproject.toml").read_text())["tool"]["poetry"]
