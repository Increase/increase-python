# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountCreateParams"]


class AccountCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name you choose for the Account."""

    entity_id: str
    """The identifier for the Entity that will own the Account."""

    informational_entity_id: str
    """
    The identifier of an Entity that, while not owning the Account, is associated
    with its activity. Its relationship to your group must be `informational`.
    """

    program_id: str
    """The identifier for the Program that this Account falls under.

    Required if you operate more than one Program.
    """
