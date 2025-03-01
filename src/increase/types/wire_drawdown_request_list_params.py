# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["WireDrawdownRequestListParams"]


class WireDrawdownRequestListParams(TypedDict, total=False):
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

    status: Literal["pending_submission", "pending_response", "fulfilled", "refused"]
    """Filter Wire Drawdown Requests for those with the specified status.

    - `pending_submission` - The drawdown request is queued to be submitted to
      Fedwire.
    - `pending_response` - The drawdown request has been sent and the recipient
      should respond in some way.
    - `fulfilled` - The drawdown request has been fulfilled by the recipient.
    - `refused` - The drawdown request has been refused by the recipient.
    """
