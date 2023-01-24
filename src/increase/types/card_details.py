# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardDetails"]


class CardDetails(BaseModel):
    card_id: str
    """The identifier for the Card for which sensitive details have been returned."""

    expiration_month: int
    """The month the card expires in M format (e.g., August is 8)."""

    expiration_year: int
    """The year the card expires in YYYY format (e.g., 2025)."""

    primary_account_number: str
    """The card number."""

    type: Literal["card_details"]
    """A constant representing the object's type.

    For this resource it will always be `card_details`.
    """

    verification_code: str
    """The three-digit verification code for the card.

    It's also known as the Card Verification Code (CVC), the Card Verification Value
    (CVV), or the Card Identification (CID).
    """
