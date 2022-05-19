# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

from increase import Increase, AsyncIncrease
from increase.types.group import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestGroups:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_retrieve_details(self) -> None:
        resource = self.client.groups.retrieve_details()
        assert isinstance(resource, Group)


class TestAsyncGroups:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_retrieve_details(self) -> None:
        resource = await self.client.groups.retrieve_details()
        assert isinstance(resource, Group)
