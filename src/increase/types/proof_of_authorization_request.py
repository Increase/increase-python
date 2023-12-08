# File generated from our OpenAPI spec by Stainless.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProofOfAuthorizationRequest", "ACHTransfer"]


class ACHTransfer(BaseModel):
    id: str
    """The ACH Transfer identifier."""


class ProofOfAuthorizationRequest(BaseModel):
    id: str
    """The Proof of Authorization Request identifier."""

    ach_transfers: List[ACHTransfer]
    """The ACH Transfers associated with the request."""

    created_at: datetime
    """The time the Proof of Authorization Request was created."""

    type: Literal["proof_of_authorization_request"]
    """A constant representing the object's type.

    For this resource it will always be `proof_of_authorization_request`.
    """

    updated_at: datetime
    """The time the Proof of Authorization Request was last updated."""
