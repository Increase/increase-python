# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardAuthenticationChallengeAttemptsParams"]


class CardAuthenticationChallengeAttemptsParams(TypedDict, total=False):
    one_time_code: Required[str]
    """The one-time code to be validated."""
