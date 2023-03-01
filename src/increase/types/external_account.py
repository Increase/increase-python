# File generated from our OpenAPI spec by Stainless.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExternalAccount"]


class ExternalAccount(BaseModel):
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
    """The type of the account to which the transfer will be sent."""

    id: str
    """The External Account's identifier."""

    routing_number: str
    """The American Bankers' Association (ABA) Routing Transit Number (RTN)."""

    status: Literal["active", "archived"]
    """The External Account's status."""

    type: Literal["external_account"]
    """A constant representing the object's type.

    For this resource it will always be `external_account`.
    """

    verification_status: Literal["unverified", "pending", "verified"]
    """If you have verified ownership of the External Account."""
