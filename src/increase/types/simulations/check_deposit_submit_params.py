# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CheckDepositSubmitParams", "Scan"]


class CheckDepositSubmitParams(TypedDict, total=False):
    scan: Scan
    """If set, the simulation will use these values for the check's scanned MICR data."""


class Scan(TypedDict, total=False):
    """If set, the simulation will use these values for the check's scanned MICR data."""

    account_number: Required[str]
    """The account number to be returned in the check deposit's scan data."""

    routing_number: Required[str]
    """The routing number to be returned in the check deposit's scan data."""

    auxiliary_on_us: str
    """The auxiliary on-us data to be returned in the check deposit's scan data."""
