# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProgramCreateParams"]


class ProgramCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the program being added."""
