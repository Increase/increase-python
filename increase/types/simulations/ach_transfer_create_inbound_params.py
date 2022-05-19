# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ACHTransferCreateInboundParams"]


class ACHTransferCreateInboundParams(TypedDict, total=False):
    account_number_id: Required[str]
    """The identifier of the Account Number the inbound ACH Transfer is for."""

    amount: Required[int]
    """The transfer amount in cents.

    A positive amount originates a credit transfer pushing funds to the receiving
    account. A negative amount originates a debit transfer pulling funds from the
    receiving account.
    """
