# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WireDrawdownRequest", "CreditorAddress", "DebtorAddress", "Submission"]


class CreditorAddress(BaseModel):
    city: str
    """The city, district, town, or village of the address."""

    country: str
    """
    The two-letter
    [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code for
    the country of the address.
    """

    line1: str
    """The first line of the address."""

    line2: Optional[str] = None
    """The second line of the address."""

    postal_code: Optional[str] = None
    """The ZIP code of the address."""

    state: Optional[str] = None
    """The address state."""


class DebtorAddress(BaseModel):
    city: str
    """The city, district, town, or village of the address."""

    country: str
    """
    The two-letter
    [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code for
    the country of the address.
    """

    line1: str
    """The first line of the address."""

    line2: Optional[str] = None
    """The second line of the address."""

    postal_code: Optional[str] = None
    """The ZIP code of the address."""

    state: Optional[str] = None
    """The address state."""


class Submission(BaseModel):
    input_message_accountability_data: str
    """
    The input message accountability data (IMAD) uniquely identifying the submission
    with Fedwire.
    """


class WireDrawdownRequest(BaseModel):
    id: str
    """The Wire drawdown request identifier."""

    account_number_id: str
    """
    The Account Number to which the debtor—the recipient of this request—is being
    requested to send funds.
    """

    amount: int
    """The amount being requested in cents."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the wire drawdown request was created.
    """

    creditor_address: CreditorAddress
    """The creditor's address."""

    creditor_name: str
    """The creditor's name."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the amount being
    requested. Will always be "USD".
    """

    debtor_account_number: str
    """The debtor's account number."""

    debtor_address: DebtorAddress
    """The debtor's address."""

    debtor_external_account_id: Optional[str] = None
    """The debtor's external account identifier."""

    debtor_name: str
    """The debtor's name."""

    debtor_routing_number: str
    """The debtor's routing number."""

    fulfillment_inbound_wire_transfer_id: Optional[str] = None
    """
    If the recipient fulfills the drawdown request by sending funds, then this will
    be the identifier of the corresponding Transaction.
    """

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    status: Literal["pending_submission", "pending_response", "fulfilled", "refused"]
    """The lifecycle status of the drawdown request.

    - `pending_submission` - The drawdown request is queued to be submitted to
      Fedwire.
    - `pending_response` - The drawdown request has been sent and the recipient
      should respond in some way.
    - `fulfilled` - The drawdown request has been fulfilled by the recipient.
    - `refused` - The drawdown request has been refused by the recipient.
    """

    submission: Optional[Submission] = None
    """
    After the drawdown request is submitted to Fedwire, this will contain
    supplemental details.
    """

    type: Literal["wire_drawdown_request"]
    """A constant representing the object's type.

    For this resource it will always be `wire_drawdown_request`.
    """

    unstructured_remittance_information: str
    """Remittance information the debtor will see as part of the drawdown request."""
