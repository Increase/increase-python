# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import ProofOfAuthorizationRequest
from increase._utils import parse_datetime
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestProofOfAuthorizationRequests:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        proof_of_authorization_request = client.proof_of_authorization_requests.retrieve(
            "string",
        )
        assert_matches_type(ProofOfAuthorizationRequest, proof_of_authorization_request, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.proof_of_authorization_requests.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proof_of_authorization_request = response.parse()
        assert_matches_type(ProofOfAuthorizationRequest, proof_of_authorization_request, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        proof_of_authorization_request = client.proof_of_authorization_requests.list()
        assert_matches_type(SyncPage[ProofOfAuthorizationRequest], proof_of_authorization_request, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        proof_of_authorization_request = client.proof_of_authorization_requests.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
        )
        assert_matches_type(SyncPage[ProofOfAuthorizationRequest], proof_of_authorization_request, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.proof_of_authorization_requests.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proof_of_authorization_request = response.parse()
        assert_matches_type(SyncPage[ProofOfAuthorizationRequest], proof_of_authorization_request, path=["response"])


class TestAsyncProofOfAuthorizationRequests:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        proof_of_authorization_request = await client.proof_of_authorization_requests.retrieve(
            "string",
        )
        assert_matches_type(ProofOfAuthorizationRequest, proof_of_authorization_request, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.proof_of_authorization_requests.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proof_of_authorization_request = response.parse()
        assert_matches_type(ProofOfAuthorizationRequest, proof_of_authorization_request, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        proof_of_authorization_request = await client.proof_of_authorization_requests.list()
        assert_matches_type(AsyncPage[ProofOfAuthorizationRequest], proof_of_authorization_request, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        proof_of_authorization_request = await client.proof_of_authorization_requests.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
        )
        assert_matches_type(AsyncPage[ProofOfAuthorizationRequest], proof_of_authorization_request, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.proof_of_authorization_requests.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proof_of_authorization_request = response.parse()
        assert_matches_type(AsyncPage[ProofOfAuthorizationRequest], proof_of_authorization_request, path=["response"])
