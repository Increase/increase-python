# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountStatement"]


class AccountStatement(BaseModel):
    """Account Statements are generated monthly for every active Account.

    You can access the statement's data via the API or retrieve a PDF with its details via its associated File.
    """

    id: str
    """The Account Statement identifier."""

    account_id: str
    """The identifier for the Account this Account Statement belongs to."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Account
    Statement was created.
    """

    ending_balance: int
    """The Account's balance at the start of its statement period."""

    file_id: str
    """The identifier of the File containing a PDF of the statement."""

    starting_balance: int
    """The Account's balance at the start of its statement period."""

    statement_period_end: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time representing the end
    of the period the Account Statement covers.
    """

    statement_period_start: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time representing the
    start of the period the Account Statement covers.
    """

    type: Literal["account_statement"]
    """A constant representing the object's type.

    For this resource it will always be `account_statement`.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
