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
        self._intrafi = intrafi

    @cached_property
    def account_enrollments(self) -> AccountEnrollmentsWithRawResponse:
        return AccountEnrollmentsWithRawResponse(self._intrafi.account_enrollments)

    @cached_property
    def balances(self) -> BalancesWithRawResponse:
        return BalancesWithRawResponse(self._intrafi.balances)

    @cached_property
    def exclusions(self) -> ExclusionsWithRawResponse:
        return ExclusionsWithRawResponse(self._intrafi.exclusions)


class AsyncIntrafiWithRawResponse:
    def __init__(self, intrafi: AsyncIntrafi) -> None:
        self._intrafi = intrafi

    @cached_property
    def account_enrollments(self) -> AsyncAccountEnrollmentsWithRawResponse:
        return AsyncAccountEnrollmentsWithRawResponse(self._intrafi.account_enrollments)

    @cached_property
    def balances(self) -> AsyncBalancesWithRawResponse:
        return AsyncBalancesWithRawResponse(self._intrafi.balances)

    @cached_property
    def exclusions(self) -> AsyncExclusionsWithRawResponse:
        return AsyncExclusionsWithRawResponse(self._intrafi.exclusions)


class IntrafiWithStreamingResponse:
    def __init__(self, intrafi: Intrafi) -> None:
        self._intrafi = intrafi

    @cached_property
    def account_enrollments(self) -> AccountEnrollmentsWithStreamingResponse:
        return AccountEnrollmentsWithStreamingResponse(self._intrafi.account_enrollments)

    @cached_property
    def balances(self) -> BalancesWithStreamingResponse:
        return BalancesWithStreamingResponse(self._intrafi.balances)

    @cached_property
    def exclusions(self) -> ExclusionsWithStreamingResponse:
        return ExclusionsWithStreamingResponse(self._intrafi.exclusions)


class AsyncIntrafiWithStreamingResponse:
    def __init__(self, intrafi: AsyncIntrafi) -> None:
        self._intrafi = intrafi

    @cached_property
    def account_enrollments(self) -> AsyncAccountEnrollmentsWithStreamingResponse:
        return AsyncAccountEnrollmentsWithStreamingResponse(self._intrafi.account_enrollments)

    @cached_property
    def balances(self) -> AsyncBalancesWithStreamingResponse:
        return AsyncBalancesWithStreamingResponse(self._intrafi.balances)

    @cached_property
    def exclusions(self) -> AsyncExclusionsWithStreamingResponse:
        return AsyncExclusionsWithStreamingResponse(self._intrafi.exclusions)
