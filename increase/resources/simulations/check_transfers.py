# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Union, Optional

from ..._types import NOT_GIVEN, Body, Query, Headers, Timeout, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations.check_transfer import CheckTransfer

__all__ = ["CheckTransfers", "AsyncCheckTransfers"]


class CheckTransfers(SyncAPIResource):
    def mail(
        self,
        check_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CheckTransfer:
        """Simulates the mailing of a Check Transfer.

        This transfer must first have a
        `status` of `pending_approval` or `pending_submission`.
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._post(
            f"/simulations/check_transfers/{check_transfer_id}/mail",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=CheckTransfer,
        )


class AsyncCheckTransfers(AsyncAPIResource):
    async def mail(
        self,
        check_transfer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CheckTransfer:
        """Simulates the mailing of a Check Transfer.

        This transfer must first have a
        `status` of `pending_approval` or `pending_submission`.
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._post(
            f"/simulations/check_transfers/{check_transfer_id}/mail",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=CheckTransfer,
        )
