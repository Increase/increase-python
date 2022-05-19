# File generated from our OpenAPI spec by Stainless.

from typing import Union

from ..._types import NOT_GIVEN, Headers, Timeout, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations.account_transfer import *

__all__ = ["AccountTransfers", "AsyncAccountTransfers"]


class AccountTransfers(SyncAPIResource):
    def complete(
        self,
        account_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountTransfer:
        """Simulates the completion of an Account Transfer.

        This transfer must first have a `status` of `pending_approval`.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            f"/simulations/account_transfers/{account_transfer_id}/complete",
            options=options,
            cast_to=AccountTransfer,
        )


class AsyncAccountTransfers(AsyncAPIResource):
    async def complete(
        self,
        account_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountTransfer:
        """Simulates the completion of an Account Transfer.

        This transfer must first have a `status` of `pending_approval`.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            f"/simulations/account_transfers/{account_transfer_id}/complete",
            options=options,
            cast_to=AccountTransfer,
        )
