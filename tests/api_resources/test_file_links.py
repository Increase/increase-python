# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import FileLink
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFileLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        file_link = client.file_links.create(
            file_id="file_makxrc67oh9l6sg7w9yc",
        )
        assert_matches_type(FileLink, file_link, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        file_link = client.file_links.create(
            file_id="file_makxrc67oh9l6sg7w9yc",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(FileLink, file_link, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.file_links.with_raw_response.create(
            file_id="file_makxrc67oh9l6sg7w9yc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_link = response.parse()
        assert_matches_type(FileLink, file_link, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.file_links.with_streaming_response.create(
            file_id="file_makxrc67oh9l6sg7w9yc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_link = response.parse()
            assert_matches_type(FileLink, file_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        file_link = client.file_links.retrieve(
            "file_link_id",
        )
        assert_matches_type(FileLink, file_link, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.file_links.with_raw_response.retrieve(
            "file_link_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_link = response.parse()
        assert_matches_type(FileLink, file_link, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.file_links.with_streaming_response.retrieve(
            "file_link_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_link = response.parse()
            assert_matches_type(FileLink, file_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_link_id` but received ''"):
            client.file_links.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        file_link = client.file_links.list(
            file_id="file_id",
        )
        assert_matches_type(SyncPage[FileLink], file_link, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        file_link = client.file_links.list(
            file_id="file_id",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
        )
        assert_matches_type(SyncPage[FileLink], file_link, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.file_links.with_raw_response.list(
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_link = response.parse()
        assert_matches_type(SyncPage[FileLink], file_link, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.file_links.with_streaming_response.list(
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_link = response.parse()
            assert_matches_type(SyncPage[FileLink], file_link, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFileLinks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        file_link = await async_client.file_links.create(
            file_id="file_makxrc67oh9l6sg7w9yc",
        )
        assert_matches_type(FileLink, file_link, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        file_link = await async_client.file_links.create(
            file_id="file_makxrc67oh9l6sg7w9yc",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(FileLink, file_link, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.file_links.with_raw_response.create(
            file_id="file_makxrc67oh9l6sg7w9yc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_link = await response.parse()
        assert_matches_type(FileLink, file_link, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.file_links.with_streaming_response.create(
            file_id="file_makxrc67oh9l6sg7w9yc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_link = await response.parse()
            assert_matches_type(FileLink, file_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        file_link = await async_client.file_links.retrieve(
            "file_link_id",
        )
        assert_matches_type(FileLink, file_link, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.file_links.with_raw_response.retrieve(
            "file_link_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_link = await response.parse()
        assert_matches_type(FileLink, file_link, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.file_links.with_streaming_response.retrieve(
            "file_link_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_link = await response.parse()
            assert_matches_type(FileLink, file_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_link_id` but received ''"):
            await async_client.file_links.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        file_link = await async_client.file_links.list(
            file_id="file_id",
        )
        assert_matches_type(AsyncPage[FileLink], file_link, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        file_link = await async_client.file_links.list(
            file_id="file_id",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
        )
        assert_matches_type(AsyncPage[FileLink], file_link, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.file_links.with_raw_response.list(
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_link = await response.parse()
        assert_matches_type(AsyncPage[FileLink], file_link, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.file_links.with_streaming_response.list(
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_link = await response.parse()
            assert_matches_type(AsyncPage[FileLink], file_link, path=["response"])

        assert cast(Any, response.is_closed) is True
