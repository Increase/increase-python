# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["AccountTransferCreateParams"]

class AccountTransferCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier for the account that will send the transfer."""

    amount: Required[int]
    """The transfer amount in the minor unit of the account currency.

    For dollars, for example, this is cents.
    """

    description: Required[str]
    """The description you choose to give the transfer."""

    destination_account_id: Required[str]
    """The identifier for the account that will receive the transfer."""