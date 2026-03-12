# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import EntityBeneficialOwner
from increase._utils import parse_date
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBeneficialOwners:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        beneficial_owner = client.beneficial_owners.retrieve(
            "entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )
        assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.beneficial_owners.with_raw_response.retrieve(
            "entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beneficial_owner = response.parse()
        assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.beneficial_owners.with_streaming_response.retrieve(
            "entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beneficial_owner = response.parse()
            assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `entity_beneficial_owner_id` but received ''"
        ):
            client.beneficial_owners.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Increase) -> None:
        beneficial_owner = client.beneficial_owners.update(
            entity_beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )
        assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Increase) -> None:
        beneficial_owner = client.beneficial_owners.update(
            entity_beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
                "line2": "Unit 2",
                "state": "NY",
                "zip": "10045",
            },
            confirmed_no_us_tax_id=True,
            identification={
                "method": "social_security_number",
                "number": "xxxx",
                "drivers_license": {
                    "expiration_date": parse_date("2019-12-27"),
                    "file_id": "file_id",
                    "state": "x",
                    "back_file_id": "back_file_id",
                },
                "other": {
                    "country": "x",
                    "description": "x",
                    "file_id": "file_id",
                    "back_file_id": "back_file_id",
                    "expiration_date": parse_date("2019-12-27"),
                },
                "passport": {
                    "country": "x",
                    "expiration_date": parse_date("2019-12-27"),
                    "file_id": "file_id",
                },
            },
            name="x",
        )
        assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Increase) -> None:
        response = client.beneficial_owners.with_raw_response.update(
            entity_beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beneficial_owner = response.parse()
        assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Increase) -> None:
        with client.beneficial_owners.with_streaming_response.update(
            entity_beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beneficial_owner = response.parse()
            assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `entity_beneficial_owner_id` but received ''"
        ):
            client.beneficial_owners.with_raw_response.update(
                entity_beneficial_owner_id="",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        beneficial_owner = client.beneficial_owners.list(
            entity_id="entity_id",
        )
        assert_matches_type(SyncPage[EntityBeneficialOwner], beneficial_owner, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        beneficial_owner = client.beneficial_owners.list(
            entity_id="entity_id",
            cursor="cursor",
            idempotency_key="x",
            limit=1,
        )
        assert_matches_type(SyncPage[EntityBeneficialOwner], beneficial_owner, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.beneficial_owners.with_raw_response.list(
            entity_id="entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beneficial_owner = response.parse()
        assert_matches_type(SyncPage[EntityBeneficialOwner], beneficial_owner, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.beneficial_owners.with_streaming_response.list(
            entity_id="entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beneficial_owner = response.parse()
            assert_matches_type(SyncPage[EntityBeneficialOwner], beneficial_owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Increase) -> None:
        beneficial_owner = client.beneficial_owners.archive(
            "entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )
        assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Increase) -> None:
        response = client.beneficial_owners.with_raw_response.archive(
            "entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beneficial_owner = response.parse()
        assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Increase) -> None:
        with client.beneficial_owners.with_streaming_response.archive(
            "entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beneficial_owner = response.parse()
            assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `entity_beneficial_owner_id` but received ''"
        ):
            client.beneficial_owners.with_raw_response.archive(
                "",
            )


class TestAsyncBeneficialOwners:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        beneficial_owner = await async_client.beneficial_owners.retrieve(
            "entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )
        assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.beneficial_owners.with_raw_response.retrieve(
            "entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beneficial_owner = await response.parse()
        assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.beneficial_owners.with_streaming_response.retrieve(
            "entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beneficial_owner = await response.parse()
            assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `entity_beneficial_owner_id` but received ''"
        ):
            await async_client.beneficial_owners.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncIncrease) -> None:
        beneficial_owner = await async_client.beneficial_owners.update(
            entity_beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )
        assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncIncrease) -> None:
        beneficial_owner = await async_client.beneficial_owners.update(
            entity_beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            address={
                "city": "New York",
                "country": "US",
                "line1": "33 Liberty Street",
                "line2": "Unit 2",
                "state": "NY",
                "zip": "10045",
            },
            confirmed_no_us_tax_id=True,
            identification={
                "method": "social_security_number",
                "number": "xxxx",
                "drivers_license": {
                    "expiration_date": parse_date("2019-12-27"),
                    "file_id": "file_id",
                    "state": "x",
                    "back_file_id": "back_file_id",
                },
                "other": {
                    "country": "x",
                    "description": "x",
                    "file_id": "file_id",
                    "back_file_id": "back_file_id",
                    "expiration_date": parse_date("2019-12-27"),
                },
                "passport": {
                    "country": "x",
                    "expiration_date": parse_date("2019-12-27"),
                    "file_id": "file_id",
                },
            },
            name="x",
        )
        assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIncrease) -> None:
        response = await async_client.beneficial_owners.with_raw_response.update(
            entity_beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beneficial_owner = await response.parse()
        assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIncrease) -> None:
        async with async_client.beneficial_owners.with_streaming_response.update(
            entity_beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beneficial_owner = await response.parse()
            assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `entity_beneficial_owner_id` but received ''"
        ):
            await async_client.beneficial_owners.with_raw_response.update(
                entity_beneficial_owner_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        beneficial_owner = await async_client.beneficial_owners.list(
            entity_id="entity_id",
        )
        assert_matches_type(AsyncPage[EntityBeneficialOwner], beneficial_owner, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        beneficial_owner = await async_client.beneficial_owners.list(
            entity_id="entity_id",
            cursor="cursor",
            idempotency_key="x",
            limit=1,
        )
        assert_matches_type(AsyncPage[EntityBeneficialOwner], beneficial_owner, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.beneficial_owners.with_raw_response.list(
            entity_id="entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beneficial_owner = await response.parse()
        assert_matches_type(AsyncPage[EntityBeneficialOwner], beneficial_owner, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.beneficial_owners.with_streaming_response.list(
            entity_id="entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beneficial_owner = await response.parse()
            assert_matches_type(AsyncPage[EntityBeneficialOwner], beneficial_owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncIncrease) -> None:
        beneficial_owner = await async_client.beneficial_owners.archive(
            "entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )
        assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncIncrease) -> None:
        response = await async_client.beneficial_owners.with_raw_response.archive(
            "entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beneficial_owner = await response.parse()
        assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncIncrease) -> None:
        async with async_client.beneficial_owners.with_streaming_response.archive(
            "entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beneficial_owner = await response.parse()
            assert_matches_type(EntityBeneficialOwner, beneficial_owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `entity_beneficial_owner_id` but received ''"
        ):
            await async_client.beneficial_owners.with_raw_response.archive(
                "",
            )
