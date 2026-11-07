# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import CheckbookCheck
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheckbookChecks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        checkbook_check = client.checkbook_checks.retrieve(
            "checkbook_check_klgh3z50guf6jcnfhibb",
        )
        assert_matches_type(CheckbookCheck, checkbook_check, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:

        response = client.checkbook_checks.with_raw_response.retrieve(
            "checkbook_check_klgh3z50guf6jcnfhibb",
        )

        assert response.is_closed is True
        checkbook_check = response.parse()
        assert_matches_type(CheckbookCheck, checkbook_check, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.checkbook_checks.with_streaming_response.retrieve(
            "checkbook_check_klgh3z50guf6jcnfhibb",
        ) as response:
            assert not response.is_closed

            checkbook_check = response.parse()
            assert_matches_type(CheckbookCheck, checkbook_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `checkbook_check_id` but received ''"):
            client.checkbook_checks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        checkbook_check = client.checkbook_checks.list()
        assert_matches_type(SyncPage[CheckbookCheck], checkbook_check, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        checkbook_check = client.checkbook_checks.list(
            account_number_id="account_number_id",
            check_number=0,
            checkbook_id="checkbook_id",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncPage[CheckbookCheck], checkbook_check, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:

        response = client.checkbook_checks.with_raw_response.list()

        assert response.is_closed is True
        checkbook_check = response.parse()
        assert_matches_type(SyncPage[CheckbookCheck], checkbook_check, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.checkbook_checks.with_streaming_response.list() as response:
            assert not response.is_closed

            checkbook_check = response.parse()
            assert_matches_type(SyncPage[CheckbookCheck], checkbook_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stop(self, client: Increase) -> None:
        checkbook_check = client.checkbook_checks.stop(
            "checkbook_check_klgh3z50guf6jcnfhibb",
        )
        assert_matches_type(CheckbookCheck, checkbook_check, path=["response"])

    @parametrize
    def test_raw_response_stop(self, client: Increase) -> None:

        response = client.checkbook_checks.with_raw_response.stop(
            "checkbook_check_klgh3z50guf6jcnfhibb",
        )

        assert response.is_closed is True
        checkbook_check = response.parse()
        assert_matches_type(CheckbookCheck, checkbook_check, path=["response"])

    @parametrize
    def test_streaming_response_stop(self, client: Increase) -> None:
        with client.checkbook_checks.with_streaming_response.stop(
            "checkbook_check_klgh3z50guf6jcnfhibb",
        ) as response:
            assert not response.is_closed

            checkbook_check = response.parse()
            assert_matches_type(CheckbookCheck, checkbook_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stop(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `checkbook_check_id` but received ''"):
            client.checkbook_checks.with_raw_response.stop(
                "",
            )


class TestAsyncCheckbookChecks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        checkbook_check = await async_client.checkbook_checks.retrieve(
            "checkbook_check_klgh3z50guf6jcnfhibb",
        )
        assert_matches_type(CheckbookCheck, checkbook_check, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:

        response = await async_client.checkbook_checks.with_raw_response.retrieve(
            "checkbook_check_klgh3z50guf6jcnfhibb",
        )

        assert response.is_closed is True
        checkbook_check = await response.parse()
        assert_matches_type(CheckbookCheck, checkbook_check, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.checkbook_checks.with_streaming_response.retrieve(
            "checkbook_check_klgh3z50guf6jcnfhibb",
        ) as response:
            assert not response.is_closed

            checkbook_check = await response.parse()
            assert_matches_type(CheckbookCheck, checkbook_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `checkbook_check_id` but received ''"):
            await async_client.checkbook_checks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        checkbook_check = await async_client.checkbook_checks.list()
        assert_matches_type(AsyncPage[CheckbookCheck], checkbook_check, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        checkbook_check = await async_client.checkbook_checks.list(
            account_number_id="account_number_id",
            check_number=0,
            checkbook_id="checkbook_id",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncPage[CheckbookCheck], checkbook_check, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:

        response = await async_client.checkbook_checks.with_raw_response.list()

        assert response.is_closed is True
        checkbook_check = await response.parse()
        assert_matches_type(AsyncPage[CheckbookCheck], checkbook_check, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.checkbook_checks.with_streaming_response.list() as response:
            assert not response.is_closed

            checkbook_check = await response.parse()
            assert_matches_type(AsyncPage[CheckbookCheck], checkbook_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stop(self, async_client: AsyncIncrease) -> None:
        checkbook_check = await async_client.checkbook_checks.stop(
            "checkbook_check_klgh3z50guf6jcnfhibb",
        )
        assert_matches_type(CheckbookCheck, checkbook_check, path=["response"])

    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncIncrease) -> None:

        response = await async_client.checkbook_checks.with_raw_response.stop(
            "checkbook_check_klgh3z50guf6jcnfhibb",
        )

        assert response.is_closed is True
        checkbook_check = await response.parse()
        assert_matches_type(CheckbookCheck, checkbook_check, path=["response"])

    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncIncrease) -> None:
        async with async_client.checkbook_checks.with_streaming_response.stop(
            "checkbook_check_klgh3z50guf6jcnfhibb",
        ) as response:
            assert not response.is_closed

            checkbook_check = await response.parse()
            assert_matches_type(CheckbookCheck, checkbook_check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stop(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `checkbook_check_id` but received ''"):
            await async_client.checkbook_checks.with_raw_response.stop(
                "",
            )
