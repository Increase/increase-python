# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.types.simulations.account_transfer import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAccountTransfers:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    @pytest.mark.skip(reason="Prism tests are broken")
    def test_method_complete(self) -> None:
        resource = self.client.simulations.account_transfers.complete(
            "string",
        )
        assert isinstance(resource, AccountTransfer)


class TestAsyncAccountTransfers:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    @pytest.mark.skip(reason="Prism tests are broken")
    async def test_method_complete(self) -> None:
        resource = await self.client.simulations.account_transfers.complete(
            "string",
        )
        assert isinstance(resource, AccountTransfer)
