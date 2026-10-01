# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import PhysicalCheckBatch

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhysicalCheckBatches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        physical_check_batch = client.physical_check_batches.create(
            mailing_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "Ian Crease",
                "postal_code": "10045",
                "state": "NY",
            },
            return_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "National Phonograph Company",
                "postal_code": "10045",
                "state": "NY",
            },
        )
        assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        physical_check_batch = client.physical_check_batches.create(
            mailing_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "Ian Crease",
                "postal_code": "10045",
                "state": "NY",
                "line2": "line2",
                "phone": "x",
            },
            return_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "National Phonograph Company",
                "postal_code": "10045",
                "state": "NY",
                "line2": "line2",
                "phone": "x",
            },
            shipping_method="usps_first_class",
        )
        assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.physical_check_batches.with_raw_response.create(
            mailing_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "Ian Crease",
                "postal_code": "10045",
                "state": "NY",
            },
            return_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "National Phonograph Company",
                "postal_code": "10045",
                "state": "NY",
            },
        )

        assert response.is_closed is True
        physical_check_batch = response.parse()
        assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.physical_check_batches.with_streaming_response.create(
            mailing_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "Ian Crease",
                "postal_code": "10045",
                "state": "NY",
            },
            return_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "National Phonograph Company",
                "postal_code": "10045",
                "state": "NY",
            },
        ) as response:
            assert not response.is_closed

            physical_check_batch = response.parse()
            assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: Increase) -> None:
        physical_check_batch = client.physical_check_batches.cancel(
            "physical_check_batch_yzdwjhdbw0in6191whce",
        )
        assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Increase) -> None:
        response = client.physical_check_batches.with_raw_response.cancel(
            "physical_check_batch_yzdwjhdbw0in6191whce",
        )

        assert response.is_closed is True
        physical_check_batch = response.parse()
        assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Increase) -> None:
        with client.physical_check_batches.with_streaming_response.cancel(
            "physical_check_batch_yzdwjhdbw0in6191whce",
        ) as response:
            assert not response.is_closed

            physical_check_batch = response.parse()
            assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `physical_check_batch_id` but received ''"
        ):
            client.physical_check_batches.with_raw_response.cancel(
                "",
            )

    @parametrize
    def test_method_complete(self, client: Increase) -> None:
        physical_check_batch = client.physical_check_batches.complete(
            "physical_check_batch_yzdwjhdbw0in6191whce",
        )
        assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

    @parametrize
    def test_raw_response_complete(self, client: Increase) -> None:
        response = client.physical_check_batches.with_raw_response.complete(
            "physical_check_batch_yzdwjhdbw0in6191whce",
        )

        assert response.is_closed is True
        physical_check_batch = response.parse()
        assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

    @parametrize
    def test_streaming_response_complete(self, client: Increase) -> None:
        with client.physical_check_batches.with_streaming_response.complete(
            "physical_check_batch_yzdwjhdbw0in6191whce",
        ) as response:
            assert not response.is_closed

            physical_check_batch = response.parse()
            assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_complete(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `physical_check_batch_id` but received ''"
        ):
            client.physical_check_batches.with_raw_response.complete(
                "",
            )


class TestAsyncPhysicalCheckBatches:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        physical_check_batch = await async_client.physical_check_batches.create(
            mailing_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "Ian Crease",
                "postal_code": "10045",
                "state": "NY",
            },
            return_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "National Phonograph Company",
                "postal_code": "10045",
                "state": "NY",
            },
        )
        assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        physical_check_batch = await async_client.physical_check_batches.create(
            mailing_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "Ian Crease",
                "postal_code": "10045",
                "state": "NY",
                "line2": "line2",
                "phone": "x",
            },
            return_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "National Phonograph Company",
                "postal_code": "10045",
                "state": "NY",
                "line2": "line2",
                "phone": "x",
            },
            shipping_method="usps_first_class",
        )
        assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.physical_check_batches.with_raw_response.create(
            mailing_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "Ian Crease",
                "postal_code": "10045",
                "state": "NY",
            },
            return_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "National Phonograph Company",
                "postal_code": "10045",
                "state": "NY",
            },
        )

        assert response.is_closed is True
        physical_check_batch = await response.parse()
        assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.physical_check_batches.with_streaming_response.create(
            mailing_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "Ian Crease",
                "postal_code": "10045",
                "state": "NY",
            },
            return_address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "name": "National Phonograph Company",
                "postal_code": "10045",
                "state": "NY",
            },
        ) as response:
            assert not response.is_closed

            physical_check_batch = await response.parse()
            assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncIncrease) -> None:
        physical_check_batch = await async_client.physical_check_batches.cancel(
            "physical_check_batch_yzdwjhdbw0in6191whce",
        )
        assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncIncrease) -> None:
        response = await async_client.physical_check_batches.with_raw_response.cancel(
            "physical_check_batch_yzdwjhdbw0in6191whce",
        )

        assert response.is_closed is True
        physical_check_batch = await response.parse()
        assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncIncrease) -> None:
        async with async_client.physical_check_batches.with_streaming_response.cancel(
            "physical_check_batch_yzdwjhdbw0in6191whce",
        ) as response:
            assert not response.is_closed

            physical_check_batch = await response.parse()
            assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `physical_check_batch_id` but received ''"
        ):
            await async_client.physical_check_batches.with_raw_response.cancel(
                "",
            )

    @parametrize
    async def test_method_complete(self, async_client: AsyncIncrease) -> None:
        physical_check_batch = await async_client.physical_check_batches.complete(
            "physical_check_batch_yzdwjhdbw0in6191whce",
        )
        assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncIncrease) -> None:
        response = await async_client.physical_check_batches.with_raw_response.complete(
            "physical_check_batch_yzdwjhdbw0in6191whce",
        )

        assert response.is_closed is True
        physical_check_batch = await response.parse()
        assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncIncrease) -> None:
        async with async_client.physical_check_batches.with_streaming_response.complete(
            "physical_check_batch_yzdwjhdbw0in6191whce",
        ) as response:
            assert not response.is_closed

            physical_check_batch = await response.parse()
            assert_matches_type(PhysicalCheckBatch, physical_check_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_complete(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `physical_check_batch_id` but received ''"
        ):
            await async_client.physical_check_batches.with_raw_response.complete(
                "",
            )
