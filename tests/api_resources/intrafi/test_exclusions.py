# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.pagination import SyncPage, AsyncPage
from increase.types.intrafi import IntrafiExclusion

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExclusions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        exclusion = client.intrafi.exclusions.create(
            bank_name="Example Bank",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.intrafi.exclusions.with_raw_response.create(
            bank_name="Example Bank",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclusion = response.parse()
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.intrafi.exclusions.with_streaming_response.create(
            bank_name="Example Bank",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exclusion = response.parse()
            assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        exclusion = client.intrafi.exclusions.retrieve(
            "string",
        )
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.intrafi.exclusions.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclusion = response.parse()
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.intrafi.exclusions.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exclusion = response.parse()
            assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `intrafi_exclusion_id` but received ''"):
            client.intrafi.exclusions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        exclusion = client.intrafi.exclusions.list()
        assert_matches_type(SyncPage[IntrafiExclusion], exclusion, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        exclusion = client.intrafi.exclusions.list(
            cursor="string",
            entity_id="string",
            idempotency_key="x",
            limit=1,
        )
        assert_matches_type(SyncPage[IntrafiExclusion], exclusion, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.intrafi.exclusions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclusion = response.parse()
        assert_matches_type(SyncPage[IntrafiExclusion], exclusion, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.intrafi.exclusions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exclusion = response.parse()
            assert_matches_type(SyncPage[IntrafiExclusion], exclusion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Increase) -> None:
        exclusion = client.intrafi.exclusions.archive(
            "string",
        )
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Increase) -> None:
        response = client.intrafi.exclusions.with_raw_response.archive(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclusion = response.parse()
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Increase) -> None:
        with client.intrafi.exclusions.with_streaming_response.archive(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exclusion = response.parse()
            assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `intrafi_exclusion_id` but received ''"):
            client.intrafi.exclusions.with_raw_response.archive(
                "",
            )


class TestAsyncExclusions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        exclusion = await async_client.intrafi.exclusions.create(
            bank_name="Example Bank",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.intrafi.exclusions.with_raw_response.create(
            bank_name="Example Bank",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclusion = response.parse()
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.intrafi.exclusions.with_streaming_response.create(
            bank_name="Example Bank",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exclusion = await response.parse()
            assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        exclusion = await async_client.intrafi.exclusions.retrieve(
            "string",
        )
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.intrafi.exclusions.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclusion = response.parse()
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.intrafi.exclusions.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exclusion = await response.parse()
            assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `intrafi_exclusion_id` but received ''"):
            await async_client.intrafi.exclusions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        exclusion = await async_client.intrafi.exclusions.list()
        assert_matches_type(AsyncPage[IntrafiExclusion], exclusion, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        exclusion = await async_client.intrafi.exclusions.list(
            cursor="string",
            entity_id="string",
            idempotency_key="x",
            limit=1,
        )
        assert_matches_type(AsyncPage[IntrafiExclusion], exclusion, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.intrafi.exclusions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclusion = response.parse()
        assert_matches_type(AsyncPage[IntrafiExclusion], exclusion, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.intrafi.exclusions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exclusion = await response.parse()
            assert_matches_type(AsyncPage[IntrafiExclusion], exclusion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncIncrease) -> None:
        exclusion = await async_client.intrafi.exclusions.archive(
            "string",
        )
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncIncrease) -> None:
        response = await async_client.intrafi.exclusions.with_raw_response.archive(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclusion = response.parse()
        assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncIncrease) -> None:
        async with async_client.intrafi.exclusions.with_streaming_response.archive(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exclusion = await response.parse()
            assert_matches_type(IntrafiExclusion, exclusion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `intrafi_exclusion_id` but received ''"):
            await async_client.intrafi.exclusions.with_raw_response.archive(
                "",
            )
