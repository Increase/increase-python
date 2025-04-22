# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    entity_list_params,
    entity_create_params,
    entity_confirm_params,
    entity_update_address_params,
    entity_update_industry_code_params,
    entity_create_beneficial_owner_params,
    entity_archive_beneficial_owner_params,
    entity_update_beneficial_owner_address_params,
)
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
from ..types.entity import Entity

__all__ = ["EntitiesResource", "AsyncEntitiesResource"]


class EntitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return EntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return EntitiesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        structure: Literal["corporation", "natural_person", "joint", "trust", "government_authority"],
        corporation: entity_create_params.Corporation | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        government_authority: entity_create_params.GovernmentAuthority | NotGiven = NOT_GIVEN,
        joint: entity_create_params.Joint | NotGiven = NOT_GIVEN,
        natural_person: entity_create_params.NaturalPerson | NotGiven = NOT_GIVEN,
        supplemental_documents: Iterable[entity_create_params.SupplementalDocument] | NotGiven = NOT_GIVEN,
        third_party_verification: entity_create_params.ThirdPartyVerification | NotGiven = NOT_GIVEN,
        trust: entity_create_params.Trust | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Create an Entity

        Args:
          structure: The type of Entity to create.

              - `corporation` - A corporation.
              - `natural_person` - An individual person.
              - `joint` - Multiple individual people.
              - `trust` - A trust.
              - `government_authority` - A government authority.

          corporation: Details of the corporation entity to create. Required if `structure` is equal to
              `corporation`.

          description: The description you choose to give the entity.

          government_authority: Details of the Government Authority entity to create. Required if `structure` is
              equal to `Government Authority`.

          joint: Details of the joint entity to create. Required if `structure` is equal to
              `joint`.

          natural_person: Details of the natural person entity to create. Required if `structure` is equal
              to `natural_person`. Natural people entities should be submitted with
              `social_security_number` or `individual_taxpayer_identification_number`
              identification methods.

          supplemental_documents: Additional documentation associated with the entity.

          third_party_verification: A reference to data stored in a third-party verification service. Your
              integration may or may not use this field.

          trust: Details of the trust entity to create. Required if `structure` is equal to
              `trust`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/entities",
            body=maybe_transform(
                {
                    "structure": structure,
                    "corporation": corporation,
                    "description": description,
                    "government_authority": government_authority,
                    "joint": joint,
                    "natural_person": natural_person,
                    "supplemental_documents": supplemental_documents,
                    "third_party_verification": third_party_verification,
                    "trust": trust,
                },
                entity_create_params.EntityCreateParams,
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

    def retrieve(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Entity:
        """
        Retrieve an Entity

        Args:
          entity_id: The identifier of the Entity to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._get(
            f"/entities/{entity_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entity,
        )

    def list(
        self,
        *,
        created_at: entity_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: entity_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Entity]:
        """
        List Entities

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
            "/entities",
            page=SyncPage[Entity],
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
                    entity_list_params.EntityListParams,
                ),
            ),
            model=Entity,
        )

    def archive(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """Archive an Entity

        Args:
          entity_id: The identifier of the Entity to archive.

        Any accounts associated with an entity
              must be closed before the entity can be archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._post(
            f"/entities/{entity_id}/archive",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Entity,
        )

    def archive_beneficial_owner(
        self,
        entity_id: str,
        *,
        beneficial_owner_id: str,
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
          entity_id: The identifier of the Entity associated with the Beneficial Owner that is being
              archived.

          beneficial_owner_id: The identifying details of anyone controlling or owning 25% or more of the
              corporation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._post(
            f"/entities/{entity_id}/archive_beneficial_owner",
            body=maybe_transform(
                {"beneficial_owner_id": beneficial_owner_id},
                entity_archive_beneficial_owner_params.EntityArchiveBeneficialOwnerParams,
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

    def confirm(
        self,
        entity_id: str,
        *,
        confirmed_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Depending on your program, you may be required to re-confirm an Entity's details
        on a recurring basis. After making any required updates, call this endpoint to
        record that your user confirmed their details.

        Args:
          entity_id: The identifier of the Entity to confirm the details of.

          confirmed_at: When your user confirmed the Entity's details. If not provided, the current time
              will be used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._post(
            f"/entities/{entity_id}/confirm",
            body=maybe_transform({"confirmed_at": confirmed_at}, entity_confirm_params.EntityConfirmParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Entity,
        )

    def create_beneficial_owner(
        self,
        entity_id: str,
        *,
        beneficial_owner: entity_create_beneficial_owner_params.BeneficialOwner,
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
          entity_id: The identifier of the Entity to associate with the new Beneficial Owner.

          beneficial_owner: The identifying details of anyone controlling or owning 25% or more of the
              corporation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._post(
            f"/entities/{entity_id}/create_beneficial_owner",
            body=maybe_transform(
                {"beneficial_owner": beneficial_owner},
                entity_create_beneficial_owner_params.EntityCreateBeneficialOwnerParams,
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
        entity_id: str,
        *,
        address: entity_update_address_params.Address,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Update a Natural Person or Corporation's address

        Args:
          entity_id: The identifier of the Entity whose address is being updated.

          address: The entity's physical address. Mail receiving locations like PO Boxes and PMB's
              are disallowed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._post(
            f"/entities/{entity_id}/update_address",
            body=maybe_transform({"address": address}, entity_update_address_params.EntityUpdateAddressParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Entity,
        )

    def update_beneficial_owner_address(
        self,
        entity_id: str,
        *,
        address: entity_update_beneficial_owner_address_params.Address,
        beneficial_owner_id: str,
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
          entity_id: The identifier of the Entity associated with the Beneficial Owner whose address
              is being updated.

          address: The individual's physical address. Mail receiving locations like PO Boxes and
              PMB's are disallowed.

          beneficial_owner_id: The identifying details of anyone controlling or owning 25% or more of the
              corporation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._post(
            f"/entities/{entity_id}/update_beneficial_owner_address",
            body=maybe_transform(
                {
                    "address": address,
                    "beneficial_owner_id": beneficial_owner_id,
                },
                entity_update_beneficial_owner_address_params.EntityUpdateBeneficialOwnerAddressParams,
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

    def update_industry_code(
        self,
        entity_id: str,
        *,
        industry_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Update the industry code for a corporate Entity

        Args:
          entity_id: The identifier of the Entity to update. This endpoint only accepts `corporation`
              entities.

          industry_code: The North American Industry Classification System (NAICS) code for the
              corporation's primary line of business. This is a number, like `5132` for
              `Software Publishers`. A full list of classification codes is available
              [here](https://increase.com/documentation/data-dictionary#north-american-industry-classification-system-codes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._post(
            f"/entities/{entity_id}/update_industry_code",
            body=maybe_transform(
                {"industry_code": industry_code}, entity_update_industry_code_params.EntityUpdateIndustryCodeParams
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


class AsyncEntitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncEntitiesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        structure: Literal["corporation", "natural_person", "joint", "trust", "government_authority"],
        corporation: entity_create_params.Corporation | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        government_authority: entity_create_params.GovernmentAuthority | NotGiven = NOT_GIVEN,
        joint: entity_create_params.Joint | NotGiven = NOT_GIVEN,
        natural_person: entity_create_params.NaturalPerson | NotGiven = NOT_GIVEN,
        supplemental_documents: Iterable[entity_create_params.SupplementalDocument] | NotGiven = NOT_GIVEN,
        third_party_verification: entity_create_params.ThirdPartyVerification | NotGiven = NOT_GIVEN,
        trust: entity_create_params.Trust | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Create an Entity

        Args:
          structure: The type of Entity to create.

              - `corporation` - A corporation.
              - `natural_person` - An individual person.
              - `joint` - Multiple individual people.
              - `trust` - A trust.
              - `government_authority` - A government authority.

          corporation: Details of the corporation entity to create. Required if `structure` is equal to
              `corporation`.

          description: The description you choose to give the entity.

          government_authority: Details of the Government Authority entity to create. Required if `structure` is
              equal to `Government Authority`.

          joint: Details of the joint entity to create. Required if `structure` is equal to
              `joint`.

          natural_person: Details of the natural person entity to create. Required if `structure` is equal
              to `natural_person`. Natural people entities should be submitted with
              `social_security_number` or `individual_taxpayer_identification_number`
              identification methods.

          supplemental_documents: Additional documentation associated with the entity.

          third_party_verification: A reference to data stored in a third-party verification service. Your
              integration may or may not use this field.

          trust: Details of the trust entity to create. Required if `structure` is equal to
              `trust`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/entities",
            body=await async_maybe_transform(
                {
                    "structure": structure,
                    "corporation": corporation,
                    "description": description,
                    "government_authority": government_authority,
                    "joint": joint,
                    "natural_person": natural_person,
                    "supplemental_documents": supplemental_documents,
                    "third_party_verification": third_party_verification,
                    "trust": trust,
                },
                entity_create_params.EntityCreateParams,
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

    async def retrieve(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Entity:
        """
        Retrieve an Entity

        Args:
          entity_id: The identifier of the Entity to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._get(
            f"/entities/{entity_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entity,
        )

    def list(
        self,
        *,
        created_at: entity_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: entity_list_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Entity, AsyncPage[Entity]]:
        """
        List Entities

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
            "/entities",
            page=AsyncPage[Entity],
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
                    entity_list_params.EntityListParams,
                ),
            ),
            model=Entity,
        )

    async def archive(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """Archive an Entity

        Args:
          entity_id: The identifier of the Entity to archive.

        Any accounts associated with an entity
              must be closed before the entity can be archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._post(
            f"/entities/{entity_id}/archive",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Entity,
        )

    async def archive_beneficial_owner(
        self,
        entity_id: str,
        *,
        beneficial_owner_id: str,
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
          entity_id: The identifier of the Entity associated with the Beneficial Owner that is being
              archived.

          beneficial_owner_id: The identifying details of anyone controlling or owning 25% or more of the
              corporation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._post(
            f"/entities/{entity_id}/archive_beneficial_owner",
            body=await async_maybe_transform(
                {"beneficial_owner_id": beneficial_owner_id},
                entity_archive_beneficial_owner_params.EntityArchiveBeneficialOwnerParams,
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

    async def confirm(
        self,
        entity_id: str,
        *,
        confirmed_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Depending on your program, you may be required to re-confirm an Entity's details
        on a recurring basis. After making any required updates, call this endpoint to
        record that your user confirmed their details.

        Args:
          entity_id: The identifier of the Entity to confirm the details of.

          confirmed_at: When your user confirmed the Entity's details. If not provided, the current time
              will be used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._post(
            f"/entities/{entity_id}/confirm",
            body=await async_maybe_transform({"confirmed_at": confirmed_at}, entity_confirm_params.EntityConfirmParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Entity,
        )

    async def create_beneficial_owner(
        self,
        entity_id: str,
        *,
        beneficial_owner: entity_create_beneficial_owner_params.BeneficialOwner,
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
          entity_id: The identifier of the Entity to associate with the new Beneficial Owner.

          beneficial_owner: The identifying details of anyone controlling or owning 25% or more of the
              corporation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._post(
            f"/entities/{entity_id}/create_beneficial_owner",
            body=await async_maybe_transform(
                {"beneficial_owner": beneficial_owner},
                entity_create_beneficial_owner_params.EntityCreateBeneficialOwnerParams,
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
        entity_id: str,
        *,
        address: entity_update_address_params.Address,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Update a Natural Person or Corporation's address

        Args:
          entity_id: The identifier of the Entity whose address is being updated.

          address: The entity's physical address. Mail receiving locations like PO Boxes and PMB's
              are disallowed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._post(
            f"/entities/{entity_id}/update_address",
            body=await async_maybe_transform(
                {"address": address}, entity_update_address_params.EntityUpdateAddressParams
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

    async def update_beneficial_owner_address(
        self,
        entity_id: str,
        *,
        address: entity_update_beneficial_owner_address_params.Address,
        beneficial_owner_id: str,
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
          entity_id: The identifier of the Entity associated with the Beneficial Owner whose address
              is being updated.

          address: The individual's physical address. Mail receiving locations like PO Boxes and
              PMB's are disallowed.

          beneficial_owner_id: The identifying details of anyone controlling or owning 25% or more of the
              corporation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._post(
            f"/entities/{entity_id}/update_beneficial_owner_address",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "beneficial_owner_id": beneficial_owner_id,
                },
                entity_update_beneficial_owner_address_params.EntityUpdateBeneficialOwnerAddressParams,
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

    async def update_industry_code(
        self,
        entity_id: str,
        *,
        industry_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Update the industry code for a corporate Entity

        Args:
          entity_id: The identifier of the Entity to update. This endpoint only accepts `corporation`
              entities.

          industry_code: The North American Industry Classification System (NAICS) code for the
              corporation's primary line of business. This is a number, like `5132` for
              `Software Publishers`. A full list of classification codes is available
              [here](https://increase.com/documentation/data-dictionary#north-american-industry-classification-system-codes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._post(
            f"/entities/{entity_id}/update_industry_code",
            body=await async_maybe_transform(
                {"industry_code": industry_code}, entity_update_industry_code_params.EntityUpdateIndustryCodeParams
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


class EntitiesResourceWithRawResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.create = to_raw_response_wrapper(
            entities.create,
        )
        self.retrieve = to_raw_response_wrapper(
            entities.retrieve,
        )
        self.list = to_raw_response_wrapper(
            entities.list,
        )
        self.archive = to_raw_response_wrapper(
            entities.archive,
        )
        self.archive_beneficial_owner = to_raw_response_wrapper(
            entities.archive_beneficial_owner,
        )
        self.confirm = to_raw_response_wrapper(
            entities.confirm,
        )
        self.create_beneficial_owner = to_raw_response_wrapper(
            entities.create_beneficial_owner,
        )
        self.update_address = to_raw_response_wrapper(
            entities.update_address,
        )
        self.update_beneficial_owner_address = to_raw_response_wrapper(
            entities.update_beneficial_owner_address,
        )
        self.update_industry_code = to_raw_response_wrapper(
            entities.update_industry_code,
        )


class AsyncEntitiesResourceWithRawResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.create = async_to_raw_response_wrapper(
            entities.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            entities.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            entities.list,
        )
        self.archive = async_to_raw_response_wrapper(
            entities.archive,
        )
        self.archive_beneficial_owner = async_to_raw_response_wrapper(
            entities.archive_beneficial_owner,
        )
        self.confirm = async_to_raw_response_wrapper(
            entities.confirm,
        )
        self.create_beneficial_owner = async_to_raw_response_wrapper(
            entities.create_beneficial_owner,
        )
        self.update_address = async_to_raw_response_wrapper(
            entities.update_address,
        )
        self.update_beneficial_owner_address = async_to_raw_response_wrapper(
            entities.update_beneficial_owner_address,
        )
        self.update_industry_code = async_to_raw_response_wrapper(
            entities.update_industry_code,
        )


class EntitiesResourceWithStreamingResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.create = to_streamed_response_wrapper(
            entities.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            entities.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            entities.list,
        )
        self.archive = to_streamed_response_wrapper(
            entities.archive,
        )
        self.archive_beneficial_owner = to_streamed_response_wrapper(
            entities.archive_beneficial_owner,
        )
        self.confirm = to_streamed_response_wrapper(
            entities.confirm,
        )
        self.create_beneficial_owner = to_streamed_response_wrapper(
            entities.create_beneficial_owner,
        )
        self.update_address = to_streamed_response_wrapper(
            entities.update_address,
        )
        self.update_beneficial_owner_address = to_streamed_response_wrapper(
            entities.update_beneficial_owner_address,
        )
        self.update_industry_code = to_streamed_response_wrapper(
            entities.update_industry_code,
        )


class AsyncEntitiesResourceWithStreamingResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.create = async_to_streamed_response_wrapper(
            entities.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            entities.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            entities.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            entities.archive,
        )
        self.archive_beneficial_owner = async_to_streamed_response_wrapper(
            entities.archive_beneficial_owner,
        )
        self.confirm = async_to_streamed_response_wrapper(
            entities.confirm,
        )
        self.create_beneficial_owner = async_to_streamed_response_wrapper(
            entities.create_beneficial_owner,
        )
        self.update_address = async_to_streamed_response_wrapper(
            entities.update_address,
        )
        self.update_beneficial_owner_address = async_to_streamed_response_wrapper(
            entities.update_beneficial_owner_address,
        )
        self.update_industry_code = async_to_streamed_response_wrapper(
            entities.update_industry_code,
        )
