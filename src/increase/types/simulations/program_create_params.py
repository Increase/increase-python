# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProgramCreateParams"]


class ProgramCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the program being added."""

    bank: Literal["blue_ridge_bank", "core_bank", "first_internet_bank", "global_innovations_bank", "grasshopper_bank"]
    """The bank for the program's accounts, defaults to First Internet Bank.

    - `blue_ridge_bank` - Blue Ridge Bank, N.A.
    - `core_bank` - Core Bank
    - `first_internet_bank` - First Internet Bank of Indiana
    - `global_innovations_bank` - Global Innovations Bank
    - `grasshopper_bank` - Grasshopper Bank
    """

    reserve_account_id: str
    """The identifier of the Account the Program should be added to is for."""
