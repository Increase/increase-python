# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import FednowTransfer
from increase._utils import parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFednowTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        fednow_transfer = client.fednow_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            creditor_name="Ian Crease",
            debtor_name="National Phonograph Company",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            unstructured_remittance_information="Invoice 29582",
        )
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        fednow_transfer = client.fednow_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            creditor_name="Ian Crease",
            debtor_name="National Phonograph Company",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            unstructured_remittance_information="Invoice 29582",
            account_number="987654321",
            creditor_address={
                "city": "New York",
                "postal_code": "10045",
                "state": "NY",
                "line1": "33 Liberty Street",
            },
            debtor_address={
                "city": "x",
                "postal_code": "x",
                "state": "x",
                "line1": "x",
            },
            external_account_id="external_account_id",
            require_approval=True,
            routing_number="101050001",
        )
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.fednow_transfers.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            creditor_name="Ian Crease",
            debtor_name="National Phonograph Company",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            unstructured_remittance_information="Invoice 29582",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fednow_transfer = response.parse()
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.fednow_transfers.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            creditor_name="Ian Crease",
            debtor_name="National Phonograph Company",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            unstructured_remittance_information="Invoice 29582",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fednow_transfer = response.parse()
            assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        fednow_transfer = client.fednow_transfers.retrieve(
            "fednow_transfer_4i0mptrdu1mueg1196bg",
        )
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.fednow_transfers.with_raw_response.retrieve(
            "fednow_transfer_4i0mptrdu1mueg1196bg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fednow_transfer = response.parse()
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.fednow_transfers.with_streaming_response.retrieve(
            "fednow_transfer_4i0mptrdu1mueg1196bg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fednow_transfer = response.parse()
            assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fednow_transfer_id` but received ''"):
            client.fednow_transfers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        fednow_transfer = client.fednow_transfers.list()
        assert_matches_type(SyncPage[FednowTransfer], fednow_transfer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        fednow_transfer = client.fednow_transfers.list(
            account_id="account_id",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            external_account_id="external_account_id",
            idempotency_key="x",
            limit=1,
            status={"in": ["pending_reviewing"]},
        )
        assert_matches_type(SyncPage[FednowTransfer], fednow_transfer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.fednow_transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fednow_transfer = response.parse()
        assert_matches_type(SyncPage[FednowTransfer], fednow_transfer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.fednow_transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fednow_transfer = response.parse()
            assert_matches_type(SyncPage[FednowTransfer], fednow_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_approve(self, client: Increase) -> None:
        fednow_transfer = client.fednow_transfers.approve(
            "fednow_transfer_4i0mptrdu1mueg1196bg",
        )
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    def test_raw_response_approve(self, client: Increase) -> None:
        response = client.fednow_transfers.with_raw_response.approve(
            "fednow_transfer_4i0mptrdu1mueg1196bg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fednow_transfer = response.parse()
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    def test_streaming_response_approve(self, client: Increase) -> None:
        with client.fednow_transfers.with_streaming_response.approve(
            "fednow_transfer_4i0mptrdu1mueg1196bg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fednow_transfer = response.parse()
            assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_approve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fednow_transfer_id` but received ''"):
            client.fednow_transfers.with_raw_response.approve(
                "",
            )

    @parametrize
    def test_method_cancel(self, client: Increase) -> None:
        fednow_transfer = client.fednow_transfers.cancel(
            "fednow_transfer_4i0mptrdu1mueg1196bg",
        )
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Increase) -> None:
        response = client.fednow_transfers.with_raw_response.cancel(
            "fednow_transfer_4i0mptrdu1mueg1196bg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fednow_transfer = response.parse()
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Increase) -> None:
        with client.fednow_transfers.with_streaming_response.cancel(
            "fednow_transfer_4i0mptrdu1mueg1196bg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fednow_transfer = response.parse()
            assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fednow_transfer_id` but received ''"):
            client.fednow_transfers.with_raw_response.cancel(
                "",
            )


class TestAsyncFednowTransfers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        fednow_transfer = await async_client.fednow_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            creditor_name="Ian Crease",
            debtor_name="National Phonograph Company",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            unstructured_remittance_information="Invoice 29582",
        )
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        fednow_transfer = await async_client.fednow_transfers.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            creditor_name="Ian Crease",
            debtor_name="National Phonograph Company",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            unstructured_remittance_information="Invoice 29582",
            account_number="987654321",
            creditor_address={
                "city": "New York",
                "postal_code": "10045",
                "state": "NY",
                "line1": "33 Liberty Street",
            },
            debtor_address={
                "city": "x",
                "postal_code": "x",
                "state": "x",
                "line1": "x",
            },
            external_account_id="external_account_id",
            require_approval=True,
            routing_number="101050001",
        )
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.fednow_transfers.with_raw_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            creditor_name="Ian Crease",
            debtor_name="National Phonograph Company",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            unstructured_remittance_information="Invoice 29582",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fednow_transfer = await response.parse()
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.fednow_transfers.with_streaming_response.create(
            account_id="account_in71c4amph0vgo2qllky",
            amount=100,
            creditor_name="Ian Crease",
            debtor_name="National Phonograph Company",
            source_account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            unstructured_remittance_information="Invoice 29582",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fednow_transfer = await response.parse()
            assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        fednow_transfer = await async_client.fednow_transfers.retrieve(
            "fednow_transfer_4i0mptrdu1mueg1196bg",
        )
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.fednow_transfers.with_raw_response.retrieve(
            "fednow_transfer_4i0mptrdu1mueg1196bg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fednow_transfer = await response.parse()
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.fednow_transfers.with_streaming_response.retrieve(
            "fednow_transfer_4i0mptrdu1mueg1196bg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fednow_transfer = await response.parse()
            assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fednow_transfer_id` but received ''"):
            await async_client.fednow_transfers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        fednow_transfer = await async_client.fednow_transfers.list()
        assert_matches_type(AsyncPage[FednowTransfer], fednow_transfer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        fednow_transfer = await async_client.fednow_transfers.list(
            account_id="account_id",
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            external_account_id="external_account_id",
            idempotency_key="x",
            limit=1,
            status={"in": ["pending_reviewing"]},
        )
        assert_matches_type(AsyncPage[FednowTransfer], fednow_transfer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.fednow_transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fednow_transfer = await response.parse()
        assert_matches_type(AsyncPage[FednowTransfer], fednow_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.fednow_transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fednow_transfer = await response.parse()
            assert_matches_type(AsyncPage[FednowTransfer], fednow_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_approve(self, async_client: AsyncIncrease) -> None:
        fednow_transfer = await async_client.fednow_transfers.approve(
            "fednow_transfer_4i0mptrdu1mueg1196bg",
        )
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    async def test_raw_response_approve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.fednow_transfers.with_raw_response.approve(
            "fednow_transfer_4i0mptrdu1mueg1196bg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fednow_transfer = await response.parse()
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_approve(self, async_client: AsyncIncrease) -> None:
        async with async_client.fednow_transfers.with_streaming_response.approve(
            "fednow_transfer_4i0mptrdu1mueg1196bg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fednow_transfer = await response.parse()
            assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_approve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fednow_transfer_id` but received ''"):
            await async_client.fednow_transfers.with_raw_response.approve(
                "",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncIncrease) -> None:
        fednow_transfer = await async_client.fednow_transfers.cancel(
            "fednow_transfer_4i0mptrdu1mueg1196bg",
        )
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncIncrease) -> None:
        response = await async_client.fednow_transfers.with_raw_response.cancel(
            "fednow_transfer_4i0mptrdu1mueg1196bg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fednow_transfer = await response.parse()
        assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncIncrease) -> None:
        async with async_client.fednow_transfers.with_streaming_response.cancel(
            "fednow_transfer_4i0mptrdu1mueg1196bg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fednow_transfer = await response.parse()
            assert_matches_type(FednowTransfer, fednow_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fednow_transfer_id` but received ''"):
            await async_client.fednow_transfers.with_raw_response.cancel(
                "",
            )
