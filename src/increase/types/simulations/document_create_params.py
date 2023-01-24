# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DocumentCreateParams"]


class DocumentCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier of the Account the tax document is for."""
