# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.file import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestFiles:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    @pytest.mark.skip(reason="file upload tests are broken on the Prism mock server")
    def test_method_create(self) -> None:
        resource = self.client.files.create(
            {
                "file": b"raw file contents",
                "purpose": "check_image_front",
            },
        )
        assert isinstance(resource, File)

    @pytest.mark.skip(reason="file upload tests are broken on the Prism mock server")
    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.files.create(
            {
                "file": b"raw file contents",
                "description": "x",
                "purpose": "check_image_front",
            },
        )
        assert isinstance(resource, File)

    def test_method_retrieve(self) -> None:
        resource = self.client.files.retrieve(
            "string",
        )
        assert isinstance(resource, File)

    def test_method_list(self) -> None:
        resource = self.client.files.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.files.list(
            {
                "cursor": "x",
                "limit": 0,
                "created_at": {
                    "after": "2019-12-27T18:11:19.117Z",
                    "before": "2019-12-27T18:11:19.117Z",
                    "on_or_after": "2019-12-27T18:11:19.117Z",
                    "on_or_before": "2019-12-27T18:11:19.117Z",
                },
                "purpose": {"in": ["check_image_front", "check_image_front", "check_image_front"]},
            },
        )
        assert isinstance(resource, SyncPage)


class TestAsyncFiles:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    @pytest.mark.skip(reason="file upload tests are broken on the Prism mock server")
    async def test_method_create(self) -> None:
        resource = await self.client.files.create(
            {
                "file": b"raw file contents",
                "purpose": "check_image_front",
            },
        )
        assert isinstance(resource, File)

    @pytest.mark.skip(reason="file upload tests are broken on the Prism mock server")
    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.files.create(
            {
                "file": b"raw file contents",
                "description": "x",
                "purpose": "check_image_front",
            },
        )
        assert isinstance(resource, File)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.files.retrieve(
            "string",
        )
        assert isinstance(resource, File)

    async def test_method_list(self) -> None:
        resource = await self.client.files.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.files.list(
            {
                "cursor": "x",
                "limit": 0,
                "created_at": {
                    "after": "2019-12-27T18:11:19.117Z",
                    "before": "2019-12-27T18:11:19.117Z",
                    "on_or_after": "2019-12-27T18:11:19.117Z",
                    "on_or_before": "2019-12-27T18:11:19.117Z",
                },
                "purpose": {"in": ["check_image_front", "check_image_front", "check_image_front"]},
            },
        )
        assert isinstance(resource, AsyncPage)
