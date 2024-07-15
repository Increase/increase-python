# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProofOfAuthorizationRequestSubmissions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        proof_of_authorization_request_submission = client.proof_of_authorization_request_submissions.create(
            authorization_terms="I agree to the terms of service.",
            authorized_at=parse_datetime("2020-01-31T23:59:59Z"),
            authorizer_email="user@example.com",
            authorizer_name="Ian Crease",
            customer_has_been_offboarded=True,
            proof_of_authorization_request_id="proof_of_authorization_request_iwp8no25h3rjvil6ad3b",
            validated_account_ownership_via_credential=True,
            validated_account_ownership_with_account_statement=True,
            validated_account_ownership_with_microdeposit=True,
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
            customer_has_been_offboarded=True,
            proof_of_authorization_request_id="proof_of_authorization_request_iwp8no25h3rjvil6ad3b",
            validated_account_ownership_via_credential=True,
            validated_account_ownership_with_account_statement=True,
            validated_account_ownership_with_microdeposit=True,
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
            customer_has_been_offboarded=True,
            proof_of_authorization_request_id="proof_of_authorization_request_iwp8no25h3rjvil6ad3b",
            validated_account_ownership_via_credential=True,
            validated_account_ownership_with_account_statement=True,
            validated_account_ownership_with_microdeposit=True,
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
            customer_has_been_offboarded=True,
            proof_of_authorization_request_id="proof_of_authorization_request_iwp8no25h3rjvil6ad3b",
            validated_account_ownership_via_credential=True,
            validated_account_ownership_with_account_statement=True,
            validated_account_ownership_with_microdeposit=True,
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
            "proof_of_authorization_request_submission_id",
        )
        assert_matches_type(
            ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
        )

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.proof_of_authorization_request_submissions.with_raw_response.retrieve(
            "proof_of_authorization_request_submission_id",
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
            "proof_of_authorization_request_submission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proof_of_authorization_request_submission = response.parse()
            assert_matches_type(
                ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `proof_of_authorization_request_submission_id` but received ''",
        ):
            client.proof_of_authorization_request_submissions.with_raw_response.retrieve(
                "",
            )

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
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            proof_of_authorization_request_id="proof_of_authorization_request_id",
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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        proof_of_authorization_request_submission = (
            await async_client.proof_of_authorization_request_submissions.create(
                authorization_terms="I agree to the terms of service.",
                authorized_at=parse_datetime("2020-01-31T23:59:59Z"),
                authorizer_email="user@example.com",
                authorizer_name="Ian Crease",
                customer_has_been_offboarded=True,
                proof_of_authorization_request_id="proof_of_authorization_request_iwp8no25h3rjvil6ad3b",
                validated_account_ownership_via_credential=True,
                validated_account_ownership_with_account_statement=True,
                validated_account_ownership_with_microdeposit=True,
            )
        )
        assert_matches_type(
            ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
        )

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        proof_of_authorization_request_submission = (
            await async_client.proof_of_authorization_request_submissions.create(
                authorization_terms="I agree to the terms of service.",
                authorized_at=parse_datetime("2020-01-31T23:59:59Z"),
                authorizer_email="user@example.com",
                authorizer_name="Ian Crease",
                customer_has_been_offboarded=True,
                proof_of_authorization_request_id="proof_of_authorization_request_iwp8no25h3rjvil6ad3b",
                validated_account_ownership_via_credential=True,
                validated_account_ownership_with_account_statement=True,
                validated_account_ownership_with_microdeposit=True,
                authorizer_company="National Phonograph Company",
                authorizer_ip_address="x",
            )
        )
        assert_matches_type(
            ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
        )

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.proof_of_authorization_request_submissions.with_raw_response.create(
            authorization_terms="I agree to the terms of service.",
            authorized_at=parse_datetime("2020-01-31T23:59:59Z"),
            authorizer_email="user@example.com",
            authorizer_name="Ian Crease",
            customer_has_been_offboarded=True,
            proof_of_authorization_request_id="proof_of_authorization_request_iwp8no25h3rjvil6ad3b",
            validated_account_ownership_via_credential=True,
            validated_account_ownership_with_account_statement=True,
            validated_account_ownership_with_microdeposit=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proof_of_authorization_request_submission = await response.parse()
        assert_matches_type(
            ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
        )

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.proof_of_authorization_request_submissions.with_streaming_response.create(
            authorization_terms="I agree to the terms of service.",
            authorized_at=parse_datetime("2020-01-31T23:59:59Z"),
            authorizer_email="user@example.com",
            authorizer_name="Ian Crease",
            customer_has_been_offboarded=True,
            proof_of_authorization_request_id="proof_of_authorization_request_iwp8no25h3rjvil6ad3b",
            validated_account_ownership_via_credential=True,
            validated_account_ownership_with_account_statement=True,
            validated_account_ownership_with_microdeposit=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proof_of_authorization_request_submission = await response.parse()
            assert_matches_type(
                ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        proof_of_authorization_request_submission = (
            await async_client.proof_of_authorization_request_submissions.retrieve(
                "proof_of_authorization_request_submission_id",
            )
        )
        assert_matches_type(
            ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
        )

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.proof_of_authorization_request_submissions.with_raw_response.retrieve(
            "proof_of_authorization_request_submission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proof_of_authorization_request_submission = await response.parse()
        assert_matches_type(
            ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
        )

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.proof_of_authorization_request_submissions.with_streaming_response.retrieve(
            "proof_of_authorization_request_submission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proof_of_authorization_request_submission = await response.parse()
            assert_matches_type(
                ProofOfAuthorizationRequestSubmission, proof_of_authorization_request_submission, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `proof_of_authorization_request_submission_id` but received ''",
        ):
            await async_client.proof_of_authorization_request_submissions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        proof_of_authorization_request_submission = await async_client.proof_of_authorization_request_submissions.list()
        assert_matches_type(
            AsyncPage[ProofOfAuthorizationRequestSubmission],
            proof_of_authorization_request_submission,
            path=["response"],
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        proof_of_authorization_request_submission = await async_client.proof_of_authorization_request_submissions.list(
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            proof_of_authorization_request_id="proof_of_authorization_request_id",
        )
        assert_matches_type(
            AsyncPage[ProofOfAuthorizationRequestSubmission],
            proof_of_authorization_request_submission,
            path=["response"],
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.proof_of_authorization_request_submissions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proof_of_authorization_request_submission = await response.parse()
        assert_matches_type(
            AsyncPage[ProofOfAuthorizationRequestSubmission],
            proof_of_authorization_request_submission,
            path=["response"],
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.proof_of_authorization_request_submissions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proof_of_authorization_request_submission = await response.parse()
            assert_matches_type(
                AsyncPage[ProofOfAuthorizationRequestSubmission],
                proof_of_authorization_request_submission,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True
