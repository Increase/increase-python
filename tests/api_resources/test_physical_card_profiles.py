# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    PhysicalCardProfile,
)
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhysicalCardProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        physical_card_profile = client.physical_card_profiles.create(
            carrier_image_file_id="file_h6v7mtipe119os47ehlu",
            contact_phone="+16505046304",
            description="My Card Profile",
            front_image_file_id="file_o6aex13wm1jcc36sgcj1",
            program_id="program_i2v2os4mwza1oetokh9i",
        )
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        physical_card_profile = client.physical_card_profiles.create(
            carrier_image_file_id="file_h6v7mtipe119os47ehlu",
            contact_phone="+16505046304",
            description="My Card Profile",
            front_image_file_id="file_o6aex13wm1jcc36sgcj1",
            program_id="program_i2v2os4mwza1oetokh9i",
            front_text={
                "line1": "x",
                "line2": "x",
            },
        )
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.physical_card_profiles.with_raw_response.create(
            carrier_image_file_id="file_h6v7mtipe119os47ehlu",
            contact_phone="+16505046304",
            description="My Card Profile",
            front_image_file_id="file_o6aex13wm1jcc36sgcj1",
            program_id="program_i2v2os4mwza1oetokh9i",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card_profile = response.parse()
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.physical_card_profiles.with_streaming_response.create(
            carrier_image_file_id="file_h6v7mtipe119os47ehlu",
            contact_phone="+16505046304",
            description="My Card Profile",
            front_image_file_id="file_o6aex13wm1jcc36sgcj1",
            program_id="program_i2v2os4mwza1oetokh9i",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card_profile = response.parse()
            assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        physical_card_profile = client.physical_card_profiles.retrieve(
            "physical_card_profile_id",
        )
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.physical_card_profiles.with_raw_response.retrieve(
            "physical_card_profile_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card_profile = response.parse()
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.physical_card_profiles.with_streaming_response.retrieve(
            "physical_card_profile_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card_profile = response.parse()
            assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `physical_card_profile_id` but received ''"
        ):
            client.physical_card_profiles.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        physical_card_profile = client.physical_card_profiles.list()
        assert_matches_type(SyncPage[PhysicalCardProfile], physical_card_profile, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        physical_card_profile = client.physical_card_profiles.list(
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["pending_creating"]},
        )
        assert_matches_type(SyncPage[PhysicalCardProfile], physical_card_profile, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.physical_card_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card_profile = response.parse()
        assert_matches_type(SyncPage[PhysicalCardProfile], physical_card_profile, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.physical_card_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card_profile = response.parse()
            assert_matches_type(SyncPage[PhysicalCardProfile], physical_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Increase) -> None:
        physical_card_profile = client.physical_card_profiles.archive(
            "physical_card_profile_id",
        )
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Increase) -> None:
        response = client.physical_card_profiles.with_raw_response.archive(
            "physical_card_profile_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card_profile = response.parse()
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Increase) -> None:
        with client.physical_card_profiles.with_streaming_response.archive(
            "physical_card_profile_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card_profile = response.parse()
            assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `physical_card_profile_id` but received ''"
        ):
            client.physical_card_profiles.with_raw_response.archive(
                "",
            )

    @parametrize
    def test_method_clone(self, client: Increase) -> None:
        physical_card_profile = client.physical_card_profiles.clone(
            physical_card_profile_id="physical_card_profile_m534d5rn9qyy9ufqxoec",
        )
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    def test_method_clone_with_all_params(self, client: Increase) -> None:
        physical_card_profile = client.physical_card_profiles.clone(
            physical_card_profile_id="physical_card_profile_m534d5rn9qyy9ufqxoec",
            carrier_image_file_id="carrier_image_file_id",
            contact_phone="x",
            description="x",
            front_image_file_id="file_o6aex13wm1jcc36sgcj1",
            front_text={
                "line1": "x",
                "line2": "x",
            },
            program_id="program_id",
        )
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    def test_raw_response_clone(self, client: Increase) -> None:
        response = client.physical_card_profiles.with_raw_response.clone(
            physical_card_profile_id="physical_card_profile_m534d5rn9qyy9ufqxoec",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card_profile = response.parse()
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    def test_streaming_response_clone(self, client: Increase) -> None:
        with client.physical_card_profiles.with_streaming_response.clone(
            physical_card_profile_id="physical_card_profile_m534d5rn9qyy9ufqxoec",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card_profile = response.parse()
            assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_clone(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `physical_card_profile_id` but received ''"
        ):
            client.physical_card_profiles.with_raw_response.clone(
                physical_card_profile_id="",
            )


class TestAsyncPhysicalCardProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        physical_card_profile = await async_client.physical_card_profiles.create(
            carrier_image_file_id="file_h6v7mtipe119os47ehlu",
            contact_phone="+16505046304",
            description="My Card Profile",
            front_image_file_id="file_o6aex13wm1jcc36sgcj1",
            program_id="program_i2v2os4mwza1oetokh9i",
        )
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        physical_card_profile = await async_client.physical_card_profiles.create(
            carrier_image_file_id="file_h6v7mtipe119os47ehlu",
            contact_phone="+16505046304",
            description="My Card Profile",
            front_image_file_id="file_o6aex13wm1jcc36sgcj1",
            program_id="program_i2v2os4mwza1oetokh9i",
            front_text={
                "line1": "x",
                "line2": "x",
            },
        )
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.physical_card_profiles.with_raw_response.create(
            carrier_image_file_id="file_h6v7mtipe119os47ehlu",
            contact_phone="+16505046304",
            description="My Card Profile",
            front_image_file_id="file_o6aex13wm1jcc36sgcj1",
            program_id="program_i2v2os4mwza1oetokh9i",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card_profile = await response.parse()
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.physical_card_profiles.with_streaming_response.create(
            carrier_image_file_id="file_h6v7mtipe119os47ehlu",
            contact_phone="+16505046304",
            description="My Card Profile",
            front_image_file_id="file_o6aex13wm1jcc36sgcj1",
            program_id="program_i2v2os4mwza1oetokh9i",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card_profile = await response.parse()
            assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        physical_card_profile = await async_client.physical_card_profiles.retrieve(
            "physical_card_profile_id",
        )
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.physical_card_profiles.with_raw_response.retrieve(
            "physical_card_profile_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card_profile = await response.parse()
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.physical_card_profiles.with_streaming_response.retrieve(
            "physical_card_profile_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card_profile = await response.parse()
            assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `physical_card_profile_id` but received ''"
        ):
            await async_client.physical_card_profiles.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        physical_card_profile = await async_client.physical_card_profiles.list()
        assert_matches_type(AsyncPage[PhysicalCardProfile], physical_card_profile, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        physical_card_profile = await async_client.physical_card_profiles.list(
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["pending_creating"]},
        )
        assert_matches_type(AsyncPage[PhysicalCardProfile], physical_card_profile, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.physical_card_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card_profile = await response.parse()
        assert_matches_type(AsyncPage[PhysicalCardProfile], physical_card_profile, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.physical_card_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card_profile = await response.parse()
            assert_matches_type(AsyncPage[PhysicalCardProfile], physical_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncIncrease) -> None:
        physical_card_profile = await async_client.physical_card_profiles.archive(
            "physical_card_profile_id",
        )
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncIncrease) -> None:
        response = await async_client.physical_card_profiles.with_raw_response.archive(
            "physical_card_profile_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card_profile = await response.parse()
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncIncrease) -> None:
        async with async_client.physical_card_profiles.with_streaming_response.archive(
            "physical_card_profile_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card_profile = await response.parse()
            assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `physical_card_profile_id` but received ''"
        ):
            await async_client.physical_card_profiles.with_raw_response.archive(
                "",
            )

    @parametrize
    async def test_method_clone(self, async_client: AsyncIncrease) -> None:
        physical_card_profile = await async_client.physical_card_profiles.clone(
            physical_card_profile_id="physical_card_profile_m534d5rn9qyy9ufqxoec",
        )
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    async def test_method_clone_with_all_params(self, async_client: AsyncIncrease) -> None:
        physical_card_profile = await async_client.physical_card_profiles.clone(
            physical_card_profile_id="physical_card_profile_m534d5rn9qyy9ufqxoec",
            carrier_image_file_id="carrier_image_file_id",
            contact_phone="x",
            description="x",
            front_image_file_id="file_o6aex13wm1jcc36sgcj1",
            front_text={
                "line1": "x",
                "line2": "x",
            },
            program_id="program_id",
        )
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncIncrease) -> None:
        response = await async_client.physical_card_profiles.with_raw_response.clone(
            physical_card_profile_id="physical_card_profile_m534d5rn9qyy9ufqxoec",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card_profile = await response.parse()
        assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncIncrease) -> None:
        async with async_client.physical_card_profiles.with_streaming_response.clone(
            physical_card_profile_id="physical_card_profile_m534d5rn9qyy9ufqxoec",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card_profile = await response.parse()
            assert_matches_type(PhysicalCardProfile, physical_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_clone(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `physical_card_profile_id` but received ''"
        ):
            await async_client.physical_card_profiles.with_raw_response.clone(
                physical_card_profile_id="",
            )
