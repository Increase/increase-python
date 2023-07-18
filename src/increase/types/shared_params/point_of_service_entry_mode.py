# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

__all__ = ["PointOfServiceEntryMode"]

PointOfServiceEntryMode = Optional[
    Literal[
        "unknown",
        "manual",
        "magnetic_stripe_no_cvv",
        "optical_code",
        "integrated_circuit_card",
        "contactless",
        "credential_on_file",
        "magnetic_stripe",
        "contactless_magnetic_stripe",
        "integrated_circuit_card_no_cvv",
    ]
]
