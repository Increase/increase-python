# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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

    customer_has_been_offboarded: Required[bool]
    """Whether the customer has been offboarded or suspended."""

    proof_of_authorization_request_id: Required[str]
    """ID of the proof of authorization request."""

    validated_account_ownership_via_credential: Required[bool]
    """Whether the account ownership was validated via credential (e.g. Plaid)."""

    validated_account_ownership_with_account_statement: Required[bool]
    """Whether the account ownership was validated with an account statement."""

    validated_account_ownership_with_microdeposit: Required[bool]
    """Whether the account ownership was validated with a microdeposit."""

    authorizer_company: str
    """Company of the authorizer."""

    authorizer_ip_address: str
    """IP address of the authorizer."""
