# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

from ..types import file_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import extract_files, deepcopy_minimal
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from ..types.file import File
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["Files", "AsyncFiles"]


class Files(SyncAPIResource):
    def create(
        self,
        *,
        file: FileTypes,
        description: str | NotGiven = NOT_GIVEN,
        purpose: Literal[
            "check_image_front",
            "check_image_back",
            "form_ss_4",
            "identity_document",
            "other",
            "trust_formation_document",
            "digital_wallet_artwork",
            "digital_wallet_app_icon",
            "entity_supplemental_document",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> File:
        """
        To upload a file to Increase, you'll need to send a request of Content-Type
        `multipart/form-data`. The request should contain the file you would like to
        upload, as well as the parameters for creating a file.

        Args:
          file: The file contents. This should follow the specifications of
              [RFC 7578](https://datatracker.ietf.org/doc/html/rfc7578) which defines file
              transfers for the multipart/form-data protocol.

          description: The description you choose to give the File.

          purpose: What the File will be used for in Increase's systems.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "description": description,
                "purpose": purpose,
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
            body=body,
            files=files,
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> File:
        return self._get(
            f"/files/{file_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=File,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        created_at: file_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        purpose: file_list_params.Purpose | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[File]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/files",
            page=SyncPage[File],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                    "created_at": created_at,
                    "purpose": purpose,
                },
            ),
            model=File,
        )


class AsyncFiles(AsyncAPIResource):
    async def create(
        self,
        *,
        file: FileTypes,
        description: str | NotGiven = NOT_GIVEN,
        purpose: Literal[
            "check_image_front",
            "check_image_back",
            "form_ss_4",
            "identity_document",
            "other",
            "trust_formation_document",
            "digital_wallet_artwork",
            "digital_wallet_app_icon",
            "entity_supplemental_document",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> File:
        """
        To upload a file to Increase, you'll need to send a request of Content-Type
        `multipart/form-data`. The request should contain the file you would like to
        upload, as well as the parameters for creating a file.

        Args:
          file: The file contents. This should follow the specifications of
              [RFC 7578](https://datatracker.ietf.org/doc/html/rfc7578) which defines file
              transfers for the multipart/form-data protocol.

          description: The description you choose to give the File.

          purpose: What the File will be used for in Increase's systems.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "description": description,
                "purpose": purpose,
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
            body=body,
            files=files,
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> File:
        return await self._get(
            f"/files/{file_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=File,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        created_at: file_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        purpose: file_list_params.Purpose | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[File, AsyncPage[File]]:
        """
        Args:
          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/files",
            page=AsyncPage[File],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "cursor": cursor,
                    "limit": limit,
                    "created_at": created_at,
                    "purpose": purpose,
                },
            ),
            model=File,
        )
