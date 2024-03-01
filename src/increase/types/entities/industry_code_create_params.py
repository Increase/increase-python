# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IndustryCodeCreateParams"]


class IndustryCodeCreateParams(TypedDict, total=False):
    industry_code: Required[str]
    """
    The North American Industry Classification System (NAICS) code for the
    corporation's primary line of business. This is a number, like `5132` for
    `Software Publishers`. A full list of classification codes is available at
    https://www.naics.com.
    """
