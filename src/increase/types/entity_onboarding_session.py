# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EntityOnboardingSession"]


class EntityOnboardingSession(BaseModel):
    """
    Entity Onboarding Sessions let your customers onboard themselves by completing Increase-hosted forms. Create a session and redirect your customer to the returned URL. When they're done, they'll be redirected back to your site. This API is used for [hosted onboarding](/documentation/hosted-onboarding).
    """

    id: str
    """The Entity Onboarding Session's identifier."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Entity Onboarding Session was created.
    """

    entity_id: Optional[str] = None
    """
    The identifier of the Entity associated with this session, if one has been
    created or was provided when creating the session.
    """

    expires_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Entity Onboarding Session will expire.
    """

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    program_id: str
    """The identifier of the Program the Entity will be onboarded to."""

    redirect_url: str
    """The URL to redirect to after the onboarding session is complete.

    Increase will include the query parameters `entity_onboarding_session_id` and
    `entity_id` when redirecting.
    """

    session_url: Optional[str] = None
    """The URL containing the onboarding form.

    You should share this link with your customer. Only present when the session is
    active.
    """

    status: Literal["active", "expired"]
    """The status of the onboarding session.

    - `active` - The Entity Onboarding Session is active.
    - `expired` - The Entity Onboarding Session has expired.
    """

    type: Literal["entity_onboarding_session"]
    """A constant representing the object's type.

    For this resource it will always be `entity_onboarding_session`.
    """
