# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LockboxRecipient"]


class LockboxRecipient(BaseModel):
    """Lockbox Recipients represent an inbox at a Lockbox Address.

    Checks received for a Lockbox Recipient are deposited into its associated Account.
    """

    id: str
    """The Lockbox Recipient identifier."""

    account_id: str
    """
    The identifier for the Account that checks sent to this Lockbox Recipient will
    be deposited into.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Lockbox
    Recipient was created.
    """

    description: Optional[str] = None
    """The description of the Lockbox Recipient."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    lockbox_address_id: str
    """
    The identifier for the Lockbox Address where this Lockbox Recipient may receive
    physical mail.
    """

    mail_stop_code: str
    """
    The mail stop code uniquely identifying this Lockbox Recipient at its Lockbox
    Address. It should be included in the mailing address intended for this Lockbox
    Recipient.
    """

    recipient_name: Optional[str] = None
    """The name of the Lockbox Recipient."""

    status: Optional[Literal["active", "disabled", "canceled"]] = None
    """The status of the Lockbox Recipient.

    - `active` - This Lockbox Recipient is active.
    - `disabled` - This Lockbox Recipient is disabled. Checks mailed to this Lockbox
      Recipient will be rejected.
    - `canceled` - This Lockbox Recipient is canceled and cannot be modified. Checks
      mailed to this Lockbox Recipient will be rejected.
    """

    type: Literal["lockbox_recipient"]
    """A constant representing the object's type.

    For this resource it will always be `lockbox_recipient`.
    """
