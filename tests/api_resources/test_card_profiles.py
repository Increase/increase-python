# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from increase.types import CardProfile
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCardProfiles:
    strict_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Increase(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        resource = client.card_profiles.create(
            description="x",
            digital_wallets={
                "issuer_name": "x",
                "card_description": "x",
                "background_image_file_id": "string",
                "app_icon_file_id": "string",
            },
        )
        assert isinstance(resource, CardProfile)

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        resource = client.card_profiles.retrieve(
            "string",
        )
        assert isinstance(resource, CardProfile)

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        resource = client.card_profiles.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        resource = client.card_profiles.list(
            cursor="string",
            limit=0,
            status={"in": ["pending", "pending", "pending"]},
        )
        assert isinstance(resource, SyncPage)


class TestAsyncCardProfiles:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        resource = await client.card_profiles.create(
            description="x",
            digital_wallets={
                "issuer_name": "x",
                "card_description": "x",
                "background_image_file_id": "string",
                "app_icon_file_id": "string",
            },
        )
        assert isinstance(resource, CardProfile)

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        resource = await client.card_profiles.retrieve(
            "string",
        )
        assert isinstance(resource, CardProfile)

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        resource = await client.card_profiles.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        resource = await client.card_profiles.list(
            cursor="string",
            limit=0,
            status={"in": ["pending", "pending", "pending"]},
        )
        assert isinstance(resource, AsyncPage)
