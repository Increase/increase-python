# File generated from our OpenAPI spec by Stainless.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExternalAccount"]


class ExternalAccount(BaseModel):
    id: str
    """The External Account's identifier."""

    account_number: str
    """The destination account number."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the External Account was created.
    """

    description: str
    """The External Account's description for display purposes."""

    funding: Literal["checking", "savings", "other"]
    """The type of the account to which the transfer will be sent.

    - `checking` - A checking account.
    - `savings` - A savings account.
    - `other` - A different type of account.
    """

    routing_number: str
    """The American Bankers' Association (ABA) Routing Transit Number (RTN)."""

    status: Literal["active", "archived"]
    """The External Account's status.

    - `active` - The External Acccount is active.
    - `archived` - The External Account is archived and won't appear in the
      dashboard.
    """

    type: Literal["external_account"]
    """A constant representing the object's type.

    For this resource it will always be `external_account`.
    """

    verification_status: Literal["unverified", "pending", "verified"]
    """If you have verified ownership of the External Account.

    - `unverified` - The External Account has not been verified.
    - `pending` - The External Account is in the process of being verified.
    - `verified` - The External Account is verified.
    """
