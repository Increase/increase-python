# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IntrafiAccountEnrollment"]


class IntrafiAccountEnrollment(BaseModel):
    id: str
    """The identifier of this enrollment at IntraFi."""

    account_id: str
    """The identifier of the Increase Account being swept into the network."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the enrollment was created.
    """

    email_address: Optional[str] = None
    """The contact email for the account owner, to be shared with IntraFi."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    intrafi_id: str
    """The identifier of the account in IntraFi's system.

    This identifier will be printed on any IntraFi statements or documents.
    """

    status: Literal["pending_enrolling", "enrolled", "pending_unenrolling", "unenrolled", "requires_attention"]
    """The status of the account in the network.

    An account takes about one business day to go from `pending_enrolling` to
    `enrolled`.

    - `pending_enrolling` - The account is being added to the IntraFi network.
    - `enrolled` - The account has been enrolled with IntraFi.
    - `pending_unenrolling` - The account is being unenrolled from IntraFi's deposit
      sweep.
    - `unenrolled` - The account was once enrolled, but is no longer enrolled at
      IntraFi.
    - `requires_attention` - Something unexpected happened with this account.
      Contact Increase support.
    """

    type: Literal["intrafi_account_enrollment"]
    """A constant representing the object's type.

    For this resource it will always be `intrafi_account_enrollment`.
    """
