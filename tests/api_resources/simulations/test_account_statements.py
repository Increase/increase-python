# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease

from increase.types.simulations.account_statement import AccountStatement

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")

class TestAccountStatements:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        resource = client.simulations.account_statements.create(
            account_id="string",
        )
        assert isinstance(resource, AccountStatement)

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        resource = client.simulations.account_statements.create(
            account_id="string",
        )
        assert isinstance(resource, AccountStatement)
class TestAsyncAccountStatements:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.account_statements.create(
            account_id="string",
        )
        assert isinstance(resource, AccountStatement)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.simulations.account_statements.create(
            account_id="string",
        )
        assert isinstance(resource, AccountStatement)