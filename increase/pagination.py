# File generated from our OpenAPI spec by Stainless.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import TypedDict

from pydantic import BaseModel

from ._types import ModelT
from ._base_client import BasePage, BaseSyncPage, BaseAsyncPage

__all__ = ["PageParams", "SyncPage", "AsyncPage"]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)


class PageParams(TypedDict, total=False):
    cursor: str
    """Return the page of entries after this one."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """


class SyncPage(BaseSyncPage[ModelT], BasePage[ModelT, PageParams], Generic[ModelT]):
    data: List[ModelT]
    next_cursor: Optional[str]

    def _get_page_items(self) -> List[ModelT]:
        return self.data

    def next_page_params(self) -> Optional[PageParams]:
        cursor = self.next_cursor
        if not cursor:
            return None

        return {"cursor": cursor}


class AsyncPage(BaseAsyncPage[ModelT], BasePage[ModelT, PageParams], Generic[ModelT]):
    data: List[ModelT]
    next_cursor: Optional[str]

    def _get_page_items(self) -> List[ModelT]:
        return self.data

    def next_page_params(self) -> Optional[PageParams]:
        cursor = self.next_cursor
        if not cursor:
            return None

        return {"cursor": cursor}
