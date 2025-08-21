# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InboundWireTransferCreateParams"]


class InboundWireTransferCreateParams(TypedDict, total=False):
    account_number_id: Required[str]
    """The identifier of the Account Number the inbound Wire Transfer is for."""

    amount: Required[int]
    """The transfer amount in cents. Must be positive."""

    creditor_address_line1: str
    """The sending bank will set creditor_address_line1 in production.

    You can simulate any value here.
    """

    creditor_address_line2: str
    """The sending bank will set creditor_address_line2 in production.

    You can simulate any value here.
    """

    creditor_address_line3: str
    """The sending bank will set creditor_address_line3 in production.

    You can simulate any value here.
    """

    creditor_name: str
    """The sending bank will set creditor_name in production.

    You can simulate any value here.
    """

    debtor_address_line1: str
    """The sending bank will set debtor_address_line1 in production.

    You can simulate any value here.
    """

    debtor_address_line2: str
    """The sending bank will set debtor_address_line2 in production.

    You can simulate any value here.
    """

    debtor_address_line3: str
    """The sending bank will set debtor_address_line3 in production.

    You can simulate any value here.
    """

    debtor_name: str
    """The sending bank will set debtor_name in production.

    You can simulate any value here.
    """

    end_to_end_identification: str
    """The sending bank will set end_to_end_identification in production.

    You can simulate any value here.
    """

    instructing_agent_routing_number: str
    """The sending bank will set instructing_agent_routing_number in production.

    You can simulate any value here.
    """

    instruction_identification: str
    """The sending bank will set instruction_identification in production.

    You can simulate any value here.
    """

    unique_end_to_end_transaction_reference: str
    """The sending bank will set unique_end_to_end_transaction_reference in production.

    You can simulate any value here.
    """

    unstructured_remittance_information: str
    """The sending bank will set unstructured_remittance_information in production.

    You can simulate any value here.
    """

    wire_drawdown_request_id: str
    """
    The identifier of a Wire Drawdown Request the inbound Wire Transfer is
    fulfilling.
    """
