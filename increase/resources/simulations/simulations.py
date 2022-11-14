# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .cards import Cards, AsyncCards
from ..._resource import SyncAPIResource, AsyncAPIResource
from .ach_transfers import ACHTransfers, AsyncACHTransfers
from .check_deposits import CheckDeposits, AsyncCheckDeposits
from .wire_transfers import WireTransfers, AsyncWireTransfers
from .check_transfers import CheckTransfers, AsyncCheckTransfers
from .account_transfers import AccountTransfers, AsyncAccountTransfers
from .account_statements import AccountStatements, AsyncAccountStatements
from .real_time_payments_transfers import (
    RealTimePaymentsTransfers,
    AsyncRealTimePaymentsTransfers,
)
from .digital_wallet_token_requests import (
    DigitalWalletTokenRequests,
    AsyncDigitalWalletTokenRequests,
)

if TYPE_CHECKING:
    from ..._client import Increase, AsyncIncrease

__all__ = ["Simulations", "AsyncSimulations"]


class Simulations(SyncAPIResource):
    account_transfers: AccountTransfers
    account_statements: AccountStatements
    ach_transfers: ACHTransfers
    check_transfers: CheckTransfers
    digital_wallet_token_requests: DigitalWalletTokenRequests
    check_deposits: CheckDeposits
    wire_transfers: WireTransfers
    cards: Cards
    real_time_payments_transfers: RealTimePaymentsTransfers

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.account_transfers = AccountTransfers(client)
        self.account_statements = AccountStatements(client)
        self.ach_transfers = ACHTransfers(client)
        self.check_transfers = CheckTransfers(client)
        self.digital_wallet_token_requests = DigitalWalletTokenRequests(client)
        self.check_deposits = CheckDeposits(client)
        self.wire_transfers = WireTransfers(client)
        self.cards = Cards(client)
        self.real_time_payments_transfers = RealTimePaymentsTransfers(client)


class AsyncSimulations(AsyncAPIResource):
    account_transfers: AsyncAccountTransfers
    account_statements: AsyncAccountStatements
    ach_transfers: AsyncACHTransfers
    check_transfers: AsyncCheckTransfers
    digital_wallet_token_requests: AsyncDigitalWalletTokenRequests
    check_deposits: AsyncCheckDeposits
    wire_transfers: AsyncWireTransfers
    cards: AsyncCards
    real_time_payments_transfers: AsyncRealTimePaymentsTransfers

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.account_transfers = AsyncAccountTransfers(client)
        self.account_statements = AsyncAccountStatements(client)
        self.ach_transfers = AsyncACHTransfers(client)
        self.check_transfers = AsyncCheckTransfers(client)
        self.digital_wallet_token_requests = AsyncDigitalWalletTokenRequests(client)
        self.check_deposits = AsyncCheckDeposits(client)
        self.wire_transfers = AsyncWireTransfers(client)
        self.cards = AsyncCards(client)
        self.real_time_payments_transfers = AsyncRealTimePaymentsTransfers(client)
