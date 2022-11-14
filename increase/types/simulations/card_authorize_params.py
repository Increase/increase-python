# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["CardAuthorizeParams"]

class CardAuthorizeParams(TypedDict, total=False):
    amount: Required[int]
    """The authorization amount in cents."""

    card_id: Required[str]
    """The identifier of the Card to be authorized."""