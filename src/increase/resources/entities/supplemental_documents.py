# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...types import Entity
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.entities import supplemental_document_create_params

__all__ = ["SupplementalDocuments", "AsyncSupplementalDocuments"]


class SupplementalDocuments(SyncAPIResource):
    def create(
        self,
        entity_id: str,
        *,
        file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Create a supplemental document for an Entity

        Args:
          file_id: The identifier of the File containing the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/entities/{entity_id}/supplemental_documents",
            body=maybe_transform(
                {"file_id": file_id}, supplemental_document_create_params.SupplementalDocumentCreateParams
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


class AsyncSupplementalDocuments(AsyncAPIResource):
    async def create(
        self,
        entity_id: str,
        *,
        file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Entity:
        """
        Create a supplemental document for an Entity

        Args:
          file_id: The identifier of the File containing the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/entities/{entity_id}/supplemental_documents",
            body=maybe_transform(
                {"file_id": file_id}, supplemental_document_create_params.SupplementalDocumentCreateParams
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
