# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["WireDrawdownRequestRefuseParams"]


class WireDrawdownRequestRefuseParams(TypedDict, total=False):
    refusal_reason_additional_information: str
    """Additional information about the refusal that the simulated refusal will have."""

    refusal_reason_code: Literal[
        "invalid_debtor_account_number",
        "transaction_forbidden",
        "unsuccessful_direct_debit",
        "inconsistent_with_end_customer",
        "narrative",
        "other",
    ]
    """The reason code that the simulated refusal will have.

    - `invalid_debtor_account_number` - The debtor's account number is invalid or
      missing. Corresponds to the Fedwire reason code `AC02`.
    - `transaction_forbidden` - The debtor account does not allow drawdown requests.
      Corresponds to the Fedwire reason code `AG01`.
    - `unsuccessful_direct_debit` - The debtor account cannot be debited for a
      generic reason. Corresponds to the Fedwire reason code `AG07`.
    - `inconsistent_with_end_customer` - The debtor's identification is inconsistent
      with the debtor account number. Corresponds to the Fedwire reason code `BE01`.
    - `narrative` - The reason is provided as narrative information in the
      additional information field. Corresponds to the Fedwire reason code `NARR`.
    - `other` - Some other error or issue has occurred.
    """
