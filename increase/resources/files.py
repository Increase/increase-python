# File generated from our OpenAPI spec by Stainless.

from typing import Any, Dict, Union, cast

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from ..types.file import *
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
    ) -> File:
        """
        To upload a file to Increase, you'll need to send a request of Content-Type
        `multipart/form-data`. The request should contain the file you would like to
        upload, as well as the parameters for creating a file.
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        headers = {"Content-Type": "multipart/form-data", **(headers or {})}

        # This cast is required because otherwise mypy will complain
        # about a Required key being deleted from a TypedDict.
        files = {"file": cast(Dict[str, object], body).pop("file")}
        options = make_request_options(headers, max_retries, timeout)
        # The cast to Any is required because of https://github.com/microsoft/pyright/issues/3526
        return self._post(
            "/files",
            body=body,
            files=cast(Any, files),
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
    ) -> File:
        options = make_request_options(headers, max_retries, timeout)
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
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/files",
            page=SyncPage[File],
            query=query,
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
    ) -> File:
        """
        To upload a file to Increase, you'll need to send a request of Content-Type
        `multipart/form-data`. The request should contain the file you would like to
        upload, as well as the parameters for creating a file.
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        headers = {"Content-Type": "multipart/form-data", **(headers or {})}

        # This cast is required because otherwise mypy will complain
        # about a Required key being deleted from a TypedDict.
        files = {"file": cast(Dict[str, object], body).pop("file")}
        options = make_request_options(headers, max_retries, timeout)
        # The cast to Any is required because of https://github.com/microsoft/pyright/issues/3526
        return await self._post(
            "/files",
            body=body,
            files=cast(Any, files),
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
    ) -> File:
        options = make_request_options(headers, max_retries, timeout)
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
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/files",
            page=AsyncPage[File],
            query=query,
            options=options,
            model=File,
        )
