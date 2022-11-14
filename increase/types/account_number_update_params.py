# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["AccountNumberUpdateParams"]

class AccountNumberUpdateParams(TypedDict, total=False):
    name: str
    """The name you choose for the Account Number."""

    status: Literal["active", "disabled", "canceled"]
    """This indicates if transfers can be made to the Account Number."""