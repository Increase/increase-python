# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["InboundMailItemActionParams", "Check"]


class InboundMailItemActionParams(TypedDict, total=False):
    checks: Required[Iterable[Check]]
    """The actions to perform on the Inbound Mail Item."""


class Check(TypedDict, total=False):
    action: Required[Literal["deposit", "ignore"]]
    """The action to perform on the Inbound Mail Item.

    - `deposit` - The check will be deposited.
    - `ignore` - The check will be ignored.
    """

    account: str
    """The identifier of the Account to deposit the check into.

    If not provided, the check will be deposited into the Account associated with
    the Lockbox.
    """
