# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .cards import Cards, AsyncCards
from .programs import Programs, AsyncPrograms
from .documents import Documents, AsyncDocuments
from ..._resource import SyncAPIResource, AsyncAPIResource
from .card_refunds import CardRefunds, AsyncCardRefunds
from .ach_transfers import ACHTransfers, AsyncACHTransfers
from .card_disputes import CardDisputes, AsyncCardDisputes
from .check_deposits import CheckDeposits, AsyncCheckDeposits
from .wire_transfers import WireTransfers, AsyncWireTransfers
from .check_transfers import CheckTransfers, AsyncCheckTransfers
from .account_transfers import AccountTransfers, AsyncAccountTransfers
from .interest_payments import InterestPayments, AsyncInterestPayments
from .account_statements import AccountStatements, AsyncAccountStatements
from .real_time_payments_transfers import (
    RealTimePaymentsTransfers,
    AsyncRealTimePaymentsTransfers,
)
from .digital_wallet_token_requests import (
    DigitalWalletTokenRequests,
    AsyncDigitalWalletTokenRequests,
)
from .inbound_wire_drawdown_requests import (
    InboundWireDrawdownRequests,
    AsyncInboundWireDrawdownRequests,
)

if TYPE_CHECKING:
    from ..._client import Increase, AsyncIncrease

__all__ = ["Simulations", "AsyncSimulations"]


class Simulations(SyncAPIResource):
    account_transfers: AccountTransfers
    account_statements: AccountStatements
    ach_transfers: ACHTransfers
    card_disputes: CardDisputes
    card_refunds: CardRefunds
    check_transfers: CheckTransfers
    documents: Documents
    digital_wallet_token_requests: DigitalWalletTokenRequests
    check_deposits: CheckDeposits
    programs: Programs
    inbound_wire_drawdown_requests: InboundWireDrawdownRequests
    interest_payments: InterestPayments
    wire_transfers: WireTransfers
    cards: Cards
    real_time_payments_transfers: RealTimePaymentsTransfers

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.account_transfers = AccountTransfers(client)
        self.account_statements = AccountStatements(client)
        self.ach_transfers = ACHTransfers(client)
        self.card_disputes = CardDisputes(client)
        self.card_refunds = CardRefunds(client)
        self.check_transfers = CheckTransfers(client)
        self.documents = Documents(client)
        self.digital_wallet_token_requests = DigitalWalletTokenRequests(client)
        self.check_deposits = CheckDeposits(client)
        self.programs = Programs(client)
        self.inbound_wire_drawdown_requests = InboundWireDrawdownRequests(client)
        self.interest_payments = InterestPayments(client)
        self.wire_transfers = WireTransfers(client)
        self.cards = Cards(client)
        self.real_time_payments_transfers = RealTimePaymentsTransfers(client)


class AsyncSimulations(AsyncAPIResource):
    account_transfers: AsyncAccountTransfers
    account_statements: AsyncAccountStatements
    ach_transfers: AsyncACHTransfers
    card_disputes: AsyncCardDisputes
    card_refunds: AsyncCardRefunds
    check_transfers: AsyncCheckTransfers
    documents: AsyncDocuments
    digital_wallet_token_requests: AsyncDigitalWalletTokenRequests
    check_deposits: AsyncCheckDeposits
    programs: AsyncPrograms
    inbound_wire_drawdown_requests: AsyncInboundWireDrawdownRequests
    interest_payments: AsyncInterestPayments
    wire_transfers: AsyncWireTransfers
    cards: AsyncCards
    real_time_payments_transfers: AsyncRealTimePaymentsTransfers

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.account_transfers = AsyncAccountTransfers(client)
        self.account_statements = AsyncAccountStatements(client)
        self.ach_transfers = AsyncACHTransfers(client)
        self.card_disputes = AsyncCardDisputes(client)
        self.card_refunds = AsyncCardRefunds(client)
        self.check_transfers = AsyncCheckTransfers(client)
        self.documents = AsyncDocuments(client)
        self.digital_wallet_token_requests = AsyncDigitalWalletTokenRequests(client)
        self.check_deposits = AsyncCheckDeposits(client)
        self.programs = AsyncPrograms(client)
        self.inbound_wire_drawdown_requests = AsyncInboundWireDrawdownRequests(client)
        self.interest_payments = AsyncInterestPayments(client)
        self.wire_transfers = AsyncWireTransfers(client)
        self.cards = AsyncCards(client)
        self.real_time_payments_transfers = AsyncRealTimePaymentsTransfers(client)
