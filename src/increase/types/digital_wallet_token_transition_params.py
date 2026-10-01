# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DigitalWalletTokenTransitionParams"]


class DigitalWalletTokenTransitionParams(TypedDict, total=False):
    status: Required[Literal["active", "suspended", "deactivated"]]
    """The status to transition the Digital Wallet Token to.

    - `active` - Reactivate a suspended Digital Wallet Token.
    - `suspended` - Temporarily pause an active Digital Wallet Token.
    - `deactivated` - Permanently cancel an active, inactive, or suspended Digital
      Wallet Token.
    """
