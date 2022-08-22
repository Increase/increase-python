# File generated from our OpenAPI spec by Stainless.

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.check_deposit import CheckDeposit
from ..types.check_deposit_list_params import CheckDepositListParams
from ..types.check_deposit_create_params import CheckDepositCreateParams

__all__ = ["CheckDeposits", "AsyncCheckDeposits"]


class CheckDeposits(SyncAPIResource):
    def create(
        self,
        body: CheckDepositCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CheckDeposit:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/check_deposits",
            body=body,
            options=options,
            cast_to=CheckDeposit,
        )

    def retrieve(
        self,
        check_deposit_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CheckDeposit:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/check_deposits/{check_deposit_id}",
            options=options,
            cast_to=CheckDeposit,
        )

    def list(
        self,
        query: CheckDepositListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[CheckDeposit]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/check_deposits",
            page=SyncPage[CheckDeposit],
            options=options,
            model=CheckDeposit,
        )


class AsyncCheckDeposits(AsyncAPIResource):
    async def create(
        self,
        body: CheckDepositCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CheckDeposit:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/check_deposits",
            body=body,
            options=options,
            cast_to=CheckDeposit,
        )

    async def retrieve(
        self,
        check_deposit_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CheckDeposit:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/check_deposits/{check_deposit_id}",
            options=options,
            cast_to=CheckDeposit,
        )

    def list(
        self,
        query: CheckDepositListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[CheckDeposit, AsyncPage[CheckDeposit]]:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/check_deposits",
            page=AsyncPage[CheckDeposit],
            options=options,
            model=CheckDeposit,
        )
