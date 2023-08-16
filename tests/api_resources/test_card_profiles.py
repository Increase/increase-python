# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
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
        card_profile = client.card_profiles.create(
            description="x",
            digital_wallets={
                "issuer_name": "x",
                "card_description": "x",
                "background_image_file_id": "string",
                "app_icon_file_id": "string",
            },
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        card_profile = client.card_profiles.create(
            description="x",
            digital_wallets={
                "text_color": {
                    "red": 0,
                    "green": 0,
                    "blue": 0,
                },
                "issuer_name": "x",
                "card_description": "x",
                "contact_website": "string",
                "contact_email": "x",
                "contact_phone": "x",
                "background_image_file_id": "string",
                "app_icon_file_id": "string",
            },
            physical_cards={
                "contact_phone": "x",
                "front_image_file_id": "string",
                "carrier_image_file_id": "string",
            },
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        card_profile = client.card_profiles.retrieve(
            "string",
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        card_profile = client.card_profiles.list()
        assert_matches_type(SyncPage[CardProfile], card_profile, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        card_profile = client.card_profiles.list(
            cursor="string",
            limit=0,
            physical_cards_status={"in": ["not_eligible", "not_eligible", "not_eligible"]},
            status={"in": ["pending", "pending", "pending"]},
        )
        assert_matches_type(SyncPage[CardProfile], card_profile, path=["response"])

    @parametrize
    def test_method_archive(self, client: Increase) -> None:
        card_profile = client.card_profiles.archive(
            "string",
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])


class TestAsyncCardProfiles:
    strict_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncIncrease(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIncrease) -> None:
        card_profile = await client.card_profiles.create(
            description="x",
            digital_wallets={
                "issuer_name": "x",
                "card_description": "x",
                "background_image_file_id": "string",
                "app_icon_file_id": "string",
            },
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIncrease) -> None:
        card_profile = await client.card_profiles.create(
            description="x",
            digital_wallets={
                "text_color": {
                    "red": 0,
                    "green": 0,
                    "blue": 0,
                },
                "issuer_name": "x",
                "card_description": "x",
                "contact_website": "string",
                "contact_email": "x",
                "contact_phone": "x",
                "background_image_file_id": "string",
                "app_icon_file_id": "string",
            },
            physical_cards={
                "contact_phone": "x",
                "front_image_file_id": "string",
                "carrier_image_file_id": "string",
            },
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIncrease) -> None:
        card_profile = await client.card_profiles.retrieve(
            "string",
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIncrease) -> None:
        card_profile = await client.card_profiles.list()
        assert_matches_type(AsyncPage[CardProfile], card_profile, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIncrease) -> None:
        card_profile = await client.card_profiles.list(
            cursor="string",
            limit=0,
            physical_cards_status={"in": ["not_eligible", "not_eligible", "not_eligible"]},
            status={"in": ["pending", "pending", "pending"]},
        )
        assert_matches_type(AsyncPage[CardProfile], card_profile, path=["response"])

    @parametrize
    async def test_method_archive(self, client: AsyncIncrease) -> None:
        card_profile = await client.card_profiles.archive(
            "string",
        )
        assert_matches_type(CardProfile, card_profile, path=["response"])
