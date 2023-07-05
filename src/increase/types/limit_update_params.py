# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LimitUpdateParams"]


class LimitUpdateParams(TypedDict, total=False):
    status: Required[Literal["inactive", "active"]]
    """The status to update the limit with.

    - `inactive` - Disable the limit temporarily.
    - `active` - Activate the limit.
    """
