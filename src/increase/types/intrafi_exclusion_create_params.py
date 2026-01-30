# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IntrafiExclusionCreateParams"]


class IntrafiExclusionCreateParams(TypedDict, total=False):
    entity_id: Required[str]
    """The identifier of the Entity whose deposits will be excluded."""

    fdic_certificate_number: Required[str]
    """The FDIC certificate number of the financial institution to be excluded.

    An FDIC certificate number uniquely identifies a financial institution, and is
    different than a routing number. To find one, we recommend searching by Bank
    Name using the
    [FDIC's bankfind tool](https://banks.data.fdic.gov/bankfind-suite/bankfind).
    """
