# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .balances import (
    Balances,
    AsyncBalances,
    BalancesWithRawResponse,
    AsyncBalancesWithRawResponse,
)
from .exclusions import (
    Exclusions,
    AsyncExclusions,
    ExclusionsWithRawResponse,
    AsyncExclusionsWithRawResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .account_enrollments import (
    AccountEnrollments,
    AsyncAccountEnrollments,
    AccountEnrollmentsWithRawResponse,
    AsyncAccountEnrollmentsWithRawResponse,
)

if TYPE_CHECKING:
    from ..._client import Increase, AsyncIncrease

__all__ = ["Intrafi", "AsyncIntrafi"]


class Intrafi(SyncAPIResource):
    account_enrollments: AccountEnrollments
    balances: Balances
    exclusions: Exclusions
    with_raw_response: IntrafiWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.account_enrollments = AccountEnrollments(client)
        self.balances = Balances(client)
        self.exclusions = Exclusions(client)
        self.with_raw_response = IntrafiWithRawResponse(self)


class AsyncIntrafi(AsyncAPIResource):
    account_enrollments: AsyncAccountEnrollments
    balances: AsyncBalances
    exclusions: AsyncExclusions
    with_raw_response: AsyncIntrafiWithRawResponse

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.account_enrollments = AsyncAccountEnrollments(client)
        self.balances = AsyncBalances(client)
        self.exclusions = AsyncExclusions(client)
        self.with_raw_response = AsyncIntrafiWithRawResponse(self)


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
