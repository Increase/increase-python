# File generated from our OpenAPI spec by Stainless.

from typing import Union

from ..._types import NOT_GIVEN, Headers, Timeout, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations.check_deposit import *

__all__ = ["CheckDeposits", "AsyncCheckDeposits"]


class CheckDeposits(SyncAPIResource):
    def reject(
        self,
        check_deposit_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> CheckDeposit:
        """
        Simulates the rejection of a Check Deposit by Increase due to factors like poor
        image quality. This Check Deposit must first have a `status` of `pending`.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            f"/simulations/check_deposits/{check_deposit_id}/reject",
            options=options,
            cast_to=CheckDeposit,
        )

    def submit(
        self,
        check_deposit_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> CheckDeposit:
        """Simulates the submission of a Check Deposit to the Federal Reserve.

        This Check Deposit must first have a `status` of `pending`.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            f"/simulations/check_deposits/{check_deposit_id}/submit",
            options=options,
            cast_to=CheckDeposit,
        )


class AsyncCheckDeposits(AsyncAPIResource):
    async def reject(
        self,
        check_deposit_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> CheckDeposit:
        """
        Simulates the rejection of a Check Deposit by Increase due to factors like poor
        image quality. This Check Deposit must first have a `status` of `pending`.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            f"/simulations/check_deposits/{check_deposit_id}/reject",
            options=options,
            cast_to=CheckDeposit,
        )

    async def submit(
        self,
        check_deposit_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> CheckDeposit:
        """Simulates the submission of a Check Deposit to the Federal Reserve.

        This Check Deposit must first have a `status` of `pending`.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            f"/simulations/check_deposits/{check_deposit_id}/submit",
            options=options,
            cast_to=CheckDeposit,
        )
