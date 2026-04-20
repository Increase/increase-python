# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import entity_list_params, entity_create_params, entity_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
        corporation: entity_create_params.Corporation | Omit = omit,
        description: str | Omit = omit,
        government_authority: entity_create_params.GovernmentAuthority | Omit = omit,
        joint: entity_create_params.Joint | Omit = omit,
        natural_person: entity_create_params.NaturalPerson | Omit = omit,
        risk_rating: entity_create_params.RiskRating | Omit = omit,
        supplemental_documents: Iterable[entity_create_params.SupplementalDocument] | Omit = omit,
        terms_agreements: Iterable[entity_create_params.TermsAgreement] | Omit = omit,
        third_party_verification: entity_create_params.ThirdPartyVerification | Omit = omit,
        trust: entity_create_params.Trust | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
              equal to `government_authority`.

          joint: Details of the joint entity to create. Required if `structure` is equal to
              `joint`.

          natural_person: Details of the natural person entity to create. Required if `structure` is equal
              to `natural_person`. Natural people entities should be submitted with
              `social_security_number` or `individual_taxpayer_identification_number`
              identification methods.

          risk_rating: An assessment of the entity's potential risk of involvement in financial crimes,
              such as money laundering.

          supplemental_documents: Additional documentation associated with the entity.

          terms_agreements: The terms that the Entity agreed to. Not all programs are required to submit
              this data.

          third_party_verification: If you are using a third-party service for identity verification, you can use
              this field to associate this Entity with the identifier that represents them in
              that service.

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
                    "risk_rating": risk_rating,
                    "supplemental_documents": supplemental_documents,
                    "terms_agreements": terms_agreements,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/entities/{entity_id}", entity_id=entity_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entity,
        )

    def update(
        self,
        entity_id: str,
        *,
        corporation: entity_update_params.Corporation | Omit = omit,
        details_confirmed_at: Union[str, datetime] | Omit = omit,
        government_authority: entity_update_params.GovernmentAuthority | Omit = omit,
        natural_person: entity_update_params.NaturalPerson | Omit = omit,
        risk_rating: entity_update_params.RiskRating | Omit = omit,
        terms_agreements: Iterable[entity_update_params.TermsAgreement] | Omit = omit,
        third_party_verification: entity_update_params.ThirdPartyVerification | Omit = omit,
        trust: entity_update_params.Trust | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Update an Entity

        Args:
          entity_id: The entity identifier.

          corporation: Details of the corporation entity to update. If you specify this parameter and
              the entity is not a corporation, the request will fail.

          details_confirmed_at: When your user last confirmed the Entity's details. Depending on your program,
              you may be required to affirmatively confirm details with your users on an
              annual basis.

          government_authority: Details of the government authority entity to update. If you specify this
              parameter and the entity is not a government authority, the request will fail.

          natural_person: Details of the natural person entity to update. If you specify this parameter
              and the entity is not a natural person, the request will fail.

          risk_rating: An assessment of the entity’s potential risk of involvement in financial crimes,
              such as money laundering.

          terms_agreements: New terms that the Entity agreed to. Not all programs are required to submit
              this data. This will not archive previously submitted terms.

          third_party_verification: If you are using a third-party service for identity verification, you can use
              this field to associate this Entity with the identifier that represents them in
              that service.

          trust: Details of the trust entity to update. If you specify this parameter and the
              entity is not a trust, the request will fail.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._patch(
            path_template("/entities/{entity_id}", entity_id=entity_id),
            body=maybe_transform(
                {
                    "corporation": corporation,
                    "details_confirmed_at": details_confirmed_at,
                    "government_authority": government_authority,
                    "natural_person": natural_person,
                    "risk_rating": risk_rating,
                    "terms_agreements": terms_agreements,
                    "third_party_verification": third_party_verification,
                    "trust": trust,
                },
                entity_update_params.EntityUpdateParams,
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

    def list(
        self,
        *,
        created_at: entity_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        status: entity_list_params.Status | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/entities/{entity_id}/archive", entity_id=entity_id),
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
        corporation: entity_create_params.Corporation | Omit = omit,
        description: str | Omit = omit,
        government_authority: entity_create_params.GovernmentAuthority | Omit = omit,
        joint: entity_create_params.Joint | Omit = omit,
        natural_person: entity_create_params.NaturalPerson | Omit = omit,
        risk_rating: entity_create_params.RiskRating | Omit = omit,
        supplemental_documents: Iterable[entity_create_params.SupplementalDocument] | Omit = omit,
        terms_agreements: Iterable[entity_create_params.TermsAgreement] | Omit = omit,
        third_party_verification: entity_create_params.ThirdPartyVerification | Omit = omit,
        trust: entity_create_params.Trust | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
              equal to `government_authority`.

          joint: Details of the joint entity to create. Required if `structure` is equal to
              `joint`.

          natural_person: Details of the natural person entity to create. Required if `structure` is equal
              to `natural_person`. Natural people entities should be submitted with
              `social_security_number` or `individual_taxpayer_identification_number`
              identification methods.

          risk_rating: An assessment of the entity's potential risk of involvement in financial crimes,
              such as money laundering.

          supplemental_documents: Additional documentation associated with the entity.

          terms_agreements: The terms that the Entity agreed to. Not all programs are required to submit
              this data.

          third_party_verification: If you are using a third-party service for identity verification, you can use
              this field to associate this Entity with the identifier that represents them in
              that service.

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
                    "risk_rating": risk_rating,
                    "supplemental_documents": supplemental_documents,
                    "terms_agreements": terms_agreements,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/entities/{entity_id}", entity_id=entity_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entity,
        )

    async def update(
        self,
        entity_id: str,
        *,
        corporation: entity_update_params.Corporation | Omit = omit,
        details_confirmed_at: Union[str, datetime] | Omit = omit,
        government_authority: entity_update_params.GovernmentAuthority | Omit = omit,
        natural_person: entity_update_params.NaturalPerson | Omit = omit,
        risk_rating: entity_update_params.RiskRating | Omit = omit,
        terms_agreements: Iterable[entity_update_params.TermsAgreement] | Omit = omit,
        third_party_verification: entity_update_params.ThirdPartyVerification | Omit = omit,
        trust: entity_update_params.Trust | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Update an Entity

        Args:
          entity_id: The entity identifier.

          corporation: Details of the corporation entity to update. If you specify this parameter and
              the entity is not a corporation, the request will fail.

          details_confirmed_at: When your user last confirmed the Entity's details. Depending on your program,
              you may be required to affirmatively confirm details with your users on an
              annual basis.

          government_authority: Details of the government authority entity to update. If you specify this
              parameter and the entity is not a government authority, the request will fail.

          natural_person: Details of the natural person entity to update. If you specify this parameter
              and the entity is not a natural person, the request will fail.

          risk_rating: An assessment of the entity’s potential risk of involvement in financial crimes,
              such as money laundering.

          terms_agreements: New terms that the Entity agreed to. Not all programs are required to submit
              this data. This will not archive previously submitted terms.

          third_party_verification: If you are using a third-party service for identity verification, you can use
              this field to associate this Entity with the identifier that represents them in
              that service.

          trust: Details of the trust entity to update. If you specify this parameter and the
              entity is not a trust, the request will fail.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._patch(
            path_template("/entities/{entity_id}", entity_id=entity_id),
            body=await async_maybe_transform(
                {
                    "corporation": corporation,
                    "details_confirmed_at": details_confirmed_at,
                    "government_authority": government_authority,
                    "natural_person": natural_person,
                    "risk_rating": risk_rating,
                    "terms_agreements": terms_agreements,
                    "third_party_verification": third_party_verification,
                    "trust": trust,
                },
                entity_update_params.EntityUpdateParams,
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

    def list(
        self,
        *,
        created_at: entity_list_params.CreatedAt | Omit = omit,
        cursor: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        limit: int | Omit = omit,
        status: entity_list_params.Status | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/entities/{entity_id}/archive", entity_id=entity_id),
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
        self.update = to_raw_response_wrapper(
            entities.update,
        )
        self.list = to_raw_response_wrapper(
            entities.list,
        )
        self.archive = to_raw_response_wrapper(
            entities.archive,
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
        self.update = async_to_raw_response_wrapper(
            entities.update,
        )
        self.list = async_to_raw_response_wrapper(
            entities.list,
        )
        self.archive = async_to_raw_response_wrapper(
            entities.archive,
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
        self.update = to_streamed_response_wrapper(
            entities.update,
        )
        self.list = to_streamed_response_wrapper(
            entities.list,
        )
        self.archive = to_streamed_response_wrapper(
            entities.archive,
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
        self.update = async_to_streamed_response_wrapper(
            entities.update,
        )
        self.list = async_to_streamed_response_wrapper(
            entities.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            entities.archive,
        )
