# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import card_validation_list_params, card_validation_create_params
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
from ..types.card_validation import CardValidation

__all__ = ["CardValidationsResource", "AsyncCardValidationsResource"]


class CardValidationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardValidationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CardValidationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardValidationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CardValidationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        card_token_id: str,
        merchant_category_code: str,
        merchant_city_name: str,
        merchant_name: str,
        merchant_postal_code: str,
        merchant_state: str,
        cardholder_first_name: str | NotGiven = NOT_GIVEN,
        cardholder_last_name: str | NotGiven = NOT_GIVEN,
        cardholder_middle_name: str | NotGiven = NOT_GIVEN,
        cardholder_postal_code: str | NotGiven = NOT_GIVEN,
        cardholder_street_address: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardValidation:
        """
        Create a Card Validation

        Args:
          account_id: The identifier of the Account from which to send the validation.

          card_token_id: The Increase identifier for the Card Token that represents the card number
              you're validating.

          merchant_category_code: A four-digit code (MCC) identifying the type of business or service provided by
              the merchant.

          merchant_city_name: The city where the merchant (typically your business) is located.

          merchant_name: The merchant name that will appear in the cardholder’s statement descriptor.
              Typically your business name.

          merchant_postal_code: The postal code for the merchant’s (typically your business’s) location.

          merchant_state: The U.S. state where the merchant (typically your business) is located.

          cardholder_first_name: The cardholder's first name.

          cardholder_last_name: The cardholder's last name.

          cardholder_middle_name: The cardholder's middle name.

          cardholder_postal_code: The postal code of the cardholder's address.

          cardholder_street_address: The cardholder's street address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/card_validations",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "card_token_id": card_token_id,
                    "merchant_category_code": merchant_category_code,
                    "merchant_city_name": merchant_city_name,
                    "merchant_name": merchant_name,
                    "merchant_postal_code": merchant_postal_code,
                    "merchant_state": merchant_state,
                    "cardholder_first_name": cardholder_first_name,
                    "cardholder_last_name": cardholder_last_name,
                    "cardholder_middle_name": cardholder_middle_name,
                    "cardholder_postal_code": cardholder_postal_code,
                    "cardholder_street_address": cardholder_street_address,
                },
                card_validation_create_params.CardValidationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardValidation,
        )

    def retrieve(
        self,
        card_validation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardValidation:
        """
        Retrieve a Card Validation

        Args:
          card_validation_id: The identifier of the Card Validation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_validation_id:
            raise ValueError(f"Expected a non-empty value for `card_validation_id` but received {card_validation_id!r}")
        return self._get(
            f"/card_validations/{card_validation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardValidation,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: card_validation_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: card_validation_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[CardValidation]:
        """
        List Card Validations

        Args:
          account_id: Filter Card Validations to ones belonging to the specified Account.

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
            "/card_validations",
            page=SyncPage[CardValidation],
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
                    card_validation_list_params.CardValidationListParams,
                ),
            ),
            model=CardValidation,
        )


class AsyncCardValidationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardValidationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardValidationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardValidationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCardValidationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        card_token_id: str,
        merchant_category_code: str,
        merchant_city_name: str,
        merchant_name: str,
        merchant_postal_code: str,
        merchant_state: str,
        cardholder_first_name: str | NotGiven = NOT_GIVEN,
        cardholder_last_name: str | NotGiven = NOT_GIVEN,
        cardholder_middle_name: str | NotGiven = NOT_GIVEN,
        cardholder_postal_code: str | NotGiven = NOT_GIVEN,
        cardholder_street_address: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardValidation:
        """
        Create a Card Validation

        Args:
          account_id: The identifier of the Account from which to send the validation.

          card_token_id: The Increase identifier for the Card Token that represents the card number
              you're validating.

          merchant_category_code: A four-digit code (MCC) identifying the type of business or service provided by
              the merchant.

          merchant_city_name: The city where the merchant (typically your business) is located.

          merchant_name: The merchant name that will appear in the cardholder’s statement descriptor.
              Typically your business name.

          merchant_postal_code: The postal code for the merchant’s (typically your business’s) location.

          merchant_state: The U.S. state where the merchant (typically your business) is located.

          cardholder_first_name: The cardholder's first name.

          cardholder_last_name: The cardholder's last name.

          cardholder_middle_name: The cardholder's middle name.

          cardholder_postal_code: The postal code of the cardholder's address.

          cardholder_street_address: The cardholder's street address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/card_validations",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "card_token_id": card_token_id,
                    "merchant_category_code": merchant_category_code,
                    "merchant_city_name": merchant_city_name,
                    "merchant_name": merchant_name,
                    "merchant_postal_code": merchant_postal_code,
                    "merchant_state": merchant_state,
                    "cardholder_first_name": cardholder_first_name,
                    "cardholder_last_name": cardholder_last_name,
                    "cardholder_middle_name": cardholder_middle_name,
                    "cardholder_postal_code": cardholder_postal_code,
                    "cardholder_street_address": cardholder_street_address,
                },
                card_validation_create_params.CardValidationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardValidation,
        )

    async def retrieve(
        self,
        card_validation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardValidation:
        """
        Retrieve a Card Validation

        Args:
          card_validation_id: The identifier of the Card Validation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_validation_id:
            raise ValueError(f"Expected a non-empty value for `card_validation_id` but received {card_validation_id!r}")
        return await self._get(
            f"/card_validations/{card_validation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardValidation,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_at: card_validation_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: card_validation_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CardValidation, AsyncPage[CardValidation]]:
        """
        List Card Validations

        Args:
          account_id: Filter Card Validations to ones belonging to the specified Account.

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
            "/card_validations",
            page=AsyncPage[CardValidation],
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
                    card_validation_list_params.CardValidationListParams,
                ),
            ),
            model=CardValidation,
        )


class CardValidationsResourceWithRawResponse:
    def __init__(self, card_validations: CardValidationsResource) -> None:
        self._card_validations = card_validations

        self.create = to_raw_response_wrapper(
            card_validations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            card_validations.retrieve,
        )
        self.list = to_raw_response_wrapper(
            card_validations.list,
        )


class AsyncCardValidationsResourceWithRawResponse:
    def __init__(self, card_validations: AsyncCardValidationsResource) -> None:
        self._card_validations = card_validations

        self.create = async_to_raw_response_wrapper(
            card_validations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            card_validations.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            card_validations.list,
        )


class CardValidationsResourceWithStreamingResponse:
    def __init__(self, card_validations: CardValidationsResource) -> None:
        self._card_validations = card_validations

        self.create = to_streamed_response_wrapper(
            card_validations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            card_validations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            card_validations.list,
        )


class AsyncCardValidationsResourceWithStreamingResponse:
    def __init__(self, card_validations: AsyncCardValidationsResource) -> None:
        self._card_validations = card_validations

        self.create = async_to_streamed_response_wrapper(
            card_validations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            card_validations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            card_validations.list,
        )
