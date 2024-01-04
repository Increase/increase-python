# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .balances import Balances, AsyncBalances, BalancesWithRawResponse, AsyncBalancesWithRawResponse
from ..._compat import cached_property
from .exclusions import Exclusions, AsyncExclusions, ExclusionsWithRawResponse, AsyncExclusionsWithRawResponse
from ..._resource import SyncAPIResource, AsyncAPIResource
from .account_enrollments import (
    AccountEnrollments,
    AsyncAccountEnrollments,
    AccountEnrollmentsWithRawResponse,
    AsyncAccountEnrollmentsWithRawResponse,
)

__all__ = ["Intrafi", "AsyncIntrafi"]


class Intrafi(SyncAPIResource):
    @cached_property
    def account_enrollments(self) -> AccountEnrollments:
        return AccountEnrollments(self._client)

    @cached_property
    def balances(self) -> Balances:
        return Balances(self._client)

    @cached_property
    def exclusions(self) -> Exclusions:
        return Exclusions(self._client)

    @cached_property
    def with_raw_response(self) -> IntrafiWithRawResponse:
        return IntrafiWithRawResponse(self)


class AsyncIntrafi(AsyncAPIResource):
    @cached_property
    def account_enrollments(self) -> AsyncAccountEnrollments:
        return AsyncAccountEnrollments(self._client)

    @cached_property
    def balances(self) -> AsyncBalances:
        return AsyncBalances(self._client)

    @cached_property
    def exclusions(self) -> AsyncExclusions:
        return AsyncExclusions(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIntrafiWithRawResponse:
        return AsyncIntrafiWithRawResponse(self)


class IntrafiWithRawResponse:
    def __init__(self, intrafi: Intrafi) -> None:
        self.account_enrollments = AccountEnrollmentsWithRawResponse(intrafi.account_enrollments)
        self.balances = BalancesWithRawResponse(intrafi.balances)
        self.exclusions = ExclusionsWithRawResponse(intrafi.exclusions)


class AsyncIntrafiWithRawResponse:
    def __init__(self, intrafi: AsyncIntrafi) -> None:
        self.account_enrollments = AsyncAccountEnrollmentsWithRawResponse(intrafi.account_enrollments)
        self.balances = AsyncBalancesWithRawResponse(intrafi.balances)
        self.exclusions = AsyncExclusionsWithRawResponse(intrafi.exclusions)
