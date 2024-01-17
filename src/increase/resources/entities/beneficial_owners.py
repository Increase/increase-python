# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ...types import Entity
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.entities import (
    beneficial_owner_create_params,
    beneficial_owner_archive_params,
    beneficial_owner_update_address_params,
)

__all__ = ["BeneficialOwners", "AsyncBeneficialOwners"]


class BeneficialOwners(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BeneficialOwnersWithRawResponse:
        return BeneficialOwnersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BeneficialOwnersWithStreamingResponse:
        return BeneficialOwnersWithStreamingResponse(self)

    def create(
        self,
        *,
        beneficial_owner: beneficial_owner_create_params.BeneficialOwner,
        entity_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Create a beneficial owner for a corporate Entity

        Args:
          beneficial_owner: The identifying details of anyone controlling or owning 25% or more of the
              corporation.

          entity_id: The identifier of the Entity to associate with the new Beneficial Owner.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/entity_beneficial_owners",
            body=maybe_transform(
                {
                    "beneficial_owner": beneficial_owner,
                    "entity_id": entity_id,
                },
                beneficial_owner_create_params.BeneficialOwnerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Entity,
        )

    def archive(
        self,
        *,
        beneficial_owner_id: str,
        entity_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Archive a beneficial owner for a corporate Entity

        Args:
          beneficial_owner_id: The identifying details of anyone controlling or owning 25% or more of the
              corporation.

          entity_id: The identifier of the Entity to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/entity_beneficial_owners/archive",
            body=maybe_transform(
                {
                    "beneficial_owner_id": beneficial_owner_id,
                    "entity_id": entity_id,
                },
                beneficial_owner_archive_params.BeneficialOwnerArchiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Entity,
        )

    def update_address(
        self,
        *,
        address: beneficial_owner_update_address_params.Address,
        beneficial_owner_id: str,
        entity_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Update the address for a beneficial owner belonging to a corporate Entity

        Args:
          address: The individual's physical address. Mail receiving locations like PO Boxes and
              PMB's are disallowed.

          beneficial_owner_id: The identifying details of anyone controlling or owning 25% or more of the
              corporation.

          entity_id: The identifier of the Entity to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/entity_beneficial_owners/address",
            body=maybe_transform(
                {
                    "address": address,
                    "beneficial_owner_id": beneficial_owner_id,
                    "entity_id": entity_id,
                },
                beneficial_owner_update_address_params.BeneficialOwnerUpdateAddressParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Entity,
        )


class AsyncBeneficialOwners(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBeneficialOwnersWithRawResponse:
        return AsyncBeneficialOwnersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBeneficialOwnersWithStreamingResponse:
        return AsyncBeneficialOwnersWithStreamingResponse(self)

    async def create(
        self,
        *,
        beneficial_owner: beneficial_owner_create_params.BeneficialOwner,
        entity_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Create a beneficial owner for a corporate Entity

        Args:
          beneficial_owner: The identifying details of anyone controlling or owning 25% or more of the
              corporation.

          entity_id: The identifier of the Entity to associate with the new Beneficial Owner.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/entity_beneficial_owners",
            body=maybe_transform(
                {
                    "beneficial_owner": beneficial_owner,
                    "entity_id": entity_id,
                },
                beneficial_owner_create_params.BeneficialOwnerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Entity,
        )

    async def archive(
        self,
        *,
        beneficial_owner_id: str,
        entity_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Archive a beneficial owner for a corporate Entity

        Args:
          beneficial_owner_id: The identifying details of anyone controlling or owning 25% or more of the
              corporation.

          entity_id: The identifier of the Entity to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/entity_beneficial_owners/archive",
            body=maybe_transform(
                {
                    "beneficial_owner_id": beneficial_owner_id,
                    "entity_id": entity_id,
                },
                beneficial_owner_archive_params.BeneficialOwnerArchiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Entity,
        )

    async def update_address(
        self,
        *,
        address: beneficial_owner_update_address_params.Address,
        beneficial_owner_id: str,
        entity_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Update the address for a beneficial owner belonging to a corporate Entity

        Args:
          address: The individual's physical address. Mail receiving locations like PO Boxes and
              PMB's are disallowed.

          beneficial_owner_id: The identifying details of anyone controlling or owning 25% or more of the
              corporation.

          entity_id: The identifier of the Entity to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/entity_beneficial_owners/address",
            body=maybe_transform(
                {
                    "address": address,
                    "beneficial_owner_id": beneficial_owner_id,
                    "entity_id": entity_id,
                },
                beneficial_owner_update_address_params.BeneficialOwnerUpdateAddressParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Entity,
        )


class BeneficialOwnersWithRawResponse:
    def __init__(self, beneficial_owners: BeneficialOwners) -> None:
        self._beneficial_owners = beneficial_owners

        self.create = _legacy_response.to_raw_response_wrapper(
            beneficial_owners.create,
        )
        self.archive = _legacy_response.to_raw_response_wrapper(
            beneficial_owners.archive,
        )
        self.update_address = _legacy_response.to_raw_response_wrapper(
            beneficial_owners.update_address,
        )


class AsyncBeneficialOwnersWithRawResponse:
    def __init__(self, beneficial_owners: AsyncBeneficialOwners) -> None:
        self._beneficial_owners = beneficial_owners

        self.create = _legacy_response.async_to_raw_response_wrapper(
            beneficial_owners.create,
        )
        self.archive = _legacy_response.async_to_raw_response_wrapper(
            beneficial_owners.archive,
        )
        self.update_address = _legacy_response.async_to_raw_response_wrapper(
            beneficial_owners.update_address,
        )


class BeneficialOwnersWithStreamingResponse:
    def __init__(self, beneficial_owners: BeneficialOwners) -> None:
        self._beneficial_owners = beneficial_owners

        self.create = to_streamed_response_wrapper(
            beneficial_owners.create,
        )
        self.archive = to_streamed_response_wrapper(
            beneficial_owners.archive,
        )
        self.update_address = to_streamed_response_wrapper(
            beneficial_owners.update_address,
        )


class AsyncBeneficialOwnersWithStreamingResponse:
    def __init__(self, beneficial_owners: AsyncBeneficialOwners) -> None:
        self._beneficial_owners = beneficial_owners

        self.create = async_to_streamed_response_wrapper(
            beneficial_owners.create,
        )
        self.archive = async_to_streamed_response_wrapper(
            beneficial_owners.archive,
        )
        self.update_address = async_to_streamed_response_wrapper(
            beneficial_owners.update_address,
        )
