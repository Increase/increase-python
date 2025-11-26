# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from pydantic import Field as FieldInfo

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncPage", "AsyncPage"]

_T = TypeVar("_T")


class SyncPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[object] = FieldInfo(alias=":data", default=None)
    next_cursor: Optional[object] = FieldInfo(alias=":next_cursor", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={":cursor": next_cursor})


class AsyncPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[object] = FieldInfo(alias=":data", default=None)
    next_cursor: Optional[object] = FieldInfo(alias=":next_cursor", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={":cursor": next_cursor})
