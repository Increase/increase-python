# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Entity

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_validation(self, client: Increase) -> None:
        entity = client.simulations.entities.validation(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            issues=[{"category": "entity_tax_identifier"}],
            status="invalid",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_raw_response_validation(self, client: Increase) -> None:
        response = client.simulations.entities.with_raw_response.validation(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            issues=[{"category": "entity_tax_identifier"}],
            status="invalid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_streaming_response_validation(self, client: Increase) -> None:
        with client.simulations.entities.with_streaming_response.validation(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            issues=[{"category": "entity_tax_identifier"}],
            status="invalid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_validation(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.simulations.entities.with_raw_response.validation(
                entity_id="",
                issues=[{"category": "entity_tax_identifier"}],
                status="invalid",
            )


class TestAsyncEntities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_validation(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.simulations.entities.validation(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            issues=[{"category": "entity_tax_identifier"}],
            status="invalid",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_validation(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.entities.with_raw_response.validation(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            issues=[{"category": "entity_tax_identifier"}],
            status="invalid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_validation(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.entities.with_streaming_response.validation(
            entity_id="entity_n8y8tnk2p9339ti393yi",
            issues=[{"category": "entity_tax_identifier"}],
            status="invalid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_validation(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.simulations.entities.with_raw_response.validation(
                entity_id="",
                issues=[{"category": "entity_tax_identifier"}],
                status="invalid",
            )
