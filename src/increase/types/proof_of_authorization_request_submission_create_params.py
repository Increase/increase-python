# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProofOfAuthorizationRequestSubmissionCreateParams"]


class ProofOfAuthorizationRequestSubmissionCreateParams(TypedDict, total=False):
    authorization_terms: Required[str]
    """Terms of authorization."""

    authorized_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Time of authorization."""

    authorizer_email: Required[str]
    """Email of the authorizer."""

    authorizer_name: Required[str]
    """Name of the authorizer."""

    proof_of_authorization_request_id: Required[str]
    """ID of the proof of authorization request."""

    authorizer_company: str
    """Company of the authorizer."""

    authorizer_ip_address: str
    """IP address of the authorizer."""
