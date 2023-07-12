# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    file: Required[FileTypes]
    """The file contents.

    This should follow the specifications of
    [RFC 7578](https://datatracker.ietf.org/doc/html/rfc7578) which defines file
    transfers for the multipart/form-data protocol.
    """

    purpose: Required[
        Literal[
            "check_image_front",
            "check_image_back",
            "form_ss_4",
            "identity_document",
            "other",
            "trust_formation_document",
            "digital_wallet_artwork",
            "digital_wallet_app_icon",
            "physical_card_front",
            "physical_card_carrier",
            "document_request",
            "entity_supplemental_document",
        ]
    ]
    """What the File will be used for in Increase's systems.

    - `check_image_front` - An image of the front of a check, used for check
      deposits.
    - `check_image_back` - An image of the back of a check, used for check deposits.
    - `form_ss_4` - IRS Form SS-4.
    - `identity_document` - An image of a government-issued ID.
    - `other` - A file purpose not covered by any of the other cases.
    - `trust_formation_document` - A legal document forming a trust.
    - `digital_wallet_artwork` - A card image to be rendered inside digital wallet
      apps. This must be a 1536x969 pixel PNG.
    - `digital_wallet_app_icon` - An icon for you app to be rendered inside digital
      wallet apps. This must be a 100x100 pixel PNG.
    - `physical_card_front` - A card image to be printed on the front of a physical
      card. This must be a 2100x1340 pixel PNG with no other color but black.
    - `physical_card_carrier` - An image representing the entirety of the carrier
      used for a physical card. This must be a 2550x3300 pixel PNG with no other
      color but black.
    - `document_request` - A document requested by Increase.
    - `entity_supplemental_document` - A supplemental document associated an an
      Entity.
    """

    description: str
    """The description you choose to give the File."""
