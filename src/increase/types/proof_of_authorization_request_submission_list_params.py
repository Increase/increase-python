# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProofOfAuthorizationRequestSubmissionListParams"]


class ProofOfAuthorizationRequestSubmissionListParams(TypedDict, total=False):
    cursor: str
    """Return the page of entries after this one."""

    idempotency_key: str
    """
    Filter records to the one with the specified `idempotency_key` you chose for
    that object. This value is unique across Increase and is used to ensure that a
    request is only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """

    proof_of_authorization_request_id: str
    """ID of the proof of authorization request."""
