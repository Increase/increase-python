# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Document", "AccountVerificationLetter", "FundingInstructions"]


class AccountVerificationLetter(BaseModel):
    account_number_id: str
    """The identifier of the Account Number the document was generated for."""


class FundingInstructions(BaseModel):
    account_number_id: str
    """The identifier of the Account Number the document was generated for."""


class Document(BaseModel):
    id: str
    """The Document identifier."""

    account_verification_letter: Optional[AccountVerificationLetter] = None
    """Properties of an account verification letter document."""

    category: Literal[
        "form_1099_int",
        "form_1099_misc",
        "proof_of_authorization",
        "company_information",
        "account_verification_letter",
        "funding_instructions",
    ]
    """The type of document.

    - `form_1099_int` - Internal Revenue Service Form 1099-INT.
    - `form_1099_misc` - Internal Revenue Service Form 1099-MISC.
    - `proof_of_authorization` - A document submitted in response to a proof of
      authorization request for an ACH transfer.
    - `company_information` - Company information, such a policies or procedures,
      typically submitted during our due diligence process.
    - `account_verification_letter` - An account verification letter.
    - `funding_instructions` - Funding instructions.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the
    Document was created.
    """

    entity_id: Optional[str] = None
    """The identifier of the Entity the document was generated for."""

    file_id: str
    """The identifier of the File containing the Document's contents."""

    funding_instructions: Optional[FundingInstructions] = None
    """Properties of a funding instructions document."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    type: Literal["document"]
    """A constant representing the object's type.

    For this resource it will always be `document`.
    """
