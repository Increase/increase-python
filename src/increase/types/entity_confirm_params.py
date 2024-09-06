# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EntityConfirmParams"]


class EntityConfirmParams(TypedDict, total=False):
    confirmed_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """When your user confirmed the Entity's details.

    If not provided, the current time will be used.
    """
