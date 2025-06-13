# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PhysicalCardAdvanceShipmentParams"]


class PhysicalCardAdvanceShipmentParams(TypedDict, total=False):
    shipment_status: Required[
        Literal[
            "pending", "canceled", "submitted", "acknowledged", "rejected", "shipped", "returned", "requires_attention"
        ]
    ]
    """The shipment status to move the Physical Card to.

    - `pending` - The physical card has not yet been shipped.
    - `canceled` - The physical card shipment was canceled prior to submission.
    - `submitted` - The physical card shipment has been submitted to the card
      fulfillment provider.
    - `acknowledged` - The physical card shipment has been acknowledged by the card
      fulfillment provider and will be processed in their next batch.
    - `rejected` - The physical card shipment was rejected by the card printer due
      to an error.
    - `shipped` - The physical card has been shipped.
    - `returned` - The physical card shipment was returned to the sender and
      destroyed by the production facility.
    - `requires_attention` - The physical card shipment requires attention from
      Increase before progressing.
    """
