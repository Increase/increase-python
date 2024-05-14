# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Entity
from increase._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBeneficialOwners:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        beneficial_owner = client.entities.beneficial_owners.create(
            beneficial_owner={
                "individual": {
                    "address": {
                        "city": "New York",
                        "line1": "33 Liberty Street",
                        "state": "NY",
                        "zip": "10045",
                    },
                    "date_of_birth": parse_date("1970-01-31"),
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                    },
                    "name": "Ian Crease",
                },
                "prongs": ["control"],
            },
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        beneficial_owner = client.entities.beneficial_owners.create(
            beneficial_owner={
                "company_title": "CEO",
                "individual": {
                    "address": {
                        "city": "New York",
                        "line1": "33 Liberty Street",
                        "line2": "x",
                        "state": "NY",
                        "zip": "10045",
                    },
                    "confirmed_no_us_tax_id": True,
                    "date_of_birth": parse_date("1970-01-31"),
                    "identification": {
                        "drivers_license": {
                            "back_file_id": "string",
                            "expiration_date": parse_date("2019-12-27"),
                            "file_id": "string",
                            "state": "x",
                        },
                        "method": "social_security_number",
                        "number": "078051120",
                        "other": {
                            "back_file_id": "string",
                            "country": "x",
                            "description": "x",
                            "expiration_date": parse_date("2019-12-27"),
                            "file_id": "string",
                        },
                        "passport": {
                            "country": "x",
                            "expiration_date": parse_date("2019-12-27"),
                            "file_id": "string",
                        },
                    },
                    "name": "Ian Crease",
                },
                "prongs": ["control"],
            },
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.entities.beneficial_owners.with_raw_response.create(
            beneficial_owner={
                "individual": {
                    "address": {
                        "city": "New York",
                        "line1": "33 Liberty Street",
                        "state": "NY",
                        "zip": "10045",
                    },
                    "date_of_birth": parse_date("1970-01-31"),
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                    },
                    "name": "Ian Crease",
                },
                "prongs": ["control"],
            },
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beneficial_owner = response.parse()
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.entities.beneficial_owners.with_streaming_response.create(
            beneficial_owner={
                "individual": {
                    "address": {
                        "city": "New York",
                        "line1": "33 Liberty Street",
                        "state": "NY",
                        "zip": "10045",
                    },
                    "date_of_birth": parse_date("1970-01-31"),
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                    },
                    "name": "Ian Crease",
                },
                "prongs": ["control"],
            },
            entity_id="entity_n8y8tnk2p9339ti393yi",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beneficial_owner = response.parse()
            assert_matches_type(Entity, beneficial_owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Increase) -> None:
        beneficial_owner = client.entities.beneficial_owners.archive(
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Increase) -> None:
        response = client.entities.beneficial_owners.with_raw_response.archive(
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beneficial_owner = response.parse()
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Increase) -> None:
        with client.entities.beneficial_owners.with_streaming_response.archive(
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beneficial_owner = response.parse()
            assert_matches_type(Entity, beneficial_owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_address(self, client: Increase) -> None:
        beneficial_owner = client.entities.beneficial_owners.update_address(
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "state": "NY",
                "zip": "10045",
            },
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    def test_method_update_address_with_all_params(self, client: Increase) -> None:
        beneficial_owner = client.entities.beneficial_owners.update_address(
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "line2": "Unit 2",
                "state": "NY",
                "zip": "10045",
            },
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    def test_raw_response_update_address(self, client: Increase) -> None:
        response = client.entities.beneficial_owners.with_raw_response.update_address(
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "state": "NY",
                "zip": "10045",
            },
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beneficial_owner = response.parse()
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    def test_streaming_response_update_address(self, client: Increase) -> None:
        with client.entities.beneficial_owners.with_streaming_response.update_address(
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "state": "NY",
                "zip": "10045",
            },
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beneficial_owner = response.parse()
            assert_matches_type(Entity, beneficial_owner, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBeneficialOwners:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        beneficial_owner = await async_client.entities.beneficial_owners.create(
            beneficial_owner={
                "individual": {
                    "address": {
                        "city": "New York",
                        "line1": "33 Liberty Street",
                        "state": "NY",
                        "zip": "10045",
                    },
                    "date_of_birth": parse_date("1970-01-31"),
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                    },
                    "name": "Ian Crease",
                },
                "prongs": ["control"],
            },
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        beneficial_owner = await async_client.entities.beneficial_owners.create(
            beneficial_owner={
                "company_title": "CEO",
                "individual": {
                    "address": {
                        "city": "New York",
                        "line1": "33 Liberty Street",
                        "line2": "x",
                        "state": "NY",
                        "zip": "10045",
                    },
                    "confirmed_no_us_tax_id": True,
                    "date_of_birth": parse_date("1970-01-31"),
                    "identification": {
                        "drivers_license": {
                            "back_file_id": "string",
                            "expiration_date": parse_date("2019-12-27"),
                            "file_id": "string",
                            "state": "x",
                        },
                        "method": "social_security_number",
                        "number": "078051120",
                        "other": {
                            "back_file_id": "string",
                            "country": "x",
                            "description": "x",
                            "expiration_date": parse_date("2019-12-27"),
                            "file_id": "string",
                        },
                        "passport": {
                            "country": "x",
                            "expiration_date": parse_date("2019-12-27"),
                            "file_id": "string",
                        },
                    },
                    "name": "Ian Crease",
                },
                "prongs": ["control"],
            },
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.beneficial_owners.with_raw_response.create(
            beneficial_owner={
                "individual": {
                    "address": {
                        "city": "New York",
                        "line1": "33 Liberty Street",
                        "state": "NY",
                        "zip": "10045",
                    },
                    "date_of_birth": parse_date("1970-01-31"),
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                    },
                    "name": "Ian Crease",
                },
                "prongs": ["control"],
            },
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beneficial_owner = response.parse()
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.beneficial_owners.with_streaming_response.create(
            beneficial_owner={
                "individual": {
                    "address": {
                        "city": "New York",
                        "line1": "33 Liberty Street",
                        "state": "NY",
                        "zip": "10045",
                    },
                    "date_of_birth": parse_date("1970-01-31"),
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                    },
                    "name": "Ian Crease",
                },
                "prongs": ["control"],
            },
            entity_id="entity_n8y8tnk2p9339ti393yi",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beneficial_owner = await response.parse()
            assert_matches_type(Entity, beneficial_owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncIncrease) -> None:
        beneficial_owner = await async_client.entities.beneficial_owners.archive(
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.beneficial_owners.with_raw_response.archive(
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beneficial_owner = response.parse()
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.beneficial_owners.with_streaming_response.archive(
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beneficial_owner = await response.parse()
            assert_matches_type(Entity, beneficial_owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_address(self, async_client: AsyncIncrease) -> None:
        beneficial_owner = await async_client.entities.beneficial_owners.update_address(
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "state": "NY",
                "zip": "10045",
            },
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    async def test_method_update_address_with_all_params(self, async_client: AsyncIncrease) -> None:
        beneficial_owner = await async_client.entities.beneficial_owners.update_address(
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "line2": "Unit 2",
                "state": "NY",
                "zip": "10045",
            },
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    async def test_raw_response_update_address(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.beneficial_owners.with_raw_response.update_address(
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "state": "NY",
                "zip": "10045",
            },
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beneficial_owner = response.parse()
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    async def test_streaming_response_update_address(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.beneficial_owners.with_streaming_response.update_address(
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "state": "NY",
                "zip": "10045",
            },
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beneficial_owner = await response.parse()
            assert_matches_type(Entity, beneficial_owner, path=["response"])

        assert cast(Any, response.is_closed) is True
