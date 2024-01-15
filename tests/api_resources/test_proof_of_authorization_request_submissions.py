# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    ProofOfAuthorizationRequestSubmission,
)
from increase._utils import parse_datetime
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestProofOfAuthorizationRequestSubmissions:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        proof_of_authorization_request_submission = client.proof_of_authorization_request_submissions.create(
            authorization_terms="I agree to the terms of service.",
            authorized_at=parse_datetime("2020-01-31T23:59:59Z"),
            authorizer_email="user@example.com",
            authorizer_name="Ian Crease",
            proof_of_authorization_request_id="proof_of_authorization_request_iwp8no25h3rjvil6ad3b",
        )
        assert_matches_type(
            ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
        )

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        proof_of_authorization_request_submission = client.proof_of_authorization_request_submissions.create(
            authorization_terms="I agree to the terms of service.",
            authorized_at=parse_datetime("2020-01-31T23:59:59Z"),
            authorizer_email="user@example.com",
            authorizer_name="Ian Crease",
            proof_of_authorization_request_id="proof_of_authorization_request_iwp8no25h3rjvil6ad3b",
            authorizer_company="National Phonograph Company",
            authorizer_ip_address="x",
        )
        assert_matches_type(
            ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
        )

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.proof_of_authorization_request_submissions.with_raw_response.create(
            authorization_terms="I agree to the terms of service.",
            authorized_at=parse_datetime("2020-01-31T23:59:59Z"),
            authorizer_email="user@example.com",
            authorizer_name="Ian Crease",
            proof_of_authorization_request_id="proof_of_authorization_request_iwp8no25h3rjvil6ad3b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proof_of_authorization_request_submission = response.parse()
        assert_matches_type(
            ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
        )

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.proof_of_authorization_request_submissions.with_streaming_response.create(
            authorization_terms="I agree to the terms of service.",
            authorized_at=parse_datetime("2020-01-31T23:59:59Z"),
            authorizer_email="user@example.com",
            authorizer_name="Ian Crease",
            proof_of_authorization_request_id="proof_of_authorization_request_iwp8no25h3rjvil6ad3b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proof_of_authorization_request_submission = response.parse()
            assert_matches_type(
                ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        proof_of_authorization_request_submission = client.proof_of_authorization_request_submissions.retrieve(
            "string",
        )
        assert_matches_type(
            ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
        )

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.proof_of_authorization_request_submissions.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proof_of_authorization_request_submission = response.parse()
        assert_matches_type(
            ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
        )

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.proof_of_authorization_request_submissions.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proof_of_authorization_request_submission = response.parse()
            assert_matches_type(
                ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        proof_of_authorization_request_submission = client.proof_of_authorization_request_submissions.list()
        assert_matches_type(
            SyncPage[ProofOfAuthorizationRequestSubmission],
            proof_of_authorization_request_submission,
            path=["response"],
        )

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        proof_of_authorization_request_submission = client.proof_of_authorization_request_submissions.list(
            cursor="string",
            limit=1,
            proof_of_authorization_request_id="string",
        )
        assert_matches_type(
            SyncPage[ProofOfAuthorizationRequestSubmission],
            proof_of_authorization_request_submission,
            path=["response"],
        )

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.proof_of_authorization_request_submissions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proof_of_authorization_request_submission = response.parse()
        assert_matches_type(
            SyncPage[ProofOfAuthorizationRequestSubmission],
            proof_of_authorization_request_submission,
            path=["response"],
        )

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.proof_of_authorization_request_submissions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proof_of_authorization_request_submission = response.parse()
            assert_matches_type(
                SyncPage[ProofOfAuthorizationRequestSubmission],
                proof_of_authorization_request_submission,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncProofOfAuthorizationRequestSubmissions:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        proof_of_authorization_request_submission = await client.proof_of_authorization_request_submissions.create(
            authorization_terms="I agree to the terms of service.",
            authorized_at=parse_datetime("2020-01-31T23:59:59Z"),
            authorizer_email="user@example.com",
            authorizer_name="Ian Crease",
            proof_of_authorization_request_id="proof_of_authorization_request_iwp8no25h3rjvil6ad3b",
        )
        assert_matches_type(
            ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
        )

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        proof_of_authorization_request_submission = await client.proof_of_authorization_request_submissions.create(
            authorization_terms="I agree to the terms of service.",
            authorized_at=parse_datetime("2020-01-31T23:59:59Z"),
            authorizer_email="user@example.com",
            authorizer_name="Ian Crease",
            proof_of_authorization_request_id="proof_of_authorization_request_iwp8no25h3rjvil6ad3b",
            authorizer_company="National Phonograph Company",
            authorizer_ip_address="x",
        )
        assert_matches_type(
            ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
        )

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.proof_of_authorization_request_submissions.with_raw_response.create(
            authorization_terms="I agree to the terms of service.",
            authorized_at=parse_datetime("2020-01-31T23:59:59Z"),
            authorizer_email="user@example.com",
            authorizer_name="Ian Crease",
            proof_of_authorization_request_id="proof_of_authorization_request_iwp8no25h3rjvil6ad3b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proof_of_authorization_request_submission = response.parse()
        assert_matches_type(
            ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
        )

    @parametrize
    async def test_streaming_response_create(self, client: AsyncIncrease) -> None:
        async with client.proof_of_authorization_request_submissions.with_streaming_response.create(
            authorization_terms="I agree to the terms of service.",
            authorized_at=parse_datetime("2020-01-31T23:59:59Z"),
            authorizer_email="user@example.com",
            authorizer_name="Ian Crease",
            proof_of_authorization_request_id="proof_of_authorization_request_iwp8no25h3rjvil6ad3b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proof_of_authorization_request_submission = await response.parse()
            assert_matches_type(
                ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        proof_of_authorization_request_submission = await client.proof_of_authorization_request_submissions.retrieve(
            "string",
        )
        assert_matches_type(
            ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
        )

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.proof_of_authorization_request_submissions.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proof_of_authorization_request_submission = response.parse()
        assert_matches_type(
            ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
        )

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncIncrease) -> None:
        async with client.proof_of_authorization_request_submissions.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proof_of_authorization_request_submission = await response.parse()
            assert_matches_type(
                ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        proof_of_authorization_request_submission = await client.proof_of_authorization_request_submissions.list()
        assert_matches_type(
            AsyncPage[ProofOfAuthorizationRequestSubmission],
            proof_of_authorization_request_submission,
            path=["response"],
        )

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        proof_of_authorization_request_submission = await client.proof_of_authorization_request_submissions.list(
            cursor="string",
            limit=1,
            proof_of_authorization_request_id="string",
        )
        assert_matches_type(
            AsyncPage[ProofOfAuthorizationRequestSubmission],
            proof_of_authorization_request_submission,
            path=["response"],
        )

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.proof_of_authorization_request_submissions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proof_of_authorization_request_submission = response.parse()
        assert_matches_type(
            AsyncPage[ProofOfAuthorizationRequestSubmission],
            proof_of_authorization_request_submission,
            path=["response"],
        )

    @parametrize
    async def test_streaming_response_list(self, client: AsyncIncrease) -> None:
        async with client.proof_of_authorization_request_submissions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proof_of_authorization_request_submission = await response.parse()
            assert_matches_type(
                AsyncPage[ProofOfAuthorizationRequestSubmission],
                proof_of_authorization_request_submission,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True
