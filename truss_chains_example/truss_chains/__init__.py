from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


def make_abs_path_here(relative_path: str) -> str:
    """Return an absolute path rooted at this package directory."""
    return str(Path(__file__).resolve().parent / relative_path)


@dataclass
class CustomImage:
    image: str
    python_executable_path: str


@dataclass
class DockerImage:
    base_image: CustomImage
    pip_requirements_file: str | None = None


@dataclass
class RemoteConfig:
    docker_image: DockerImage


class ChainletBase:
    remote_config: RemoteConfig

    def run_remote(self, *args: Any, **kwargs: Any) -> Any:  # pragma: no cover - placeholder
        raise NotImplementedError("Subclasses must implement run_remote")
