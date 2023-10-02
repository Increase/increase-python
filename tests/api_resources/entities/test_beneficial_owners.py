# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Entity
from increase._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestBeneficialOwners:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        beneficial_owner = client.entities.beneficial_owners.create(
            beneficial_owner={
                "individual": {
                    "name": "x",
                    "date_of_birth": parse_date("2019-12-27"),
                    "address": {
                        "line1": "x",
                        "city": "x",
                        "state": "x",
                        "zip": "x",
                    },
                    "identification": {
                        "method": "social_security_number",
                        "number": "xxxx",
                    },
                },
                "prongs": ["ownership", "control"],
            },
            entity_id="string",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        beneficial_owner = client.entities.beneficial_owners.create(
            beneficial_owner={
                "individual": {
                    "name": "x",
                    "date_of_birth": parse_date("2019-12-27"),
                    "address": {
                        "line1": "x",
                        "line2": "x",
                        "city": "x",
                        "state": "x",
                        "zip": "x",
                    },
                    "confirmed_no_us_tax_id": True,
                    "identification": {
                        "method": "social_security_number",
                        "number": "xxxx",
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
                "company_title": "x",
                "prongs": ["ownership", "control"],
            },
            entity_id="string",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    def test_method_archive(self, client: Increase) -> None:
        beneficial_owner = client.entities.beneficial_owners.archive(
            beneficial_owner_id="string",
            entity_id="string",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    def test_method_update_address(self, client: Increase) -> None:
        beneficial_owner = client.entities.beneficial_owners.update_address(
            address={
                "line1": "x",
                "city": "x",
                "state": "x",
                "zip": "x",
            },
            beneficial_owner_id="string",
            entity_id="string",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    def test_method_update_address_with_all_params(self, client: Increase) -> None:
        beneficial_owner = client.entities.beneficial_owners.update_address(
            address={
                "line1": "x",
                "line2": "x",
                "city": "x",
                "state": "x",
                "zip": "x",
            },
            beneficial_owner_id="string",
            entity_id="string",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])


class TestAsyncBeneficialOwners:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        beneficial_owner = await client.entities.beneficial_owners.create(
            beneficial_owner={
                "individual": {
                    "name": "x",
                    "date_of_birth": parse_date("2019-12-27"),
                    "address": {
                        "line1": "x",
                        "city": "x",
                        "state": "x",
                        "zip": "x",
                    },
                    "identification": {
                        "method": "social_security_number",
                        "number": "xxxx",
                    },
                },
                "prongs": ["ownership", "control"],
            },
            entity_id="string",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        beneficial_owner = await client.entities.beneficial_owners.create(
            beneficial_owner={
                "individual": {
                    "name": "x",
                    "date_of_birth": parse_date("2019-12-27"),
                    "address": {
                        "line1": "x",
                        "line2": "x",
                        "city": "x",
                        "state": "x",
                        "zip": "x",
                    },
                    "confirmed_no_us_tax_id": True,
                    "identification": {
                        "method": "social_security_number",
                        "number": "xxxx",
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
                "company_title": "x",
                "prongs": ["ownership", "control"],
            },
            entity_id="string",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    async def test_method_archive(self, client: AsyncIncrease) -> None:
        beneficial_owner = await client.entities.beneficial_owners.archive(
            beneficial_owner_id="string",
            entity_id="string",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    async def test_method_update_address(self, client: AsyncIncrease) -> None:
        beneficial_owner = await client.entities.beneficial_owners.update_address(
            address={
                "line1": "x",
                "city": "x",
                "state": "x",
                "zip": "x",
            },
            beneficial_owner_id="string",
            entity_id="string",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])

    @parametrize
    async def test_method_update_address_with_all_params(self, client: AsyncIncrease) -> None:
        beneficial_owner = await client.entities.beneficial_owners.update_address(
            address={
                "line1": "x",
                "line2": "x",
                "city": "x",
                "state": "x",
                "zip": "x",
            },
            beneficial_owner_id="string",
            entity_id="string",
        )
        assert_matches_type(Entity, beneficial_owner, path=["response"])
