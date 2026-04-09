# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EntityOnboardingSessionCreateParams"]


class EntityOnboardingSessionCreateParams(TypedDict, total=False):
    program_id: Required[str]
    """The identifier of the Program the Entity will be onboarded to."""

    redirect_url: Required[str]
    """The URL to redirect the customer to after they complete the onboarding form.

    The redirect will include `entity_onboarding_session_id` and `entity_id` query
    parameters.
    """

    entity_id: str
    """The identifier of an existing Entity to associate with the onboarding session.

    If provided, the onboarding form will display any outstanding tasks required to
    complete the Entity's onboarding.
    """
