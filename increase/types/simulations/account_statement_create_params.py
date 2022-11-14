# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["AccountStatementCreateParams"]

class AccountStatementCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier of the Account the statement is for."""