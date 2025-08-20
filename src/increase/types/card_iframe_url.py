# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardIframeURL"]


class CardIframeURL(BaseModel):
    expires_at: datetime
    """The time the iframe URL will expire."""

    iframe_url: str
    """The iframe URL for the Card. Treat this as an opaque URL."""

    type: Literal["card_iframe_url"]
    """A constant representing the object's type.

    For this resource it will always be `card_iframe_url`.
    """
