# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .inbound_mail_item import InboundMailItem

__all__ = ["InboundMailItemList"]


class InboundMailItemList(BaseModel):
    data: List[InboundMailItem]
    """The contents of the list."""

    next_cursor: Optional[str] = None
    """A pointer to a place in the list."""
