# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .balances import (
    Balances,
    AsyncBalances,
    BalancesWithRawResponse,
    AsyncBalancesWithRawResponse,
    BalancesWithStreamingResponse,
    AsyncBalancesWithStreamingResponse,
)
from ..._compat import cached_property
from .exclusions import (
    Exclusions,
    AsyncExclusions,
    ExclusionsWithRawResponse,
    AsyncExclusionsWithRawResponse,
    ExclusionsWithStreamingResponse,
    AsyncExclusionsWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .account_enrollments import (
    AccountEnrollments,
    AsyncAccountEnrollments,
    AccountEnrollmentsWithRawResponse,
    AsyncAccountEnrollmentsWithRawResponse,
    AccountEnrollmentsWithStreamingResponse,
    AsyncAccountEnrollmentsWithStreamingResponse,
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

    @cached_property
    def with_streaming_response(self) -> IntrafiWithStreamingResponse:
        return IntrafiWithStreamingResponse(self)


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

    @cached_property
    def with_streaming_response(self) -> AsyncIntrafiWithStreamingResponse:
        return AsyncIntrafiWithStreamingResponse(self)


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


class IntrafiWithStreamingResponse:
    def __init__(self, intrafi: Intrafi) -> None:
        self.account_enrollments = AccountEnrollmentsWithStreamingResponse(intrafi.account_enrollments)
        self.balances = BalancesWithStreamingResponse(intrafi.balances)
        self.exclusions = ExclusionsWithStreamingResponse(intrafi.exclusions)


class AsyncIntrafiWithStreamingResponse:
    def __init__(self, intrafi: AsyncIntrafi) -> None:
        self.account_enrollments = AsyncAccountEnrollmentsWithStreamingResponse(intrafi.account_enrollments)
        self.balances = AsyncBalancesWithStreamingResponse(intrafi.balances)
        self.exclusions = AsyncExclusionsWithStreamingResponse(intrafi.exclusions)
