# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["DigitalWalletTokenRequestCreateParams"]

class DigitalWalletTokenRequestCreateParams(TypedDict, total=False):
    card_id: Required[str]
    """The identifier of the Card to be authorized."""