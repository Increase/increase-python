# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    Account,
    BalanceLookup,
)
from increase._utils import parse_datetime
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestAccounts:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        account = client.accounts.create(
            name="New Account!",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        account = client.accounts.create(
            name="New Account!",
            entity_id="entity_n8y8tnk2p9339ti393yi",
            informational_entity_id="string",
            program_id="program_i2v2os4mwza1oetokh9i",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.accounts.with_raw_response.create(
            name="New Account!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.accounts.with_streaming_response.create(
            name="New Account!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        account = client.accounts.retrieve(
            "string",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.accounts.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.accounts.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        account = client.accounts.update(
            "string",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Increase) -> None:
        account = client.accounts.update(
            "string",
            name="My renamed account",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Increase) -> None:
        response = client.accounts.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Increase) -> None:
        with client.accounts.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        account = client.accounts.list()
        assert_matches_type(SyncPage[Account], account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        account = client.accounts.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            entity_id="string",
            informational_entity_id="string",
            limit=1,
            status="open",
        )
        assert_matches_type(SyncPage[Account], account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(SyncPage[Account], account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(SyncPage[Account], account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_balance(self, client: Increase) -> None:
        account = client.accounts.balance(
            "string",
        )
        assert_matches_type(BalanceLookup, account, path=["response"])

    @parametrize
    def test_method_balance_with_all_params(self, client: Increase) -> None:
        account = client.accounts.balance(
            "string",
            at_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BalanceLookup, account, path=["response"])

    @parametrize
    def test_raw_response_balance(self, client: Increase) -> None:
        response = client.accounts.with_raw_response.balance(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(BalanceLookup, account, path=["response"])

    @parametrize
    def test_streaming_response_balance(self, client: Increase) -> None:
        with client.accounts.with_streaming_response.balance(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(BalanceLookup, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_balance(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.balance(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_method_close(self, client: Increase) -> None:
        account = client.accounts.close(
            "string",
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_raw_response_close(self, client: Increase) -> None:
        response = client.accounts.with_raw_response.close(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_streaming_response_close(self, client: Increase) -> None:
        with client.accounts.with_streaming_response.close(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_path_params_close(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.close(
                "",
            )


class TestAsyncAccounts:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        account = await client.accounts.create(
            name="New Account!",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        account = await client.accounts.create(
            name="New Account!",
            entity_id="entity_n8y8tnk2p9339ti393yi",
            informational_entity_id="string",
            program_id="program_i2v2os4mwza1oetokh9i",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.accounts.with_raw_response.create(
            name="New Account!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncIncrease) -> None:
        async with client.accounts.with_streaming_response.create(
            name="New Account!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        account = await client.accounts.retrieve(
            "string",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.accounts.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncIncrease) -> None:
        async with client.accounts.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await client.accounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, client: AsyncIncrease) -> None:
        account = await client.accounts.update(
            "string",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncIncrease) -> None:
        account = await client.accounts.update(
            "string",
            name="My renamed account",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncIncrease) -> None:
        response = await client.accounts.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, client: AsyncIncrease) -> None:
        async with client.accounts.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await client.accounts.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        account = await client.accounts.list()
        assert_matches_type(AsyncPage[Account], account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        account = await client.accounts.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            entity_id="string",
            informational_entity_id="string",
            limit=1,
            status="open",
        )
        assert_matches_type(AsyncPage[Account], account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AsyncPage[Account], account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncIncrease) -> None:
        async with client.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AsyncPage[Account], account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_balance(self, client: AsyncIncrease) -> None:
        account = await client.accounts.balance(
            "string",
        )
        assert_matches_type(BalanceLookup, account, path=["response"])

    @parametrize
    async def test_method_balance_with_all_params(self, client: AsyncIncrease) -> None:
        account = await client.accounts.balance(
            "string",
            at_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BalanceLookup, account, path=["response"])

    @parametrize
    async def test_raw_response_balance(self, client: AsyncIncrease) -> None:
        response = await client.accounts.with_raw_response.balance(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(BalanceLookup, account, path=["response"])

    @parametrize
    async def test_streaming_response_balance(self, client: AsyncIncrease) -> None:
        async with client.accounts.with_streaming_response.balance(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(BalanceLookup, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_balance(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await client.accounts.with_raw_response.balance(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_method_close(self, client: AsyncIncrease) -> None:
        account = await client.accounts.close(
            "string",
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_raw_response_close(self, client: AsyncIncrease) -> None:
        response = await client.accounts.with_raw_response.close(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_streaming_response_close(self, client: AsyncIncrease) -> None:
        async with client.accounts.with_streaming_response.close(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_path_params_close(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await client.accounts.with_raw_response.close(
                "",
            )
