# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional

from ..._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations.account_transfer import AccountTransfer

if TYPE_CHECKING:
    pass

__all__ = ["AccountTransfers", "AsyncAccountTransfers"]


class AccountTransfers(SyncAPIResource):
    def complete(
        self,
        account_transfer_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> AccountTransfer:
        """Simulates the completion of an Account Transfer.

        This transfer must first have a `status` of `pending_approval`.
        """
        options = make_request_options(headers, max_retries, timeout, query)
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
        query: Optional[Query] = None,
    ) -> AccountTransfer:
        """Simulates the completion of an Account Transfer.

        This transfer must first have a `status` of `pending_approval`.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            f"/simulations/account_transfers/{account_transfer_id}/complete",
            options=options,
            cast_to=AccountTransfer,
        )
