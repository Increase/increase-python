# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PhysicalCardUpdateParams"]


class PhysicalCardUpdateParams(TypedDict, total=False):
    status: Required[Literal["active", "disabled", "canceled"]]
    """The status to update the Physical Card to.

    - `active` - The physical card is active.
    - `disabled` - The physical card is temporarily disabled.
    - `canceled` - The physical card is permanently canceled.
    """
