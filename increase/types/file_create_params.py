# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["FileCreateParams"]

class FileCreateParams(TypedDict, total=False):
    file: Required[FileTypes]
    """The file contents.

    This should follow the specifications of
    [RFC 7578](https://datatracker.ietf.org/doc/html/rfc7578) which defines file
    transfers for the multipart/form-data protocol.
    """

    purpose: Required[Literal["check_image_front", "check_image_back", "form_ss_4", "identity_document", "other", "trust_formation_document", "digital_wallet_artwork", "digital_wallet_app_icon", "entity_supplemental_document"]]
    """What the File will be used for in Increase's systems."""

    description: str
    """The description you choose to give the File."""