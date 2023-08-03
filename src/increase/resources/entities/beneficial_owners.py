# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...types import Entity
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.entities import beneficial_owner_create_params

__all__ = ["BeneficialOwners", "AsyncBeneficialOwners"]


class BeneficialOwners(SyncAPIResource):
    def create(
        self,
        entity_id: str,
        *,
        beneficial_owner: beneficial_owner_create_params.BeneficialOwner,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Create a beneficial owner for a corporate Entity

        Args:
          entity_id: The identifier of the Entity to retrieve.

          beneficial_owner: The identifying details of anyone controlling or owning 25% or more of the
              corporation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/entities/{entity_id}/beneficial_owners",
            body=maybe_transform(
                {"beneficial_owner": beneficial_owner}, beneficial_owner_create_params.BeneficialOwnerCreateParams
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
    async def create(
        self,
        entity_id: str,
        *,
        beneficial_owner: beneficial_owner_create_params.BeneficialOwner,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Create a beneficial owner for a corporate Entity

        Args:
          entity_id: The identifier of the Entity to retrieve.

          beneficial_owner: The identifying details of anyone controlling or owning 25% or more of the
              corporation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/entities/{entity_id}/beneficial_owners",
            body=maybe_transform(
                {"beneficial_owner": beneficial_owner}, beneficial_owner_create_params.BeneficialOwnerCreateParams
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
