# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.simulations import card_balance_inquiry_create_params
from ...types.card_payment import CardPayment

__all__ = ["CardBalanceInquiriesResource", "AsyncCardBalanceInquiriesResource"]


class CardBalanceInquiriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardBalanceInquiriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CardBalanceInquiriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardBalanceInquiriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CardBalanceInquiriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        balance: int | Omit = omit,
        card_id: str | Omit = omit,
        decline_reason: Literal[
            "account_closed",
            "card_not_active",
            "card_canceled",
            "physical_card_not_active",
            "entity_not_active",
            "group_locked",
            "insufficient_funds",
            "cvv2_mismatch",
            "pin_mismatch",
            "card_expiration_mismatch",
            "transaction_not_allowed",
            "breaches_limit",
            "webhook_declined",
            "webhook_timed_out",
            "declined_by_stand_in_processing",
            "invalid_physical_card",
            "missing_original_authorization",
            "failed_3ds_authentication",
            "suspected_card_testing",
            "suspected_fraud",
        ]
        | Omit = omit,
        digital_wallet_token_id: str | Omit = omit,
        event_subscription_id: str | Omit = omit,
        merchant_acceptor_id: str | Omit = omit,
        merchant_category_code: str | Omit = omit,
        merchant_city: str | Omit = omit,
        merchant_country: str | Omit = omit,
        merchant_descriptor: str | Omit = omit,
        merchant_state: str | Omit = omit,
        network_details: card_balance_inquiry_create_params.NetworkDetails | Omit = omit,
        network_risk_score: int | Omit = omit,
        physical_card_id: str | Omit = omit,
        terminal_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """
        Simulates a balance inquiry on a [Card](#cards).

        Args:
          balance: The balance amount in cents. The account balance will be used if not provided.

          card_id: The identifier of the Card to be authorized.

          decline_reason: Forces a card decline with a specific reason. No real time decision will be
              sent.

              - `account_closed` - The account has been closed.
              - `card_not_active` - The Card was not active.
              - `card_canceled` - The Card has been canceled.
              - `physical_card_not_active` - The Physical Card was not active.
              - `entity_not_active` - The account's entity was not active.
              - `group_locked` - The account was inactive.
              - `insufficient_funds` - The Card's Account did not have a sufficient available
                balance.
              - `cvv2_mismatch` - The given CVV2 did not match the card's value.
              - `pin_mismatch` - The given PIN did not match the card's value.
              - `card_expiration_mismatch` - The given expiration date did not match the
                card's value. Only applies when a CVV2 is present.
              - `transaction_not_allowed` - The attempted card transaction is not allowed per
                Increase's terms.
              - `breaches_limit` - The transaction was blocked by a Limit.
              - `webhook_declined` - Your application declined the transaction via webhook.
              - `webhook_timed_out` - Your application webhook did not respond without the
                required timeout.
              - `declined_by_stand_in_processing` - Declined by stand-in processing.
              - `invalid_physical_card` - The card read had an invalid CVV, dCVV, or
                authorization request cryptogram.
              - `missing_original_authorization` - The original card authorization for this
                incremental authorization does not exist.
              - `failed_3ds_authentication` - The transaction was declined because the 3DS
                authentication failed.
              - `suspected_card_testing` - The transaction was suspected to be used by a card
                tester to test for valid card numbers.
              - `suspected_fraud` - The transaction was suspected to be fraudulent. Please
                reach out to support@increase.com for more information.

          digital_wallet_token_id: The identifier of the Digital Wallet Token to be authorized.

          event_subscription_id: The identifier of the Event Subscription to use. If provided, will override the
              default real time event subscription. Because you can only create one real time
              decision event subscription, you can use this field to route events to any
              specified event subscription for testing purposes.

          merchant_acceptor_id: The merchant identifier (commonly abbreviated as MID) of the merchant the card
              is transacting with.

          merchant_category_code: The Merchant Category Code (commonly abbreviated as MCC) of the merchant the
              card is transacting with.

          merchant_city: The city the merchant resides in.

          merchant_country: The country the merchant resides in.

          merchant_descriptor: The merchant descriptor of the merchant the card is transacting with.

          merchant_state: The state the merchant resides in.

          network_details: Fields specific to a given card network.

          network_risk_score: The risk score generated by the card network. For Visa this is the Visa Advanced
              Authorization risk score, from 0 to 99, where 99 is the riskiest.

          physical_card_id: The identifier of the Physical Card to be authorized.

          terminal_id: The terminal identifier (commonly abbreviated as TID) of the terminal the card
              is transacting with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/card_balance_inquiries",
            body=maybe_transform(
                {
                    "balance": balance,
                    "card_id": card_id,
                    "decline_reason": decline_reason,
                    "digital_wallet_token_id": digital_wallet_token_id,
                    "event_subscription_id": event_subscription_id,
                    "merchant_acceptor_id": merchant_acceptor_id,
                    "merchant_category_code": merchant_category_code,
                    "merchant_city": merchant_city,
                    "merchant_country": merchant_country,
                    "merchant_descriptor": merchant_descriptor,
                    "merchant_state": merchant_state,
                    "network_details": network_details,
                    "network_risk_score": network_risk_score,
                    "physical_card_id": physical_card_id,
                    "terminal_id": terminal_id,
                },
                card_balance_inquiry_create_params.CardBalanceInquiryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPayment,
        )


class AsyncCardBalanceInquiriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardBalanceInquiriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardBalanceInquiriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardBalanceInquiriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCardBalanceInquiriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        balance: int | Omit = omit,
        card_id: str | Omit = omit,
        decline_reason: Literal[
            "account_closed",
            "card_not_active",
            "card_canceled",
            "physical_card_not_active",
            "entity_not_active",
            "group_locked",
            "insufficient_funds",
            "cvv2_mismatch",
            "pin_mismatch",
            "card_expiration_mismatch",
            "transaction_not_allowed",
            "breaches_limit",
            "webhook_declined",
            "webhook_timed_out",
            "declined_by_stand_in_processing",
            "invalid_physical_card",
            "missing_original_authorization",
            "failed_3ds_authentication",
            "suspected_card_testing",
            "suspected_fraud",
        ]
        | Omit = omit,
        digital_wallet_token_id: str | Omit = omit,
        event_subscription_id: str | Omit = omit,
        merchant_acceptor_id: str | Omit = omit,
        merchant_category_code: str | Omit = omit,
        merchant_city: str | Omit = omit,
        merchant_country: str | Omit = omit,
        merchant_descriptor: str | Omit = omit,
        merchant_state: str | Omit = omit,
        network_details: card_balance_inquiry_create_params.NetworkDetails | Omit = omit,
        network_risk_score: int | Omit = omit,
        physical_card_id: str | Omit = omit,
        terminal_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """
        Simulates a balance inquiry on a [Card](#cards).

        Args:
          balance: The balance amount in cents. The account balance will be used if not provided.

          card_id: The identifier of the Card to be authorized.

          decline_reason: Forces a card decline with a specific reason. No real time decision will be
              sent.

              - `account_closed` - The account has been closed.
              - `card_not_active` - The Card was not active.
              - `card_canceled` - The Card has been canceled.
              - `physical_card_not_active` - The Physical Card was not active.
              - `entity_not_active` - The account's entity was not active.
              - `group_locked` - The account was inactive.
              - `insufficient_funds` - The Card's Account did not have a sufficient available
                balance.
              - `cvv2_mismatch` - The given CVV2 did not match the card's value.
              - `pin_mismatch` - The given PIN did not match the card's value.
              - `card_expiration_mismatch` - The given expiration date did not match the
                card's value. Only applies when a CVV2 is present.
              - `transaction_not_allowed` - The attempted card transaction is not allowed per
                Increase's terms.
              - `breaches_limit` - The transaction was blocked by a Limit.
              - `webhook_declined` - Your application declined the transaction via webhook.
              - `webhook_timed_out` - Your application webhook did not respond without the
                required timeout.
              - `declined_by_stand_in_processing` - Declined by stand-in processing.
              - `invalid_physical_card` - The card read had an invalid CVV, dCVV, or
                authorization request cryptogram.
              - `missing_original_authorization` - The original card authorization for this
                incremental authorization does not exist.
              - `failed_3ds_authentication` - The transaction was declined because the 3DS
                authentication failed.
              - `suspected_card_testing` - The transaction was suspected to be used by a card
                tester to test for valid card numbers.
              - `suspected_fraud` - The transaction was suspected to be fraudulent. Please
                reach out to support@increase.com for more information.

          digital_wallet_token_id: The identifier of the Digital Wallet Token to be authorized.

          event_subscription_id: The identifier of the Event Subscription to use. If provided, will override the
              default real time event subscription. Because you can only create one real time
              decision event subscription, you can use this field to route events to any
              specified event subscription for testing purposes.

          merchant_acceptor_id: The merchant identifier (commonly abbreviated as MID) of the merchant the card
              is transacting with.

          merchant_category_code: The Merchant Category Code (commonly abbreviated as MCC) of the merchant the
              card is transacting with.

          merchant_city: The city the merchant resides in.

          merchant_country: The country the merchant resides in.

          merchant_descriptor: The merchant descriptor of the merchant the card is transacting with.

          merchant_state: The state the merchant resides in.

          network_details: Fields specific to a given card network.

          network_risk_score: The risk score generated by the card network. For Visa this is the Visa Advanced
              Authorization risk score, from 0 to 99, where 99 is the riskiest.

          physical_card_id: The identifier of the Physical Card to be authorized.

          terminal_id: The terminal identifier (commonly abbreviated as TID) of the terminal the card
              is transacting with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/card_balance_inquiries",
            body=await async_maybe_transform(
                {
                    "balance": balance,
                    "card_id": card_id,
                    "decline_reason": decline_reason,
                    "digital_wallet_token_id": digital_wallet_token_id,
                    "event_subscription_id": event_subscription_id,
                    "merchant_acceptor_id": merchant_acceptor_id,
                    "merchant_category_code": merchant_category_code,
                    "merchant_city": merchant_city,
                    "merchant_country": merchant_country,
                    "merchant_descriptor": merchant_descriptor,
                    "merchant_state": merchant_state,
                    "network_details": network_details,
                    "network_risk_score": network_risk_score,
                    "physical_card_id": physical_card_id,
                    "terminal_id": terminal_id,
                },
                card_balance_inquiry_create_params.CardBalanceInquiryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPayment,
        )


class CardBalanceInquiriesResourceWithRawResponse:
    def __init__(self, card_balance_inquiries: CardBalanceInquiriesResource) -> None:
        self._card_balance_inquiries = card_balance_inquiries

        self.create = to_raw_response_wrapper(
            card_balance_inquiries.create,
        )


class AsyncCardBalanceInquiriesResourceWithRawResponse:
    def __init__(self, card_balance_inquiries: AsyncCardBalanceInquiriesResource) -> None:
        self._card_balance_inquiries = card_balance_inquiries

        self.create = async_to_raw_response_wrapper(
            card_balance_inquiries.create,
        )


class CardBalanceInquiriesResourceWithStreamingResponse:
    def __init__(self, card_balance_inquiries: CardBalanceInquiriesResource) -> None:
        self._card_balance_inquiries = card_balance_inquiries

        self.create = to_streamed_response_wrapper(
            card_balance_inquiries.create,
        )


class AsyncCardBalanceInquiriesResourceWithStreamingResponse:
    def __init__(self, card_balance_inquiries: AsyncCardBalanceInquiriesResource) -> None:
        self._card_balance_inquiries = card_balance_inquiries

        self.create = async_to_streamed_response_wrapper(
            card_balance_inquiries.create,
        )
