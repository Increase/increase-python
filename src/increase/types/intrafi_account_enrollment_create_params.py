# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IntrafiAccountEnrollmentCreateParams"]


class IntrafiAccountEnrollmentCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The identifier for the account to be added to IntraFi."""

    email_address: Required[str]
    """The contact email for the account owner, to be shared with IntraFi."""
