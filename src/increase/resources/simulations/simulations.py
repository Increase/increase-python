# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .cards import (
    Cards,
    AsyncCards,
    CardsWithRawResponse,
    AsyncCardsWithRawResponse,
    CardsWithStreamingResponse,
    AsyncCardsWithStreamingResponse,
)
from .programs import (
    Programs,
    AsyncPrograms,
    ProgramsWithRawResponse,
    AsyncProgramsWithRawResponse,
    ProgramsWithStreamingResponse,
    AsyncProgramsWithStreamingResponse,
)
from ..._compat import cached_property
from .documents import (
    Documents,
    AsyncDocuments,
    DocumentsWithRawResponse,
    AsyncDocumentsWithRawResponse,
    DocumentsWithStreamingResponse,
    AsyncDocumentsWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .card_refunds import (
    CardRefunds,
    AsyncCardRefunds,
    CardRefundsWithRawResponse,
    AsyncCardRefundsWithRawResponse,
    CardRefundsWithStreamingResponse,
    AsyncCardRefundsWithStreamingResponse,
)
from .ach_transfers import (
    ACHTransfers,
    AsyncACHTransfers,
    ACHTransfersWithRawResponse,
    AsyncACHTransfersWithRawResponse,
    ACHTransfersWithStreamingResponse,
    AsyncACHTransfersWithStreamingResponse,
)
from .card_disputes import (
    CardDisputes,
    AsyncCardDisputes,
    CardDisputesWithRawResponse,
    AsyncCardDisputesWithRawResponse,
    CardDisputesWithStreamingResponse,
    AsyncCardDisputesWithStreamingResponse,
)
from .card_profiles import (
    CardProfiles,
    AsyncCardProfiles,
    CardProfilesWithRawResponse,
    AsyncCardProfilesWithRawResponse,
    CardProfilesWithStreamingResponse,
    AsyncCardProfilesWithStreamingResponse,
)
from .check_deposits import (
    CheckDeposits,
    AsyncCheckDeposits,
    CheckDepositsWithRawResponse,
    AsyncCheckDepositsWithRawResponse,
    CheckDepositsWithStreamingResponse,
    AsyncCheckDepositsWithStreamingResponse,
)
from .physical_cards import (
    PhysicalCards,
    AsyncPhysicalCards,
    PhysicalCardsWithRawResponse,
    AsyncPhysicalCardsWithRawResponse,
    PhysicalCardsWithStreamingResponse,
    AsyncPhysicalCardsWithStreamingResponse,
)
from .wire_transfers import (
    WireTransfers,
    AsyncWireTransfers,
    WireTransfersWithRawResponse,
    AsyncWireTransfersWithRawResponse,
    WireTransfersWithStreamingResponse,
    AsyncWireTransfersWithStreamingResponse,
)
from .check_transfers import (
    CheckTransfers,
    AsyncCheckTransfers,
    CheckTransfersWithRawResponse,
    AsyncCheckTransfersWithRawResponse,
    CheckTransfersWithStreamingResponse,
    AsyncCheckTransfersWithStreamingResponse,
)
from .account_transfers import (
    AccountTransfers,
    AsyncAccountTransfers,
    AccountTransfersWithRawResponse,
    AsyncAccountTransfersWithRawResponse,
    AccountTransfersWithStreamingResponse,
    AsyncAccountTransfersWithStreamingResponse,
)
from .interest_payments import (
    InterestPayments,
    AsyncInterestPayments,
    InterestPaymentsWithRawResponse,
    AsyncInterestPaymentsWithRawResponse,
    InterestPaymentsWithStreamingResponse,
    AsyncInterestPaymentsWithStreamingResponse,
)
from .account_statements import (
    AccountStatements,
    AsyncAccountStatements,
    AccountStatementsWithRawResponse,
    AsyncAccountStatementsWithRawResponse,
    AccountStatementsWithStreamingResponse,
    AsyncAccountStatementsWithStreamingResponse,
)
from .inbound_funds_holds import (
    InboundFundsHolds,
    AsyncInboundFundsHolds,
    InboundFundsHoldsWithRawResponse,
    AsyncInboundFundsHoldsWithRawResponse,
    InboundFundsHoldsWithStreamingResponse,
    AsyncInboundFundsHoldsWithStreamingResponse,
)
from .real_time_payments_transfers import (
    RealTimePaymentsTransfers,
    AsyncRealTimePaymentsTransfers,
    RealTimePaymentsTransfersWithRawResponse,
    AsyncRealTimePaymentsTransfersWithRawResponse,
    RealTimePaymentsTransfersWithStreamingResponse,
    AsyncRealTimePaymentsTransfersWithStreamingResponse,
)
from .digital_wallet_token_requests import (
    DigitalWalletTokenRequests,
    AsyncDigitalWalletTokenRequests,
    DigitalWalletTokenRequestsWithRawResponse,
    AsyncDigitalWalletTokenRequestsWithRawResponse,
    DigitalWalletTokenRequestsWithStreamingResponse,
    AsyncDigitalWalletTokenRequestsWithStreamingResponse,
)
from .inbound_wire_drawdown_requests import (
    InboundWireDrawdownRequests,
    AsyncInboundWireDrawdownRequests,
    InboundWireDrawdownRequestsWithRawResponse,
    AsyncInboundWireDrawdownRequestsWithRawResponse,
    InboundWireDrawdownRequestsWithStreamingResponse,
    AsyncInboundWireDrawdownRequestsWithStreamingResponse,
)

__all__ = ["Simulations", "AsyncSimulations"]


class Simulations(SyncAPIResource):
    @cached_property
    def account_transfers(self) -> AccountTransfers:
        return AccountTransfers(self._client)

    @cached_property
    def account_statements(self) -> AccountStatements:
        return AccountStatements(self._client)

    @cached_property
    def ach_transfers(self) -> ACHTransfers:
        return ACHTransfers(self._client)

    @cached_property
    def card_disputes(self) -> CardDisputes:
        return CardDisputes(self._client)

    @cached_property
    def card_profiles(self) -> CardProfiles:
        return CardProfiles(self._client)

    @cached_property
    def card_refunds(self) -> CardRefunds:
        return CardRefunds(self._client)

    @cached_property
    def check_transfers(self) -> CheckTransfers:
        return CheckTransfers(self._client)

    @cached_property
    def documents(self) -> Documents:
        return Documents(self._client)

    @cached_property
    def digital_wallet_token_requests(self) -> DigitalWalletTokenRequests:
        return DigitalWalletTokenRequests(self._client)

    @cached_property
    def check_deposits(self) -> CheckDeposits:
        return CheckDeposits(self._client)

    @cached_property
    def programs(self) -> Programs:
        return Programs(self._client)

    @cached_property
    def inbound_wire_drawdown_requests(self) -> InboundWireDrawdownRequests:
        return InboundWireDrawdownRequests(self._client)

    @cached_property
    def inbound_funds_holds(self) -> InboundFundsHolds:
        return InboundFundsHolds(self._client)

    @cached_property
    def interest_payments(self) -> InterestPayments:
        return InterestPayments(self._client)

    @cached_property
    def wire_transfers(self) -> WireTransfers:
        return WireTransfers(self._client)

    @cached_property
    def cards(self) -> Cards:
        return Cards(self._client)

    @cached_property
    def real_time_payments_transfers(self) -> RealTimePaymentsTransfers:
        return RealTimePaymentsTransfers(self._client)

    @cached_property
    def physical_cards(self) -> PhysicalCards:
        return PhysicalCards(self._client)

    @cached_property
    def with_raw_response(self) -> SimulationsWithRawResponse:
        return SimulationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationsWithStreamingResponse:
        return SimulationsWithStreamingResponse(self)


class AsyncSimulations(AsyncAPIResource):
    @cached_property
    def account_transfers(self) -> AsyncAccountTransfers:
        return AsyncAccountTransfers(self._client)

    @cached_property
    def account_statements(self) -> AsyncAccountStatements:
        return AsyncAccountStatements(self._client)

    @cached_property
    def ach_transfers(self) -> AsyncACHTransfers:
        return AsyncACHTransfers(self._client)

    @cached_property
    def card_disputes(self) -> AsyncCardDisputes:
        return AsyncCardDisputes(self._client)

    @cached_property
    def card_profiles(self) -> AsyncCardProfiles:
        return AsyncCardProfiles(self._client)

    @cached_property
    def card_refunds(self) -> AsyncCardRefunds:
        return AsyncCardRefunds(self._client)

    @cached_property
    def check_transfers(self) -> AsyncCheckTransfers:
        return AsyncCheckTransfers(self._client)

    @cached_property
    def documents(self) -> AsyncDocuments:
        return AsyncDocuments(self._client)

    @cached_property
    def digital_wallet_token_requests(self) -> AsyncDigitalWalletTokenRequests:
        return AsyncDigitalWalletTokenRequests(self._client)

    @cached_property
    def check_deposits(self) -> AsyncCheckDeposits:
        return AsyncCheckDeposits(self._client)

    @cached_property
    def programs(self) -> AsyncPrograms:
        return AsyncPrograms(self._client)

    @cached_property
    def inbound_wire_drawdown_requests(self) -> AsyncInboundWireDrawdownRequests:
        return AsyncInboundWireDrawdownRequests(self._client)

    @cached_property
    def inbound_funds_holds(self) -> AsyncInboundFundsHolds:
        return AsyncInboundFundsHolds(self._client)

    @cached_property
    def interest_payments(self) -> AsyncInterestPayments:
        return AsyncInterestPayments(self._client)

    @cached_property
    def wire_transfers(self) -> AsyncWireTransfers:
        return AsyncWireTransfers(self._client)

    @cached_property
    def cards(self) -> AsyncCards:
        return AsyncCards(self._client)

    @cached_property
    def real_time_payments_transfers(self) -> AsyncRealTimePaymentsTransfers:
        return AsyncRealTimePaymentsTransfers(self._client)

    @cached_property
    def physical_cards(self) -> AsyncPhysicalCards:
        return AsyncPhysicalCards(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSimulationsWithRawResponse:
        return AsyncSimulationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationsWithStreamingResponse:
        return AsyncSimulationsWithStreamingResponse(self)


class SimulationsWithRawResponse:
    def __init__(self, simulations: Simulations) -> None:
        self._simulations = simulations

    @cached_property
    def account_transfers(self) -> AccountTransfersWithRawResponse:
        return AccountTransfersWithRawResponse(self._simulations.account_transfers)

    @cached_property
    def account_statements(self) -> AccountStatementsWithRawResponse:
        return AccountStatementsWithRawResponse(self._simulations.account_statements)

    @cached_property
    def ach_transfers(self) -> ACHTransfersWithRawResponse:
        return ACHTransfersWithRawResponse(self._simulations.ach_transfers)

    @cached_property
    def card_disputes(self) -> CardDisputesWithRawResponse:
        return CardDisputesWithRawResponse(self._simulations.card_disputes)

    @cached_property
    def card_profiles(self) -> CardProfilesWithRawResponse:
        return CardProfilesWithRawResponse(self._simulations.card_profiles)

    @cached_property
    def card_refunds(self) -> CardRefundsWithRawResponse:
        return CardRefundsWithRawResponse(self._simulations.card_refunds)

    @cached_property
    def check_transfers(self) -> CheckTransfersWithRawResponse:
        return CheckTransfersWithRawResponse(self._simulations.check_transfers)

    @cached_property
    def documents(self) -> DocumentsWithRawResponse:
        return DocumentsWithRawResponse(self._simulations.documents)

    @cached_property
    def digital_wallet_token_requests(self) -> DigitalWalletTokenRequestsWithRawResponse:
        return DigitalWalletTokenRequestsWithRawResponse(self._simulations.digital_wallet_token_requests)

    @cached_property
    def check_deposits(self) -> CheckDepositsWithRawResponse:
        return CheckDepositsWithRawResponse(self._simulations.check_deposits)

    @cached_property
    def programs(self) -> ProgramsWithRawResponse:
        return ProgramsWithRawResponse(self._simulations.programs)

    @cached_property
    def inbound_wire_drawdown_requests(self) -> InboundWireDrawdownRequestsWithRawResponse:
        return InboundWireDrawdownRequestsWithRawResponse(self._simulations.inbound_wire_drawdown_requests)

    @cached_property
    def inbound_funds_holds(self) -> InboundFundsHoldsWithRawResponse:
        return InboundFundsHoldsWithRawResponse(self._simulations.inbound_funds_holds)

    @cached_property
    def interest_payments(self) -> InterestPaymentsWithRawResponse:
        return InterestPaymentsWithRawResponse(self._simulations.interest_payments)

    @cached_property
    def wire_transfers(self) -> WireTransfersWithRawResponse:
        return WireTransfersWithRawResponse(self._simulations.wire_transfers)

    @cached_property
    def cards(self) -> CardsWithRawResponse:
        return CardsWithRawResponse(self._simulations.cards)

    @cached_property
    def real_time_payments_transfers(self) -> RealTimePaymentsTransfersWithRawResponse:
        return RealTimePaymentsTransfersWithRawResponse(self._simulations.real_time_payments_transfers)

    @cached_property
    def physical_cards(self) -> PhysicalCardsWithRawResponse:
        return PhysicalCardsWithRawResponse(self._simulations.physical_cards)


class AsyncSimulationsWithRawResponse:
    def __init__(self, simulations: AsyncSimulations) -> None:
        self._simulations = simulations

    @cached_property
    def account_transfers(self) -> AsyncAccountTransfersWithRawResponse:
        return AsyncAccountTransfersWithRawResponse(self._simulations.account_transfers)

    @cached_property
    def account_statements(self) -> AsyncAccountStatementsWithRawResponse:
        return AsyncAccountStatementsWithRawResponse(self._simulations.account_statements)

    @cached_property
    def ach_transfers(self) -> AsyncACHTransfersWithRawResponse:
        return AsyncACHTransfersWithRawResponse(self._simulations.ach_transfers)

    @cached_property
    def card_disputes(self) -> AsyncCardDisputesWithRawResponse:
        return AsyncCardDisputesWithRawResponse(self._simulations.card_disputes)

    @cached_property
    def card_profiles(self) -> AsyncCardProfilesWithRawResponse:
        return AsyncCardProfilesWithRawResponse(self._simulations.card_profiles)

    @cached_property
    def card_refunds(self) -> AsyncCardRefundsWithRawResponse:
        return AsyncCardRefundsWithRawResponse(self._simulations.card_refunds)

    @cached_property
    def check_transfers(self) -> AsyncCheckTransfersWithRawResponse:
        return AsyncCheckTransfersWithRawResponse(self._simulations.check_transfers)

    @cached_property
    def documents(self) -> AsyncDocumentsWithRawResponse:
        return AsyncDocumentsWithRawResponse(self._simulations.documents)

    @cached_property
    def digital_wallet_token_requests(self) -> AsyncDigitalWalletTokenRequestsWithRawResponse:
        return AsyncDigitalWalletTokenRequestsWithRawResponse(self._simulations.digital_wallet_token_requests)

    @cached_property
    def check_deposits(self) -> AsyncCheckDepositsWithRawResponse:
        return AsyncCheckDepositsWithRawResponse(self._simulations.check_deposits)

    @cached_property
    def programs(self) -> AsyncProgramsWithRawResponse:
        return AsyncProgramsWithRawResponse(self._simulations.programs)

    @cached_property
    def inbound_wire_drawdown_requests(self) -> AsyncInboundWireDrawdownRequestsWithRawResponse:
        return AsyncInboundWireDrawdownRequestsWithRawResponse(self._simulations.inbound_wire_drawdown_requests)

    @cached_property
    def inbound_funds_holds(self) -> AsyncInboundFundsHoldsWithRawResponse:
        return AsyncInboundFundsHoldsWithRawResponse(self._simulations.inbound_funds_holds)

    @cached_property
    def interest_payments(self) -> AsyncInterestPaymentsWithRawResponse:
        return AsyncInterestPaymentsWithRawResponse(self._simulations.interest_payments)

    @cached_property
    def wire_transfers(self) -> AsyncWireTransfersWithRawResponse:
        return AsyncWireTransfersWithRawResponse(self._simulations.wire_transfers)

    @cached_property
    def cards(self) -> AsyncCardsWithRawResponse:
        return AsyncCardsWithRawResponse(self._simulations.cards)

    @cached_property
    def real_time_payments_transfers(self) -> AsyncRealTimePaymentsTransfersWithRawResponse:
        return AsyncRealTimePaymentsTransfersWithRawResponse(self._simulations.real_time_payments_transfers)

    @cached_property
    def physical_cards(self) -> AsyncPhysicalCardsWithRawResponse:
        return AsyncPhysicalCardsWithRawResponse(self._simulations.physical_cards)


class SimulationsWithStreamingResponse:
    def __init__(self, simulations: Simulations) -> None:
        self._simulations = simulations

    @cached_property
    def account_transfers(self) -> AccountTransfersWithStreamingResponse:
        return AccountTransfersWithStreamingResponse(self._simulations.account_transfers)

    @cached_property
    def account_statements(self) -> AccountStatementsWithStreamingResponse:
        return AccountStatementsWithStreamingResponse(self._simulations.account_statements)

    @cached_property
    def ach_transfers(self) -> ACHTransfersWithStreamingResponse:
        return ACHTransfersWithStreamingResponse(self._simulations.ach_transfers)

    @cached_property
    def card_disputes(self) -> CardDisputesWithStreamingResponse:
        return CardDisputesWithStreamingResponse(self._simulations.card_disputes)

    @cached_property
    def card_profiles(self) -> CardProfilesWithStreamingResponse:
        return CardProfilesWithStreamingResponse(self._simulations.card_profiles)

    @cached_property
    def card_refunds(self) -> CardRefundsWithStreamingResponse:
        return CardRefundsWithStreamingResponse(self._simulations.card_refunds)

    @cached_property
    def check_transfers(self) -> CheckTransfersWithStreamingResponse:
        return CheckTransfersWithStreamingResponse(self._simulations.check_transfers)

    @cached_property
    def documents(self) -> DocumentsWithStreamingResponse:
        return DocumentsWithStreamingResponse(self._simulations.documents)

    @cached_property
    def digital_wallet_token_requests(self) -> DigitalWalletTokenRequestsWithStreamingResponse:
        return DigitalWalletTokenRequestsWithStreamingResponse(self._simulations.digital_wallet_token_requests)

    @cached_property
    def check_deposits(self) -> CheckDepositsWithStreamingResponse:
        return CheckDepositsWithStreamingResponse(self._simulations.check_deposits)

    @cached_property
    def programs(self) -> ProgramsWithStreamingResponse:
        return ProgramsWithStreamingResponse(self._simulations.programs)

    @cached_property
    def inbound_wire_drawdown_requests(self) -> InboundWireDrawdownRequestsWithStreamingResponse:
        return InboundWireDrawdownRequestsWithStreamingResponse(self._simulations.inbound_wire_drawdown_requests)

    @cached_property
    def inbound_funds_holds(self) -> InboundFundsHoldsWithStreamingResponse:
        return InboundFundsHoldsWithStreamingResponse(self._simulations.inbound_funds_holds)

    @cached_property
    def interest_payments(self) -> InterestPaymentsWithStreamingResponse:
        return InterestPaymentsWithStreamingResponse(self._simulations.interest_payments)

    @cached_property
    def wire_transfers(self) -> WireTransfersWithStreamingResponse:
        return WireTransfersWithStreamingResponse(self._simulations.wire_transfers)

    @cached_property
    def cards(self) -> CardsWithStreamingResponse:
        return CardsWithStreamingResponse(self._simulations.cards)

    @cached_property
    def real_time_payments_transfers(self) -> RealTimePaymentsTransfersWithStreamingResponse:
        return RealTimePaymentsTransfersWithStreamingResponse(self._simulations.real_time_payments_transfers)

    @cached_property
    def physical_cards(self) -> PhysicalCardsWithStreamingResponse:
        return PhysicalCardsWithStreamingResponse(self._simulations.physical_cards)


class AsyncSimulationsWithStreamingResponse:
    def __init__(self, simulations: AsyncSimulations) -> None:
        self._simulations = simulations

    @cached_property
    def account_transfers(self) -> AsyncAccountTransfersWithStreamingResponse:
        return AsyncAccountTransfersWithStreamingResponse(self._simulations.account_transfers)

    @cached_property
    def account_statements(self) -> AsyncAccountStatementsWithStreamingResponse:
        return AsyncAccountStatementsWithStreamingResponse(self._simulations.account_statements)

    @cached_property
    def ach_transfers(self) -> AsyncACHTransfersWithStreamingResponse:
        return AsyncACHTransfersWithStreamingResponse(self._simulations.ach_transfers)

    @cached_property
    def card_disputes(self) -> AsyncCardDisputesWithStreamingResponse:
        return AsyncCardDisputesWithStreamingResponse(self._simulations.card_disputes)

    @cached_property
    def card_profiles(self) -> AsyncCardProfilesWithStreamingResponse:
        return AsyncCardProfilesWithStreamingResponse(self._simulations.card_profiles)

    @cached_property
    def card_refunds(self) -> AsyncCardRefundsWithStreamingResponse:
        return AsyncCardRefundsWithStreamingResponse(self._simulations.card_refunds)

    @cached_property
    def check_transfers(self) -> AsyncCheckTransfersWithStreamingResponse:
        return AsyncCheckTransfersWithStreamingResponse(self._simulations.check_transfers)

    @cached_property
    def documents(self) -> AsyncDocumentsWithStreamingResponse:
        return AsyncDocumentsWithStreamingResponse(self._simulations.documents)

    @cached_property
    def digital_wallet_token_requests(self) -> AsyncDigitalWalletTokenRequestsWithStreamingResponse:
        return AsyncDigitalWalletTokenRequestsWithStreamingResponse(self._simulations.digital_wallet_token_requests)

    @cached_property
    def check_deposits(self) -> AsyncCheckDepositsWithStreamingResponse:
        return AsyncCheckDepositsWithStreamingResponse(self._simulations.check_deposits)

    @cached_property
    def programs(self) -> AsyncProgramsWithStreamingResponse:
        return AsyncProgramsWithStreamingResponse(self._simulations.programs)

    @cached_property
    def inbound_wire_drawdown_requests(self) -> AsyncInboundWireDrawdownRequestsWithStreamingResponse:
        return AsyncInboundWireDrawdownRequestsWithStreamingResponse(self._simulations.inbound_wire_drawdown_requests)

    @cached_property
    def inbound_funds_holds(self) -> AsyncInboundFundsHoldsWithStreamingResponse:
        return AsyncInboundFundsHoldsWithStreamingResponse(self._simulations.inbound_funds_holds)

    @cached_property
    def interest_payments(self) -> AsyncInterestPaymentsWithStreamingResponse:
        return AsyncInterestPaymentsWithStreamingResponse(self._simulations.interest_payments)

    @cached_property
    def wire_transfers(self) -> AsyncWireTransfersWithStreamingResponse:
        return AsyncWireTransfersWithStreamingResponse(self._simulations.wire_transfers)

    @cached_property
    def cards(self) -> AsyncCardsWithStreamingResponse:
        return AsyncCardsWithStreamingResponse(self._simulations.cards)

    @cached_property
    def real_time_payments_transfers(self) -> AsyncRealTimePaymentsTransfersWithStreamingResponse:
        return AsyncRealTimePaymentsTransfersWithStreamingResponse(self._simulations.real_time_payments_transfers)

    @cached_property
    def physical_cards(self) -> AsyncPhysicalCardsWithStreamingResponse:
        return AsyncPhysicalCardsWithStreamingResponse(self._simulations.physical_cards)
