# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
            informational_entity_id="informational_entity_id",
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
            "account_id",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.accounts.with_raw_response.retrieve(
            "account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.accounts.with_streaming_response.retrieve(
            "account_id",
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
            account_id="account_in71c4amph0vgo2qllky",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Increase) -> None:
        account = client.accounts.update(
            account_id="account_in71c4amph0vgo2qllky",
            credit_limit=0,
            name="My renamed account",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Increase) -> None:
        response = client.accounts.with_raw_response.update(
            account_id="account_in71c4amph0vgo2qllky",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Increase) -> None:
        with client.accounts.with_streaming_response.update(
            account_id="account_in71c4amph0vgo2qllky",
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
                account_id="",
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
            cursor="cursor",
            entity_id="entity_id",
            idempotency_key="x",
            informational_entity_id="informational_entity_id",
            limit=1,
            program_id="program_id",
            status={"in": ["closed"]},
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
            account_id="account_in71c4amph0vgo2qllky",
        )
        assert_matches_type(BalanceLookup, account, path=["response"])

    @parametrize
    def test_method_balance_with_all_params(self, client: Increase) -> None:
        account = client.accounts.balance(
            account_id="account_in71c4amph0vgo2qllky",
            at_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BalanceLookup, account, path=["response"])

    @parametrize
    def test_raw_response_balance(self, client: Increase) -> None:
        response = client.accounts.with_raw_response.balance(
            account_id="account_in71c4amph0vgo2qllky",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(BalanceLookup, account, path=["response"])

    @parametrize
    def test_streaming_response_balance(self, client: Increase) -> None:
        with client.accounts.with_streaming_response.balance(
            account_id="account_in71c4amph0vgo2qllky",
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
                account_id="",
            )

    @parametrize
    def test_method_close(self, client: Increase) -> None:
        account = client.accounts.close(
            "account_id",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_raw_response_close(self, client: Increase) -> None:
        response = client.accounts.with_raw_response.close(
            "account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_streaming_response_close(self, client: Increase) -> None:
        with client.accounts.with_streaming_response.close(
            "account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_close(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.close(
                "",
            )


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        account = await async_client.accounts.create(
            name="New Account!",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        account = await async_client.accounts.create(
            name="New Account!",
            entity_id="entity_n8y8tnk2p9339ti393yi",
            informational_entity_id="informational_entity_id",
            program_id="program_i2v2os4mwza1oetokh9i",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.accounts.with_raw_response.create(
            name="New Account!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.accounts.with_streaming_response.create(
            name="New Account!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        account = await async_client.accounts.retrieve(
            "account_id",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.accounts.with_raw_response.retrieve(
            "account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.accounts.with_streaming_response.retrieve(
            "account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncIncrease) -> None:
        account = await async_client.accounts.update(
            account_id="account_in71c4amph0vgo2qllky",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncIncrease) -> None:
        account = await async_client.accounts.update(
            account_id="account_in71c4amph0vgo2qllky",
            credit_limit=0,
            name="My renamed account",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIncrease) -> None:
        response = await async_client.accounts.with_raw_response.update(
            account_id="account_in71c4amph0vgo2qllky",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIncrease) -> None:
        async with async_client.accounts.with_streaming_response.update(
            account_id="account_in71c4amph0vgo2qllky",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.update(
                account_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        account = await async_client.accounts.list()
        assert_matches_type(AsyncPage[Account], account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        account = await async_client.accounts.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            entity_id="entity_id",
            idempotency_key="x",
            informational_entity_id="informational_entity_id",
            limit=1,
            program_id="program_id",
            status={"in": ["closed"]},
        )
        assert_matches_type(AsyncPage[Account], account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AsyncPage[Account], account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AsyncPage[Account], account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_balance(self, async_client: AsyncIncrease) -> None:
        account = await async_client.accounts.balance(
            account_id="account_in71c4amph0vgo2qllky",
        )
        assert_matches_type(BalanceLookup, account, path=["response"])

    @parametrize
    async def test_method_balance_with_all_params(self, async_client: AsyncIncrease) -> None:
        account = await async_client.accounts.balance(
            account_id="account_in71c4amph0vgo2qllky",
            at_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BalanceLookup, account, path=["response"])

    @parametrize
    async def test_raw_response_balance(self, async_client: AsyncIncrease) -> None:
        response = await async_client.accounts.with_raw_response.balance(
            account_id="account_in71c4amph0vgo2qllky",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(BalanceLookup, account, path=["response"])

    @parametrize
    async def test_streaming_response_balance(self, async_client: AsyncIncrease) -> None:
        async with async_client.accounts.with_streaming_response.balance(
            account_id="account_in71c4amph0vgo2qllky",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(BalanceLookup, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_balance(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.balance(
                account_id="",
            )

    @parametrize
    async def test_method_close(self, async_client: AsyncIncrease) -> None:
        account = await async_client.accounts.close(
            "account_id",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_raw_response_close(self, async_client: AsyncIncrease) -> None:
        response = await async_client.accounts.with_raw_response.close(
            "account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_streaming_response_close(self, async_client: AsyncIncrease) -> None:
        async with async_client.accounts.with_streaming_response.close(
            "account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_close(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.close(
                "",
            )
