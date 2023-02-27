# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import Entity
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestEntities:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        entity = client.entities.create(
            structure="corporation",
            relationship="affiliated",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        entity = client.entities.create(
            structure="corporation",
            corporation={
                "name": "x",
                "website": "string",
                "tax_identifier": "x",
                "incorporation_state": "x",
                "address": {
                    "line1": "x",
                    "line2": "x",
                    "city": "x",
                    "state": "x",
                    "zip": "x",
                },
                "beneficial_owners": [
                    {
                        "individual": {
                            "name": "x",
                            "date_of_birth": "2019-12-27",
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
                                "number": "x",
                                "passport": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "state": "x",
                                },
                                "other": {
                                    "country": "x",
                                    "description": "x",
                                    "expiration_date": "2019-12-27",
                                    "file_id": "string",
                                },
                            },
                        },
                        "company_title": "x",
                        "prong": "ownership",
                    },
                    {
                        "individual": {
                            "name": "x",
                            "date_of_birth": "2019-12-27",
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
                                "number": "x",
                                "passport": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "state": "x",
                                },
                                "other": {
                                    "country": "x",
                                    "description": "x",
                                    "expiration_date": "2019-12-27",
                                    "file_id": "string",
                                },
                            },
                        },
                        "company_title": "x",
                        "prong": "ownership",
                    },
                    {
                        "individual": {
                            "name": "x",
                            "date_of_birth": "2019-12-27",
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
                                "number": "x",
                                "passport": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "state": "x",
                                },
                                "other": {
                                    "country": "x",
                                    "description": "x",
                                    "expiration_date": "2019-12-27",
                                    "file_id": "string",
                                },
                            },
                        },
                        "company_title": "x",
                        "prong": "ownership",
                    },
                ],
            },
            natural_person={
                "name": "x",
                "date_of_birth": "2019-12-27",
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
                    "number": "x",
                    "passport": {
                        "file_id": "string",
                        "expiration_date": "2019-12-27",
                        "country": "x",
                    },
                    "drivers_license": {
                        "file_id": "string",
                        "expiration_date": "2019-12-27",
                        "state": "x",
                    },
                    "other": {
                        "country": "x",
                        "description": "x",
                        "expiration_date": "2019-12-27",
                        "file_id": "string",
                    },
                },
            },
            joint={
                "name": "x",
                "individuals": [
                    {
                        "name": "x",
                        "date_of_birth": "2019-12-27",
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
                            "number": "x",
                            "passport": {
                                "file_id": "string",
                                "expiration_date": "2019-12-27",
                                "country": "x",
                            },
                            "drivers_license": {
                                "file_id": "string",
                                "expiration_date": "2019-12-27",
                                "state": "x",
                            },
                            "other": {
                                "country": "x",
                                "description": "x",
                                "expiration_date": "2019-12-27",
                                "file_id": "string",
                            },
                        },
                    },
                    {
                        "name": "x",
                        "date_of_birth": "2019-12-27",
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
                            "number": "x",
                            "passport": {
                                "file_id": "string",
                                "expiration_date": "2019-12-27",
                                "country": "x",
                            },
                            "drivers_license": {
                                "file_id": "string",
                                "expiration_date": "2019-12-27",
                                "state": "x",
                            },
                            "other": {
                                "country": "x",
                                "description": "x",
                                "expiration_date": "2019-12-27",
                                "file_id": "string",
                            },
                        },
                    },
                    {
                        "name": "x",
                        "date_of_birth": "2019-12-27",
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
                            "number": "x",
                            "passport": {
                                "file_id": "string",
                                "expiration_date": "2019-12-27",
                                "country": "x",
                            },
                            "drivers_license": {
                                "file_id": "string",
                                "expiration_date": "2019-12-27",
                                "state": "x",
                            },
                            "other": {
                                "country": "x",
                                "description": "x",
                                "expiration_date": "2019-12-27",
                                "file_id": "string",
                            },
                        },
                    },
                ],
            },
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
                            "date_of_birth": "2019-12-27",
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
                                "number": "x",
                                "passport": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "state": "x",
                                },
                                "other": {
                                    "country": "x",
                                    "description": "x",
                                    "expiration_date": "2019-12-27",
                                    "file_id": "string",
                                },
                            },
                        },
                    },
                    {
                        "structure": "individual",
                        "individual": {
                            "name": "x",
                            "date_of_birth": "2019-12-27",
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
                                "number": "x",
                                "passport": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "state": "x",
                                },
                                "other": {
                                    "country": "x",
                                    "description": "x",
                                    "expiration_date": "2019-12-27",
                                    "file_id": "string",
                                },
                            },
                        },
                    },
                    {
                        "structure": "individual",
                        "individual": {
                            "name": "x",
                            "date_of_birth": "2019-12-27",
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
                                "number": "x",
                                "passport": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "state": "x",
                                },
                                "other": {
                                    "country": "x",
                                    "description": "x",
                                    "expiration_date": "2019-12-27",
                                    "file_id": "string",
                                },
                            },
                        },
                    },
                ],
                "grantor": {
                    "name": "x",
                    "date_of_birth": "2019-12-27",
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
                        "number": "x",
                        "passport": {
                            "file_id": "string",
                            "expiration_date": "2019-12-27",
                            "country": "x",
                        },
                        "drivers_license": {
                            "file_id": "string",
                            "expiration_date": "2019-12-27",
                            "state": "x",
                        },
                        "other": {
                            "country": "x",
                            "description": "x",
                            "expiration_date": "2019-12-27",
                            "file_id": "string",
                        },
                    },
                },
            },
            description="x",
            relationship="affiliated",
            supplemental_documents=[{"file_id": "string"}, {"file_id": "string"}, {"file_id": "string"}],
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        entity = client.entities.retrieve(
            "string",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        entity = client.entities.list()
        assert_matches_type(SyncPage[Entity], entity, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        entity = client.entities.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(SyncPage[Entity], entity, path=["response"])


class TestAsyncEntities:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        entity = await client.entities.create(
            structure="corporation",
            relationship="affiliated",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        entity = await client.entities.create(
            structure="corporation",
            corporation={
                "name": "x",
                "website": "string",
                "tax_identifier": "x",
                "incorporation_state": "x",
                "address": {
                    "line1": "x",
                    "line2": "x",
                    "city": "x",
                    "state": "x",
                    "zip": "x",
                },
                "beneficial_owners": [
                    {
                        "individual": {
                            "name": "x",
                            "date_of_birth": "2019-12-27",
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
                                "number": "x",
                                "passport": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "state": "x",
                                },
                                "other": {
                                    "country": "x",
                                    "description": "x",
                                    "expiration_date": "2019-12-27",
                                    "file_id": "string",
                                },
                            },
                        },
                        "company_title": "x",
                        "prong": "ownership",
                    },
                    {
                        "individual": {
                            "name": "x",
                            "date_of_birth": "2019-12-27",
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
                                "number": "x",
                                "passport": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "state": "x",
                                },
                                "other": {
                                    "country": "x",
                                    "description": "x",
                                    "expiration_date": "2019-12-27",
                                    "file_id": "string",
                                },
                            },
                        },
                        "company_title": "x",
                        "prong": "ownership",
                    },
                    {
                        "individual": {
                            "name": "x",
                            "date_of_birth": "2019-12-27",
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
                                "number": "x",
                                "passport": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "state": "x",
                                },
                                "other": {
                                    "country": "x",
                                    "description": "x",
                                    "expiration_date": "2019-12-27",
                                    "file_id": "string",
                                },
                            },
                        },
                        "company_title": "x",
                        "prong": "ownership",
                    },
                ],
            },
            natural_person={
                "name": "x",
                "date_of_birth": "2019-12-27",
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
                    "number": "x",
                    "passport": {
                        "file_id": "string",
                        "expiration_date": "2019-12-27",
                        "country": "x",
                    },
                    "drivers_license": {
                        "file_id": "string",
                        "expiration_date": "2019-12-27",
                        "state": "x",
                    },
                    "other": {
                        "country": "x",
                        "description": "x",
                        "expiration_date": "2019-12-27",
                        "file_id": "string",
                    },
                },
            },
            joint={
                "name": "x",
                "individuals": [
                    {
                        "name": "x",
                        "date_of_birth": "2019-12-27",
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
                            "number": "x",
                            "passport": {
                                "file_id": "string",
                                "expiration_date": "2019-12-27",
                                "country": "x",
                            },
                            "drivers_license": {
                                "file_id": "string",
                                "expiration_date": "2019-12-27",
                                "state": "x",
                            },
                            "other": {
                                "country": "x",
                                "description": "x",
                                "expiration_date": "2019-12-27",
                                "file_id": "string",
                            },
                        },
                    },
                    {
                        "name": "x",
                        "date_of_birth": "2019-12-27",
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
                            "number": "x",
                            "passport": {
                                "file_id": "string",
                                "expiration_date": "2019-12-27",
                                "country": "x",
                            },
                            "drivers_license": {
                                "file_id": "string",
                                "expiration_date": "2019-12-27",
                                "state": "x",
                            },
                            "other": {
                                "country": "x",
                                "description": "x",
                                "expiration_date": "2019-12-27",
                                "file_id": "string",
                            },
                        },
                    },
                    {
                        "name": "x",
                        "date_of_birth": "2019-12-27",
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
                            "number": "x",
                            "passport": {
                                "file_id": "string",
                                "expiration_date": "2019-12-27",
                                "country": "x",
                            },
                            "drivers_license": {
                                "file_id": "string",
                                "expiration_date": "2019-12-27",
                                "state": "x",
                            },
                            "other": {
                                "country": "x",
                                "description": "x",
                                "expiration_date": "2019-12-27",
                                "file_id": "string",
                            },
                        },
                    },
                ],
            },
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
                            "date_of_birth": "2019-12-27",
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
                                "number": "x",
                                "passport": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "state": "x",
                                },
                                "other": {
                                    "country": "x",
                                    "description": "x",
                                    "expiration_date": "2019-12-27",
                                    "file_id": "string",
                                },
                            },
                        },
                    },
                    {
                        "structure": "individual",
                        "individual": {
                            "name": "x",
                            "date_of_birth": "2019-12-27",
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
                                "number": "x",
                                "passport": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "state": "x",
                                },
                                "other": {
                                    "country": "x",
                                    "description": "x",
                                    "expiration_date": "2019-12-27",
                                    "file_id": "string",
                                },
                            },
                        },
                    },
                    {
                        "structure": "individual",
                        "individual": {
                            "name": "x",
                            "date_of_birth": "2019-12-27",
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
                                "number": "x",
                                "passport": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27",
                                    "state": "x",
                                },
                                "other": {
                                    "country": "x",
                                    "description": "x",
                                    "expiration_date": "2019-12-27",
                                    "file_id": "string",
                                },
                            },
                        },
                    },
                ],
                "grantor": {
                    "name": "x",
                    "date_of_birth": "2019-12-27",
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
                        "number": "x",
                        "passport": {
                            "file_id": "string",
                            "expiration_date": "2019-12-27",
                            "country": "x",
                        },
                        "drivers_license": {
                            "file_id": "string",
                            "expiration_date": "2019-12-27",
                            "state": "x",
                        },
                        "other": {
                            "country": "x",
                            "description": "x",
                            "expiration_date": "2019-12-27",
                            "file_id": "string",
                        },
                    },
                },
            },
            description="x",
            relationship="affiliated",
            supplemental_documents=[{"file_id": "string"}, {"file_id": "string"}, {"file_id": "string"}],
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        entity = await client.entities.retrieve(
            "string",
        )
        assert_matches_type(Entity, entity, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        entity = await client.entities.list()
        assert_matches_type(AsyncPage[Entity], entity, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        entity = await client.entities.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[Entity], entity, path=["response"])
