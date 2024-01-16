# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Entity
from increase._utils import parse_date, parse_datetime
from increase._client import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestEntities:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        entity = client.entities.create(
            structure="corporation",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        entity = client.entities.create(
            structure="corporation",
            corporation={
                "name": "National Phonograph Company",
                "website": "https://example.com",
                "tax_identifier": "602214076",
                "incorporation_state": "NY",
                "address": {
                    "line1": "33 Liberty Street",
                    "line2": "x",
                    "city": "New York",
                    "state": "NY",
                    "zip": "10045",
                },
                "beneficial_owners": [
                    {
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
                    }
                ],
            },
            description="x",
            joint={
                "name": "x",
                "individuals": [
                    {
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
                    {
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
                    {
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
                ],
            },
            natural_person={
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
            relationship="affiliated",
            supplemental_documents=[{"file_id": "file_makxrc67oh9l6sg7w9yc"}],
            trust={
                "name": "x",
                "category": "revocable",
                "tax_identifier": "x",
                "formation_state": "x",
                "address": {
                    "line1": "x",
                    "line2": "x",
                    "city": "x",
                    "state": "x",
                    "zip": "x",
                },
                "formation_document_file_id": "string",
                "trustees": [
                    {
                        "structure": "individual",
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
                    },
                    {
                        "structure": "individual",
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
                    },
                    {
                        "structure": "individual",
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
                    },
                ],
                "grantor": {
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
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.entities.with_raw_response.create(
            structure="corporation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.entities.with_streaming_response.create(
            structure="corporation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        entity = client.entities.retrieve(
            "string",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.entities.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.entities.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        entity = client.entities.list()
        assert_matches_type(SyncPage[Entity], entity, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        entity = client.entities.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
            status={"in": ["active", "archived", "disabled"]},
        )
        assert_matches_type(SyncPage[Entity], entity, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.entities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(SyncPage[Entity], entity, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.entities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(SyncPage[Entity], entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Increase) -> None:
        entity = client.entities.archive(
            "string",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Increase) -> None:
        response = client.entities.with_raw_response.archive(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Increase) -> None:
        with client.entities.with_streaming_response.archive(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.with_raw_response.archive(
                "",
            )

    @parametrize
    def test_method_update_address(self, client: Increase) -> None:
        entity = client.entities.update_address(
            "string",
            address={
                "line1": "33 Liberty Street",
                "city": "New York",
                "state": "NY",
                "zip": "10045",
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_method_update_address_with_all_params(self, client: Increase) -> None:
        entity = client.entities.update_address(
            "string",
            address={
                "line1": "33 Liberty Street",
                "line2": "Unit 2",
                "city": "New York",
                "state": "NY",
                "zip": "10045",
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_raw_response_update_address(self, client: Increase) -> None:
        response = client.entities.with_raw_response.update_address(
            "string",
            address={
                "line1": "33 Liberty Street",
                "city": "New York",
                "state": "NY",
                "zip": "10045",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_streaming_response_update_address(self, client: Increase) -> None:
        with client.entities.with_streaming_response.update_address(
            "string",
            address={
                "line1": "33 Liberty Street",
                "city": "New York",
                "state": "NY",
                "zip": "10045",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_address(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.with_raw_response.update_address(
                "",
                address={
                    "line1": "33 Liberty Street",
                    "city": "New York",
                    "state": "NY",
                    "zip": "10045",
                },
            )


class TestAsyncEntities:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        entity = await client.entities.create(
            structure="corporation",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        entity = await client.entities.create(
            structure="corporation",
            corporation={
                "name": "National Phonograph Company",
                "website": "https://example.com",
                "tax_identifier": "602214076",
                "incorporation_state": "NY",
                "address": {
                    "line1": "33 Liberty Street",
                    "line2": "x",
                    "city": "New York",
                    "state": "NY",
                    "zip": "10045",
                },
                "beneficial_owners": [
                    {
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
                    }
                ],
            },
            description="x",
            joint={
                "name": "x",
                "individuals": [
                    {
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
                    {
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
                    {
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
                ],
            },
            natural_person={
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
            relationship="affiliated",
            supplemental_documents=[{"file_id": "file_makxrc67oh9l6sg7w9yc"}],
            trust={
                "name": "x",
                "category": "revocable",
                "tax_identifier": "x",
                "formation_state": "x",
                "address": {
                    "line1": "x",
                    "line2": "x",
                    "city": "x",
                    "state": "x",
                    "zip": "x",
                },
                "formation_document_file_id": "string",
                "trustees": [
                    {
                        "structure": "individual",
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
                    },
                    {
                        "structure": "individual",
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
                    },
                    {
                        "structure": "individual",
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
                    },
                ],
                "grantor": {
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
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIncrease) -> None:
        response = await client.entities.with_raw_response.create(
            structure="corporation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, client: AsyncIncrease) -> None:
        async with client.entities.with_streaming_response.create(
            structure="corporation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        entity = await client.entities.retrieve(
            "string",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIncrease) -> None:
        response = await client.entities.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncIncrease) -> None:
        async with client.entities.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await client.entities.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        entity = await client.entities.list()
        assert_matches_type(AsyncPage[Entity], entity, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        entity = await client.entities.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            limit=1,
            status={"in": ["active", "archived", "disabled"]},
        )
        assert_matches_type(AsyncPage[Entity], entity, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIncrease) -> None:
        response = await client.entities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(AsyncPage[Entity], entity, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncIncrease) -> None:
        async with client.entities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(AsyncPage[Entity], entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, client: AsyncIncrease) -> None:
        entity = await client.entities.archive(
            "string",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, client: AsyncIncrease) -> None:
        response = await client.entities.with_raw_response.archive(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, client: AsyncIncrease) -> None:
        async with client.entities.with_streaming_response.archive(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await client.entities.with_raw_response.archive(
                "",
            )

    @parametrize
    async def test_method_update_address(self, client: AsyncIncrease) -> None:
        entity = await client.entities.update_address(
            "string",
            address={
                "line1": "33 Liberty Street",
                "city": "New York",
                "state": "NY",
                "zip": "10045",
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_method_update_address_with_all_params(self, client: AsyncIncrease) -> None:
        entity = await client.entities.update_address(
            "string",
            address={
                "line1": "33 Liberty Street",
                "line2": "Unit 2",
                "city": "New York",
                "state": "NY",
                "zip": "10045",
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_update_address(self, client: AsyncIncrease) -> None:
        response = await client.entities.with_raw_response.update_address(
            "string",
            address={
                "line1": "33 Liberty Street",
                "city": "New York",
                "state": "NY",
                "zip": "10045",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_update_address(self, client: AsyncIncrease) -> None:
        async with client.entities.with_streaming_response.update_address(
            "string",
            address={
                "line1": "33 Liberty Street",
                "city": "New York",
                "state": "NY",
                "zip": "10045",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_address(self, client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await client.entities.with_raw_response.update_address(
                "",
                address={
                    "line1": "33 Liberty Street",
                    "city": "New York",
                    "state": "NY",
                    "zip": "10045",
                },
            )
