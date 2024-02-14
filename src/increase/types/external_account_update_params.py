# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ExternalAccountUpdateParams"]


class ExternalAccountUpdateParams(TypedDict, total=False):
    account_holder: Literal["business", "individual"]
    """The type of entity that owns the External Account.

    - `business` - The External Account is owned by a business.
    - `individual` - The External Account is owned by an individual.
    """

    description: str
    """The description you choose to give the external account."""

    status: Literal["active", "archived"]
    """The status of the External Account.

    - `active` - The External Account is active.
    - `archived` - The External Account is archived and won't appear in the
      dashboard.
    """
