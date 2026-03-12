# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import beneficial_owner_list_params, beneficial_owner_update_params
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
from ..types.entity_beneficial_owner import EntityBeneficialOwner

__all__ = ["BeneficialOwnersResource", "AsyncBeneficialOwnersResource"]


class BeneficialOwnersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BeneficialOwnersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return BeneficialOwnersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BeneficialOwnersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return BeneficialOwnersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        entity_beneficial_owner_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityBeneficialOwner:
        """
        Retrieve a Beneficial Owner

        Args:
          entity_beneficial_owner_id: The identifier of the Beneficial Owner to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_beneficial_owner_id:
            raise ValueError(
                f"Expected a non-empty value for `entity_beneficial_owner_id` but received {entity_beneficial_owner_id!r}"
            )
        return self._get(
            f"/entity_beneficial_owners/{entity_beneficial_owner_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityBeneficialOwner,
        )

    def update(
        self,
        entity_beneficial_owner_id: str,
        *,
        address: beneficial_owner_update_params.Address | Omit = omit,
        confirmed_no_us_tax_id: bool | Omit = omit,
        identification: beneficial_owner_update_params.Identification | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> EntityBeneficialOwner:
        """
        Update a Beneficial Owner

        Args:
          entity_beneficial_owner_id: The identifier of the Beneficial Owner to update.

          address: The individual's physical address. Mail receiving locations like PO Boxes and
              PMB's are disallowed.

          confirmed_no_us_tax_id: The identification method for an individual can only be a passport, driver's
              license, or other document if you've confirmed the individual does not have a US
              tax id (either a Social Security Number or Individual Taxpayer Identification
              Number).

          identification: A means of verifying the person's identity.

          name: The individual's legal name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_beneficial_owner_id:
            raise ValueError(
                f"Expected a non-empty value for `entity_beneficial_owner_id` but received {entity_beneficial_owner_id!r}"
            )
        return self._patch(
            f"/entity_beneficial_owners/{entity_beneficial_owner_id}",
            body=maybe_transform(
                {
                    "address": address,
                    "confirmed_no_us_tax_id": confirmed_no_us_tax_id,
                    "identification": identification,
                    "name": name,
                },
                beneficial_owner_update_params.BeneficialOwnerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EntityBeneficialOwner,
        )

    def list(
        self,
        *,
        entity_id: str,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[EntityBeneficialOwner]:
        """
        List Beneficial Owners

        Args:
          entity_id: The identifier of the Entity to list beneficial owners for. Only `corporation`
              entities have beneficial owners.

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
            "/entity_beneficial_owners",
            page=SyncPage[EntityBeneficialOwner],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity_id": entity_id,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    beneficial_owner_list_params.BeneficialOwnerListParams,
                ),
            ),
            model=EntityBeneficialOwner,
        )

    def archive(
        self,
        entity_beneficial_owner_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> EntityBeneficialOwner:
        """
        Archive a Beneficial Owner

        Args:
          entity_beneficial_owner_id: The identifier of the Beneficial Owner to archive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_beneficial_owner_id:
            raise ValueError(
                f"Expected a non-empty value for `entity_beneficial_owner_id` but received {entity_beneficial_owner_id!r}"
            )
        return self._post(
            f"/entity_beneficial_owners/{entity_beneficial_owner_id}/archive",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EntityBeneficialOwner,
        )


class AsyncBeneficialOwnersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBeneficialOwnersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBeneficialOwnersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBeneficialOwnersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncBeneficialOwnersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        entity_beneficial_owner_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityBeneficialOwner:
        """
        Retrieve a Beneficial Owner

        Args:
          entity_beneficial_owner_id: The identifier of the Beneficial Owner to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_beneficial_owner_id:
            raise ValueError(
                f"Expected a non-empty value for `entity_beneficial_owner_id` but received {entity_beneficial_owner_id!r}"
            )
        return await self._get(
            f"/entity_beneficial_owners/{entity_beneficial_owner_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityBeneficialOwner,
        )

    async def update(
        self,
        entity_beneficial_owner_id: str,
        *,
        address: beneficial_owner_update_params.Address | Omit = omit,
        confirmed_no_us_tax_id: bool | Omit = omit,
        identification: beneficial_owner_update_params.Identification | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> EntityBeneficialOwner:
        """
        Update a Beneficial Owner

        Args:
          entity_beneficial_owner_id: The identifier of the Beneficial Owner to update.

          address: The individual's physical address. Mail receiving locations like PO Boxes and
              PMB's are disallowed.

          confirmed_no_us_tax_id: The identification method for an individual can only be a passport, driver's
              license, or other document if you've confirmed the individual does not have a US
              tax id (either a Social Security Number or Individual Taxpayer Identification
              Number).

          identification: A means of verifying the person's identity.

          name: The individual's legal name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_beneficial_owner_id:
            raise ValueError(
                f"Expected a non-empty value for `entity_beneficial_owner_id` but received {entity_beneficial_owner_id!r}"
            )
        return await self._patch(
            f"/entity_beneficial_owners/{entity_beneficial_owner_id}",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "confirmed_no_us_tax_id": confirmed_no_us_tax_id,
                    "identification": identification,
                    "name": name,
                },
                beneficial_owner_update_params.BeneficialOwnerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EntityBeneficialOwner,
        )

    def list(
        self,
        *,
        entity_id: str,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EntityBeneficialOwner, AsyncPage[EntityBeneficialOwner]]:
        """
        List Beneficial Owners

        Args:
          entity_id: The identifier of the Entity to list beneficial owners for. Only `corporation`
              entities have beneficial owners.

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
            "/entity_beneficial_owners",
            page=AsyncPage[EntityBeneficialOwner],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity_id": entity_id,
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    beneficial_owner_list_params.BeneficialOwnerListParams,
                ),
            ),
            model=EntityBeneficialOwner,
        )

    async def archive(
        self,
        entity_beneficial_owner_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> EntityBeneficialOwner:
        """
        Archive a Beneficial Owner

        Args:
          entity_beneficial_owner_id: The identifier of the Beneficial Owner to archive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_beneficial_owner_id:
            raise ValueError(
                f"Expected a non-empty value for `entity_beneficial_owner_id` but received {entity_beneficial_owner_id!r}"
            )
        return await self._post(
            f"/entity_beneficial_owners/{entity_beneficial_owner_id}/archive",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EntityBeneficialOwner,
        )


class BeneficialOwnersResourceWithRawResponse:
    def __init__(self, beneficial_owners: BeneficialOwnersResource) -> None:
        self._beneficial_owners = beneficial_owners

        self.retrieve = to_raw_response_wrapper(
            beneficial_owners.retrieve,
        )
        self.update = to_raw_response_wrapper(
            beneficial_owners.update,
        )
        self.list = to_raw_response_wrapper(
            beneficial_owners.list,
        )
        self.archive = to_raw_response_wrapper(
            beneficial_owners.archive,
        )


class AsyncBeneficialOwnersResourceWithRawResponse:
    def __init__(self, beneficial_owners: AsyncBeneficialOwnersResource) -> None:
        self._beneficial_owners = beneficial_owners

        self.retrieve = async_to_raw_response_wrapper(
            beneficial_owners.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            beneficial_owners.update,
        )
        self.list = async_to_raw_response_wrapper(
            beneficial_owners.list,
        )
        self.archive = async_to_raw_response_wrapper(
            beneficial_owners.archive,
        )


class BeneficialOwnersResourceWithStreamingResponse:
    def __init__(self, beneficial_owners: BeneficialOwnersResource) -> None:
        self._beneficial_owners = beneficial_owners

        self.retrieve = to_streamed_response_wrapper(
            beneficial_owners.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            beneficial_owners.update,
        )
        self.list = to_streamed_response_wrapper(
            beneficial_owners.list,
        )
        self.archive = to_streamed_response_wrapper(
            beneficial_owners.archive,
        )


class AsyncBeneficialOwnersResourceWithStreamingResponse:
    def __init__(self, beneficial_owners: AsyncBeneficialOwnersResource) -> None:
        self._beneficial_owners = beneficial_owners

        self.retrieve = async_to_streamed_response_wrapper(
            beneficial_owners.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            beneficial_owners.update,
        )
        self.list = async_to_streamed_response_wrapper(
            beneficial_owners.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            beneficial_owners.archive,
        )
