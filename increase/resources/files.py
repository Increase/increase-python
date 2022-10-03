# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._utils import extract_files, maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from ..types.file import File
from .._base_client import AsyncPaginator, make_request_options
from ..types.file_list_params import FileListParams
from ..types.file_create_params import FileCreateParams

__all__ = ["Files", "AsyncFiles"]


class Files(SyncAPIResource):
    def create(
        self,
        body: FileCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> File:
        """
        To upload a file to Increase, you'll need to send a request of Content-Type
        `multipart/form-data`. The request should contain the file you would like to
        upload, as well as the parameters for creating a file.
        """
        # Make a copy of the input so that our internal mutations (extracting files)
        # don't incidentally mutate the user's dictionary.
        body = body.copy()
        files = extract_files(body, paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            headers = {"Content-Type": "multipart/form-data", **(headers or {})}

        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/files",
            body=maybe_transform(body, FileCreateParams),
            files=files,
            options=options,
            cast_to=File,
        )

    def retrieve(
        self,
        file_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> File:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/files/{file_id}",
            options=options,
            cast_to=File,
        )

    def list(
        self,
        query: FileListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[File]:
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, FileListParams))
        return self._get_api_list(
            "/files",
            page=SyncPage[File],
            options=options,
            model=File,
        )


class AsyncFiles(AsyncAPIResource):
    async def create(
        self,
        body: FileCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> File:
        """
        To upload a file to Increase, you'll need to send a request of Content-Type
        `multipart/form-data`. The request should contain the file you would like to
        upload, as well as the parameters for creating a file.
        """
        # Make a copy of the input so that our internal mutations (extracting files)
        # don't incidentally mutate the user's dictionary.
        body = body.copy()
        files = extract_files(body, paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            headers = {"Content-Type": "multipart/form-data", **(headers or {})}

        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/files",
            body=maybe_transform(body, FileCreateParams),
            files=files,
            options=options,
            cast_to=File,
        )

    async def retrieve(
        self,
        file_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> File:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/files/{file_id}",
            options=options,
            cast_to=File,
        )

    def list(
        self,
        query: FileListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[File, AsyncPage[File]]:
        options = make_request_options(headers, max_retries, timeout, maybe_transform(query, FileListParams))
        return self._get_api_list(
            "/files",
            page=AsyncPage[File],
            options=options,
            model=File,
        )
