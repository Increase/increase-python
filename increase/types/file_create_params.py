# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    file: Required[FileTypes]
    """The file contents.

    This should follow the specifications of
    [RFC 7578](https://datatracker.ietf.org/doc/html/rfc7578) which defines file
    transfers for the multipart/form-data protocol.
    """

    purpose: Required[Literal["check_image_front", "check_image_back", "form_ss_4", "identity_document", "other"]]
    """What the File will be used for in Increase's systems."""

    description: str
    """The description you choose to give the File."""
