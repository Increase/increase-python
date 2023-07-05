# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ExternalAccountUpdateParams"]


class ExternalAccountUpdateParams(TypedDict, total=False):
    description: str
    """The description you choose to give the external account."""

    status: Literal["active", "archived"]
    """The status of the External Account.

    - `active` - The External Acccount is active.
    - `archived` - The External Account is archived and won't appear in the
      dashboard.
    """
