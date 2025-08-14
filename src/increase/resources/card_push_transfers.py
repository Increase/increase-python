# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import card_push_transfer_list_params, card_push_transfer_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.card_push_transfer import CardPushTransfer

__all__ = ["CardPushTransfersResource", "AsyncCardPushTransfersResource"]


class CardPushTransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardPushTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CardPushTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardPushTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CardPushTransfersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        business_application_identifier: Literal[
            "account_to_account",
            "business_to_business",
            "money_transfer_bank_initiated",
            "non_card_bill_payment",
            "consumer_bill_payment",
            "card_bill_payment",
            "funds_disbursement",
            "funds_transfer",
            "loyalty_and_offers",
            "merchant_disbursement",
            "merchant_payment",
            "person_to_person",
            "top_up",
            "wallet_transfer",
        ],
        card_token_id: str,
        merchant_category_code: str,
        merchant_city_name: str,
        merchant_name: str,
        merchant_name_prefix: str,
        merchant_postal_code: str,
        merchant_state: str,
        recipient_name: str,
        sender_address_city: str,
        sender_address_line1: str,
        sender_address_postal_code: str,
        sender_address_state: str,
        sender_name: str,
        source_account_number_id: str,
        require_approval: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPushTransfer:
        """Create a Card Push Transfer

        Args:
          amount: The transfer amount in USD cents.

        For Card Push transfers, must be positive.

          business_application_identifier: The Business Application Identifier describes the type of transaction being
              performed. Your program must be approved for the specified Business Application
              Identifier in order to use it.

              - `account_to_account` - Account to Account
              - `business_to_business` - Business to Business
              - `money_transfer_bank_initiated` - Money Transfer Bank Initiated
              - `non_card_bill_payment` - Non-Card Bill Payment
              - `consumer_bill_payment` - Consumer Bill Payment
              - `card_bill_payment` - Card Bill Payment
              - `funds_disbursement` - Funds Disbursement
              - `funds_transfer` - Funds Transfer
              - `loyalty_and_offers` - Loyalty and Offers
              - `merchant_disbursement` - Merchant Disbursement
              - `merchant_payment` - Merchant Payment
              - `person_to_person` - Person to Person
              - `top_up` - Top Up
              - `wallet_transfer` - Wallet Transfer

          card_token_id: The Increase identifier for the Card Token that represents the card number
              you're pushing funds to.

          merchant_category_code: The merchant category code (MCC) of the merchant (generally your business)
              sending the transfer. This is a four-digit code that describes the type of
              business or service provided by the merchant. Your program must be approved for
              the specified MCC in order to use it.

          merchant_city_name: The city name of the merchant (generally your business) sending the transfer.

          merchant_name: The merchant name shows up as the statement descriptor for the transfer. This is
              typically the name of your business or organization.

          merchant_name_prefix: For certain Business Application Identifiers, the statement descriptor is
              `merchant_name_prefix*sender_name`, where the `merchant_name_prefix` is a one to
              four character prefix that identifies the merchant.

          merchant_postal_code: The postal code of the merchant (generally your business) sending the transfer.

          merchant_state: The state of the merchant (generally your business) sending the transfer.

          recipient_name: The name of the funds recipient.

          sender_address_city: The city of the sender.

          sender_address_line1: The address line 1 of the sender.

          sender_address_postal_code: The postal code of the sender.

          sender_address_state: The state of the sender.

          sender_name: The name of the funds originator.

          source_account_number_id: The identifier of the Account Number from which to send the transfer.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/card_push_transfers",
            body=maybe_transform(
                {
                    "amount": amount,
                    "business_application_identifier": business_application_identifier,
                    "card_token_id": card_token_id,
                    "merchant_category_code": merchant_category_code,
                    "merchant_city_name": merchant_city_name,
                    "merchant_name": merchant_name,
                    "merchant_name_prefix": merchant_name_prefix,
                    "merchant_postal_code": merchant_postal_code,
                    "merchant_state": merchant_state,
                    "recipient_name": recipient_name,
                    "sender_address_city": sender_address_city,
                    "sender_address_line1": sender_address_line1,
                    "sender_address_postal_code": sender_address_postal_code,
                    "sender_address_state": sender_address_state,
                    "sender_name": sender_name,
                    "source_account_number_id": source_account_number_id,
                    "require_approval": require_approval,
                },
                card_push_transfer_create_params.CardPushTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPushTransfer,
        )

    def retrieve(
        self,
        card_push_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardPushTransfer:
        """
        Retrieve a Card Push Transfer

        Args:
          card_push_transfer_id: The identifier of the Card Push Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_push_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `card_push_transfer_id` but received {card_push_transfer_id!r}"
            )
        return self._get(
            f"/card_push_transfers/{card_push_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardPushTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: card_push_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: card_push_transfer_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[CardPushTransfer]:
        """
        List Card Push Transfers

        Args:
          account_id: Filter Card Push Transfers to ones belonging to the specified Account.

          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/card_push_transfers",
            page=SyncPage[CardPushTransfer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    card_push_transfer_list_params.CardPushTransferListParams,
                ),
            ),
            model=CardPushTransfer,
        )

    def approve(
        self,
        card_push_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPushTransfer:
        """
        Approves a Card Push Transfer in a pending_approval state.

        Args:
          card_push_transfer_id: The identifier of the Card Push Transfer to approve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_push_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `card_push_transfer_id` but received {card_push_transfer_id!r}"
            )
        return self._post(
            f"/card_push_transfers/{card_push_transfer_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPushTransfer,
        )

    def cancel(
        self,
        card_push_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPushTransfer:
        """
        Cancels a Card Push Transfer in a pending_approval state.

        Args:
          card_push_transfer_id: The identifier of the pending Card Push Transfer to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_push_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `card_push_transfer_id` but received {card_push_transfer_id!r}"
            )
        return self._post(
            f"/card_push_transfers/{card_push_transfer_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPushTransfer,
        )


class AsyncCardPushTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardPushTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardPushTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardPushTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCardPushTransfersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        business_application_identifier: Literal[
            "account_to_account",
            "business_to_business",
            "money_transfer_bank_initiated",
            "non_card_bill_payment",
            "consumer_bill_payment",
            "card_bill_payment",
            "funds_disbursement",
            "funds_transfer",
            "loyalty_and_offers",
            "merchant_disbursement",
            "merchant_payment",
            "person_to_person",
            "top_up",
            "wallet_transfer",
        ],
        card_token_id: str,
        merchant_category_code: str,
        merchant_city_name: str,
        merchant_name: str,
        merchant_name_prefix: str,
        merchant_postal_code: str,
        merchant_state: str,
        recipient_name: str,
        sender_address_city: str,
        sender_address_line1: str,
        sender_address_postal_code: str,
        sender_address_state: str,
        sender_name: str,
        source_account_number_id: str,
        require_approval: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPushTransfer:
        """Create a Card Push Transfer

        Args:
          amount: The transfer amount in USD cents.

        For Card Push transfers, must be positive.

          business_application_identifier: The Business Application Identifier describes the type of transaction being
              performed. Your program must be approved for the specified Business Application
              Identifier in order to use it.

              - `account_to_account` - Account to Account
              - `business_to_business` - Business to Business
              - `money_transfer_bank_initiated` - Money Transfer Bank Initiated
              - `non_card_bill_payment` - Non-Card Bill Payment
              - `consumer_bill_payment` - Consumer Bill Payment
              - `card_bill_payment` - Card Bill Payment
              - `funds_disbursement` - Funds Disbursement
              - `funds_transfer` - Funds Transfer
              - `loyalty_and_offers` - Loyalty and Offers
              - `merchant_disbursement` - Merchant Disbursement
              - `merchant_payment` - Merchant Payment
              - `person_to_person` - Person to Person
              - `top_up` - Top Up
              - `wallet_transfer` - Wallet Transfer

          card_token_id: The Increase identifier for the Card Token that represents the card number
              you're pushing funds to.

          merchant_category_code: The merchant category code (MCC) of the merchant (generally your business)
              sending the transfer. This is a four-digit code that describes the type of
              business or service provided by the merchant. Your program must be approved for
              the specified MCC in order to use it.

          merchant_city_name: The city name of the merchant (generally your business) sending the transfer.

          merchant_name: The merchant name shows up as the statement descriptor for the transfer. This is
              typically the name of your business or organization.

          merchant_name_prefix: For certain Business Application Identifiers, the statement descriptor is
              `merchant_name_prefix*sender_name`, where the `merchant_name_prefix` is a one to
              four character prefix that identifies the merchant.

          merchant_postal_code: The postal code of the merchant (generally your business) sending the transfer.

          merchant_state: The state of the merchant (generally your business) sending the transfer.

          recipient_name: The name of the funds recipient.

          sender_address_city: The city of the sender.

          sender_address_line1: The address line 1 of the sender.

          sender_address_postal_code: The postal code of the sender.

          sender_address_state: The state of the sender.

          sender_name: The name of the funds originator.

          source_account_number_id: The identifier of the Account Number from which to send the transfer.

          require_approval: Whether the transfer requires explicit approval via the dashboard or API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/card_push_transfers",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "business_application_identifier": business_application_identifier,
                    "card_token_id": card_token_id,
                    "merchant_category_code": merchant_category_code,
                    "merchant_city_name": merchant_city_name,
                    "merchant_name": merchant_name,
                    "merchant_name_prefix": merchant_name_prefix,
                    "merchant_postal_code": merchant_postal_code,
                    "merchant_state": merchant_state,
                    "recipient_name": recipient_name,
                    "sender_address_city": sender_address_city,
                    "sender_address_line1": sender_address_line1,
                    "sender_address_postal_code": sender_address_postal_code,
                    "sender_address_state": sender_address_state,
                    "sender_name": sender_name,
                    "source_account_number_id": source_account_number_id,
                    "require_approval": require_approval,
                },
                card_push_transfer_create_params.CardPushTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPushTransfer,
        )

    async def retrieve(
        self,
        card_push_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardPushTransfer:
        """
        Retrieve a Card Push Transfer

        Args:
          card_push_transfer_id: The identifier of the Card Push Transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_push_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `card_push_transfer_id` but received {card_push_transfer_id!r}"
            )
        return await self._get(
            f"/card_push_transfers/{card_push_transfer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardPushTransfer,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: card_push_transfer_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: card_push_transfer_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CardPushTransfer, AsyncPage[CardPushTransfer]]:
        """
        List Card Push Transfers

        Args:
          account_id: Filter Card Push Transfers to ones belonging to the specified Account.

          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/card_push_transfers",
            page=AsyncPage[CardPushTransfer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    card_push_transfer_list_params.CardPushTransferListParams,
                ),
            ),
            model=CardPushTransfer,
        )

    async def approve(
        self,
        card_push_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPushTransfer:
        """
        Approves a Card Push Transfer in a pending_approval state.

        Args:
          card_push_transfer_id: The identifier of the Card Push Transfer to approve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_push_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `card_push_transfer_id` but received {card_push_transfer_id!r}"
            )
        return await self._post(
            f"/card_push_transfers/{card_push_transfer_id}/approve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPushTransfer,
        )

    async def cancel(
        self,
        card_push_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPushTransfer:
        """
        Cancels a Card Push Transfer in a pending_approval state.

        Args:
          card_push_transfer_id: The identifier of the pending Card Push Transfer to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_push_transfer_id:
            raise ValueError(
                f"Expected a non-empty value for `card_push_transfer_id` but received {card_push_transfer_id!r}"
            )
        return await self._post(
            f"/card_push_transfers/{card_push_transfer_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPushTransfer,
        )


class CardPushTransfersResourceWithRawResponse:
    def __init__(self, card_push_transfers: CardPushTransfersResource) -> None:
        self._card_push_transfers = card_push_transfers

        self.create = to_raw_response_wrapper(
            card_push_transfers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            card_push_transfers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            card_push_transfers.list,
        )
        self.approve = to_raw_response_wrapper(
            card_push_transfers.approve,
        )
        self.cancel = to_raw_response_wrapper(
            card_push_transfers.cancel,
        )


class AsyncCardPushTransfersResourceWithRawResponse:
    def __init__(self, card_push_transfers: AsyncCardPushTransfersResource) -> None:
        self._card_push_transfers = card_push_transfers

        self.create = async_to_raw_response_wrapper(
            card_push_transfers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            card_push_transfers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            card_push_transfers.list,
        )
        self.approve = async_to_raw_response_wrapper(
            card_push_transfers.approve,
        )
        self.cancel = async_to_raw_response_wrapper(
            card_push_transfers.cancel,
        )


class CardPushTransfersResourceWithStreamingResponse:
    def __init__(self, card_push_transfers: CardPushTransfersResource) -> None:
        self._card_push_transfers = card_push_transfers

        self.create = to_streamed_response_wrapper(
            card_push_transfers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            card_push_transfers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            card_push_transfers.list,
        )
        self.approve = to_streamed_response_wrapper(
            card_push_transfers.approve,
        )
        self.cancel = to_streamed_response_wrapper(
            card_push_transfers.cancel,
        )


class AsyncCardPushTransfersResourceWithStreamingResponse:
    def __init__(self, card_push_transfers: AsyncCardPushTransfersResource) -> None:
        self._card_push_transfers = card_push_transfers

        self.create = async_to_streamed_response_wrapper(
            card_push_transfers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            card_push_transfers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            card_push_transfers.list,
        )
        self.approve = async_to_streamed_response_wrapper(
            card_push_transfers.approve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            card_push_transfers.cancel,
        )
