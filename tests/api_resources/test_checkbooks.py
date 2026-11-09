# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Checkbook
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheckbooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        checkbook = client.checkbooks.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            mailing_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "Ian Crease",
                "postal_code": "10045",
                "state": "NY",
            },
            payer=[
                {"contents": "National Phonograph Company"},
                {"contents": "33 Liberty Street"},
                {"contents": "New York, NY 10045"},
            ],
        )
        assert_matches_type(Checkbook, checkbook, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        checkbook = client.checkbooks.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            mailing_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "Ian Crease",
                "postal_code": "10045",
                "state": "NY",
                "line2": "line2",
            },
            payer=[
                {"contents": "National Phonograph Company"},
                {"contents": "33 Liberty Street"},
                {"contents": "New York, NY 10045"},
            ],
        )
        assert_matches_type(Checkbook, checkbook, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:

        response = client.checkbooks.with_raw_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            mailing_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "Ian Crease",
                "postal_code": "10045",
                "state": "NY",
            },
            payer=[
                {"contents": "National Phonograph Company"},
                {"contents": "33 Liberty Street"},
                {"contents": "New York, NY 10045"},
            ],
        )

        assert response.is_closed is True
        checkbook = response.parse()
        assert_matches_type(Checkbook, checkbook, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.checkbooks.with_streaming_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            mailing_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "Ian Crease",
                "postal_code": "10045",
                "state": "NY",
            },
            payer=[
                {"contents": "National Phonograph Company"},
                {"contents": "33 Liberty Street"},
                {"contents": "New York, NY 10045"},
            ],
        ) as response:
            assert not response.is_closed

            checkbook = response.parse()
            assert_matches_type(Checkbook, checkbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        checkbook = client.checkbooks.retrieve(
            "checkbook_7iudxhxum6vlkcjxmi8y",
        )
        assert_matches_type(Checkbook, checkbook, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:

        response = client.checkbooks.with_raw_response.retrieve(
            "checkbook_7iudxhxum6vlkcjxmi8y",
        )

        assert response.is_closed is True
        checkbook = response.parse()
        assert_matches_type(Checkbook, checkbook, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.checkbooks.with_streaming_response.retrieve(
            "checkbook_7iudxhxum6vlkcjxmi8y",
        ) as response:
            assert not response.is_closed

            checkbook = response.parse()
            assert_matches_type(Checkbook, checkbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `checkbook_id` but received ''"):
            client.checkbooks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        checkbook = client.checkbooks.list()
        assert_matches_type(SyncPage[Checkbook], checkbook, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        checkbook = client.checkbooks.list(
            account_number_id="account_number_id",
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["pending_submission"]},
        )
        assert_matches_type(SyncPage[Checkbook], checkbook, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:

        response = client.checkbooks.with_raw_response.list()

        assert response.is_closed is True
        checkbook = response.parse()
        assert_matches_type(SyncPage[Checkbook], checkbook, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.checkbooks.with_streaming_response.list() as response:
            assert not response.is_closed

            checkbook = response.parse()
            assert_matches_type(SyncPage[Checkbook], checkbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stop(self, client: Increase) -> None:
        checkbook = client.checkbooks.stop(
            "checkbook_7iudxhxum6vlkcjxmi8y",
        )
        assert_matches_type(Checkbook, checkbook, path=["response"])

    @parametrize
    def test_raw_response_stop(self, client: Increase) -> None:

        response = client.checkbooks.with_raw_response.stop(
            "checkbook_7iudxhxum6vlkcjxmi8y",
        )

        assert response.is_closed is True
        checkbook = response.parse()
        assert_matches_type(Checkbook, checkbook, path=["response"])

    @parametrize
    def test_streaming_response_stop(self, client: Increase) -> None:
        with client.checkbooks.with_streaming_response.stop(
            "checkbook_7iudxhxum6vlkcjxmi8y",
        ) as response:
            assert not response.is_closed

            checkbook = response.parse()
            assert_matches_type(Checkbook, checkbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stop(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `checkbook_id` but received ''"):
            client.checkbooks.with_raw_response.stop(
                "",
            )


class TestAsyncCheckbooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        checkbook = await async_client.checkbooks.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            mailing_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "Ian Crease",
                "postal_code": "10045",
                "state": "NY",
            },
            payer=[
                {"contents": "National Phonograph Company"},
                {"contents": "33 Liberty Street"},
                {"contents": "New York, NY 10045"},
            ],
        )
        assert_matches_type(Checkbook, checkbook, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        checkbook = await async_client.checkbooks.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            mailing_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "Ian Crease",
                "postal_code": "10045",
                "state": "NY",
                "line2": "line2",
            },
            payer=[
                {"contents": "National Phonograph Company"},
                {"contents": "33 Liberty Street"},
                {"contents": "New York, NY 10045"},
            ],
        )
        assert_matches_type(Checkbook, checkbook, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:

        response = await async_client.checkbooks.with_raw_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            mailing_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "Ian Crease",
                "postal_code": "10045",
                "state": "NY",
            },
            payer=[
                {"contents": "National Phonograph Company"},
                {"contents": "33 Liberty Street"},
                {"contents": "New York, NY 10045"},
            ],
        )

        assert response.is_closed is True
        checkbook = await response.parse()
        assert_matches_type(Checkbook, checkbook, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.checkbooks.with_streaming_response.create(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            mailing_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "Ian Crease",
                "postal_code": "10045",
                "state": "NY",
            },
            payer=[
                {"contents": "National Phonograph Company"},
                {"contents": "33 Liberty Street"},
                {"contents": "New York, NY 10045"},
            ],
        ) as response:
            assert not response.is_closed

            checkbook = await response.parse()
            assert_matches_type(Checkbook, checkbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        checkbook = await async_client.checkbooks.retrieve(
            "checkbook_7iudxhxum6vlkcjxmi8y",
        )
        assert_matches_type(Checkbook, checkbook, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:

        response = await async_client.checkbooks.with_raw_response.retrieve(
            "checkbook_7iudxhxum6vlkcjxmi8y",
        )

        assert response.is_closed is True
        checkbook = await response.parse()
        assert_matches_type(Checkbook, checkbook, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.checkbooks.with_streaming_response.retrieve(
            "checkbook_7iudxhxum6vlkcjxmi8y",
        ) as response:
            assert not response.is_closed

            checkbook = await response.parse()
            assert_matches_type(Checkbook, checkbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `checkbook_id` but received ''"):
            await async_client.checkbooks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        checkbook = await async_client.checkbooks.list()
        assert_matches_type(AsyncPage[Checkbook], checkbook, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        checkbook = await async_client.checkbooks.list(
            account_number_id="account_number_id",
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["pending_submission"]},
        )
        assert_matches_type(AsyncPage[Checkbook], checkbook, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:

        response = await async_client.checkbooks.with_raw_response.list()

        assert response.is_closed is True
        checkbook = await response.parse()
        assert_matches_type(AsyncPage[Checkbook], checkbook, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.checkbooks.with_streaming_response.list() as response:
            assert not response.is_closed

            checkbook = await response.parse()
            assert_matches_type(AsyncPage[Checkbook], checkbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stop(self, async_client: AsyncIncrease) -> None:
        checkbook = await async_client.checkbooks.stop(
            "checkbook_7iudxhxum6vlkcjxmi8y",
        )
        assert_matches_type(Checkbook, checkbook, path=["response"])

    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncIncrease) -> None:

        response = await async_client.checkbooks.with_raw_response.stop(
            "checkbook_7iudxhxum6vlkcjxmi8y",
        )

        assert response.is_closed is True
        checkbook = await response.parse()
        assert_matches_type(Checkbook, checkbook, path=["response"])

    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncIncrease) -> None:
        async with async_client.checkbooks.with_streaming_response.stop(
            "checkbook_7iudxhxum6vlkcjxmi8y",
        ) as response:
            assert not response.is_closed

            checkbook = await response.parse()
            assert_matches_type(Checkbook, checkbook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stop(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `checkbook_id` but received ''"):
            await async_client.checkbooks.with_raw_response.stop(
                "",
            )
