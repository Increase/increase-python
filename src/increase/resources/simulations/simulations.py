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


class SimulationsWithStreamingResponse:
    def __init__(self, simulations: Simulations) -> None:
        self.account_transfers = AccountTransfersWithStreamingResponse(simulations.account_transfers)
        self.account_statements = AccountStatementsWithStreamingResponse(simulations.account_statements)
        self.ach_transfers = ACHTransfersWithStreamingResponse(simulations.ach_transfers)
        self.card_disputes = CardDisputesWithStreamingResponse(simulations.card_disputes)
        self.card_profiles = CardProfilesWithStreamingResponse(simulations.card_profiles)
        self.card_refunds = CardRefundsWithStreamingResponse(simulations.card_refunds)
        self.check_transfers = CheckTransfersWithStreamingResponse(simulations.check_transfers)
        self.documents = DocumentsWithStreamingResponse(simulations.documents)
        self.digital_wallet_token_requests = DigitalWalletTokenRequestsWithStreamingResponse(
            simulations.digital_wallet_token_requests
        )
        self.check_deposits = CheckDepositsWithStreamingResponse(simulations.check_deposits)
        self.programs = ProgramsWithStreamingResponse(simulations.programs)
        self.inbound_wire_drawdown_requests = InboundWireDrawdownRequestsWithStreamingResponse(
            simulations.inbound_wire_drawdown_requests
        )
        self.inbound_funds_holds = InboundFundsHoldsWithStreamingResponse(simulations.inbound_funds_holds)
        self.interest_payments = InterestPaymentsWithStreamingResponse(simulations.interest_payments)
        self.wire_transfers = WireTransfersWithStreamingResponse(simulations.wire_transfers)
        self.cards = CardsWithStreamingResponse(simulations.cards)
        self.real_time_payments_transfers = RealTimePaymentsTransfersWithStreamingResponse(
            simulations.real_time_payments_transfers
        )
        self.physical_cards = PhysicalCardsWithStreamingResponse(simulations.physical_cards)


class AsyncSimulationsWithStreamingResponse:
    def __init__(self, simulations: AsyncSimulations) -> None:
        self.account_transfers = AsyncAccountTransfersWithStreamingResponse(simulations.account_transfers)
        self.account_statements = AsyncAccountStatementsWithStreamingResponse(simulations.account_statements)
        self.ach_transfers = AsyncACHTransfersWithStreamingResponse(simulations.ach_transfers)
        self.card_disputes = AsyncCardDisputesWithStreamingResponse(simulations.card_disputes)
        self.card_profiles = AsyncCardProfilesWithStreamingResponse(simulations.card_profiles)
        self.card_refunds = AsyncCardRefundsWithStreamingResponse(simulations.card_refunds)
        self.check_transfers = AsyncCheckTransfersWithStreamingResponse(simulations.check_transfers)
        self.documents = AsyncDocumentsWithStreamingResponse(simulations.documents)
        self.digital_wallet_token_requests = AsyncDigitalWalletTokenRequestsWithStreamingResponse(
            simulations.digital_wallet_token_requests
        )
        self.check_deposits = AsyncCheckDepositsWithStreamingResponse(simulations.check_deposits)
        self.programs = AsyncProgramsWithStreamingResponse(simulations.programs)
        self.inbound_wire_drawdown_requests = AsyncInboundWireDrawdownRequestsWithStreamingResponse(
            simulations.inbound_wire_drawdown_requests
        )
        self.inbound_funds_holds = AsyncInboundFundsHoldsWithStreamingResponse(simulations.inbound_funds_holds)
        self.interest_payments = AsyncInterestPaymentsWithStreamingResponse(simulations.interest_payments)
        self.wire_transfers = AsyncWireTransfersWithStreamingResponse(simulations.wire_transfers)
        self.cards = AsyncCardsWithStreamingResponse(simulations.cards)
        self.real_time_payments_transfers = AsyncRealTimePaymentsTransfersWithStreamingResponse(
            simulations.real_time_payments_transfers
        )
        self.physical_cards = AsyncPhysicalCardsWithStreamingResponse(simulations.physical_cards)
