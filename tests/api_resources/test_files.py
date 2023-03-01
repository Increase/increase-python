# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import File
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestFiles:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="file upload tests are broken on the Prism mock server")
    @parametrize
    def test_method_create(self, client: Increase) -> None:
        file = client.files.create(
            file=b"raw file contents",
            purpose="check_image_front",
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="file upload tests are broken on the Prism mock server")
    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        file = client.files.create(
            file=b"raw file contents",
            description="x",
            purpose="check_image_front",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        file = client.files.retrieve(
            "string",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        file = client.files.list()
        assert_matches_type(SyncPage[File], file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        file = client.files.list(
            cursor="string",
            limit=0,
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            purpose={"in": ["check_image_front", "check_image_front", "check_image_front"]},
        )
        assert_matches_type(SyncPage[File], file, path=["response"])


class TestAsyncFiles:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="file upload tests are broken on the Prism mock server")
    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        file = await client.files.create(
            file=b"raw file contents",
            purpose="check_image_front",
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="file upload tests are broken on the Prism mock server")
    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        file = await client.files.create(
            file=b"raw file contents",
            description="x",
            purpose="check_image_front",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        file = await client.files.retrieve(
            "string",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        file = await client.files.list()
        assert_matches_type(AsyncPage[File], file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        file = await client.files.list(
            cursor="string",
            limit=0,
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            purpose={"in": ["check_image_front", "check_image_front", "check_image_front"]},
        )
        assert_matches_type(AsyncPage[File], file, path=["response"])
