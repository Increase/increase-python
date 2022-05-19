# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EventSubscription"]


class EventSubscription(BaseModel):
    created_at: str
    """The time the event subscription was created."""

    id: str
    """The event subscription identifier."""

    shared_secret: str
    """The key that will be used to sign webhooks."""

    status: Literal["active", "disabled", "deleted", "requires_attention"]
    """This indicates if we'll send notifications to this subscription."""

    type: Literal["event_subscription"]
    """A constant representing the object's type.

    For this resource it will always be `event_subscription`.
    """

    url: str
    """The webhook url where we'll send notifications."""
