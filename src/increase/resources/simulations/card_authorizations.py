# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.simulations import card_authorization_create_params
from ...types.simulations.card_authorization_create_response import CardAuthorizationCreateResponse

__all__ = ["CardAuthorizationsResource", "AsyncCardAuthorizationsResource"]


class CardAuthorizationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardAuthorizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CardAuthorizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardAuthorizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CardAuthorizationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        authenticated_card_payment_id: str | NotGiven = NOT_GIVEN,
        card_id: str | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        digital_wallet_token_id: str | NotGiven = NOT_GIVEN,
        event_subscription_id: str | NotGiven = NOT_GIVEN,
        merchant_acceptor_id: str | NotGiven = NOT_GIVEN,
        merchant_category_code: str | NotGiven = NOT_GIVEN,
        merchant_city: str | NotGiven = NOT_GIVEN,
        merchant_country: str | NotGiven = NOT_GIVEN,
        merchant_descriptor: str | NotGiven = NOT_GIVEN,
        merchant_state: str | NotGiven = NOT_GIVEN,
        network_details: card_authorization_create_params.NetworkDetails | NotGiven = NOT_GIVEN,
        network_risk_score: int | NotGiven = NOT_GIVEN,
        physical_card_id: str | NotGiven = NOT_GIVEN,
        processing_category: card_authorization_create_params.ProcessingCategory | NotGiven = NOT_GIVEN,
        terminal_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardAuthorizationCreateResponse:
        """Simulates a purchase authorization on a [Card](#cards).

        Depending on the balance
        available to the card and the `amount` submitted, the authorization activity
        will result in a [Pending Transaction](#pending-transactions) of type
        `card_authorization` or a [Declined Transaction](#declined-transactions) of type
        `card_decline`. You can pass either a Card id or a
        [Digital Wallet Token](#digital-wallet-tokens) id to simulate the two different
        ways purchases can be made.

        Args:
          amount: The authorization amount in cents.

          authenticated_card_payment_id: The identifier of a Card Payment with a `card_authentication` if you want to
              simulate an authenticated authorization.

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

          processing_category: Fields specific to a specific type of authorization, such as Automatic Fuel
              Dispensers, Refund Authorizations, or Cash Disbursements.

          terminal_id: The terminal identifier (commonly abbreviated as TID) of the terminal the card
              is transacting with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/card_authorizations",
            body=maybe_transform(
                {
                    "amount": amount,
                    "authenticated_card_payment_id": authenticated_card_payment_id,
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
                    "processing_category": processing_category,
                    "terminal_id": terminal_id,
                },
                card_authorization_create_params.CardAuthorizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardAuthorizationCreateResponse,
        )


class AsyncCardAuthorizationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardAuthorizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardAuthorizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardAuthorizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCardAuthorizationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        authenticated_card_payment_id: str | NotGiven = NOT_GIVEN,
        card_id: str | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        digital_wallet_token_id: str | NotGiven = NOT_GIVEN,
        event_subscription_id: str | NotGiven = NOT_GIVEN,
        merchant_acceptor_id: str | NotGiven = NOT_GIVEN,
        merchant_category_code: str | NotGiven = NOT_GIVEN,
        merchant_city: str | NotGiven = NOT_GIVEN,
        merchant_country: str | NotGiven = NOT_GIVEN,
        merchant_descriptor: str | NotGiven = NOT_GIVEN,
        merchant_state: str | NotGiven = NOT_GIVEN,
        network_details: card_authorization_create_params.NetworkDetails | NotGiven = NOT_GIVEN,
        network_risk_score: int | NotGiven = NOT_GIVEN,
        physical_card_id: str | NotGiven = NOT_GIVEN,
        processing_category: card_authorization_create_params.ProcessingCategory | NotGiven = NOT_GIVEN,
        terminal_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardAuthorizationCreateResponse:
        """Simulates a purchase authorization on a [Card](#cards).

        Depending on the balance
        available to the card and the `amount` submitted, the authorization activity
        will result in a [Pending Transaction](#pending-transactions) of type
        `card_authorization` or a [Declined Transaction](#declined-transactions) of type
        `card_decline`. You can pass either a Card id or a
        [Digital Wallet Token](#digital-wallet-tokens) id to simulate the two different
        ways purchases can be made.

        Args:
          amount: The authorization amount in cents.

          authenticated_card_payment_id: The identifier of a Card Payment with a `card_authentication` if you want to
              simulate an authenticated authorization.

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

          processing_category: Fields specific to a specific type of authorization, such as Automatic Fuel
              Dispensers, Refund Authorizations, or Cash Disbursements.

          terminal_id: The terminal identifier (commonly abbreviated as TID) of the terminal the card
              is transacting with.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/card_authorizations",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "authenticated_card_payment_id": authenticated_card_payment_id,
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
                    "processing_category": processing_category,
                    "terminal_id": terminal_id,
                },
                card_authorization_create_params.CardAuthorizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardAuthorizationCreateResponse,
        )


class CardAuthorizationsResourceWithRawResponse:
    def __init__(self, card_authorizations: CardAuthorizationsResource) -> None:
        self._card_authorizations = card_authorizations

        self.create = to_raw_response_wrapper(
            card_authorizations.create,
        )


class AsyncCardAuthorizationsResourceWithRawResponse:
    def __init__(self, card_authorizations: AsyncCardAuthorizationsResource) -> None:
        self._card_authorizations = card_authorizations

        self.create = async_to_raw_response_wrapper(
            card_authorizations.create,
        )


class CardAuthorizationsResourceWithStreamingResponse:
    def __init__(self, card_authorizations: CardAuthorizationsResource) -> None:
        self._card_authorizations = card_authorizations

        self.create = to_streamed_response_wrapper(
            card_authorizations.create,
        )


class AsyncCardAuthorizationsResourceWithStreamingResponse:
    def __init__(self, card_authorizations: AsyncCardAuthorizationsResource) -> None:
        self._card_authorizations = card_authorizations

        self.create = async_to_streamed_response_wrapper(
            card_authorizations.create,
        )
