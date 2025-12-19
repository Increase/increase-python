# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExportCreateParams", "Form1099Int"]


class ExportCreateParams(TypedDict, total=False):
    category: Required[Literal["form_1099_int"]]
    """The type of Export to create.

    - `form_1099_int` - A PDF of an Internal Revenue Service Form 1099-INT.
    """

    form_1099_int: Form1099Int
    """Options for the created export.

    Required if `category` is equal to `form_1099_int`.
    """


class Form1099Int(TypedDict, total=False):
    """Options for the created export.

    Required if `category` is equal to `form_1099_int`.
    """

    account_id: Required[str]
    """The identifier of the Account the tax document is for."""
