# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import BalanceLookupLookupResponse
from increase._utils import parse_datetime
from increase._client import Increase, AsyncIncrease

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestBalanceLookups:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_lookup(self, client: Increase) -> None:
        balance_lookup = client.balance_lookups.lookup(
            account_id="account_in71c4amph0vgo2qllky",
        )
        assert_matches_type(BalanceLookupLookupResponse, balance_lookup, path=["response"])

    @parametrize
    def test_method_lookup_with_all_params(self, client: Increase) -> None:
        balance_lookup = client.balance_lookups.lookup(
            account_id="account_in71c4amph0vgo2qllky",
            at_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BalanceLookupLookupResponse, balance_lookup, path=["response"])

    @parametrize
    def test_raw_response_lookup(self, client: Increase) -> None:
        response = client.balance_lookups.with_raw_response.lookup(
            account_id="account_in71c4amph0vgo2qllky",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_lookup = response.parse()
        assert_matches_type(BalanceLookupLookupResponse, balance_lookup, path=["response"])


class TestAsyncBalanceLookups:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_lookup(self, client: AsyncIncrease) -> None:
        balance_lookup = await client.balance_lookups.lookup(
            account_id="account_in71c4amph0vgo2qllky",
        )
        assert_matches_type(BalanceLookupLookupResponse, balance_lookup, path=["response"])

    @parametrize
    async def test_method_lookup_with_all_params(self, client: AsyncIncrease) -> None:
        balance_lookup = await client.balance_lookups.lookup(
            account_id="account_in71c4amph0vgo2qllky",
            at_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BalanceLookupLookupResponse, balance_lookup, path=["response"])

    @parametrize
    async def test_raw_response_lookup(self, client: AsyncIncrease) -> None:
        response = await client.balance_lookups.with_raw_response.lookup(
            account_id="account_in71c4amph0vgo2qllky",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_lookup = response.parse()
        assert_matches_type(BalanceLookupLookupResponse, balance_lookup, path=["response"])
