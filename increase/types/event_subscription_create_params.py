# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EventSubscriptionCreateParams"]


class EventSubscriptionCreateParams(TypedDict, total=False):
    url: Required[str]
    """The URL you'd like us to send webhooks to."""

    shared_secret: str
    """The key that will be used to sign webhooks.

    If no value is passed, a random string will be used as default.
    """
