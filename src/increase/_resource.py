# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._client import Increase, AsyncIncrease


class SyncAPIResource:
    _client: Increase

    def __init__(self, client: Increase) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete
        self._get_api_list = client.get_api_list


class AsyncAPIResource:
    _client: AsyncIncrease

    def __init__(self, client: AsyncIncrease) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete
        self._get_api_list = client.get_api_list
