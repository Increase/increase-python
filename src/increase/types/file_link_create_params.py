# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FileLinkCreateParams"]


class FileLinkCreateParams(TypedDict, total=False):
    file_id: Required[str]
    """The File to create a File Link for."""

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The time at which the File Link will expire.

    The default is 1 hour from the time of the request. The maxiumum is 1 day from
    the time of the request.
    """
