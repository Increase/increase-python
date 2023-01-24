# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WireTransferCreateInboundParams"]


class WireTransferCreateInboundParams(TypedDict, total=False):
    account_number_id: Required[str]
    """The identifier of the Account Number the inbound Wire Transfer is for."""

    amount: Required[int]
    """The transfer amount in cents. Must be positive."""

    beneficiary_address_line1: str
    """The sending bank will set beneficiary_address_line1 in production.

    You can simulate any value here.
    """

    beneficiary_address_line2: str
    """The sending bank will set beneficiary_address_line2 in production.

    You can simulate any value here.
    """

    beneficiary_address_line3: str
    """The sending bank will set beneficiary_address_line3 in production.

    You can simulate any value here.
    """

    beneficiary_name: str
    """The sending bank will set beneficiary_name in production.

    You can simulate any value here.
    """

    beneficiary_reference: str
    """The sending bank will set beneficiary_reference in production.

    You can simulate any value here.
    """

    originator_address_line1: str
    """The sending bank will set originator_address_line1 in production.

    You can simulate any value here.
    """

    originator_address_line2: str
    """The sending bank will set originator_address_line2 in production.

    You can simulate any value here.
    """

    originator_address_line3: str
    """The sending bank will set originator_address_line3 in production.

    You can simulate any value here.
    """

    originator_name: str
    """The sending bank will set originator_name in production.

    You can simulate any value here.
    """

    originator_to_beneficiary_information_line1: str
    """
    The sending bank will set originator_to_beneficiary_information_line1 in
    production. You can simulate any value here.
    """

    originator_to_beneficiary_information_line2: str
    """
    The sending bank will set originator_to_beneficiary_information_line2 in
    production. You can simulate any value here.
    """

    originator_to_beneficiary_information_line3: str
    """
    The sending bank will set originator_to_beneficiary_information_line3 in
    production. You can simulate any value here.
    """

    originator_to_beneficiary_information_line4: str
    """
    The sending bank will set originator_to_beneficiary_information_line4 in
    production. You can simulate any value here.
    """
