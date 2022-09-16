# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.entity import Entity

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestEntities:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
    def test_method_list_with_optional_params(self, client: Increase) -> None:
        resource = client.entities.list(
            {
                "cursor": "string",
                "limit": 0,
            },
        )
        assert isinstance(resource, SyncPage)

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_method_create_corporation(self, client: Increase) -> None:
        resource = client.entities.create_corporation(
            {
                "address_line1": "33 Liberty Street",
                "address_city": "New York",
                "address_state": "NY",
                "address_zip": "10045",
                "name": "National Phonograph Company",
                "state": "NJ",
            },
        )
        assert isinstance(resource, Entity)

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_method_create_corporation_with_optional_params(self, client: Increase) -> None:
        resource = client.entities.create_corporation(
            {
                "address_line1": "33 Liberty Street",
                "address_line2": "x",
                "address_city": "New York",
                "address_state": "NY",
                "address_zip": "10045",
                "beneficial_owners": [
                    {
                        "address_line1": "x",
                        "address_line2": "x",
                        "address_city": "x",
                        "address_state": "x",
                        "address_zip": "x",
                        "date_of_birth": "2019-12-27T18:11:19.117Z",
                        "name": "x",
                        "social_security_number_last4": "xxxx",
                        "prong": "ownership",
                        "company_title": "x",
                    },
                    {
                        "address_line1": "x",
                        "address_line2": "x",
                        "address_city": "x",
                        "address_state": "x",
                        "address_zip": "x",
                        "date_of_birth": "2019-12-27T18:11:19.117Z",
                        "name": "x",
                        "social_security_number_last4": "xxxx",
                        "prong": "ownership",
                        "company_title": "x",
                    },
                    {
                        "address_line1": "x",
                        "address_line2": "x",
                        "address_city": "x",
                        "address_state": "x",
                        "address_zip": "x",
                        "date_of_birth": "2019-12-27T18:11:19.117Z",
                        "name": "x",
                        "social_security_number_last4": "xxxx",
                        "prong": "ownership",
                        "company_title": "x",
                    },
                ],
                "name": "National Phonograph Company",
                "state": "NJ",
                "tax_id": "602214076",
                "ss4_file_id": "string",
                "website": "https://example.com",
            },
        )
        assert isinstance(resource, Entity)

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_method_create_person(self, client: Increase) -> None:
        resource = client.entities.create_person(
            {
                "address_line1": "33 Liberty Street",
                "address_city": "New York",
                "address_state": "NY",
                "address_zip": "10045",
                "date_of_birth": "1970-01-31",
                "name": "Ian Crease",
                "social_security_number_last4": "1120",
            },
        )
        assert isinstance(resource, Entity)

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    def test_method_create_person_with_optional_params(self, client: Increase) -> None:
        resource = client.entities.create_person(
            {
                "address_line1": "33 Liberty Street",
                "address_line2": "x",
                "address_city": "New York",
                "address_state": "NY",
                "address_zip": "10045",
                "date_of_birth": "1970-01-31",
                "name": "Ian Crease",
                "social_security_number_last4": "1120",
            },
        )
        assert isinstance(resource, Entity)


class TestAsyncEntities:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
    async def test_method_list_with_optional_params(self, client: AsyncIncrease) -> None:
        resource = await client.entities.list(
            {
                "cursor": "string",
                "limit": 0,
            },
        )
        assert isinstance(resource, AsyncPage)

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_method_create_corporation(self, client: AsyncIncrease) -> None:
        resource = await client.entities.create_corporation(
            {
                "address_line1": "33 Liberty Street",
                "address_city": "New York",
                "address_state": "NY",
                "address_zip": "10045",
                "name": "National Phonograph Company",
                "state": "NJ",
            },
        )
        assert isinstance(resource, Entity)

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_method_create_corporation_with_optional_params(self, client: AsyncIncrease) -> None:
        resource = await client.entities.create_corporation(
            {
                "address_line1": "33 Liberty Street",
                "address_line2": "x",
                "address_city": "New York",
                "address_state": "NY",
                "address_zip": "10045",
                "beneficial_owners": [
                    {
                        "address_line1": "x",
                        "address_line2": "x",
                        "address_city": "x",
                        "address_state": "x",
                        "address_zip": "x",
                        "date_of_birth": "2019-12-27T18:11:19.117Z",
                        "name": "x",
                        "social_security_number_last4": "xxxx",
                        "prong": "ownership",
                        "company_title": "x",
                    },
                    {
                        "address_line1": "x",
                        "address_line2": "x",
                        "address_city": "x",
                        "address_state": "x",
                        "address_zip": "x",
                        "date_of_birth": "2019-12-27T18:11:19.117Z",
                        "name": "x",
                        "social_security_number_last4": "xxxx",
                        "prong": "ownership",
                        "company_title": "x",
                    },
                    {
                        "address_line1": "x",
                        "address_line2": "x",
                        "address_city": "x",
                        "address_state": "x",
                        "address_zip": "x",
                        "date_of_birth": "2019-12-27T18:11:19.117Z",
                        "name": "x",
                        "social_security_number_last4": "xxxx",
                        "prong": "ownership",
                        "company_title": "x",
                    },
                ],
                "name": "National Phonograph Company",
                "state": "NJ",
                "tax_id": "602214076",
                "ss4_file_id": "string",
                "website": "https://example.com",
            },
        )
        assert isinstance(resource, Entity)

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_method_create_person(self, client: AsyncIncrease) -> None:
        resource = await client.entities.create_person(
            {
                "address_line1": "33 Liberty Street",
                "address_city": "New York",
                "address_state": "NY",
                "address_zip": "10045",
                "date_of_birth": "1970-01-31",
                "name": "Ian Crease",
                "social_security_number_last4": "1120",
            },
        )
        assert isinstance(resource, Entity)

    @pytest.mark.skip(reason="Prism tests are broken")
    @parametrize
    async def test_method_create_person_with_optional_params(self, client: AsyncIncrease) -> None:
        resource = await client.entities.create_person(
            {
                "address_line1": "33 Liberty Street",
                "address_line2": "x",
                "address_city": "New York",
                "address_state": "NY",
                "address_zip": "10045",
                "date_of_birth": "1970-01-31",
                "name": "Ian Crease",
                "social_security_number_last4": "1120",
            },
        )
        assert isinstance(resource, Entity)
