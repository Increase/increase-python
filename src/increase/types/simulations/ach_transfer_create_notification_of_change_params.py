# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ACHTransferCreateNotificationOfChangeParams"]


class ACHTransferCreateNotificationOfChangeParams(TypedDict, total=False):
    change_code: Required[
        Literal[
            "incorrect_account_number",
            "incorrect_routing_number",
            "incorrect_routing_number_and_account_number",
            "incorrect_transaction_code",
            "incorrect_account_number_and_transaction_code",
            "incorrect_routing_number_account_number_and_transaction_code",
            "incorrect_receiving_depository_financial_institution_identification",
            "incorrect_individual_identification_number",
            "addenda_format_error",
            "incorrect_standard_entry_class_code_for_outbound_international_payment",
            "misrouted_notification_of_change",
            "incorrect_trace_number",
            "incorrect_company_identification_number",
            "incorrect_identification_number",
            "incorrectly_formatted_corrected_data",
            "incorrect_discretionary_data",
            "routing_number_not_from_original_entry_detail_record",
            "depository_financial_institution_account_number_not_from_original_entry_detail_record",
            "incorrect_transaction_code_by_originating_depository_financial_institution",
        ]
    ]
    """The reason for the notification of change.

    - `incorrect_account_number` - The account number was incorrect.
    - `incorrect_routing_number` - The routing number was incorrect.
    - `incorrect_routing_number_and_account_number` - Both the routing number and
      the account number were incorrect.
    - `incorrect_transaction_code` - The transaction code was incorrect. Try
      changing the `funding` parameter from checking to savings or vice-versa.
    - `incorrect_account_number_and_transaction_code` - The account number and the
      transaction code were incorrect.
    - `incorrect_routing_number_account_number_and_transaction_code` - The routing
      number, account number, and transaction code were incorrect.
    - `incorrect_receiving_depository_financial_institution_identification` - The
      receiving depository financial institution identification was incorrect.
    - `incorrect_individual_identification_number` - The individual identification
      number was incorrect.
    - `addenda_format_error` - The addenda had an incorrect format.
    - `incorrect_standard_entry_class_code_for_outbound_international_payment` - The
      standard entry class code was incorrect for an outbound international payment.
    - `misrouted_notification_of_change` - The notification of change was misrouted.
    - `incorrect_trace_number` - The trace number was incorrect.
    - `incorrect_company_identification_number` - The company identification number
      was incorrect.
    - `incorrect_identification_number` - The individual identification number or
      identification number was incorrect.
    - `incorrectly_formatted_corrected_data` - The corrected data was incorrectly
      formatted.
    - `incorrect_discretionary_data` - The discretionary data was incorrect.
    - `routing_number_not_from_original_entry_detail_record` - The routing number
      was not from the original entry detail record.
    - `depository_financial_institution_account_number_not_from_original_entry_detail_record` -
      The depository financial institution account number was not from the original
      entry detail record.
    - `incorrect_transaction_code_by_originating_depository_financial_institution` -
      The transaction code was incorrect, initiated by the originating depository
      financial institution.
    """

    corrected_data: Required[str]
    """The corrected data for the notification of change (e.g., a new routing number)."""
