# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["LimitUpdateParams"]

class LimitUpdateParams(TypedDict, total=False):
    status: Required[Literal["inactive", "active"]]
    """The status to update the limit with."""