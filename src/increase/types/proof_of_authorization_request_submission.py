# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProofOfAuthorizationRequestSubmission"]


class ProofOfAuthorizationRequestSubmission(BaseModel):
    id: str
    """The Proof of Authorization Request Submission identifier."""

    authorization_terms: str
    """Terms of authorization."""

    authorized_at: datetime
    """Time of authorization."""

    authorizer_company: Optional[str] = None
    """Company of the authorizer."""

    authorizer_email: Optional[str] = None
    """Email of the authorizer."""

    authorizer_ip_address: Optional[str] = None
    """IP address of the authorizer."""

    authorizer_name: Optional[str] = None
    """Name of the authorizer."""

    created_at: datetime
    """The time the Proof of Authorization Request Submission was created."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    proof_of_authorization_request_id: str
    """ID of the proof of authorization request."""

    status: Literal["pending_review", "rejected", "pending_sending", "sent"]
    """Status of the proof of authorization request submission.

    - `pending_review` - The proof of authorization request submission is pending
      review.
    - `rejected` - The proof of authorization request submission was rejected.
    - `pending_sending` - The proof of authorization request submission is pending
      sending.
    - `sent` - The proof of authorization request submission was sent.
    """

    type: Literal["proof_of_authorization_request_submission"]
    """A constant representing the object's type.

    For this resource it will always be `proof_of_authorization_request_submission`.
    """

    updated_at: datetime
    """The time the Proof of Authorization Request Submission was last updated."""
