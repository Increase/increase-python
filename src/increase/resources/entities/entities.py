# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List
from typing_extensions import Literal

from ...types import (
    Entity,
    entity_list_params,
    entity_create_params,
    entity_update_address_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from .beneficial_owners import BeneficialOwners, AsyncBeneficialOwners
from .supplemental_documents import SupplementalDocuments, AsyncSupplementalDocuments

if TYPE_CHECKING:
    from ..._client import Increase, AsyncIncrease

__all__ = ["Entities", "AsyncEntities"]


class Entities(SyncAPIResource):
    beneficial_owners: BeneficialOwners
    supplemental_documents: SupplementalDocuments

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.beneficial_owners = BeneficialOwners(client)
        self.supplemental_documents = SupplementalDocuments(client)

    def create(
        self,
        *,
        structure: Literal["corporation", "natural_person", "joint", "trust"],
        corporation: entity_create_params.Corporation | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        joint: entity_create_params.Joint | NotGiven = NOT_GIVEN,
        natural_person: entity_create_params.NaturalPerson | NotGiven = NOT_GIVEN,
        relationship: Literal["affiliated", "informational", "unaffiliated"] | NotGiven = NOT_GIVEN,
        supplemental_documents: List[entity_create_params.SupplementalDocument] | NotGiven = NOT_GIVEN,
        trust: entity_create_params.Trust | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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

          corporation: Details of the corporation entity to create. Required if `structure` is equal to
              `corporation`.

          description: The description you choose to give the entity.

          joint: Details of the joint entity to create. Required if `structure` is equal to
              `joint`.

          natural_person: Details of the natural person entity to create. Required if `structure` is equal
              to `natural_person`. Natural people entities should be submitted with
              `social_security_number` or `individual_taxpayer_identification_number`
              identification methods.

          relationship: The relationship between your group and the entity.

              - `affiliated` - The entity is controlled by your group.
              - `informational` - The entity is for informational purposes only.
              - `unaffiliated` - The entity is not controlled by your group, but can still
                directly open accounts.

          supplemental_documents: Additional documentation associated with the entity.

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
                    "joint": joint,
                    "natural_person": natural_person,
                    "relationship": relationship,
                    "supplemental_documents": supplemental_documents,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Entity]:
        """
        List Entities

        Args:
          cursor: Return the page of entries after this one.

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
                        "limit": limit,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Update a Natural Person or Corporation's address

        Args:
          entity_id: The identifier of the Entity to archive.

          address: The entity's physical address. Post Office Boxes are disallowed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/entities/{entity_id}/address",
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


class AsyncEntities(AsyncAPIResource):
    beneficial_owners: AsyncBeneficialOwners
    supplemental_documents: AsyncSupplementalDocuments

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.beneficial_owners = AsyncBeneficialOwners(client)
        self.supplemental_documents = AsyncSupplementalDocuments(client)

    async def create(
        self,
        *,
        structure: Literal["corporation", "natural_person", "joint", "trust"],
        corporation: entity_create_params.Corporation | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        joint: entity_create_params.Joint | NotGiven = NOT_GIVEN,
        natural_person: entity_create_params.NaturalPerson | NotGiven = NOT_GIVEN,
        relationship: Literal["affiliated", "informational", "unaffiliated"] | NotGiven = NOT_GIVEN,
        supplemental_documents: List[entity_create_params.SupplementalDocument] | NotGiven = NOT_GIVEN,
        trust: entity_create_params.Trust | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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

          corporation: Details of the corporation entity to create. Required if `structure` is equal to
              `corporation`.

          description: The description you choose to give the entity.

          joint: Details of the joint entity to create. Required if `structure` is equal to
              `joint`.

          natural_person: Details of the natural person entity to create. Required if `structure` is equal
              to `natural_person`. Natural people entities should be submitted with
              `social_security_number` or `individual_taxpayer_identification_number`
              identification methods.

          relationship: The relationship between your group and the entity.

              - `affiliated` - The entity is controlled by your group.
              - `informational` - The entity is for informational purposes only.
              - `unaffiliated` - The entity is not controlled by your group, but can still
                directly open accounts.

          supplemental_documents: Additional documentation associated with the entity.

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
            body=maybe_transform(
                {
                    "structure": structure,
                    "corporation": corporation,
                    "description": description,
                    "joint": joint,
                    "natural_person": natural_person,
                    "relationship": relationship,
                    "supplemental_documents": supplemental_documents,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Entity, AsyncPage[Entity]]:
        """
        List Entities

        Args:
          cursor: Return the page of entries after this one.

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
                        "limit": limit,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Update a Natural Person or Corporation's address

        Args:
          entity_id: The identifier of the Entity to archive.

          address: The entity's physical address. Post Office Boxes are disallowed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/entities/{entity_id}/address",
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
