# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import card_dispute_list_params, card_dispute_create_params, card_dispute_submit_user_submission_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.card_dispute import CardDispute

__all__ = ["CardDisputesResource", "AsyncCardDisputesResource"]


class CardDisputesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardDisputesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return CardDisputesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardDisputesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return CardDisputesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        disputed_transaction_id: str,
        network: Literal["visa"],
        amount: int | Omit = omit,
        attachment_files: Iterable[card_dispute_create_params.AttachmentFile] | Omit = omit,
        visa: card_dispute_create_params.Visa | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardDispute:
        """
        Create a Card Dispute

        Args:
          disputed_transaction_id: The Transaction you wish to dispute. This Transaction must have a `source_type`
              of `card_settlement`.

          network: The network of the disputed transaction. Details specific to the network are
              required under the sub-object with the same identifier as the network.

              - `visa` - Visa

          amount: The monetary amount of the part of the transaction that is being disputed. This
              is optional and will default to the full amount of the transaction if not
              provided. If provided, the amount must be less than or equal to the amount of
              the transaction.

          attachment_files: The files to be attached to the initial dispute submission.

          visa: The Visa-specific parameters for the dispute. Required if and only if `network`
              is `visa`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/card_disputes",
            body=maybe_transform(
                {
                    "disputed_transaction_id": disputed_transaction_id,
                    "network": network,
                    "amount": amount,
                    "attachment_files": attachment_files,
                    "visa": visa,
                },
                card_dispute_create_params.CardDisputeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardDispute,
        )

    def retrieve(
        self,
        card_dispute_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardDispute:
        """
        Retrieve a Card Dispute

        Args:
          card_dispute_id: The identifier of the Card Dispute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_dispute_id:
            raise ValueError(f"Expected a non-empty value for `card_dispute_id` but received {card_dispute_id!r}")
        return self._get(
            f"/card_disputes/{card_dispute_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardDispute,
        )

    def list(
        self,
        *,
        created_at: card_dispute_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        status: card_dispute_list_params.Status | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[CardDispute]:
        """
        List Card Disputes

        Args:
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
            "/card_disputes",
            page=SyncPage[CardDispute],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    card_dispute_list_params.CardDisputeListParams,
                ),
            ),
            model=CardDispute,
        )

    def submit_user_submission(
        self,
        card_dispute_id: str,
        *,
        network: Literal["visa"],
        amount: int | Omit = omit,
        attachment_files: Iterable[card_dispute_submit_user_submission_params.AttachmentFile] | Omit = omit,
        visa: card_dispute_submit_user_submission_params.Visa | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardDispute:
        """
        Submit a User Submission for a Card Dispute

        Args:
          card_dispute_id: The identifier of the Card Dispute to submit a user submission for.

          network: The network of the Card Dispute. Details specific to the network are required
              under the sub-object with the same identifier as the network.

              - `visa` - Visa

          amount: The adjusted monetary amount of the part of the transaction that is being
              disputed. This is optional and will default to the most recent amount provided.
              If provided, the amount must be less than or equal to the amount of the
              transaction.

          attachment_files: The files to be attached to the user submission.

          visa: The Visa-specific parameters for the dispute. Required if and only if `network`
              is `visa`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_dispute_id:
            raise ValueError(f"Expected a non-empty value for `card_dispute_id` but received {card_dispute_id!r}")
        return self._post(
            f"/card_disputes/{card_dispute_id}/submit_user_submission",
            body=maybe_transform(
                {
                    "network": network,
                    "amount": amount,
                    "attachment_files": attachment_files,
                    "visa": visa,
                },
                card_dispute_submit_user_submission_params.CardDisputeSubmitUserSubmissionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardDispute,
        )

    def withdraw(
        self,
        card_dispute_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardDispute:
        """
        Withdraw a Card Dispute

        Args:
          card_dispute_id: The identifier of the Card Dispute to withdraw.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_dispute_id:
            raise ValueError(f"Expected a non-empty value for `card_dispute_id` but received {card_dispute_id!r}")
        return self._post(
            f"/card_disputes/{card_dispute_id}/withdraw",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardDispute,
        )


class AsyncCardDisputesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardDisputesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardDisputesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardDisputesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncCardDisputesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        disputed_transaction_id: str,
        network: Literal["visa"],
        amount: int | Omit = omit,
        attachment_files: Iterable[card_dispute_create_params.AttachmentFile] | Omit = omit,
        visa: card_dispute_create_params.Visa | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardDispute:
        """
        Create a Card Dispute

        Args:
          disputed_transaction_id: The Transaction you wish to dispute. This Transaction must have a `source_type`
              of `card_settlement`.

          network: The network of the disputed transaction. Details specific to the network are
              required under the sub-object with the same identifier as the network.

              - `visa` - Visa

          amount: The monetary amount of the part of the transaction that is being disputed. This
              is optional and will default to the full amount of the transaction if not
              provided. If provided, the amount must be less than or equal to the amount of
              the transaction.

          attachment_files: The files to be attached to the initial dispute submission.

          visa: The Visa-specific parameters for the dispute. Required if and only if `network`
              is `visa`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/card_disputes",
            body=await async_maybe_transform(
                {
                    "disputed_transaction_id": disputed_transaction_id,
                    "network": network,
                    "amount": amount,
                    "attachment_files": attachment_files,
                    "visa": visa,
                },
                card_dispute_create_params.CardDisputeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardDispute,
        )

    async def retrieve(
        self,
        card_dispute_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardDispute:
        """
        Retrieve a Card Dispute

        Args:
          card_dispute_id: The identifier of the Card Dispute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_dispute_id:
            raise ValueError(f"Expected a non-empty value for `card_dispute_id` but received {card_dispute_id!r}")
        return await self._get(
            f"/card_disputes/{card_dispute_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardDispute,
        )

    def list(
        self,
        *,
        created_at: card_dispute_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        status: card_dispute_list_params.Status | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CardDispute, AsyncPage[CardDispute]]:
        """
        List Card Disputes

        Args:
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
            "/card_disputes",
            page=AsyncPage[CardDispute],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                        "status": status,
                    },
                    card_dispute_list_params.CardDisputeListParams,
                ),
            ),
            model=CardDispute,
        )

    async def submit_user_submission(
        self,
        card_dispute_id: str,
        *,
        network: Literal["visa"],
        amount: int | Omit = omit,
        attachment_files: Iterable[card_dispute_submit_user_submission_params.AttachmentFile] | Omit = omit,
        visa: card_dispute_submit_user_submission_params.Visa | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardDispute:
        """
        Submit a User Submission for a Card Dispute

        Args:
          card_dispute_id: The identifier of the Card Dispute to submit a user submission for.

          network: The network of the Card Dispute. Details specific to the network are required
              under the sub-object with the same identifier as the network.

              - `visa` - Visa

          amount: The adjusted monetary amount of the part of the transaction that is being
              disputed. This is optional and will default to the most recent amount provided.
              If provided, the amount must be less than or equal to the amount of the
              transaction.

          attachment_files: The files to be attached to the user submission.

          visa: The Visa-specific parameters for the dispute. Required if and only if `network`
              is `visa`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_dispute_id:
            raise ValueError(f"Expected a non-empty value for `card_dispute_id` but received {card_dispute_id!r}")
        return await self._post(
            f"/card_disputes/{card_dispute_id}/submit_user_submission",
            body=await async_maybe_transform(
                {
                    "network": network,
                    "amount": amount,
                    "attachment_files": attachment_files,
                    "visa": visa,
                },
                card_dispute_submit_user_submission_params.CardDisputeSubmitUserSubmissionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardDispute,
        )

    async def withdraw(
        self,
        card_dispute_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CardDispute:
        """
        Withdraw a Card Dispute

        Args:
          card_dispute_id: The identifier of the Card Dispute to withdraw.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not card_dispute_id:
            raise ValueError(f"Expected a non-empty value for `card_dispute_id` but received {card_dispute_id!r}")
        return await self._post(
            f"/card_disputes/{card_dispute_id}/withdraw",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardDispute,
        )


class CardDisputesResourceWithRawResponse:
    def __init__(self, card_disputes: CardDisputesResource) -> None:
        self._card_disputes = card_disputes

        self.create = to_raw_response_wrapper(
            card_disputes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            card_disputes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            card_disputes.list,
        )
        self.submit_user_submission = to_raw_response_wrapper(
            card_disputes.submit_user_submission,
        )
        self.withdraw = to_raw_response_wrapper(
            card_disputes.withdraw,
        )


class AsyncCardDisputesResourceWithRawResponse:
    def __init__(self, card_disputes: AsyncCardDisputesResource) -> None:
        self._card_disputes = card_disputes

        self.create = async_to_raw_response_wrapper(
            card_disputes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            card_disputes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            card_disputes.list,
        )
        self.submit_user_submission = async_to_raw_response_wrapper(
            card_disputes.submit_user_submission,
        )
        self.withdraw = async_to_raw_response_wrapper(
            card_disputes.withdraw,
        )


class CardDisputesResourceWithStreamingResponse:
    def __init__(self, card_disputes: CardDisputesResource) -> None:
        self._card_disputes = card_disputes

        self.create = to_streamed_response_wrapper(
            card_disputes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            card_disputes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            card_disputes.list,
        )
        self.submit_user_submission = to_streamed_response_wrapper(
            card_disputes.submit_user_submission,
        )
        self.withdraw = to_streamed_response_wrapper(
            card_disputes.withdraw,
        )


class AsyncCardDisputesResourceWithStreamingResponse:
    def __init__(self, card_disputes: AsyncCardDisputesResource) -> None:
        self._card_disputes = card_disputes

        self.create = async_to_streamed_response_wrapper(
            card_disputes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            card_disputes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            card_disputes.list,
        )
        self.submit_user_submission = async_to_streamed_response_wrapper(
            card_disputes.submit_user_submission,
        )
        self.withdraw = async_to_streamed_response_wrapper(
            card_disputes.withdraw,
        )
