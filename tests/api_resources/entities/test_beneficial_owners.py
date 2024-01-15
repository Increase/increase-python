# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Entity
from increase._utils import parse_date
from increase._client import Increase, AsyncIncrease

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestBeneficialOwners:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        beneficial_owner = client.entities.beneficial_owners.create(
            beneficial_owner={
                "individual": {
                    "name": "Ian Crease",
                    "date_of_birth": parse_date("1970-01-31"),
                    "address": {
                        "line1": "33 Liberty Street",
                        "city": "New York",
                        "state": "NY",
                        "zip": "10045",
                    },
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                    },
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
                "individual": {
                    "name": "Ian Crease",
                    "date_of_birth": parse_date("1970-01-31"),
                    "address": {
                        "line1": "33 Liberty Street",
                        "line2": "x",
                        "city": "New York",
                        "state": "NY",
                        "zip": "10045",
                    },
                    "confirmed_no_us_tax_id": True,
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                        "passport": {
                            "file_id": "string",
                            "expiration_date": parse_date("2019-12-27"),
                            "country": "x",
                        },
                        "drivers_license": {
                            "file_id": "string",
                            "back_file_id": "string",
                            "expiration_date": parse_date("2019-12-27"),
                            "state": "x",
                        },
                        "other": {
                            "country": "x",
                            "description": "x",
                            "expiration_date": parse_date("2019-12-27"),
                            "file_id": "string",
                            "back_file_id": "string",
                        },
                    },
                },
                "company_title": "CEO",
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
                    "name": "Ian Crease",
                    "date_of_birth": parse_date("1970-01-31"),
                    "address": {
                        "line1": "33 Liberty Street",
                        "city": "New York",
                        "state": "NY",
                        "zip": "10045",
                    },
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                    },
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
                    "name": "Ian Crease",
                    "date_of_birth": parse_date("1970-01-31"),
                    "address": {
                        "line1": "33 Liberty Street",
                        "city": "New York",
                        "state": "NY",
                        "zip": "10045",
                    },
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                    },
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
                "line1": "33 Liberty Street",
                "city": "New York",
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
                "line1": "33 Liberty Street",
                "line2": "Unit 2",
                "city": "New York",
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
                "line1": "33 Liberty Street",
                "city": "New York",
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
                "line1": "33 Liberty Street",
                "city": "New York",
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
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        beneficial_owner = await client.entities.beneficial_owners.create(
            beneficial_owner={
                "individual": {
                    "name": "Ian Crease",
                    "date_of_birth": parse_date("1970-01-31"),
                    "address": {
                        "line1": "33 Liberty Street",
                        "city": "New York",
                        "state": "NY",
                        "zip": "10045",
                    },
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                    },
                },
                "prongs": ["control"],
            },
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        beneficial_owner = await client.entities.beneficial_owners.create(
            beneficial_owner={
                "individual": {
                    "name": "Ian Crease",
                    "date_of_birth": parse_date("1970-01-31"),
                    "address": {
                        "line1": "33 Liberty Street",
                        "line2": "x",
                        "city": "New York",
                        "state": "NY",
                        "zip": "10045",
                    },
                    "confirmed_no_us_tax_id": True,
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                        "passport": {
                            "file_id": "string",
                            "expiration_date": parse_date("2019-12-27"),
                            "country": "x",
                        },
                        "drivers_license": {
                            "file_id": "string",
                            "back_file_id": "string",
                            "expiration_date": parse_date("2019-12-27"),
                            "state": "x",
                        },
                        "other": {
                            "country": "x",
                            "description": "x",
                            "expiration_date": parse_date("2019-12-27"),
                            "file_id": "string",
                            "back_file_id": "string",
                        },
                    },
                },
                "company_title": "CEO",
                "prongs": ["control"],
            },
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.entities.beneficial_owners.with_raw_response.create(
            beneficial_owner={
                "individual": {
                    "name": "Ian Crease",
                    "date_of_birth": parse_date("1970-01-31"),
                    "address": {
                        "line1": "33 Liberty Street",
                        "city": "New York",
                        "state": "NY",
                        "zip": "10045",
                    },
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                    },
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
    async def test_streaming_response_create(self, client: AsyncIncrease) -> None:
        async with client.entities.beneficial_owners.with_streaming_response.create(
            beneficial_owner={
                "individual": {
                    "name": "Ian Crease",
                    "date_of_birth": parse_date("1970-01-31"),
                    "address": {
                        "line1": "33 Liberty Street",
                        "city": "New York",
                        "state": "NY",
                        "zip": "10045",
                    },
                    "identification": {
                        "method": "social_security_number",
                        "number": "078051120",
                    },
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
    async def test_method_archive(self, client: AsyncIncrease) -> None:
        beneficial_owner = await client.entities.beneficial_owners.archive(
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, client: AsyncIncrease) -> None:
        response = await client.entities.beneficial_owners.with_raw_response.archive(
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beneficial_owner = response.parse()
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, client: AsyncIncrease) -> None:
        async with client.entities.beneficial_owners.with_streaming_response.archive(
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beneficial_owner = await response.parse()
            assert_matches_type(Entity, beneficial_owner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_address(self, client: AsyncIncrease) -> None:
        beneficial_owner = await client.entities.beneficial_owners.update_address(
            address={
                "line1": "33 Liberty Street",
                "city": "New York",
                "state": "NY",
                "zip": "10045",
            },
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    async def test_method_update_address_with_all_params(self, client: AsyncIncrease) -> None:
        beneficial_owner = await client.entities.beneficial_owners.update_address(
            address={
                "line1": "33 Liberty Street",
                "line2": "Unit 2",
                "city": "New York",
                "state": "NY",
                "zip": "10045",
            },
            beneficial_owner_id="entity_setup_beneficial_owner_submission_vgkyk7dj5eb4sfhdbkx7",
            entity_id="entity_n8y8tnk2p9339ti393yi",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    async def test_raw_response_update_address(self, client: AsyncIncrease) -> None:
        response = await client.entities.beneficial_owners.with_raw_response.update_address(
            address={
                "line1": "33 Liberty Street",
                "city": "New York",
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
    async def test_streaming_response_update_address(self, client: AsyncIncrease) -> None:
        async with client.entities.beneficial_owners.with_streaming_response.update_address(
            address={
                "line1": "33 Liberty Street",
                "city": "New York",
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
