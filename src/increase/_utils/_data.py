from __future__ import annotations

import io
import base64
import pathlib

import anyio


def to_base64_str(data: object) -> str:
    from .._files import is_base64_file_input

    if isinstance(data, str):
        return data

    if is_base64_file_input(data):
        binary: str | bytes | None = None

        if isinstance(data, pathlib.Path):
            binary = data.read_bytes()
        elif isinstance(data, io.IOBase):
            binary = data.read()

            if isinstance(binary, str):  # type: ignore[unreachable]
                binary = binary.encode()

        if not isinstance(binary, bytes):
            raise RuntimeError(f"Could not read bytes from {data}; Received {type(binary)}")

        return base64.b64encode(binary).decode("ascii")

    raise TypeError(f"Expected base64 input to be a string, io object or PathLike object but got {data}")


async def to_base64_str_async(data: object) -> str:
    from .._files import is_base64_file_input

    if isinstance(data, str):
        return data

    if is_base64_file_input(data):
        binary: str | bytes | None = None

        if isinstance(data, pathlib.Path):
            binary = await anyio.Path(data).read_bytes()
        elif isinstance(data, io.IOBase):
            binary = data.read()

            if isinstance(binary, str):  # type: ignore[unreachable]
                binary = binary.encode()

        if not isinstance(binary, bytes):
            raise RuntimeError(f"Could not read bytes from {data}; Received {type(binary)}")

        return base64.b64encode(binary).decode("ascii")
    raise TypeError(f"Expected base64 input to be a string, io object or PathLike object but got {data}")
