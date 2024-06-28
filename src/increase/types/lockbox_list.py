# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .lockbox import Lockbox
from .._models import BaseModel

__all__ = ["LockboxList"]


class LockboxList(BaseModel):
    data: List[Lockbox]
    """The contents of the list."""

    next_cursor: Optional[str] = None
    """A pointer to a place in the list."""
