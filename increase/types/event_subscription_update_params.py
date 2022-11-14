# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["EventSubscriptionUpdateParams"]

class EventSubscriptionUpdateParams(TypedDict, total=False):
    status: Literal["active", "disabled", "deleted"]
    """The status to update the Event Subscription with."""