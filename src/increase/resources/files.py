# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

from ..types import File, file_list_params, file_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import extract_files, maybe_transform, deepcopy_minimal
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["Files", "AsyncFiles"]


class Files(SyncAPIResource):
    def create(
        self,
        *,
        file: FileTypes,
        purpose: Literal[
            "check_image_front",
            "check_image_back",
            "form_ss_4",
            "identity_document",
            "other",
            "trust_formation_document",
            "digital_wallet_artwork",
            "digital_wallet_app_icon",
            "physical_card_front",
            "physical_card_carrier",
            "document_request",
            "entity_supplemental_document",
        ],
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> File:
        """
        To upload a file to Increase, you'll need to send a request of Content-Type
        `multipart/form-data`. The request should contain the file you would like to
        upload, as well as the parameters for creating a file.

        Args:
          file: The file contents. This should follow the specifications of
              [RFC 7578](https://datatracker.ietf.org/doc/html/rfc7578) which defines file
              transfers for the multipart/form-data protocol.

          purpose: What the File will be used for in Increase's systems.

              - `check_image_front` - An image of the front of a check, used for check
                deposits.
              - `check_image_back` - An image of the back of a check, used for check deposits.
              - `form_ss_4` - IRS Form SS-4.
              - `identity_document` - An image of a government-issued ID.
              - `other` - A file purpose not covered by any of the other cases.
              - `trust_formation_document` - A legal document forming a trust.
              - `digital_wallet_artwork` - A card image to be rendered inside digital wallet
                apps. This must be a 1536x969 pixel PNG.
              - `digital_wallet_app_icon` - An icon for you app to be rendered inside digital
                wallet apps. This must be a 100x100 pixel PNG.
              - `physical_card_front` - A card image to be printed on the front of a physical
                card. This must be a 2100x1340 pixel PNG with no other color but black.
              - `physical_card_carrier` - An image representing the entirety of the carrier
                used for a physical card. This must be a 2550x3300 pixel PNG with no other
                color but black.
              - `document_request` - A document requested by Increase.
              - `entity_supplemental_document` - A supplemental document associated an an
                Entity.

          description: The description you choose to give the File.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "purpose": purpose,
                "description": description,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}

        return self._post(
            "/files",
            body=maybe_transform(body, file_create_params.FileCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=File,
        )

    def retrieve(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> File:
        """
        Retrieve a File

        Args:
          file_id: The identifier of the File.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    def list(
        self,
        *,
        created_at: file_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        purpose: file_list_params.Purpose | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[File]:
        """
        List Files

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
            "/files",
            page=SyncPage[File],
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
                        "purpose": purpose,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            model=File,
        )


class AsyncFiles(AsyncAPIResource):
    async def create(
        self,
        *,
        file: FileTypes,
        purpose: Literal[
            "check_image_front",
            "check_image_back",
            "form_ss_4",
            "identity_document",
            "other",
            "trust_formation_document",
            "digital_wallet_artwork",
            "digital_wallet_app_icon",
            "physical_card_front",
            "physical_card_carrier",
            "document_request",
            "entity_supplemental_document",
        ],
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> File:
        """
        To upload a file to Increase, you'll need to send a request of Content-Type
        `multipart/form-data`. The request should contain the file you would like to
        upload, as well as the parameters for creating a file.

        Args:
          file: The file contents. This should follow the specifications of
              [RFC 7578](https://datatracker.ietf.org/doc/html/rfc7578) which defines file
              transfers for the multipart/form-data protocol.

          purpose: What the File will be used for in Increase's systems.

              - `check_image_front` - An image of the front of a check, used for check
                deposits.
              - `check_image_back` - An image of the back of a check, used for check deposits.
              - `form_ss_4` - IRS Form SS-4.
              - `identity_document` - An image of a government-issued ID.
              - `other` - A file purpose not covered by any of the other cases.
              - `trust_formation_document` - A legal document forming a trust.
              - `digital_wallet_artwork` - A card image to be rendered inside digital wallet
                apps. This must be a 1536x969 pixel PNG.
              - `digital_wallet_app_icon` - An icon for you app to be rendered inside digital
                wallet apps. This must be a 100x100 pixel PNG.
              - `physical_card_front` - A card image to be printed on the front of a physical
                card. This must be a 2100x1340 pixel PNG with no other color but black.
              - `physical_card_carrier` - An image representing the entirety of the carrier
                used for a physical card. This must be a 2550x3300 pixel PNG with no other
                color but black.
              - `document_request` - A document requested by Increase.
              - `entity_supplemental_document` - A supplemental document associated an an
                Entity.

          description: The description you choose to give the File.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "purpose": purpose,
                "description": description,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}

        return await self._post(
            "/files",
            body=maybe_transform(body, file_create_params.FileCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=File,
        )

    async def retrieve(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> File:
        """
        Retrieve a File

        Args:
          file_id: The identifier of the File.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    def list(
        self,
        *,
        created_at: file_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        purpose: file_list_params.Purpose | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[File, AsyncPage[File]]:
        """
        List Files

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
            "/files",
            page=AsyncPage[File],
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
                        "purpose": purpose,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            model=File,
        )
