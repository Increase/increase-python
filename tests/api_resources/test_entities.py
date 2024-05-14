# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    Entity,
)
from increase._utils import parse_date, parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
                "address": {
                    "city": "New York",
                    "line1": "33 Liberty Street",
                    "line2": "x",
                    "state": "NY",
                    "zip": "10045",
                },
                "beneficial_owners": [
                    {
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
                    }
                ],
                "incorporation_state": "NY",
                "industry_code": "x",
                "name": "National Phonograph Company",
                "tax_identifier": "602214076",
                "website": "https://example.com",
            },
            description="x",
            government_authority={
                "address": {
                    "city": "x",
                    "line1": "x",
                    "line2": "x",
                    "state": "x",
                    "zip": "x",
                },
                "authorized_persons": [{"name": "x"}, {"name": "x"}, {"name": "x"}],
                "category": "municipality",
                "name": "x",
                "tax_identifier": "x",
                "website": "string",
            },
            joint={
                "individuals": [
                    {
                        "address": {
                            "city": "x",
                            "line1": "x",
                            "line2": "x",
                            "state": "x",
                            "zip": "x",
                        },
                        "confirmed_no_us_tax_id": True,
                        "date_of_birth": parse_date("2019-12-27"),
                        "identification": {
                            "drivers_license": {
                                "back_file_id": "string",
                                "expiration_date": parse_date("2019-12-27"),
                                "file_id": "string",
                                "state": "x",
                            },
                            "method": "social_security_number",
                            "number": "xxxx",
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
                        "name": "x",
                    },
                    {
                        "address": {
                            "city": "x",
                            "line1": "x",
                            "line2": "x",
                            "state": "x",
                            "zip": "x",
                        },
                        "confirmed_no_us_tax_id": True,
                        "date_of_birth": parse_date("2019-12-27"),
                        "identification": {
                            "drivers_license": {
                                "back_file_id": "string",
                                "expiration_date": parse_date("2019-12-27"),
                                "file_id": "string",
                                "state": "x",
                            },
                            "method": "social_security_number",
                            "number": "xxxx",
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
                        "name": "x",
                    },
                    {
                        "address": {
                            "city": "x",
                            "line1": "x",
                            "line2": "x",
                            "state": "x",
                            "zip": "x",
                        },
                        "confirmed_no_us_tax_id": True,
                        "date_of_birth": parse_date("2019-12-27"),
                        "identification": {
                            "drivers_license": {
                                "back_file_id": "string",
                                "expiration_date": parse_date("2019-12-27"),
                                "file_id": "string",
                                "state": "x",
                            },
                            "method": "social_security_number",
                            "number": "xxxx",
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
                        "name": "x",
                    },
                ],
                "name": "x",
            },
            natural_person={
                "address": {
                    "city": "x",
                    "line1": "x",
                    "line2": "x",
                    "state": "x",
                    "zip": "x",
                },
                "confirmed_no_us_tax_id": True,
                "date_of_birth": parse_date("2019-12-27"),
                "identification": {
                    "drivers_license": {
                        "back_file_id": "string",
                        "expiration_date": parse_date("2019-12-27"),
                        "file_id": "string",
                        "state": "x",
                    },
                    "method": "social_security_number",
                    "number": "xxxx",
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
                "name": "x",
            },
            supplemental_documents=[{"file_id": "file_makxrc67oh9l6sg7w9yc"}],
            trust={
                "address": {
                    "city": "x",
                    "line1": "x",
                    "line2": "x",
                    "state": "x",
                    "zip": "x",
                },
                "category": "revocable",
                "formation_document_file_id": "string",
                "formation_state": "x",
                "grantor": {
                    "address": {
                        "city": "x",
                        "line1": "x",
                        "line2": "x",
                        "state": "x",
                        "zip": "x",
                    },
                    "confirmed_no_us_tax_id": True,
                    "date_of_birth": parse_date("2019-12-27"),
                    "identification": {
                        "drivers_license": {
                            "back_file_id": "string",
                            "expiration_date": parse_date("2019-12-27"),
                            "file_id": "string",
                            "state": "x",
                        },
                        "method": "social_security_number",
                        "number": "xxxx",
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
                    "name": "x",
                },
                "name": "x",
                "tax_identifier": "x",
                "trustees": [
                    {
                        "individual": {
                            "address": {
                                "city": "x",
                                "line1": "x",
                                "line2": "x",
                                "state": "x",
                                "zip": "x",
                            },
                            "confirmed_no_us_tax_id": True,
                            "date_of_birth": parse_date("2019-12-27"),
                            "identification": {
                                "drivers_license": {
                                    "back_file_id": "string",
                                    "expiration_date": parse_date("2019-12-27"),
                                    "file_id": "string",
                                    "state": "x",
                                },
                                "method": "social_security_number",
                                "number": "xxxx",
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
                            "name": "x",
                        },
                        "structure": "individual",
                    },
                    {
                        "individual": {
                            "address": {
                                "city": "x",
                                "line1": "x",
                                "line2": "x",
                                "state": "x",
                                "zip": "x",
                            },
                            "confirmed_no_us_tax_id": True,
                            "date_of_birth": parse_date("2019-12-27"),
                            "identification": {
                                "drivers_license": {
                                    "back_file_id": "string",
                                    "expiration_date": parse_date("2019-12-27"),
                                    "file_id": "string",
                                    "state": "x",
                                },
                                "method": "social_security_number",
                                "number": "xxxx",
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
                            "name": "x",
                        },
                        "structure": "individual",
                    },
                    {
                        "individual": {
                            "address": {
                                "city": "x",
                                "line1": "x",
                                "line2": "x",
                                "state": "x",
                                "zip": "x",
                            },
                            "confirmed_no_us_tax_id": True,
                            "date_of_birth": parse_date("2019-12-27"),
                            "identification": {
                                "drivers_license": {
                                    "back_file_id": "string",
                                    "expiration_date": parse_date("2019-12-27"),
                                    "file_id": "string",
                                    "state": "x",
                                },
                                "method": "social_security_number",
                                "number": "xxxx",
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
                            "name": "x",
                        },
                        "structure": "individual",
                    },
                ],
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
            idempotency_key="x",
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
    def test_method_confirm(self, client: Increase) -> None:
        entity = client.entities.confirm(
            "string",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_method_confirm_with_all_params(self, client: Increase) -> None:
        entity = client.entities.confirm(
            "string",
            confirmed_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_raw_response_confirm(self, client: Increase) -> None:
        response = client.entities.with_raw_response.confirm(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_streaming_response_confirm(self, client: Increase) -> None:
        with client.entities.with_streaming_response.confirm(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_confirm(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.with_raw_response.confirm(
                "",
            )

    @parametrize
    def test_method_update_address(self, client: Increase) -> None:
        entity = client.entities.update_address(
            "string",
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
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
                "city": "New York",
                "line1": "33 Liberty Street",
                "line2": "Unit 2",
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
                "city": "New York",
                "line1": "33 Liberty Street",
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
                "city": "New York",
                "line1": "33 Liberty Street",
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
                    "city": "New York",
                    "line1": "33 Liberty Street",
                    "state": "NY",
                    "zip": "10045",
                },
            )


class TestAsyncEntities:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.create(
            structure="corporation",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.create(
            structure="corporation",
            corporation={
                "address": {
                    "city": "New York",
                    "line1": "33 Liberty Street",
                    "line2": "x",
                    "state": "NY",
                    "zip": "10045",
                },
                "beneficial_owners": [
                    {
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
                    }
                ],
                "incorporation_state": "NY",
                "industry_code": "x",
                "name": "National Phonograph Company",
                "tax_identifier": "602214076",
                "website": "https://example.com",
            },
            description="x",
            government_authority={
                "address": {
                    "city": "x",
                    "line1": "x",
                    "line2": "x",
                    "state": "x",
                    "zip": "x",
                },
                "authorized_persons": [{"name": "x"}, {"name": "x"}, {"name": "x"}],
                "category": "municipality",
                "name": "x",
                "tax_identifier": "x",
                "website": "string",
            },
            joint={
                "individuals": [
                    {
                        "address": {
                            "city": "x",
                            "line1": "x",
                            "line2": "x",
                            "state": "x",
                            "zip": "x",
                        },
                        "confirmed_no_us_tax_id": True,
                        "date_of_birth": parse_date("2019-12-27"),
                        "identification": {
                            "drivers_license": {
                                "back_file_id": "string",
                                "expiration_date": parse_date("2019-12-27"),
                                "file_id": "string",
                                "state": "x",
                            },
                            "method": "social_security_number",
                            "number": "xxxx",
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
                        "name": "x",
                    },
                    {
                        "address": {
                            "city": "x",
                            "line1": "x",
                            "line2": "x",
                            "state": "x",
                            "zip": "x",
                        },
                        "confirmed_no_us_tax_id": True,
                        "date_of_birth": parse_date("2019-12-27"),
                        "identification": {
                            "drivers_license": {
                                "back_file_id": "string",
                                "expiration_date": parse_date("2019-12-27"),
                                "file_id": "string",
                                "state": "x",
                            },
                            "method": "social_security_number",
                            "number": "xxxx",
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
                        "name": "x",
                    },
                    {
                        "address": {
                            "city": "x",
                            "line1": "x",
                            "line2": "x",
                            "state": "x",
                            "zip": "x",
                        },
                        "confirmed_no_us_tax_id": True,
                        "date_of_birth": parse_date("2019-12-27"),
                        "identification": {
                            "drivers_license": {
                                "back_file_id": "string",
                                "expiration_date": parse_date("2019-12-27"),
                                "file_id": "string",
                                "state": "x",
                            },
                            "method": "social_security_number",
                            "number": "xxxx",
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
                        "name": "x",
                    },
                ],
                "name": "x",
            },
            natural_person={
                "address": {
                    "city": "x",
                    "line1": "x",
                    "line2": "x",
                    "state": "x",
                    "zip": "x",
                },
                "confirmed_no_us_tax_id": True,
                "date_of_birth": parse_date("2019-12-27"),
                "identification": {
                    "drivers_license": {
                        "back_file_id": "string",
                        "expiration_date": parse_date("2019-12-27"),
                        "file_id": "string",
                        "state": "x",
                    },
                    "method": "social_security_number",
                    "number": "xxxx",
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
                "name": "x",
            },
            supplemental_documents=[{"file_id": "file_makxrc67oh9l6sg7w9yc"}],
            trust={
                "address": {
                    "city": "x",
                    "line1": "x",
                    "line2": "x",
                    "state": "x",
                    "zip": "x",
                },
                "category": "revocable",
                "formation_document_file_id": "string",
                "formation_state": "x",
                "grantor": {
                    "address": {
                        "city": "x",
                        "line1": "x",
                        "line2": "x",
                        "state": "x",
                        "zip": "x",
                    },
                    "confirmed_no_us_tax_id": True,
                    "date_of_birth": parse_date("2019-12-27"),
                    "identification": {
                        "drivers_license": {
                            "back_file_id": "string",
                            "expiration_date": parse_date("2019-12-27"),
                            "file_id": "string",
                            "state": "x",
                        },
                        "method": "social_security_number",
                        "number": "xxxx",
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
                    "name": "x",
                },
                "name": "x",
                "tax_identifier": "x",
                "trustees": [
                    {
                        "individual": {
                            "address": {
                                "city": "x",
                                "line1": "x",
                                "line2": "x",
                                "state": "x",
                                "zip": "x",
                            },
                            "confirmed_no_us_tax_id": True,
                            "date_of_birth": parse_date("2019-12-27"),
                            "identification": {
                                "drivers_license": {
                                    "back_file_id": "string",
                                    "expiration_date": parse_date("2019-12-27"),
                                    "file_id": "string",
                                    "state": "x",
                                },
                                "method": "social_security_number",
                                "number": "xxxx",
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
                            "name": "x",
                        },
                        "structure": "individual",
                    },
                    {
                        "individual": {
                            "address": {
                                "city": "x",
                                "line1": "x",
                                "line2": "x",
                                "state": "x",
                                "zip": "x",
                            },
                            "confirmed_no_us_tax_id": True,
                            "date_of_birth": parse_date("2019-12-27"),
                            "identification": {
                                "drivers_license": {
                                    "back_file_id": "string",
                                    "expiration_date": parse_date("2019-12-27"),
                                    "file_id": "string",
                                    "state": "x",
                                },
                                "method": "social_security_number",
                                "number": "xxxx",
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
                            "name": "x",
                        },
                        "structure": "individual",
                    },
                    {
                        "individual": {
                            "address": {
                                "city": "x",
                                "line1": "x",
                                "line2": "x",
                                "state": "x",
                                "zip": "x",
                            },
                            "confirmed_no_us_tax_id": True,
                            "date_of_birth": parse_date("2019-12-27"),
                            "identification": {
                                "drivers_license": {
                                    "back_file_id": "string",
                                    "expiration_date": parse_date("2019-12-27"),
                                    "file_id": "string",
                                    "state": "x",
                                },
                                "method": "social_security_number",
                                "number": "xxxx",
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
                            "name": "x",
                        },
                        "structure": "individual",
                    },
                ],
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.with_raw_response.create(
            structure="corporation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.with_streaming_response.create(
            structure="corporation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.retrieve(
            "string",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entities.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.list()
        assert_matches_type(AsyncPage[Entity], entity, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="string",
            idempotency_key="x",
            limit=1,
            status={"in": ["active", "archived", "disabled"]},
        )
        assert_matches_type(AsyncPage[Entity], entity, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(AsyncPage[Entity], entity, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(AsyncPage[Entity], entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.archive(
            "string",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.with_raw_response.archive(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.with_streaming_response.archive(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entities.with_raw_response.archive(
                "",
            )

    @parametrize
    async def test_method_confirm(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.confirm(
            "string",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_method_confirm_with_all_params(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.confirm(
            "string",
            confirmed_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_confirm(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.with_raw_response.confirm(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_confirm(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.with_streaming_response.confirm(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(Entity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_confirm(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entities.with_raw_response.confirm(
                "",
            )

    @parametrize
    async def test_method_update_address(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.update_address(
            "string",
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "state": "NY",
                "zip": "10045",
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_method_update_address_with_all_params(self, async_client: AsyncIncrease) -> None:
        entity = await async_client.entities.update_address(
            "string",
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "line2": "Unit 2",
                "state": "NY",
                "zip": "10045",
            },
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_raw_response_update_address(self, async_client: AsyncIncrease) -> None:
        response = await async_client.entities.with_raw_response.update_address(
            "string",
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
                "state": "NY",
                "zip": "10045",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_update_address(self, async_client: AsyncIncrease) -> None:
        async with async_client.entities.with_streaming_response.update_address(
            "string",
            address={
                "city": "New York",
                "line1": "33 Liberty Street",
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
    async def test_path_params_update_address(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entities.with_raw_response.update_address(
                "",
                address={
                    "city": "New York",
                    "line1": "33 Liberty Street",
                    "state": "NY",
                    "zip": "10045",
                },
            )
