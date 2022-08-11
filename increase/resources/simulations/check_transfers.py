# File generated from our OpenAPI spec by Stainless.

from typing import Union, Optional

from ..._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations.check_transfer import *

__all__ = ["CheckTransfers", "AsyncCheckTransfers"]


class CheckTransfers(SyncAPIResource):
    def mail(
        self,
        check_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CheckTransfer:
        """Simulates the mailing of a Check Transfer.

        This transfer must first have a `status` of `pending_approval` or
        `pending_submission`.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            f"/simulations/check_transfers/{check_transfer_id}/mail",
            options=options,
            cast_to=CheckTransfer,
        )


class AsyncCheckTransfers(AsyncAPIResource):
    async def mail(
        self,
        check_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CheckTransfer:
        """Simulates the mailing of a Check Transfer.

        This transfer must first have a `status` of `pending_approval` or
        `pending_submission`.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            f"/simulations/check_transfers/{check_transfer_id}/mail",
            options=options,
            cast_to=CheckTransfer,
        )
