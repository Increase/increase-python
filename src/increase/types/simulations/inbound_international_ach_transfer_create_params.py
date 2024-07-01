# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InboundInternationalACHTransferCreateParams"]


class InboundInternationalACHTransferCreateParams(TypedDict, total=False):
    account_number_id: Required[str]
    """
    The identifier of the Account Number the inbound international ACH Transfer is
    for.
    """

    amount: Required[int]
    """The transfer amount in cents.

    A positive amount originates a credit transfer pushing funds to the receiving
    account. A negative amount originates a debit transfer pulling funds from the
    receiving account.
    """

    foreign_payment_amount: Required[int]
    """The amount in the minor unit of the foreign payment currency.

    For dollars, for example, this is cents.
    """

    originating_currency_code: Required[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code for the
    originating bank account.
    """

    originator_company_entry_description: str
    """A description field set by the originator."""

    originator_name: str
    """Either the name of the originator or an intermediary money transmitter."""

    receiving_company_or_individual_name: str
    """The name of the receiver of the transfer."""
