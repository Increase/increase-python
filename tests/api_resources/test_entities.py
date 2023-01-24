# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
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
        resource = client.entities.create(
            structure="corporation",
            relationship="affiliated",
        )
        assert isinstance(resource, Entity)

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        resource = client.entities.create(
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
                            "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "state": "x",
                                },
                            },
                        },
                        "company_title": "x",
                        "prong": "ownership",
                    },
                    {
                        "individual": {
                            "name": "x",
                            "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "state": "x",
                                },
                            },
                        },
                        "company_title": "x",
                        "prong": "ownership",
                    },
                    {
                        "individual": {
                            "name": "x",
                            "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "state": "x",
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
                "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                        "expiration_date": "2019-12-27T18:11:19.117Z",
                        "country": "x",
                    },
                    "drivers_license": {
                        "file_id": "string",
                        "expiration_date": "2019-12-27T18:11:19.117Z",
                        "state": "x",
                    },
                },
            },
            joint={
                "name": "x",
                "individuals": [
                    {
                        "name": "x",
                        "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                                "expiration_date": "2019-12-27T18:11:19.117Z",
                                "country": "x",
                            },
                            "drivers_license": {
                                "file_id": "string",
                                "expiration_date": "2019-12-27T18:11:19.117Z",
                                "state": "x",
                            },
                        },
                    },
                    {
                        "name": "x",
                        "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                                "expiration_date": "2019-12-27T18:11:19.117Z",
                                "country": "x",
                            },
                            "drivers_license": {
                                "file_id": "string",
                                "expiration_date": "2019-12-27T18:11:19.117Z",
                                "state": "x",
                            },
                        },
                    },
                    {
                        "name": "x",
                        "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                                "expiration_date": "2019-12-27T18:11:19.117Z",
                                "country": "x",
                            },
                            "drivers_license": {
                                "file_id": "string",
                                "expiration_date": "2019-12-27T18:11:19.117Z",
                                "state": "x",
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
                            "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "state": "x",
                                },
                            },
                        },
                    },
                    {
                        "structure": "individual",
                        "individual": {
                            "name": "x",
                            "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "state": "x",
                                },
                            },
                        },
                    },
                    {
                        "structure": "individual",
                        "individual": {
                            "name": "x",
                            "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "state": "x",
                                },
                            },
                        },
                    },
                ],
                "grantor": {
                    "name": "x",
                    "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                            "expiration_date": "2019-12-27T18:11:19.117Z",
                            "country": "x",
                        },
                        "drivers_license": {
                            "file_id": "string",
                            "expiration_date": "2019-12-27T18:11:19.117Z",
                            "state": "x",
                        },
                    },
                },
            },
            description="x",
            relationship="affiliated",
            supplemental_documents=[{"file_id": "string"}, {"file_id": "string"}, {"file_id": "string"}],
        )
        assert isinstance(resource, Entity)

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        resource = client.entities.retrieve(
            "string",
        )
        assert isinstance(resource, Entity)

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        resource = client.entities.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        resource = client.entities.list(
            cursor="string",
            limit=0,
        )
        assert isinstance(resource, SyncPage)


class TestAsyncEntities:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        resource = await client.entities.create(
            structure="corporation",
            relationship="affiliated",
        )
        assert isinstance(resource, Entity)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.entities.create(
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
                            "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "state": "x",
                                },
                            },
                        },
                        "company_title": "x",
                        "prong": "ownership",
                    },
                    {
                        "individual": {
                            "name": "x",
                            "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "state": "x",
                                },
                            },
                        },
                        "company_title": "x",
                        "prong": "ownership",
                    },
                    {
                        "individual": {
                            "name": "x",
                            "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "state": "x",
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
                "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                        "expiration_date": "2019-12-27T18:11:19.117Z",
                        "country": "x",
                    },
                    "drivers_license": {
                        "file_id": "string",
                        "expiration_date": "2019-12-27T18:11:19.117Z",
                        "state": "x",
                    },
                },
            },
            joint={
                "name": "x",
                "individuals": [
                    {
                        "name": "x",
                        "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                                "expiration_date": "2019-12-27T18:11:19.117Z",
                                "country": "x",
                            },
                            "drivers_license": {
                                "file_id": "string",
                                "expiration_date": "2019-12-27T18:11:19.117Z",
                                "state": "x",
                            },
                        },
                    },
                    {
                        "name": "x",
                        "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                                "expiration_date": "2019-12-27T18:11:19.117Z",
                                "country": "x",
                            },
                            "drivers_license": {
                                "file_id": "string",
                                "expiration_date": "2019-12-27T18:11:19.117Z",
                                "state": "x",
                            },
                        },
                    },
                    {
                        "name": "x",
                        "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                                "expiration_date": "2019-12-27T18:11:19.117Z",
                                "country": "x",
                            },
                            "drivers_license": {
                                "file_id": "string",
                                "expiration_date": "2019-12-27T18:11:19.117Z",
                                "state": "x",
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
                            "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "state": "x",
                                },
                            },
                        },
                    },
                    {
                        "structure": "individual",
                        "individual": {
                            "name": "x",
                            "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "state": "x",
                                },
                            },
                        },
                    },
                    {
                        "structure": "individual",
                        "individual": {
                            "name": "x",
                            "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "country": "x",
                                },
                                "drivers_license": {
                                    "file_id": "string",
                                    "expiration_date": "2019-12-27T18:11:19.117Z",
                                    "state": "x",
                                },
                            },
                        },
                    },
                ],
                "grantor": {
                    "name": "x",
                    "date_of_birth": "2019-12-27T18:11:19.117Z",
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
                            "expiration_date": "2019-12-27T18:11:19.117Z",
                            "country": "x",
                        },
                        "drivers_license": {
                            "file_id": "string",
                            "expiration_date": "2019-12-27T18:11:19.117Z",
                            "state": "x",
                        },
                    },
                },
            },
            description="x",
            relationship="affiliated",
            supplemental_documents=[{"file_id": "string"}, {"file_id": "string"}, {"file_id": "string"}],
        )
        assert isinstance(resource, Entity)

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        resource = await client.entities.retrieve(
            "string",
        )
        assert isinstance(resource, Entity)

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        resource = await client.entities.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.entities.list(
            cursor="string",
            limit=0,
        )
        assert isinstance(resource, AsyncPage)
