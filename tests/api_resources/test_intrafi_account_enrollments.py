# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    IntrafiAccountEnrollment,
)
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntrafiAccountEnrollments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        intrafi_account_enrollment = client.intrafi_account_enrollments.create(
            account_id="account_in71c4amph0vgo2qllky",
            email_address="user@example.com",
        )
        assert_matches_type(IntrafiAccountEnrollment, intrafi_account_enrollment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.intrafi_account_enrollments.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            email_address="user@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intrafi_account_enrollment = response.parse()
        assert_matches_type(IntrafiAccountEnrollment, intrafi_account_enrollment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.intrafi_account_enrollments.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            email_address="user@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intrafi_account_enrollment = response.parse()
            assert_matches_type(IntrafiAccountEnrollment, intrafi_account_enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        intrafi_account_enrollment = client.intrafi_account_enrollments.retrieve(
            "intrafi_account_enrollment_id",
        )
        assert_matches_type(IntrafiAccountEnrollment, intrafi_account_enrollment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.intrafi_account_enrollments.with_raw_response.retrieve(
            "intrafi_account_enrollment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intrafi_account_enrollment = response.parse()
        assert_matches_type(IntrafiAccountEnrollment, intrafi_account_enrollment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.intrafi_account_enrollments.with_streaming_response.retrieve(
            "intrafi_account_enrollment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intrafi_account_enrollment = response.parse()
            assert_matches_type(IntrafiAccountEnrollment, intrafi_account_enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `intrafi_account_enrollment_id` but received ''"
        ):
            client.intrafi_account_enrollments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        intrafi_account_enrollment = client.intrafi_account_enrollments.list()
        assert_matches_type(SyncPage[IntrafiAccountEnrollment], intrafi_account_enrollment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        intrafi_account_enrollment = client.intrafi_account_enrollments.list(
            account_id="account_id",
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["pending_enrolling"]},
        )
        assert_matches_type(SyncPage[IntrafiAccountEnrollment], intrafi_account_enrollment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.intrafi_account_enrollments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intrafi_account_enrollment = response.parse()
        assert_matches_type(SyncPage[IntrafiAccountEnrollment], intrafi_account_enrollment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.intrafi_account_enrollments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intrafi_account_enrollment = response.parse()
            assert_matches_type(SyncPage[IntrafiAccountEnrollment], intrafi_account_enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unenroll(self, client: Increase) -> None:
        intrafi_account_enrollment = client.intrafi_account_enrollments.unenroll(
            "intrafi_account_enrollment_id",
        )
        assert_matches_type(IntrafiAccountEnrollment, intrafi_account_enrollment, path=["response"])

    @parametrize
    def test_raw_response_unenroll(self, client: Increase) -> None:
        response = client.intrafi_account_enrollments.with_raw_response.unenroll(
            "intrafi_account_enrollment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intrafi_account_enrollment = response.parse()
        assert_matches_type(IntrafiAccountEnrollment, intrafi_account_enrollment, path=["response"])

    @parametrize
    def test_streaming_response_unenroll(self, client: Increase) -> None:
        with client.intrafi_account_enrollments.with_streaming_response.unenroll(
            "intrafi_account_enrollment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intrafi_account_enrollment = response.parse()
            assert_matches_type(IntrafiAccountEnrollment, intrafi_account_enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unenroll(self, client: Increase) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `intrafi_account_enrollment_id` but received ''"
        ):
            client.intrafi_account_enrollments.with_raw_response.unenroll(
                "",
            )


class TestAsyncIntrafiAccountEnrollments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        intrafi_account_enrollment = await async_client.intrafi_account_enrollments.create(
            account_id="account_in71c4amph0vgo2qllky",
            email_address="user@example.com",
        )
        assert_matches_type(IntrafiAccountEnrollment, intrafi_account_enrollment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.intrafi_account_enrollments.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            email_address="user@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intrafi_account_enrollment = await response.parse()
        assert_matches_type(IntrafiAccountEnrollment, intrafi_account_enrollment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.intrafi_account_enrollments.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            email_address="user@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intrafi_account_enrollment = await response.parse()
            assert_matches_type(IntrafiAccountEnrollment, intrafi_account_enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        intrafi_account_enrollment = await async_client.intrafi_account_enrollments.retrieve(
            "intrafi_account_enrollment_id",
        )
        assert_matches_type(IntrafiAccountEnrollment, intrafi_account_enrollment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.intrafi_account_enrollments.with_raw_response.retrieve(
            "intrafi_account_enrollment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intrafi_account_enrollment = await response.parse()
        assert_matches_type(IntrafiAccountEnrollment, intrafi_account_enrollment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.intrafi_account_enrollments.with_streaming_response.retrieve(
            "intrafi_account_enrollment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intrafi_account_enrollment = await response.parse()
            assert_matches_type(IntrafiAccountEnrollment, intrafi_account_enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `intrafi_account_enrollment_id` but received ''"
        ):
            await async_client.intrafi_account_enrollments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        intrafi_account_enrollment = await async_client.intrafi_account_enrollments.list()
        assert_matches_type(AsyncPage[IntrafiAccountEnrollment], intrafi_account_enrollment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        intrafi_account_enrollment = await async_client.intrafi_account_enrollments.list(
            account_id="account_id",
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["pending_enrolling"]},
        )
        assert_matches_type(AsyncPage[IntrafiAccountEnrollment], intrafi_account_enrollment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.intrafi_account_enrollments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intrafi_account_enrollment = await response.parse()
        assert_matches_type(AsyncPage[IntrafiAccountEnrollment], intrafi_account_enrollment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.intrafi_account_enrollments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intrafi_account_enrollment = await response.parse()
            assert_matches_type(AsyncPage[IntrafiAccountEnrollment], intrafi_account_enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unenroll(self, async_client: AsyncIncrease) -> None:
        intrafi_account_enrollment = await async_client.intrafi_account_enrollments.unenroll(
            "intrafi_account_enrollment_id",
        )
        assert_matches_type(IntrafiAccountEnrollment, intrafi_account_enrollment, path=["response"])

    @parametrize
    async def test_raw_response_unenroll(self, async_client: AsyncIncrease) -> None:
        response = await async_client.intrafi_account_enrollments.with_raw_response.unenroll(
            "intrafi_account_enrollment_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        intrafi_account_enrollment = await response.parse()
        assert_matches_type(IntrafiAccountEnrollment, intrafi_account_enrollment, path=["response"])

    @parametrize
    async def test_streaming_response_unenroll(self, async_client: AsyncIncrease) -> None:
        async with async_client.intrafi_account_enrollments.with_streaming_response.unenroll(
            "intrafi_account_enrollment_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            intrafi_account_enrollment = await response.parse()
            assert_matches_type(IntrafiAccountEnrollment, intrafi_account_enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unenroll(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `intrafi_account_enrollment_id` but received ''"
        ):
            await async_client.intrafi_account_enrollments.with_raw_response.unenroll(
                "",
            )
