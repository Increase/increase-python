# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountCreateParams", "Loan"]


class AccountCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name you choose for the Account."""

    entity_id: str
    """The identifier for the Entity that will own the Account."""

    funding: Literal["loan", "deposits"]
    """Whether the Account is funded by a loan or by deposits.

    - `loan` - An account funded by a loan. Before opening a loan account, contact
      support@increase.com to set up a loan program.
    - `deposits` - An account funded by deposits.
    """

    informational_entity_id: str
    """
    The identifier of an Entity that, while not owning the Account, is associated
    with its activity. This is generally the beneficiary of the funds.
    """

    loan: Loan
    """The loan details for the account."""

    program_id: str
    """The identifier for the Program that this Account falls under.

    Required if you operate more than one Program.
    """


class Loan(TypedDict, total=False):
    """The loan details for the account."""

    credit_limit: Required[int]
    """The maximum amount of money that can be drawn from the Account."""

    grace_period_days: Required[int]
    """
    The number of days after the statement date that the Account can be past due
    before being considered delinquent.
    """

    statement_day_of_month: Required[int]
    """The day of the month on which the loan statement is generated."""

    statement_payment_type: Required[Literal["balance", "interest_until_maturity"]]
    """The type of statement payment for the account.

    - `balance` - The borrower must pay the full balance of the loan at the end of
      the statement period.
    - `interest_until_maturity` - The borrower must pay the accrued interest at the
      end of the statement period.
    """

    maturity_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """The date on which the loan matures."""
