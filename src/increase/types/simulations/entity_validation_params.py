# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["EntityValidationParams", "Issue"]


class EntityValidationParams(TypedDict, total=False):
    issues: Required[Iterable[Issue]]
    """The validation issues to attach. Only allowed when `status` is `invalid`."""

    status: Required[Literal["valid", "invalid", "pending"]]
    """The validation status to set on the Entity.

    - `valid` - The submitted data is valid.
    - `invalid` - Additional information is required to validate the data.
    - `pending` - The submitted data is being validated.
    """


class Issue(TypedDict, total=False):
    category: Required[
        Literal["entity_tax_identifier", "entity_address", "beneficial_owner_identity", "beneficial_owner_address"]
    ]
    """The type of issue.

    - `entity_tax_identifier` - The entity's tax identifier could not be validated.
      Update the tax ID with the
      [update an entity API](/documentation/api/entities#update-an-entity.corporation.legal_identifier).
    - `entity_address` - The entity's address could not be validated. Update the
      address with the
      [update an entity API](/documentation/api/entities#update-an-entity.corporation.address).
    - `beneficial_owner_identity` - A beneficial owner's identity could not be
      verified. Update the identification with the
      [update a beneficial owner API](/documentation/api/beneficial-owners#update-a-beneficial-owner).
    - `beneficial_owner_address` - A beneficial owner's address could not be
      validated. Update the address with the
      [update a beneficial owner API](/documentation/api/beneficial-owners#update-a-beneficial-owner).
    """
