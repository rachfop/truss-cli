from pathlib import Path

import truss_chains as chains

# Custom Docker image configuration pointing to python:3.11-slim-bookworm.
IMAGE_CUSTOM = chains.DockerImage(
    base_image=chains.CustomImage(
        image="python:3.11-slim-bookworm",
        python_executable_path="/usr/local/bin/python",
    ),
    pip_requirements_file=str(Path(__file__).resolve().parent / "requirements.txt"),
)


class MyChainlet(chains.ChainletBase):
    remote_config = chains.RemoteConfig(docker_image=IMAGE_CUSTOM)

    def run_remote(self, data: str) -> str:
        return data.upper()


if __name__ == "__main__":
    chain = MyChainlet()
    result = chain.run_remote("hello, world!")
    print(result)
