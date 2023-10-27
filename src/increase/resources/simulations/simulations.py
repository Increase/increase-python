# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .cards import Cards, AsyncCards, CardsWithRawResponse, AsyncCardsWithRawResponse
from .programs import (
    Programs,
    AsyncPrograms,
    ProgramsWithRawResponse,
    AsyncProgramsWithRawResponse,
)
from .documents import (
    Documents,
    AsyncDocuments,
    DocumentsWithRawResponse,
    AsyncDocumentsWithRawResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .card_refunds import (
    CardRefunds,
    AsyncCardRefunds,
    CardRefundsWithRawResponse,
    AsyncCardRefundsWithRawResponse,
)
from .ach_transfers import (
    ACHTransfers,
    AsyncACHTransfers,
    ACHTransfersWithRawResponse,
    AsyncACHTransfersWithRawResponse,
)
from .card_disputes import (
    CardDisputes,
    AsyncCardDisputes,
    CardDisputesWithRawResponse,
    AsyncCardDisputesWithRawResponse,
)
from .card_profiles import (
    CardProfiles,
    AsyncCardProfiles,
    CardProfilesWithRawResponse,
    AsyncCardProfilesWithRawResponse,
)
from .check_deposits import (
    CheckDeposits,
    AsyncCheckDeposits,
    CheckDepositsWithRawResponse,
    AsyncCheckDepositsWithRawResponse,
)
from .physical_cards import (
    PhysicalCards,
    AsyncPhysicalCards,
    PhysicalCardsWithRawResponse,
    AsyncPhysicalCardsWithRawResponse,
)
from .wire_transfers import (
    WireTransfers,
    AsyncWireTransfers,
    WireTransfersWithRawResponse,
    AsyncWireTransfersWithRawResponse,
)
from .check_transfers import (
    CheckTransfers,
    AsyncCheckTransfers,
    CheckTransfersWithRawResponse,
    AsyncCheckTransfersWithRawResponse,
)
from .account_transfers import (
    AccountTransfers,
    AsyncAccountTransfers,
    AccountTransfersWithRawResponse,
    AsyncAccountTransfersWithRawResponse,
)
from .interest_payments import (
    InterestPayments,
    AsyncInterestPayments,
    InterestPaymentsWithRawResponse,
    AsyncInterestPaymentsWithRawResponse,
)
from .account_statements import (
    AccountStatements,
    AsyncAccountStatements,
    AccountStatementsWithRawResponse,
    AsyncAccountStatementsWithRawResponse,
)
from .inbound_funds_holds import (
    InboundFundsHolds,
    AsyncInboundFundsHolds,
    InboundFundsHoldsWithRawResponse,
    AsyncInboundFundsHoldsWithRawResponse,
)
from .real_time_payments_transfers import (
    RealTimePaymentsTransfers,
    AsyncRealTimePaymentsTransfers,
    RealTimePaymentsTransfersWithRawResponse,
    AsyncRealTimePaymentsTransfersWithRawResponse,
)
from .digital_wallet_token_requests import (
    DigitalWalletTokenRequests,
    AsyncDigitalWalletTokenRequests,
    DigitalWalletTokenRequestsWithRawResponse,
    AsyncDigitalWalletTokenRequestsWithRawResponse,
)
from .inbound_wire_drawdown_requests import (
    InboundWireDrawdownRequests,
    AsyncInboundWireDrawdownRequests,
    InboundWireDrawdownRequestsWithRawResponse,
    AsyncInboundWireDrawdownRequestsWithRawResponse,
)

if TYPE_CHECKING:
    from ..._client import Increase, AsyncIncrease

__all__ = ["Simulations", "AsyncSimulations"]


class Simulations(SyncAPIResource):
    account_transfers: AccountTransfers
    account_statements: AccountStatements
    ach_transfers: ACHTransfers
    card_disputes: CardDisputes
    card_profiles: CardProfiles
    card_refunds: CardRefunds
    check_transfers: CheckTransfers
    documents: Documents
    digital_wallet_token_requests: DigitalWalletTokenRequests
    check_deposits: CheckDeposits
    programs: Programs
    inbound_wire_drawdown_requests: InboundWireDrawdownRequests
    inbound_funds_holds: InboundFundsHolds
    interest_payments: InterestPayments
    wire_transfers: WireTransfers
    cards: Cards
    real_time_payments_transfers: RealTimePaymentsTransfers
    physical_cards: PhysicalCards
    with_raw_response: SimulationsWithRawResponse

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.account_transfers = AccountTransfers(client)
        self.account_statements = AccountStatements(client)
        self.ach_transfers = ACHTransfers(client)
        self.card_disputes = CardDisputes(client)
        self.card_profiles = CardProfiles(client)
        self.card_refunds = CardRefunds(client)
        self.check_transfers = CheckTransfers(client)
        self.documents = Documents(client)
        self.digital_wallet_token_requests = DigitalWalletTokenRequests(client)
        self.check_deposits = CheckDeposits(client)
        self.programs = Programs(client)
        self.inbound_wire_drawdown_requests = InboundWireDrawdownRequests(client)
        self.inbound_funds_holds = InboundFundsHolds(client)
        self.interest_payments = InterestPayments(client)
        self.wire_transfers = WireTransfers(client)
        self.cards = Cards(client)
        self.real_time_payments_transfers = RealTimePaymentsTransfers(client)
        self.physical_cards = PhysicalCards(client)
        self.with_raw_response = SimulationsWithRawResponse(self)


class AsyncSimulations(AsyncAPIResource):
    account_transfers: AsyncAccountTransfers
    account_statements: AsyncAccountStatements
    ach_transfers: AsyncACHTransfers
    card_disputes: AsyncCardDisputes
    card_profiles: AsyncCardProfiles
    card_refunds: AsyncCardRefunds
    check_transfers: AsyncCheckTransfers
    documents: AsyncDocuments
    digital_wallet_token_requests: AsyncDigitalWalletTokenRequests
    check_deposits: AsyncCheckDeposits
    programs: AsyncPrograms
    inbound_wire_drawdown_requests: AsyncInboundWireDrawdownRequests
    inbound_funds_holds: AsyncInboundFundsHolds
    interest_payments: AsyncInterestPayments
    wire_transfers: AsyncWireTransfers
    cards: AsyncCards
    real_time_payments_transfers: AsyncRealTimePaymentsTransfers
    physical_cards: AsyncPhysicalCards
    with_raw_response: AsyncSimulationsWithRawResponse

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.account_transfers = AsyncAccountTransfers(client)
        self.account_statements = AsyncAccountStatements(client)
        self.ach_transfers = AsyncACHTransfers(client)
        self.card_disputes = AsyncCardDisputes(client)
        self.card_profiles = AsyncCardProfiles(client)
        self.card_refunds = AsyncCardRefunds(client)
        self.check_transfers = AsyncCheckTransfers(client)
        self.documents = AsyncDocuments(client)
        self.digital_wallet_token_requests = AsyncDigitalWalletTokenRequests(client)
        self.check_deposits = AsyncCheckDeposits(client)
        self.programs = AsyncPrograms(client)
        self.inbound_wire_drawdown_requests = AsyncInboundWireDrawdownRequests(client)
        self.inbound_funds_holds = AsyncInboundFundsHolds(client)
        self.interest_payments = AsyncInterestPayments(client)
        self.wire_transfers = AsyncWireTransfers(client)
        self.cards = AsyncCards(client)
        self.real_time_payments_transfers = AsyncRealTimePaymentsTransfers(client)
        self.physical_cards = AsyncPhysicalCards(client)
        self.with_raw_response = AsyncSimulationsWithRawResponse(self)


class SimulationsWithRawResponse:
    def __init__(self, simulations: Simulations) -> None:
        self.account_transfers = AccountTransfersWithRawResponse(simulations.account_transfers)
        self.account_statements = AccountStatementsWithRawResponse(simulations.account_statements)
        self.ach_transfers = ACHTransfersWithRawResponse(simulations.ach_transfers)
        self.card_disputes = CardDisputesWithRawResponse(simulations.card_disputes)
        self.card_profiles = CardProfilesWithRawResponse(simulations.card_profiles)
        self.card_refunds = CardRefundsWithRawResponse(simulations.card_refunds)
        self.check_transfers = CheckTransfersWithRawResponse(simulations.check_transfers)
        self.documents = DocumentsWithRawResponse(simulations.documents)
        self.digital_wallet_token_requests = DigitalWalletTokenRequestsWithRawResponse(
            simulations.digital_wallet_token_requests
        )
        self.check_deposits = CheckDepositsWithRawResponse(simulations.check_deposits)
        self.programs = ProgramsWithRawResponse(simulations.programs)
        self.inbound_wire_drawdown_requests = InboundWireDrawdownRequestsWithRawResponse(
            simulations.inbound_wire_drawdown_requests
        )
        self.inbound_funds_holds = InboundFundsHoldsWithRawResponse(simulations.inbound_funds_holds)
        self.interest_payments = InterestPaymentsWithRawResponse(simulations.interest_payments)
        self.wire_transfers = WireTransfersWithRawResponse(simulations.wire_transfers)
        self.cards = CardsWithRawResponse(simulations.cards)
        self.real_time_payments_transfers = RealTimePaymentsTransfersWithRawResponse(
            simulations.real_time_payments_transfers
        )
        self.physical_cards = PhysicalCardsWithRawResponse(simulations.physical_cards)


class AsyncSimulationsWithRawResponse:
    def __init__(self, simulations: AsyncSimulations) -> None:
        self.account_transfers = AsyncAccountTransfersWithRawResponse(simulations.account_transfers)
        self.account_statements = AsyncAccountStatementsWithRawResponse(simulations.account_statements)
        self.ach_transfers = AsyncACHTransfersWithRawResponse(simulations.ach_transfers)
        self.card_disputes = AsyncCardDisputesWithRawResponse(simulations.card_disputes)
        self.card_profiles = AsyncCardProfilesWithRawResponse(simulations.card_profiles)
        self.card_refunds = AsyncCardRefundsWithRawResponse(simulations.card_refunds)
        self.check_transfers = AsyncCheckTransfersWithRawResponse(simulations.check_transfers)
        self.documents = AsyncDocumentsWithRawResponse(simulations.documents)
        self.digital_wallet_token_requests = AsyncDigitalWalletTokenRequestsWithRawResponse(
            simulations.digital_wallet_token_requests
        )
        self.check_deposits = AsyncCheckDepositsWithRawResponse(simulations.check_deposits)
        self.programs = AsyncProgramsWithRawResponse(simulations.programs)
        self.inbound_wire_drawdown_requests = AsyncInboundWireDrawdownRequestsWithRawResponse(
            simulations.inbound_wire_drawdown_requests
        )
        self.inbound_funds_holds = AsyncInboundFundsHoldsWithRawResponse(simulations.inbound_funds_holds)
        self.interest_payments = AsyncInterestPaymentsWithRawResponse(simulations.interest_payments)
        self.wire_transfers = AsyncWireTransfersWithRawResponse(simulations.wire_transfers)
        self.cards = AsyncCardsWithRawResponse(simulations.cards)
        self.real_time_payments_transfers = AsyncRealTimePaymentsTransfersWithRawResponse(
            simulations.real_time_payments_transfers
        )
        self.physical_cards = AsyncPhysicalCardsWithRawResponse(simulations.physical_cards)
