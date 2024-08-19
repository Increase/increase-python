# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InboundCheckDepositReturnParams"]


class InboundCheckDepositReturnParams(TypedDict, total=False):
    reason: Required[
        Literal[
            "altered_or_fictitious",
            "not_authorized",
            "duplicate_presentment",
            "endorsement_missing",
            "endorsement_irregular",
        ]
    ]
    """The reason to return the Inbound Check Deposit.

    - `altered_or_fictitious` - The check was altered or fictitious.
    - `not_authorized` - The check was not authorized.
    - `duplicate_presentment` - The check was a duplicate presentment.
    - `endorsement_missing` - The check was not endorsed.
    - `endorsement_irregular` - The check was not endorsed by the payee.
    """
