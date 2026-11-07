# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Checkbook", "MailingAddress", "Payer", "ReturnAddress", "TrackingUpdate"]


class MailingAddress(BaseModel):
    """The destination address that the Checkbook will be mailed to."""

    city: str
    """The city of the destination address."""

    line1: str
    """The first line of the destination address."""

    line2: Optional[str] = None
    """The second line of the destination address."""

    name: str
    """The recipient at the destination address."""

    postal_code: str
    """The postal code of the destination address."""

    state: str
    """The state of the destination address."""


class Payer(BaseModel):
    contents: str
    """The contents of the line."""


class ReturnAddress(BaseModel):
    """The address the Checkbook will return to if there is a delivery issue."""

    city: str
    """The city of the return address."""

    line1: str
    """The first line of the return address."""

    line2: Optional[str] = None
    """The second line of the return address."""

    name: str
    """The recipient at the return address."""

    postal_code: str
    """The postal code of the return address."""

    state: str
    """The state of the return address."""


class TrackingUpdate(BaseModel):
    category: Literal[
        "in_transit",
        "processed_for_delivery",
        "delivered",
        "delivery_issue",
        "returning_to_sender",
        "returned_to_sender",
    ]
    """The type of tracking event.

    - `in_transit` - The checkbook is in transit.
    - `processed_for_delivery` - The checkbook has been processed for delivery.
    - `delivered` - The checkbook has been delivered. Note that some couriers track
      delivery status based on driver location data rather than an explicit scan.
      While uncommon, a single checkbook may have more than one delivered event.
    - `delivery_issue` - There is an issue preventing delivery. The delivery will be
      attempted again if possible. If the issue cannot be resolved, the checkbook
      will be rerouted to the return address.
    - `returning_to_sender` - The checkbook has been rerouted to the return address.
    - `returned_to_sender` - The checkbook has been delivered to the return address.
    """

    country: str
    """The ISO 3166-1 alpha-2 country code for the country where the event took place."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the tracking event took place.
    """

    postal_code: str
    """The postal code where the event took place."""


class Checkbook(BaseModel):
    """
    Checkbooks are sets of blank checks that Increase prints and mails on your behalf.
    """

    id: str
    """The Checkbook's identifier."""

    account_number_id: str
    """The identifier of the Account Number the Checkbook is attached to."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Checkbook was created.
    """

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    mailing_address: MailingAddress
    """The destination address that the Checkbook will be mailed to."""

    payer: List[Payer]
    """The payer information printed on the top-left corner of each check."""

    return_address: ReturnAddress
    """The address the Checkbook will return to if there is a delivery issue."""

    status: Literal["pending_submission", "pending_mailing", "mailed", "stopped"]
    """The lifecycle status of the Checkbook.

    - `pending_submission` - The Checkbook is pending submission to the printer.
    - `pending_mailing` - The Checkbook has been submitted to the printer and is
      pending mailing.
    - `mailed` - The Checkbook has been mailed.
    - `stopped` - The Checkbook has been stopped and its checks can no longer be
      deposited.
    """

    style: Literal["three_ring_binder", "folder"]
    """The physical format of the Checkbook.

    - `three_ring_binder` - A half-inch three-ring binder holding 75 pages of checks
      with 3 checks per page.
    - `folder` - A folder holding 15 pages of checks with 3 checks per page.
    """

    tracking_updates: List[TrackingUpdate]
    """Tracking updates relating to the Checkbook's delivery."""

    type: Literal["checkbook"]
    """A constant representing the object's type.

    For this resource it will always be `checkbook`.
    """
