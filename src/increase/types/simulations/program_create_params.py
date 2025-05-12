# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProgramCreateParams"]


class ProgramCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the program being added."""

    reserve_account_id: str
    """The identifier of the Account the Program should be added to is for."""
