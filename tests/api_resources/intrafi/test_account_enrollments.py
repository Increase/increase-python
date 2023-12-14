# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.intrafi import IntrafiAccountEnrollment

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestAccountEnrollments:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        account_enrollment = client.intrafi.account_enrollments.create(
            account_id="account_in71c4amph0vgo2qllky",
            email_address="user@example.com",
        )
        assert_matches_type(IntrafiAccountEnrollment, account_enrollment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.intrafi.account_enrollments.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            email_address="user@example.com",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_enrollment = response.parse()
        assert_matches_type(IntrafiAccountEnrollment, account_enrollment, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        account_enrollment = client.intrafi.account_enrollments.retrieve(
            "string",
        )
        assert_matches_type(IntrafiAccountEnrollment, account_enrollment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.intrafi.account_enrollments.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_enrollment = response.parse()
        assert_matches_type(IntrafiAccountEnrollment, account_enrollment, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        account_enrollment = client.intrafi.account_enrollments.list()
        assert_matches_type(SyncPage[IntrafiAccountEnrollment], account_enrollment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        account_enrollment = client.intrafi.account_enrollments.list(
            account_id="string",
            cursor="string",
            limit=1,
            status={"in": ["pending_enrolling", "enrolled", "pending_unenrolling"]},
        )
        assert_matches_type(SyncPage[IntrafiAccountEnrollment], account_enrollment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.intrafi.account_enrollments.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_enrollment = response.parse()
        assert_matches_type(SyncPage[IntrafiAccountEnrollment], account_enrollment, path=["response"])

    @parametrize
    def test_method_unenroll(self, client: Increase) -> None:
        account_enrollment = client.intrafi.account_enrollments.unenroll(
            "string",
        )
        assert_matches_type(IntrafiAccountEnrollment, account_enrollment, path=["response"])

    @parametrize
    def test_raw_response_unenroll(self, client: Increase) -> None:
        response = client.intrafi.account_enrollments.with_raw_response.unenroll(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_enrollment = response.parse()
        assert_matches_type(IntrafiAccountEnrollment, account_enrollment, path=["response"])


class TestAsyncAccountEnrollments:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        account_enrollment = await client.intrafi.account_enrollments.create(
            account_id="account_in71c4amph0vgo2qllky",
            email_address="user@example.com",
        )
        assert_matches_type(IntrafiAccountEnrollment, account_enrollment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.intrafi.account_enrollments.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            email_address="user@example.com",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_enrollment = response.parse()
        assert_matches_type(IntrafiAccountEnrollment, account_enrollment, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        account_enrollment = await client.intrafi.account_enrollments.retrieve(
            "string",
        )
        assert_matches_type(IntrafiAccountEnrollment, account_enrollment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.intrafi.account_enrollments.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_enrollment = response.parse()
        assert_matches_type(IntrafiAccountEnrollment, account_enrollment, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        account_enrollment = await client.intrafi.account_enrollments.list()
        assert_matches_type(AsyncPage[IntrafiAccountEnrollment], account_enrollment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        account_enrollment = await client.intrafi.account_enrollments.list(
            account_id="string",
            cursor="string",
            limit=1,
            status={"in": ["pending_enrolling", "enrolled", "pending_unenrolling"]},
        )
        assert_matches_type(AsyncPage[IntrafiAccountEnrollment], account_enrollment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.intrafi.account_enrollments.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_enrollment = response.parse()
        assert_matches_type(AsyncPage[IntrafiAccountEnrollment], account_enrollment, path=["response"])

    @parametrize
    async def test_method_unenroll(self, client: AsyncIncrease) -> None:
        account_enrollment = await client.intrafi.account_enrollments.unenroll(
            "string",
        )
        assert_matches_type(IntrafiAccountEnrollment, account_enrollment, path=["response"])

    @parametrize
    async def test_raw_response_unenroll(self, client: AsyncIncrease) -> None:
        response = await client.intrafi.account_enrollments.with_raw_response.unenroll(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_enrollment = response.parse()
        assert_matches_type(IntrafiAccountEnrollment, account_enrollment, path=["response"])
