# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InboundWireDrawdownRequestCreateParams"]


class InboundWireDrawdownRequestCreateParams(TypedDict, total=False):
    amount: Required[int]
    """The amount being requested in cents."""

    beneficiary_account_number: Required[str]
    """The drawdown request's beneficiary's account number."""

    beneficiary_routing_number: Required[str]
    """The drawdown request's beneficiary's routing number."""

    currency: Required[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the amount being
    requested. Will always be "USD".
    """

    message_to_recipient: Required[str]
    """A message from the drawdown request's originator."""

    originator_account_number: Required[str]
    """The drawdown request's originator's account number."""

    originator_routing_number: Required[str]
    """The drawdown request's originator's routing number."""

    recipient_account_number_id: Required[str]
    """
    The Account Number to which the recipient of this request is being requested to
    send funds from.
    """

    beneficiary_address_line1: str
    """Line 1 of the drawdown request's beneficiary's address."""

    beneficiary_address_line2: str
    """Line 2 of the drawdown request's beneficiary's address."""

    beneficiary_address_line3: str
    """Line 3 of the drawdown request's beneficiary's address."""

    beneficiary_name: str
    """The drawdown request's beneficiary's name."""

    originator_address_line1: str
    """Line 1 of the drawdown request's originator's address."""

    originator_address_line2: str
    """Line 2 of the drawdown request's originator's address."""

    originator_address_line3: str
    """Line 3 of the drawdown request's originator's address."""

    originator_name: str
    """The drawdown request's originator's name."""

    originator_to_beneficiary_information_line1: str
    """
    Line 1 of the information conveyed from the originator of the message to the
    beneficiary.
    """

    originator_to_beneficiary_information_line2: str
    """
    Line 2 of the information conveyed from the originator of the message to the
    beneficiary.
    """

    originator_to_beneficiary_information_line3: str
    """
    Line 3 of the information conveyed from the originator of the message to the
    beneficiary.
    """

    originator_to_beneficiary_information_line4: str
    """
    Line 4 of the information conveyed from the originator of the message to the
    beneficiary.
    """
