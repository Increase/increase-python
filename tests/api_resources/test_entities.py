# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

from increase import Increase, AsyncIncrease
from increase.pagination import SyncPage, AsyncPage
from increase.types.entity import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestEntities:
    client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_retrieve(self) -> None:
        resource = self.client.entities.retrieve(
            "string",
        )
        assert isinstance(resource, Entity)

    def test_method_list(self) -> None:
        resource = self.client.entities.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.entities.list(
            {
                "cursor": "string",
                "limit": 0,
            },
        )
        assert isinstance(resource, SyncPage)

    def test_method_create_corporation(self) -> None:
        resource = self.client.entities.create_corporation(
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

    def test_method_create_corporation_with_optional_params(self) -> None:
        resource = self.client.entities.create_corporation(
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
                    },
                ],
                "name": "National Phonograph Company",
                "website": "https://example.com",
                "state": "NJ",
                "tax_id": "602214076",
                "ss4_file_id": "string",
            },
        )
        assert isinstance(resource, Entity)

    def test_method_create_person(self) -> None:
        resource = self.client.entities.create_person(
            {
                "address_line1": "33 Liberty Street",
                "address_city": "New York",
                "address_state": "NY",
                "address_zip": "10045",
                "date_of_birth": "1970-01-31T18:11:19.117Z",
                "name": "Ian Crease",
                "social_security_number_last4": "1120",
            },
        )
        assert isinstance(resource, Entity)

    def test_method_create_person_with_optional_params(self) -> None:
        resource = self.client.entities.create_person(
            {
                "address_line1": "33 Liberty Street",
                "address_line2": "x",
                "address_city": "New York",
                "address_state": "NY",
                "address_zip": "10045",
                "date_of_birth": "1970-01-31T18:11:19.117Z",
                "name": "Ian Crease",
                "social_security_number_last4": "1120",
            },
        )
        assert isinstance(resource, Entity)


class TestAsyncEntities:
    client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.entities.retrieve(
            "string",
        )
        assert isinstance(resource, Entity)

    async def test_method_list(self) -> None:
        resource = await self.client.entities.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.entities.list(
            {
                "cursor": "string",
                "limit": 0,
            },
        )
        assert isinstance(resource, AsyncPage)

    async def test_method_create_corporation(self) -> None:
        resource = await self.client.entities.create_corporation(
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

    async def test_method_create_corporation_with_optional_params(self) -> None:
        resource = await self.client.entities.create_corporation(
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
                    },
                ],
                "name": "National Phonograph Company",
                "website": "https://example.com",
                "state": "NJ",
                "tax_id": "602214076",
                "ss4_file_id": "string",
            },
        )
        assert isinstance(resource, Entity)

    async def test_method_create_person(self) -> None:
        resource = await self.client.entities.create_person(
            {
                "address_line1": "33 Liberty Street",
                "address_city": "New York",
                "address_state": "NY",
                "address_zip": "10045",
                "date_of_birth": "1970-01-31T18:11:19.117Z",
                "name": "Ian Crease",
                "social_security_number_last4": "1120",
            },
        )
        assert isinstance(resource, Entity)

    async def test_method_create_person_with_optional_params(self) -> None:
        resource = await self.client.entities.create_person(
            {
                "address_line1": "33 Liberty Street",
                "address_line2": "x",
                "address_city": "New York",
                "address_state": "NY",
                "address_zip": "10045",
                "date_of_birth": "1970-01-31T18:11:19.117Z",
                "name": "Ian Crease",
                "social_security_number_last4": "1120",
            },
        )
        assert isinstance(resource, Entity)
