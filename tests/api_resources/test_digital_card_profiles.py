# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    DigitalCardProfile,
)
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDigitalCardProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        digital_card_profile = client.digital_card_profiles.create(
            app_icon_file_id="file_8zxqkwlh43wo144u8yec",
            background_image_file_id="file_1ai913suu1zfn1pdetru",
            card_description="MyBank Signature Card",
            description="My Card Profile",
            issuer_name="MyBank",
        )
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        digital_card_profile = client.digital_card_profiles.create(
            app_icon_file_id="file_8zxqkwlh43wo144u8yec",
            background_image_file_id="file_1ai913suu1zfn1pdetru",
            card_description="MyBank Signature Card",
            description="My Card Profile",
            issuer_name="MyBank",
            contact_email="user@example.com",
            contact_phone="+18885551212",
            contact_website="https://example.com",
            text_color={
                "blue": 59,
                "green": 43,
                "red": 26,
            },
        )
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.digital_card_profiles.with_raw_response.create(
            app_icon_file_id="file_8zxqkwlh43wo144u8yec",
            background_image_file_id="file_1ai913suu1zfn1pdetru",
            card_description="MyBank Signature Card",
            description="My Card Profile",
            issuer_name="MyBank",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_card_profile = response.parse()
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.digital_card_profiles.with_streaming_response.create(
            app_icon_file_id="file_8zxqkwlh43wo144u8yec",
            background_image_file_id="file_1ai913suu1zfn1pdetru",
            card_description="MyBank Signature Card",
            description="My Card Profile",
            issuer_name="MyBank",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_card_profile = response.parse()
            assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        digital_card_profile = client.digital_card_profiles.retrieve(
            "digital_card_profile_id",
        )
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.digital_card_profiles.with_raw_response.retrieve(
            "digital_card_profile_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_card_profile = response.parse()
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.digital_card_profiles.with_streaming_response.retrieve(
            "digital_card_profile_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_card_profile = response.parse()
            assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `digital_card_profile_id` but received ''"
        ):
            client.digital_card_profiles.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        digital_card_profile = client.digital_card_profiles.list()
        assert_matches_type(SyncPage[DigitalCardProfile], digital_card_profile, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        digital_card_profile = client.digital_card_profiles.list(
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["pending"]},
        )
        assert_matches_type(SyncPage[DigitalCardProfile], digital_card_profile, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.digital_card_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_card_profile = response.parse()
        assert_matches_type(SyncPage[DigitalCardProfile], digital_card_profile, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.digital_card_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_card_profile = response.parse()
            assert_matches_type(SyncPage[DigitalCardProfile], digital_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Increase) -> None:
        digital_card_profile = client.digital_card_profiles.archive(
            "digital_card_profile_id",
        )
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Increase) -> None:
        response = client.digital_card_profiles.with_raw_response.archive(
            "digital_card_profile_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_card_profile = response.parse()
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Increase) -> None:
        with client.digital_card_profiles.with_streaming_response.archive(
            "digital_card_profile_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_card_profile = response.parse()
            assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `digital_card_profile_id` but received ''"
        ):
            client.digital_card_profiles.with_raw_response.archive(
                "",
            )

    @parametrize
    def test_method_clone(self, client: Increase) -> None:
        digital_card_profile = client.digital_card_profiles.clone(
            digital_card_profile_id="digital_card_profile_s3puplu90f04xhcwkiga",
        )
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    def test_method_clone_with_all_params(self, client: Increase) -> None:
        digital_card_profile = client.digital_card_profiles.clone(
            digital_card_profile_id="digital_card_profile_s3puplu90f04xhcwkiga",
            app_icon_file_id="app_icon_file_id",
            background_image_file_id="file_1ai913suu1zfn1pdetru",
            card_description="x",
            contact_email="x",
            contact_phone="x",
            contact_website="contact_website",
            description="x",
            issuer_name="x",
            text_color={
                "blue": 0,
                "green": 0,
                "red": 0,
            },
        )
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    def test_raw_response_clone(self, client: Increase) -> None:
        response = client.digital_card_profiles.with_raw_response.clone(
            digital_card_profile_id="digital_card_profile_s3puplu90f04xhcwkiga",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_card_profile = response.parse()
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    def test_streaming_response_clone(self, client: Increase) -> None:
        with client.digital_card_profiles.with_streaming_response.clone(
            digital_card_profile_id="digital_card_profile_s3puplu90f04xhcwkiga",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_card_profile = response.parse()
            assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_clone(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `digital_card_profile_id` but received ''"
        ):
            client.digital_card_profiles.with_raw_response.clone(
                digital_card_profile_id="",
            )


class TestAsyncDigitalCardProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        digital_card_profile = await async_client.digital_card_profiles.create(
            app_icon_file_id="file_8zxqkwlh43wo144u8yec",
            background_image_file_id="file_1ai913suu1zfn1pdetru",
            card_description="MyBank Signature Card",
            description="My Card Profile",
            issuer_name="MyBank",
        )
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        digital_card_profile = await async_client.digital_card_profiles.create(
            app_icon_file_id="file_8zxqkwlh43wo144u8yec",
            background_image_file_id="file_1ai913suu1zfn1pdetru",
            card_description="MyBank Signature Card",
            description="My Card Profile",
            issuer_name="MyBank",
            contact_email="user@example.com",
            contact_phone="+18885551212",
            contact_website="https://example.com",
            text_color={
                "blue": 59,
                "green": 43,
                "red": 26,
            },
        )
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.digital_card_profiles.with_raw_response.create(
            app_icon_file_id="file_8zxqkwlh43wo144u8yec",
            background_image_file_id="file_1ai913suu1zfn1pdetru",
            card_description="MyBank Signature Card",
            description="My Card Profile",
            issuer_name="MyBank",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_card_profile = await response.parse()
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.digital_card_profiles.with_streaming_response.create(
            app_icon_file_id="file_8zxqkwlh43wo144u8yec",
            background_image_file_id="file_1ai913suu1zfn1pdetru",
            card_description="MyBank Signature Card",
            description="My Card Profile",
            issuer_name="MyBank",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_card_profile = await response.parse()
            assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        digital_card_profile = await async_client.digital_card_profiles.retrieve(
            "digital_card_profile_id",
        )
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.digital_card_profiles.with_raw_response.retrieve(
            "digital_card_profile_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_card_profile = await response.parse()
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.digital_card_profiles.with_streaming_response.retrieve(
            "digital_card_profile_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_card_profile = await response.parse()
            assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `digital_card_profile_id` but received ''"
        ):
            await async_client.digital_card_profiles.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        digital_card_profile = await async_client.digital_card_profiles.list()
        assert_matches_type(AsyncPage[DigitalCardProfile], digital_card_profile, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        digital_card_profile = await async_client.digital_card_profiles.list(
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["pending"]},
        )
        assert_matches_type(AsyncPage[DigitalCardProfile], digital_card_profile, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.digital_card_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_card_profile = await response.parse()
        assert_matches_type(AsyncPage[DigitalCardProfile], digital_card_profile, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.digital_card_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_card_profile = await response.parse()
            assert_matches_type(AsyncPage[DigitalCardProfile], digital_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncIncrease) -> None:
        digital_card_profile = await async_client.digital_card_profiles.archive(
            "digital_card_profile_id",
        )
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncIncrease) -> None:
        response = await async_client.digital_card_profiles.with_raw_response.archive(
            "digital_card_profile_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_card_profile = await response.parse()
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncIncrease) -> None:
        async with async_client.digital_card_profiles.with_streaming_response.archive(
            "digital_card_profile_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_card_profile = await response.parse()
            assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `digital_card_profile_id` but received ''"
        ):
            await async_client.digital_card_profiles.with_raw_response.archive(
                "",
            )

    @parametrize
    async def test_method_clone(self, async_client: AsyncIncrease) -> None:
        digital_card_profile = await async_client.digital_card_profiles.clone(
            digital_card_profile_id="digital_card_profile_s3puplu90f04xhcwkiga",
        )
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    async def test_method_clone_with_all_params(self, async_client: AsyncIncrease) -> None:
        digital_card_profile = await async_client.digital_card_profiles.clone(
            digital_card_profile_id="digital_card_profile_s3puplu90f04xhcwkiga",
            app_icon_file_id="app_icon_file_id",
            background_image_file_id="file_1ai913suu1zfn1pdetru",
            card_description="x",
            contact_email="x",
            contact_phone="x",
            contact_website="contact_website",
            description="x",
            issuer_name="x",
            text_color={
                "blue": 0,
                "green": 0,
                "red": 0,
            },
        )
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncIncrease) -> None:
        response = await async_client.digital_card_profiles.with_raw_response.clone(
            digital_card_profile_id="digital_card_profile_s3puplu90f04xhcwkiga",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_card_profile = await response.parse()
        assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncIncrease) -> None:
        async with async_client.digital_card_profiles.with_streaming_response.clone(
            digital_card_profile_id="digital_card_profile_s3puplu90f04xhcwkiga",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_card_profile = await response.parse()
            assert_matches_type(DigitalCardProfile, digital_card_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_clone(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `digital_card_profile_id` but received ''"
        ):
            await async_client.digital_card_profiles.with_raw_response.clone(
                digital_card_profile_id="",
            )
