# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExternalAccount"]


class ExternalAccount(BaseModel):
    id: str
    """The External Account's identifier."""

    account_holder: Literal["business", "individual", "unknown"]
    """The type of entity that owns the External Account.

    - `business` - The External Account is owned by a business.
    - `individual` - The External Account is owned by an individual.
    - `unknown` - It's unknown what kind of entity owns the External Account.
    """

    account_number: str
    """The destination account number."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the External Account was created.
    """

    description: str
    """The External Account's description for display purposes."""

    funding: Literal["checking", "savings", "general_ledger", "other"]
    """The type of the account to which the transfer will be sent.

    - `checking` - A checking account.
    - `savings` - A savings account.
    - `general_ledger` - A general ledger account.
    - `other` - A different type of account.
    """

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    routing_number: str
    """The American Bankers' Association (ABA) Routing Transit Number (RTN)."""

    status: Literal["active", "archived"]
    """The External Account's status.

    - `active` - The External Account is active.
    - `archived` - The External Account is archived and won't appear in the
      dashboard.
    """

    type: Literal["external_account"]
    """A constant representing the object's type.

    For this resource it will always be `external_account`.
    """
