# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentCreateParams", "AccountVerificationLetter", "FundingInstructions"]


class DocumentCreateParams(TypedDict, total=False):
    category: Required[Literal["account_verification_letter", "funding_instructions"]]
    """The type of document to create.

    - `account_verification_letter` - An account verification letter.
    - `funding_instructions` - Funding instructions.
    """

    account_verification_letter: AccountVerificationLetter
    """An account verification letter."""

    funding_instructions: FundingInstructions
    """Funding instructions."""


class AccountVerificationLetter(TypedDict, total=False):
    account_number_id: Required[str]
    """The Account Number the bank letter should be generated for."""

    balance_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """If provided, the letter will include the Account's balance as of the date."""


class FundingInstructions(TypedDict, total=False):
    account_number_id: Required[str]
    """The Account Number the funding instructions should be generated for."""
