# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.pagination import AsyncPage, SyncPage

from increase.types.file import File

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestFiles:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="file upload tests are broken on the Prism mock server")
    @parametrize
    def test_method_create(self, client: Increase) -> None:
        resource = client.files.create(
            file=b"raw file contents",
            purpose="check_image_front",
        )
        assert isinstance(resource, File)

    @pytest.mark.skip(reason="file upload tests are broken on the Prism mock server")
    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        resource = client.files.create(
            file=b"raw file contents",
            description="x",
            purpose="check_image_front",
        )
        assert isinstance(resource, File)

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        resource = client.files.retrieve(
            "string",
        )
        assert isinstance(resource, File)

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        resource = client.files.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        resource = client.files.list(
            cursor="string",
            limit=0,
            created_at={
                "after": "2019-12-27T18:11:19.117Z",
                "before": "2019-12-27T18:11:19.117Z",
                "on_or_after": "2019-12-27T18:11:19.117Z",
                "on_or_before": "2019-12-27T18:11:19.117Z",
            },
            purpose={"in": ["check_image_front", "check_image_front", "check_image_front"]},
        )
        assert isinstance(resource, SyncPage)


class TestAsyncFiles:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="file upload tests are broken on the Prism mock server")
    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        resource = await client.files.create(
            file=b"raw file contents",
            purpose="check_image_front",
        )
        assert isinstance(resource, File)

    @pytest.mark.skip(reason="file upload tests are broken on the Prism mock server")
    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.files.create(
            file=b"raw file contents",
            description="x",
            purpose="check_image_front",
        )
        assert isinstance(resource, File)

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        resource = await client.files.retrieve(
            "string",
        )
        assert isinstance(resource, File)

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        resource = await client.files.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.files.list(
            cursor="string",
            limit=0,
            created_at={
                "after": "2019-12-27T18:11:19.117Z",
                "before": "2019-12-27T18:11:19.117Z",
                "on_or_after": "2019-12-27T18:11:19.117Z",
                "on_or_before": "2019-12-27T18:11:19.117Z",
            },
            purpose={"in": ["check_image_front", "check_image_front", "check_image_front"]},
        )
        assert isinstance(resource, AsyncPage)
