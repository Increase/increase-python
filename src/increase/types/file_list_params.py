# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FileListParams", "CreatedAt", "Purpose"]


class FileListParams(TypedDict, total=False):
    created_at: CreatedAt

    cursor: str
    """Return the page of entries after this one."""

    idempotency_key: str
    """
    Filter records to the one with the specified `idempotency_key` you chose for
    that object. This value is unique across Increase and is used to ensure that a
    request is only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """

    purpose: Purpose


class CreatedAt(TypedDict, total=False):
    after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    timestamp.
    """

    before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    timestamp.
    """

    on_or_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results on or after this
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp.
    """

    on_or_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results on or before this
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp.
    """


_PurposeReservedKeywords = TypedDict(
    "_PurposeReservedKeywords",
    {
        "in": List[
            Literal[
                "card_dispute_attachment",
                "check_image_front",
                "check_image_back",
                "processed_check_image_front",
                "processed_check_image_back",
                "mailed_check_image",
                "check_attachment",
                "inbound_mail_item",
                "form_1099_int",
                "form_1099_misc",
                "form_ss_4",
                "identity_document",
                "increase_statement",
                "other",
                "trust_formation_document",
                "digital_wallet_artwork",
                "digital_wallet_app_icon",
                "physical_card_front",
                "physical_card_back",
                "physical_card_carrier",
                "document_request",
                "entity_supplemental_document",
                "export",
                "unusual_activity_report_attachment",
                "deposit_account_control_agreement",
                "proof_of_authorization_request_submission",
                "account_verification_letter",
                "funding_instructions",
                "hold_harmless_letter",
            ]
        ],
    },
    total=False,
)


class Purpose(_PurposeReservedKeywords, total=False):
    pass
