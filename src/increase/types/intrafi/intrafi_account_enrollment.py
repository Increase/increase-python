# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IntrafiAccountEnrollment"]


class IntrafiAccountEnrollment(BaseModel):
    id: str
    """The identifier of this enrollment at IntraFi."""

    account_id: str
    """The identifier of the Increase Account being swept into the network."""

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
