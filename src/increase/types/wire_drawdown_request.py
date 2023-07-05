# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WireDrawdownRequest", "Submission"]


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
    The Account Number to which the recipient of this request is being requested to
    send funds.
    """

    amount: int
    """The amount being requested in cents."""

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the amount being
    requested. Will always be "USD".
    """

    fulfillment_transaction_id: Optional[str]
    """
    If the recipient fulfills the drawdown request by sending funds, then this will
    be the identifier of the corresponding Transaction.
    """

    message_to_recipient: str
    """The message the recipient will see as part of the drawdown request."""

    recipient_account_number: str
    """The drawdown request's recipient's account number."""

    recipient_address_line1: Optional[str]
    """Line 1 of the drawdown request's recipient's address."""

    recipient_address_line2: Optional[str]
    """Line 2 of the drawdown request's recipient's address."""

    recipient_address_line3: Optional[str]
    """Line 3 of the drawdown request's recipient's address."""

    recipient_name: Optional[str]
    """The drawdown request's recipient's name."""

    recipient_routing_number: str
    """The drawdown request's recipient's routing number."""

    status: Literal["pending_submission", "pending_response", "fulfilled", "refused"]
    """The lifecycle status of the drawdown request.

    - `pending_submission` - The drawdown request is queued to be submitted to
      Fedwire.
    - `pending_response` - The drawdown request has been sent and the recipient
      should respond in some way.
    - `fulfilled` - The drawdown request has been fulfilled by the recipient.
    - `refused` - The drawdown request has been refused by the recipient.
    """

    submission: Optional[Submission]
    """
    After the drawdown request is submitted to Fedwire, this will contain
    supplemental details.
    """

    type: Literal["wire_drawdown_request"]
    """A constant representing the object's type.

    For this resource it will always be `wire_drawdown_request`.
    """
