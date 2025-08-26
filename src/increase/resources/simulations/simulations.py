# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .programs import (
    ProgramsResource,
    AsyncProgramsResource,
    ProgramsResourceWithRawResponse,
    AsyncProgramsResourceWithRawResponse,
    ProgramsResourceWithStreamingResponse,
    AsyncProgramsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .documents import (
    DocumentsResource,
    AsyncDocumentsResource,
    DocumentsResourceWithRawResponse,
    AsyncDocumentsResourceWithRawResponse,
    DocumentsResourceWithStreamingResponse,
    AsyncDocumentsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .card_tokens import (
    CardTokensResource,
    AsyncCardTokensResource,
    CardTokensResourceWithRawResponse,
    AsyncCardTokensResourceWithRawResponse,
    CardTokensResourceWithStreamingResponse,
    AsyncCardTokensResourceWithStreamingResponse,
)
from .card_refunds import (
    CardRefundsResource,
    AsyncCardRefundsResource,
    CardRefundsResourceWithRawResponse,
    AsyncCardRefundsResourceWithRawResponse,
    CardRefundsResourceWithStreamingResponse,
    AsyncCardRefundsResourceWithStreamingResponse,
)
from .ach_transfers import (
    ACHTransfersResource,
    AsyncACHTransfersResource,
    ACHTransfersResourceWithRawResponse,
    AsyncACHTransfersResourceWithRawResponse,
    ACHTransfersResourceWithStreamingResponse,
    AsyncACHTransfersResourceWithStreamingResponse,
)
from .card_disputes import (
    CardDisputesResource,
    AsyncCardDisputesResource,
    CardDisputesResourceWithRawResponse,
    AsyncCardDisputesResourceWithRawResponse,
    CardDisputesResourceWithStreamingResponse,
    AsyncCardDisputesResourceWithStreamingResponse,
)
from .card_reversals import (
    CardReversalsResource,
    AsyncCardReversalsResource,
    CardReversalsResourceWithRawResponse,
    AsyncCardReversalsResourceWithRawResponse,
    CardReversalsResourceWithStreamingResponse,
    AsyncCardReversalsResourceWithStreamingResponse,
)
from .check_deposits import (
    CheckDepositsResource,
    AsyncCheckDepositsResource,
    CheckDepositsResourceWithRawResponse,
    AsyncCheckDepositsResourceWithRawResponse,
    CheckDepositsResourceWithStreamingResponse,
    AsyncCheckDepositsResourceWithStreamingResponse,
)
from .physical_cards import (
    PhysicalCardsResource,
    AsyncPhysicalCardsResource,
    PhysicalCardsResourceWithRawResponse,
    AsyncPhysicalCardsResourceWithRawResponse,
    PhysicalCardsResourceWithStreamingResponse,
    AsyncPhysicalCardsResourceWithStreamingResponse,
)
from .wire_transfers import (
    WireTransfersResource,
    AsyncWireTransfersResource,
    WireTransfersResourceWithRawResponse,
    AsyncWireTransfersResourceWithRawResponse,
    WireTransfersResourceWithStreamingResponse,
    AsyncWireTransfersResourceWithStreamingResponse,
)
from .card_increments import (
    CardIncrementsResource,
    AsyncCardIncrementsResource,
    CardIncrementsResourceWithRawResponse,
    AsyncCardIncrementsResourceWithRawResponse,
    CardIncrementsResourceWithStreamingResponse,
    AsyncCardIncrementsResourceWithStreamingResponse,
)
from .check_transfers import (
    CheckTransfersResource,
    AsyncCheckTransfersResource,
    CheckTransfersResourceWithRawResponse,
    AsyncCheckTransfersResourceWithRawResponse,
    CheckTransfersResourceWithStreamingResponse,
    AsyncCheckTransfersResourceWithStreamingResponse,
)
from .card_settlements import (
    CardSettlementsResource,
    AsyncCardSettlementsResource,
    CardSettlementsResourceWithRawResponse,
    AsyncCardSettlementsResourceWithRawResponse,
    CardSettlementsResourceWithStreamingResponse,
    AsyncCardSettlementsResourceWithStreamingResponse,
)
from .account_transfers import (
    AccountTransfersResource,
    AsyncAccountTransfersResource,
    AccountTransfersResourceWithRawResponse,
    AsyncAccountTransfersResourceWithRawResponse,
    AccountTransfersResourceWithStreamingResponse,
    AsyncAccountTransfersResourceWithStreamingResponse,
)
from .interest_payments import (
    InterestPaymentsResource,
    AsyncInterestPaymentsResource,
    InterestPaymentsResourceWithRawResponse,
    AsyncInterestPaymentsResourceWithRawResponse,
    InterestPaymentsResourceWithStreamingResponse,
    AsyncInterestPaymentsResourceWithStreamingResponse,
)
from .account_statements import (
    AccountStatementsResource,
    AsyncAccountStatementsResource,
    AccountStatementsResourceWithRawResponse,
    AsyncAccountStatementsResourceWithRawResponse,
    AccountStatementsResourceWithStreamingResponse,
    AsyncAccountStatementsResourceWithStreamingResponse,
)
from .inbound_mail_items import (
    InboundMailItemsResource,
    AsyncInboundMailItemsResource,
    InboundMailItemsResourceWithRawResponse,
    AsyncInboundMailItemsResourceWithRawResponse,
    InboundMailItemsResourceWithStreamingResponse,
    AsyncInboundMailItemsResourceWithStreamingResponse,
)
from .card_authorizations import (
    CardAuthorizationsResource,
    AsyncCardAuthorizationsResource,
    CardAuthorizationsResourceWithRawResponse,
    AsyncCardAuthorizationsResourceWithRawResponse,
    CardAuthorizationsResourceWithStreamingResponse,
    AsyncCardAuthorizationsResourceWithStreamingResponse,
)
from .pending_transactions import (
    PendingTransactionsResource,
    AsyncPendingTransactionsResource,
    PendingTransactionsResourceWithRawResponse,
    AsyncPendingTransactionsResourceWithRawResponse,
    PendingTransactionsResourceWithStreamingResponse,
    AsyncPendingTransactionsResourceWithStreamingResponse,
)
from .inbound_ach_transfers import (
    InboundACHTransfersResource,
    AsyncInboundACHTransfersResource,
    InboundACHTransfersResourceWithRawResponse,
    AsyncInboundACHTransfersResourceWithRawResponse,
    InboundACHTransfersResourceWithStreamingResponse,
    AsyncInboundACHTransfersResourceWithStreamingResponse,
)
from .inbound_check_deposits import (
    InboundCheckDepositsResource,
    AsyncInboundCheckDepositsResource,
    InboundCheckDepositsResourceWithRawResponse,
    AsyncInboundCheckDepositsResourceWithRawResponse,
    InboundCheckDepositsResourceWithStreamingResponse,
    AsyncInboundCheckDepositsResourceWithStreamingResponse,
)
from .inbound_wire_transfers import (
    InboundWireTransfersResource,
    AsyncInboundWireTransfersResource,
    InboundWireTransfersResourceWithRawResponse,
    AsyncInboundWireTransfersResourceWithRawResponse,
    InboundWireTransfersResourceWithStreamingResponse,
    AsyncInboundWireTransfersResourceWithStreamingResponse,
)
from .wire_drawdown_requests import (
    WireDrawdownRequestsResource,
    AsyncWireDrawdownRequestsResource,
    WireDrawdownRequestsResourceWithRawResponse,
    AsyncWireDrawdownRequestsResourceWithRawResponse,
    WireDrawdownRequestsResourceWithStreamingResponse,
    AsyncWireDrawdownRequestsResourceWithStreamingResponse,
)
from .card_fuel_confirmations import (
    CardFuelConfirmationsResource,
    AsyncCardFuelConfirmationsResource,
    CardFuelConfirmationsResourceWithRawResponse,
    AsyncCardFuelConfirmationsResourceWithRawResponse,
    CardFuelConfirmationsResourceWithStreamingResponse,
    AsyncCardFuelConfirmationsResourceWithStreamingResponse,
)
from .real_time_payments_transfers import (
    RealTimePaymentsTransfersResource,
    AsyncRealTimePaymentsTransfersResource,
    RealTimePaymentsTransfersResourceWithRawResponse,
    AsyncRealTimePaymentsTransfersResourceWithRawResponse,
    RealTimePaymentsTransfersResourceWithStreamingResponse,
    AsyncRealTimePaymentsTransfersResourceWithStreamingResponse,
)
from .digital_wallet_token_requests import (
    DigitalWalletTokenRequestsResource,
    AsyncDigitalWalletTokenRequestsResource,
    DigitalWalletTokenRequestsResourceWithRawResponse,
    AsyncDigitalWalletTokenRequestsResourceWithRawResponse,
    DigitalWalletTokenRequestsResourceWithStreamingResponse,
    AsyncDigitalWalletTokenRequestsResourceWithStreamingResponse,
)
from .card_authorization_expirations import (
    CardAuthorizationExpirationsResource,
    AsyncCardAuthorizationExpirationsResource,
    CardAuthorizationExpirationsResourceWithRawResponse,
    AsyncCardAuthorizationExpirationsResourceWithRawResponse,
    CardAuthorizationExpirationsResourceWithStreamingResponse,
    AsyncCardAuthorizationExpirationsResourceWithStreamingResponse,
)
from .inbound_wire_drawdown_requests import (
    InboundWireDrawdownRequestsResource,
    AsyncInboundWireDrawdownRequestsResource,
    InboundWireDrawdownRequestsResourceWithRawResponse,
    AsyncInboundWireDrawdownRequestsResourceWithRawResponse,
    InboundWireDrawdownRequestsResourceWithStreamingResponse,
    AsyncInboundWireDrawdownRequestsResourceWithStreamingResponse,
)
from .inbound_real_time_payments_transfers import (
    InboundRealTimePaymentsTransfersResource,
    AsyncInboundRealTimePaymentsTransfersResource,
    InboundRealTimePaymentsTransfersResourceWithRawResponse,
    AsyncInboundRealTimePaymentsTransfersResourceWithRawResponse,
    InboundRealTimePaymentsTransfersResourceWithStreamingResponse,
    AsyncInboundRealTimePaymentsTransfersResourceWithStreamingResponse,
)

__all__ = ["SimulationsResource", "AsyncSimulationsResource"]


class SimulationsResource(SyncAPIResource):
    @cached_property
    def interest_payments(self) -> InterestPaymentsResource:
        return InterestPaymentsResource(self._client)

    @cached_property
    def card_authorizations(self) -> CardAuthorizationsResource:
        return CardAuthorizationsResource(self._client)

    @cached_property
    def card_authorization_expirations(self) -> CardAuthorizationExpirationsResource:
        return CardAuthorizationExpirationsResource(self._client)

    @cached_property
    def card_settlements(self) -> CardSettlementsResource:
        return CardSettlementsResource(self._client)

    @cached_property
    def card_reversals(self) -> CardReversalsResource:
        return CardReversalsResource(self._client)

    @cached_property
    def card_increments(self) -> CardIncrementsResource:
        return CardIncrementsResource(self._client)

    @cached_property
    def card_fuel_confirmations(self) -> CardFuelConfirmationsResource:
        return CardFuelConfirmationsResource(self._client)

    @cached_property
    def card_refunds(self) -> CardRefundsResource:
        return CardRefundsResource(self._client)

    @cached_property
    def card_disputes(self) -> CardDisputesResource:
        return CardDisputesResource(self._client)

    @cached_property
    def physical_cards(self) -> PhysicalCardsResource:
        return PhysicalCardsResource(self._client)

    @cached_property
    def digital_wallet_token_requests(self) -> DigitalWalletTokenRequestsResource:
        return DigitalWalletTokenRequestsResource(self._client)

    @cached_property
    def pending_transactions(self) -> PendingTransactionsResource:
        return PendingTransactionsResource(self._client)

    @cached_property
    def account_transfers(self) -> AccountTransfersResource:
        return AccountTransfersResource(self._client)

    @cached_property
    def ach_transfers(self) -> ACHTransfersResource:
        return ACHTransfersResource(self._client)

    @cached_property
    def inbound_ach_transfers(self) -> InboundACHTransfersResource:
        return InboundACHTransfersResource(self._client)

    @cached_property
    def wire_transfers(self) -> WireTransfersResource:
        return WireTransfersResource(self._client)

    @cached_property
    def inbound_wire_transfers(self) -> InboundWireTransfersResource:
        return InboundWireTransfersResource(self._client)

    @cached_property
    def wire_drawdown_requests(self) -> WireDrawdownRequestsResource:
        return WireDrawdownRequestsResource(self._client)

    @cached_property
    def inbound_wire_drawdown_requests(self) -> InboundWireDrawdownRequestsResource:
        return InboundWireDrawdownRequestsResource(self._client)

    @cached_property
    def check_transfers(self) -> CheckTransfersResource:
        return CheckTransfersResource(self._client)

    @cached_property
    def inbound_check_deposits(self) -> InboundCheckDepositsResource:
        return InboundCheckDepositsResource(self._client)

    @cached_property
    def real_time_payments_transfers(self) -> RealTimePaymentsTransfersResource:
        return RealTimePaymentsTransfersResource(self._client)

    @cached_property
    def inbound_real_time_payments_transfers(self) -> InboundRealTimePaymentsTransfersResource:
        return InboundRealTimePaymentsTransfersResource(self._client)

    @cached_property
    def check_deposits(self) -> CheckDepositsResource:
        return CheckDepositsResource(self._client)

    @cached_property
    def inbound_mail_items(self) -> InboundMailItemsResource:
        return InboundMailItemsResource(self._client)

    @cached_property
    def programs(self) -> ProgramsResource:
        return ProgramsResource(self._client)

    @cached_property
    def account_statements(self) -> AccountStatementsResource:
        return AccountStatementsResource(self._client)

    @cached_property
    def documents(self) -> DocumentsResource:
        return DocumentsResource(self._client)

    @cached_property
    def card_tokens(self) -> CardTokensResource:
        return CardTokensResource(self._client)

    @cached_property
    def with_raw_response(self) -> SimulationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return SimulationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return SimulationsResourceWithStreamingResponse(self)


class AsyncSimulationsResource(AsyncAPIResource):
    @cached_property
    def interest_payments(self) -> AsyncInterestPaymentsResource:
        return AsyncInterestPaymentsResource(self._client)

    @cached_property
    def card_authorizations(self) -> AsyncCardAuthorizationsResource:
        return AsyncCardAuthorizationsResource(self._client)

    @cached_property
    def card_authorization_expirations(self) -> AsyncCardAuthorizationExpirationsResource:
        return AsyncCardAuthorizationExpirationsResource(self._client)

    @cached_property
    def card_settlements(self) -> AsyncCardSettlementsResource:
        return AsyncCardSettlementsResource(self._client)

    @cached_property
    def card_reversals(self) -> AsyncCardReversalsResource:
        return AsyncCardReversalsResource(self._client)

    @cached_property
    def card_increments(self) -> AsyncCardIncrementsResource:
        return AsyncCardIncrementsResource(self._client)

    @cached_property
    def card_fuel_confirmations(self) -> AsyncCardFuelConfirmationsResource:
        return AsyncCardFuelConfirmationsResource(self._client)

    @cached_property
    def card_refunds(self) -> AsyncCardRefundsResource:
        return AsyncCardRefundsResource(self._client)

    @cached_property
    def card_disputes(self) -> AsyncCardDisputesResource:
        return AsyncCardDisputesResource(self._client)

    @cached_property
    def physical_cards(self) -> AsyncPhysicalCardsResource:
        return AsyncPhysicalCardsResource(self._client)

    @cached_property
    def digital_wallet_token_requests(self) -> AsyncDigitalWalletTokenRequestsResource:
        return AsyncDigitalWalletTokenRequestsResource(self._client)

    @cached_property
    def pending_transactions(self) -> AsyncPendingTransactionsResource:
        return AsyncPendingTransactionsResource(self._client)

    @cached_property
    def account_transfers(self) -> AsyncAccountTransfersResource:
        return AsyncAccountTransfersResource(self._client)

    @cached_property
    def ach_transfers(self) -> AsyncACHTransfersResource:
        return AsyncACHTransfersResource(self._client)

    @cached_property
    def inbound_ach_transfers(self) -> AsyncInboundACHTransfersResource:
        return AsyncInboundACHTransfersResource(self._client)

    @cached_property
    def wire_transfers(self) -> AsyncWireTransfersResource:
        return AsyncWireTransfersResource(self._client)

    @cached_property
    def inbound_wire_transfers(self) -> AsyncInboundWireTransfersResource:
        return AsyncInboundWireTransfersResource(self._client)

    @cached_property
    def wire_drawdown_requests(self) -> AsyncWireDrawdownRequestsResource:
        return AsyncWireDrawdownRequestsResource(self._client)

    @cached_property
    def inbound_wire_drawdown_requests(self) -> AsyncInboundWireDrawdownRequestsResource:
        return AsyncInboundWireDrawdownRequestsResource(self._client)

    @cached_property
    def check_transfers(self) -> AsyncCheckTransfersResource:
        return AsyncCheckTransfersResource(self._client)

    @cached_property
    def inbound_check_deposits(self) -> AsyncInboundCheckDepositsResource:
        return AsyncInboundCheckDepositsResource(self._client)

    @cached_property
    def real_time_payments_transfers(self) -> AsyncRealTimePaymentsTransfersResource:
        return AsyncRealTimePaymentsTransfersResource(self._client)

    @cached_property
    def inbound_real_time_payments_transfers(self) -> AsyncInboundRealTimePaymentsTransfersResource:
        return AsyncInboundRealTimePaymentsTransfersResource(self._client)

    @cached_property
    def check_deposits(self) -> AsyncCheckDepositsResource:
        return AsyncCheckDepositsResource(self._client)

    @cached_property
    def inbound_mail_items(self) -> AsyncInboundMailItemsResource:
        return AsyncInboundMailItemsResource(self._client)

    @cached_property
    def programs(self) -> AsyncProgramsResource:
        return AsyncProgramsResource(self._client)

    @cached_property
    def account_statements(self) -> AsyncAccountStatementsResource:
        return AsyncAccountStatementsResource(self._client)

    @cached_property
    def documents(self) -> AsyncDocumentsResource:
        return AsyncDocumentsResource(self._client)

    @cached_property
    def card_tokens(self) -> AsyncCardTokensResource:
        return AsyncCardTokensResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSimulationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncSimulationsResourceWithStreamingResponse(self)


class SimulationsResourceWithRawResponse:
    def __init__(self, simulations: SimulationsResource) -> None:
        self._simulations = simulations

    @cached_property
    def interest_payments(self) -> InterestPaymentsResourceWithRawResponse:
        return InterestPaymentsResourceWithRawResponse(self._simulations.interest_payments)

    @cached_property
    def card_authorizations(self) -> CardAuthorizationsResourceWithRawResponse:
        return CardAuthorizationsResourceWithRawResponse(self._simulations.card_authorizations)

    @cached_property
    def card_authorization_expirations(self) -> CardAuthorizationExpirationsResourceWithRawResponse:
        return CardAuthorizationExpirationsResourceWithRawResponse(self._simulations.card_authorization_expirations)

    @cached_property
    def card_settlements(self) -> CardSettlementsResourceWithRawResponse:
        return CardSettlementsResourceWithRawResponse(self._simulations.card_settlements)

    @cached_property
    def card_reversals(self) -> CardReversalsResourceWithRawResponse:
        return CardReversalsResourceWithRawResponse(self._simulations.card_reversals)

    @cached_property
    def card_increments(self) -> CardIncrementsResourceWithRawResponse:
        return CardIncrementsResourceWithRawResponse(self._simulations.card_increments)

    @cached_property
    def card_fuel_confirmations(self) -> CardFuelConfirmationsResourceWithRawResponse:
        return CardFuelConfirmationsResourceWithRawResponse(self._simulations.card_fuel_confirmations)

    @cached_property
    def card_refunds(self) -> CardRefundsResourceWithRawResponse:
        return CardRefundsResourceWithRawResponse(self._simulations.card_refunds)

    @cached_property
    def card_disputes(self) -> CardDisputesResourceWithRawResponse:
        return CardDisputesResourceWithRawResponse(self._simulations.card_disputes)

    @cached_property
    def physical_cards(self) -> PhysicalCardsResourceWithRawResponse:
        return PhysicalCardsResourceWithRawResponse(self._simulations.physical_cards)

    @cached_property
    def digital_wallet_token_requests(self) -> DigitalWalletTokenRequestsResourceWithRawResponse:
        return DigitalWalletTokenRequestsResourceWithRawResponse(self._simulations.digital_wallet_token_requests)

    @cached_property
    def pending_transactions(self) -> PendingTransactionsResourceWithRawResponse:
        return PendingTransactionsResourceWithRawResponse(self._simulations.pending_transactions)

    @cached_property
    def account_transfers(self) -> AccountTransfersResourceWithRawResponse:
        return AccountTransfersResourceWithRawResponse(self._simulations.account_transfers)

    @cached_property
    def ach_transfers(self) -> ACHTransfersResourceWithRawResponse:
        return ACHTransfersResourceWithRawResponse(self._simulations.ach_transfers)

    @cached_property
    def inbound_ach_transfers(self) -> InboundACHTransfersResourceWithRawResponse:
        return InboundACHTransfersResourceWithRawResponse(self._simulations.inbound_ach_transfers)

    @cached_property
    def wire_transfers(self) -> WireTransfersResourceWithRawResponse:
        return WireTransfersResourceWithRawResponse(self._simulations.wire_transfers)

    @cached_property
    def inbound_wire_transfers(self) -> InboundWireTransfersResourceWithRawResponse:
        return InboundWireTransfersResourceWithRawResponse(self._simulations.inbound_wire_transfers)

    @cached_property
    def wire_drawdown_requests(self) -> WireDrawdownRequestsResourceWithRawResponse:
        return WireDrawdownRequestsResourceWithRawResponse(self._simulations.wire_drawdown_requests)

    @cached_property
    def inbound_wire_drawdown_requests(self) -> InboundWireDrawdownRequestsResourceWithRawResponse:
        return InboundWireDrawdownRequestsResourceWithRawResponse(self._simulations.inbound_wire_drawdown_requests)

    @cached_property
    def check_transfers(self) -> CheckTransfersResourceWithRawResponse:
        return CheckTransfersResourceWithRawResponse(self._simulations.check_transfers)

    @cached_property
    def inbound_check_deposits(self) -> InboundCheckDepositsResourceWithRawResponse:
        return InboundCheckDepositsResourceWithRawResponse(self._simulations.inbound_check_deposits)

    @cached_property
    def real_time_payments_transfers(self) -> RealTimePaymentsTransfersResourceWithRawResponse:
        return RealTimePaymentsTransfersResourceWithRawResponse(self._simulations.real_time_payments_transfers)

    @cached_property
    def inbound_real_time_payments_transfers(self) -> InboundRealTimePaymentsTransfersResourceWithRawResponse:
        return InboundRealTimePaymentsTransfersResourceWithRawResponse(
            self._simulations.inbound_real_time_payments_transfers
        )

    @cached_property
    def check_deposits(self) -> CheckDepositsResourceWithRawResponse:
        return CheckDepositsResourceWithRawResponse(self._simulations.check_deposits)

    @cached_property
    def inbound_mail_items(self) -> InboundMailItemsResourceWithRawResponse:
        return InboundMailItemsResourceWithRawResponse(self._simulations.inbound_mail_items)

    @cached_property
    def programs(self) -> ProgramsResourceWithRawResponse:
        return ProgramsResourceWithRawResponse(self._simulations.programs)

    @cached_property
    def account_statements(self) -> AccountStatementsResourceWithRawResponse:
        return AccountStatementsResourceWithRawResponse(self._simulations.account_statements)

    @cached_property
    def documents(self) -> DocumentsResourceWithRawResponse:
        return DocumentsResourceWithRawResponse(self._simulations.documents)

    @cached_property
    def card_tokens(self) -> CardTokensResourceWithRawResponse:
        return CardTokensResourceWithRawResponse(self._simulations.card_tokens)


class AsyncSimulationsResourceWithRawResponse:
    def __init__(self, simulations: AsyncSimulationsResource) -> None:
        self._simulations = simulations

    @cached_property
    def interest_payments(self) -> AsyncInterestPaymentsResourceWithRawResponse:
        return AsyncInterestPaymentsResourceWithRawResponse(self._simulations.interest_payments)

    @cached_property
    def card_authorizations(self) -> AsyncCardAuthorizationsResourceWithRawResponse:
        return AsyncCardAuthorizationsResourceWithRawResponse(self._simulations.card_authorizations)

    @cached_property
    def card_authorization_expirations(self) -> AsyncCardAuthorizationExpirationsResourceWithRawResponse:
        return AsyncCardAuthorizationExpirationsResourceWithRawResponse(
            self._simulations.card_authorization_expirations
        )

    @cached_property
    def card_settlements(self) -> AsyncCardSettlementsResourceWithRawResponse:
        return AsyncCardSettlementsResourceWithRawResponse(self._simulations.card_settlements)

    @cached_property
    def card_reversals(self) -> AsyncCardReversalsResourceWithRawResponse:
        return AsyncCardReversalsResourceWithRawResponse(self._simulations.card_reversals)

    @cached_property
    def card_increments(self) -> AsyncCardIncrementsResourceWithRawResponse:
        return AsyncCardIncrementsResourceWithRawResponse(self._simulations.card_increments)

    @cached_property
    def card_fuel_confirmations(self) -> AsyncCardFuelConfirmationsResourceWithRawResponse:
        return AsyncCardFuelConfirmationsResourceWithRawResponse(self._simulations.card_fuel_confirmations)

    @cached_property
    def card_refunds(self) -> AsyncCardRefundsResourceWithRawResponse:
        return AsyncCardRefundsResourceWithRawResponse(self._simulations.card_refunds)

    @cached_property
    def card_disputes(self) -> AsyncCardDisputesResourceWithRawResponse:
        return AsyncCardDisputesResourceWithRawResponse(self._simulations.card_disputes)

    @cached_property
    def physical_cards(self) -> AsyncPhysicalCardsResourceWithRawResponse:
        return AsyncPhysicalCardsResourceWithRawResponse(self._simulations.physical_cards)

    @cached_property
    def digital_wallet_token_requests(self) -> AsyncDigitalWalletTokenRequestsResourceWithRawResponse:
        return AsyncDigitalWalletTokenRequestsResourceWithRawResponse(self._simulations.digital_wallet_token_requests)

    @cached_property
    def pending_transactions(self) -> AsyncPendingTransactionsResourceWithRawResponse:
        return AsyncPendingTransactionsResourceWithRawResponse(self._simulations.pending_transactions)

    @cached_property
    def account_transfers(self) -> AsyncAccountTransfersResourceWithRawResponse:
        return AsyncAccountTransfersResourceWithRawResponse(self._simulations.account_transfers)

    @cached_property
    def ach_transfers(self) -> AsyncACHTransfersResourceWithRawResponse:
        return AsyncACHTransfersResourceWithRawResponse(self._simulations.ach_transfers)

    @cached_property
    def inbound_ach_transfers(self) -> AsyncInboundACHTransfersResourceWithRawResponse:
        return AsyncInboundACHTransfersResourceWithRawResponse(self._simulations.inbound_ach_transfers)

    @cached_property
    def wire_transfers(self) -> AsyncWireTransfersResourceWithRawResponse:
        return AsyncWireTransfersResourceWithRawResponse(self._simulations.wire_transfers)

    @cached_property
    def inbound_wire_transfers(self) -> AsyncInboundWireTransfersResourceWithRawResponse:
        return AsyncInboundWireTransfersResourceWithRawResponse(self._simulations.inbound_wire_transfers)

    @cached_property
    def wire_drawdown_requests(self) -> AsyncWireDrawdownRequestsResourceWithRawResponse:
        return AsyncWireDrawdownRequestsResourceWithRawResponse(self._simulations.wire_drawdown_requests)

    @cached_property
    def inbound_wire_drawdown_requests(self) -> AsyncInboundWireDrawdownRequestsResourceWithRawResponse:
        return AsyncInboundWireDrawdownRequestsResourceWithRawResponse(self._simulations.inbound_wire_drawdown_requests)

    @cached_property
    def check_transfers(self) -> AsyncCheckTransfersResourceWithRawResponse:
        return AsyncCheckTransfersResourceWithRawResponse(self._simulations.check_transfers)

    @cached_property
    def inbound_check_deposits(self) -> AsyncInboundCheckDepositsResourceWithRawResponse:
        return AsyncInboundCheckDepositsResourceWithRawResponse(self._simulations.inbound_check_deposits)

    @cached_property
    def real_time_payments_transfers(self) -> AsyncRealTimePaymentsTransfersResourceWithRawResponse:
        return AsyncRealTimePaymentsTransfersResourceWithRawResponse(self._simulations.real_time_payments_transfers)

    @cached_property
    def inbound_real_time_payments_transfers(self) -> AsyncInboundRealTimePaymentsTransfersResourceWithRawResponse:
        return AsyncInboundRealTimePaymentsTransfersResourceWithRawResponse(
            self._simulations.inbound_real_time_payments_transfers
        )

    @cached_property
    def check_deposits(self) -> AsyncCheckDepositsResourceWithRawResponse:
        return AsyncCheckDepositsResourceWithRawResponse(self._simulations.check_deposits)

    @cached_property
    def inbound_mail_items(self) -> AsyncInboundMailItemsResourceWithRawResponse:
        return AsyncInboundMailItemsResourceWithRawResponse(self._simulations.inbound_mail_items)

    @cached_property
    def programs(self) -> AsyncProgramsResourceWithRawResponse:
        return AsyncProgramsResourceWithRawResponse(self._simulations.programs)

    @cached_property
    def account_statements(self) -> AsyncAccountStatementsResourceWithRawResponse:
        return AsyncAccountStatementsResourceWithRawResponse(self._simulations.account_statements)

    @cached_property
    def documents(self) -> AsyncDocumentsResourceWithRawResponse:
        return AsyncDocumentsResourceWithRawResponse(self._simulations.documents)

    @cached_property
    def card_tokens(self) -> AsyncCardTokensResourceWithRawResponse:
        return AsyncCardTokensResourceWithRawResponse(self._simulations.card_tokens)


class SimulationsResourceWithStreamingResponse:
    def __init__(self, simulations: SimulationsResource) -> None:
        self._simulations = simulations

    @cached_property
    def interest_payments(self) -> InterestPaymentsResourceWithStreamingResponse:
        return InterestPaymentsResourceWithStreamingResponse(self._simulations.interest_payments)

    @cached_property
    def card_authorizations(self) -> CardAuthorizationsResourceWithStreamingResponse:
        return CardAuthorizationsResourceWithStreamingResponse(self._simulations.card_authorizations)

    @cached_property
    def card_authorization_expirations(self) -> CardAuthorizationExpirationsResourceWithStreamingResponse:
        return CardAuthorizationExpirationsResourceWithStreamingResponse(
            self._simulations.card_authorization_expirations
        )

    @cached_property
    def card_settlements(self) -> CardSettlementsResourceWithStreamingResponse:
        return CardSettlementsResourceWithStreamingResponse(self._simulations.card_settlements)

    @cached_property
    def card_reversals(self) -> CardReversalsResourceWithStreamingResponse:
        return CardReversalsResourceWithStreamingResponse(self._simulations.card_reversals)

    @cached_property
    def card_increments(self) -> CardIncrementsResourceWithStreamingResponse:
        return CardIncrementsResourceWithStreamingResponse(self._simulations.card_increments)

    @cached_property
    def card_fuel_confirmations(self) -> CardFuelConfirmationsResourceWithStreamingResponse:
        return CardFuelConfirmationsResourceWithStreamingResponse(self._simulations.card_fuel_confirmations)

    @cached_property
    def card_refunds(self) -> CardRefundsResourceWithStreamingResponse:
        return CardRefundsResourceWithStreamingResponse(self._simulations.card_refunds)

    @cached_property
    def card_disputes(self) -> CardDisputesResourceWithStreamingResponse:
        return CardDisputesResourceWithStreamingResponse(self._simulations.card_disputes)

    @cached_property
    def physical_cards(self) -> PhysicalCardsResourceWithStreamingResponse:
        return PhysicalCardsResourceWithStreamingResponse(self._simulations.physical_cards)

    @cached_property
    def digital_wallet_token_requests(self) -> DigitalWalletTokenRequestsResourceWithStreamingResponse:
        return DigitalWalletTokenRequestsResourceWithStreamingResponse(self._simulations.digital_wallet_token_requests)

    @cached_property
    def pending_transactions(self) -> PendingTransactionsResourceWithStreamingResponse:
        return PendingTransactionsResourceWithStreamingResponse(self._simulations.pending_transactions)

    @cached_property
    def account_transfers(self) -> AccountTransfersResourceWithStreamingResponse:
        return AccountTransfersResourceWithStreamingResponse(self._simulations.account_transfers)

    @cached_property
    def ach_transfers(self) -> ACHTransfersResourceWithStreamingResponse:
        return ACHTransfersResourceWithStreamingResponse(self._simulations.ach_transfers)

    @cached_property
    def inbound_ach_transfers(self) -> InboundACHTransfersResourceWithStreamingResponse:
        return InboundACHTransfersResourceWithStreamingResponse(self._simulations.inbound_ach_transfers)

    @cached_property
    def wire_transfers(self) -> WireTransfersResourceWithStreamingResponse:
        return WireTransfersResourceWithStreamingResponse(self._simulations.wire_transfers)

    @cached_property
    def inbound_wire_transfers(self) -> InboundWireTransfersResourceWithStreamingResponse:
        return InboundWireTransfersResourceWithStreamingResponse(self._simulations.inbound_wire_transfers)

    @cached_property
    def wire_drawdown_requests(self) -> WireDrawdownRequestsResourceWithStreamingResponse:
        return WireDrawdownRequestsResourceWithStreamingResponse(self._simulations.wire_drawdown_requests)

    @cached_property
    def inbound_wire_drawdown_requests(self) -> InboundWireDrawdownRequestsResourceWithStreamingResponse:
        return InboundWireDrawdownRequestsResourceWithStreamingResponse(
            self._simulations.inbound_wire_drawdown_requests
        )

    @cached_property
    def check_transfers(self) -> CheckTransfersResourceWithStreamingResponse:
        return CheckTransfersResourceWithStreamingResponse(self._simulations.check_transfers)

    @cached_property
    def inbound_check_deposits(self) -> InboundCheckDepositsResourceWithStreamingResponse:
        return InboundCheckDepositsResourceWithStreamingResponse(self._simulations.inbound_check_deposits)

    @cached_property
    def real_time_payments_transfers(self) -> RealTimePaymentsTransfersResourceWithStreamingResponse:
        return RealTimePaymentsTransfersResourceWithStreamingResponse(self._simulations.real_time_payments_transfers)

    @cached_property
    def inbound_real_time_payments_transfers(self) -> InboundRealTimePaymentsTransfersResourceWithStreamingResponse:
        return InboundRealTimePaymentsTransfersResourceWithStreamingResponse(
            self._simulations.inbound_real_time_payments_transfers
        )

    @cached_property
    def check_deposits(self) -> CheckDepositsResourceWithStreamingResponse:
        return CheckDepositsResourceWithStreamingResponse(self._simulations.check_deposits)

    @cached_property
    def inbound_mail_items(self) -> InboundMailItemsResourceWithStreamingResponse:
        return InboundMailItemsResourceWithStreamingResponse(self._simulations.inbound_mail_items)

    @cached_property
    def programs(self) -> ProgramsResourceWithStreamingResponse:
        return ProgramsResourceWithStreamingResponse(self._simulations.programs)

    @cached_property
    def account_statements(self) -> AccountStatementsResourceWithStreamingResponse:
        return AccountStatementsResourceWithStreamingResponse(self._simulations.account_statements)

    @cached_property
    def documents(self) -> DocumentsResourceWithStreamingResponse:
        return DocumentsResourceWithStreamingResponse(self._simulations.documents)

    @cached_property
    def card_tokens(self) -> CardTokensResourceWithStreamingResponse:
        return CardTokensResourceWithStreamingResponse(self._simulations.card_tokens)


class AsyncSimulationsResourceWithStreamingResponse:
    def __init__(self, simulations: AsyncSimulationsResource) -> None:
        self._simulations = simulations

    @cached_property
    def interest_payments(self) -> AsyncInterestPaymentsResourceWithStreamingResponse:
        return AsyncInterestPaymentsResourceWithStreamingResponse(self._simulations.interest_payments)

    @cached_property
    def card_authorizations(self) -> AsyncCardAuthorizationsResourceWithStreamingResponse:
        return AsyncCardAuthorizationsResourceWithStreamingResponse(self._simulations.card_authorizations)

    @cached_property
    def card_authorization_expirations(self) -> AsyncCardAuthorizationExpirationsResourceWithStreamingResponse:
        return AsyncCardAuthorizationExpirationsResourceWithStreamingResponse(
            self._simulations.card_authorization_expirations
        )

    @cached_property
    def card_settlements(self) -> AsyncCardSettlementsResourceWithStreamingResponse:
        return AsyncCardSettlementsResourceWithStreamingResponse(self._simulations.card_settlements)

    @cached_property
    def card_reversals(self) -> AsyncCardReversalsResourceWithStreamingResponse:
        return AsyncCardReversalsResourceWithStreamingResponse(self._simulations.card_reversals)

    @cached_property
    def card_increments(self) -> AsyncCardIncrementsResourceWithStreamingResponse:
        return AsyncCardIncrementsResourceWithStreamingResponse(self._simulations.card_increments)

    @cached_property
    def card_fuel_confirmations(self) -> AsyncCardFuelConfirmationsResourceWithStreamingResponse:
        return AsyncCardFuelConfirmationsResourceWithStreamingResponse(self._simulations.card_fuel_confirmations)

    @cached_property
    def card_refunds(self) -> AsyncCardRefundsResourceWithStreamingResponse:
        return AsyncCardRefundsResourceWithStreamingResponse(self._simulations.card_refunds)

    @cached_property
    def card_disputes(self) -> AsyncCardDisputesResourceWithStreamingResponse:
        return AsyncCardDisputesResourceWithStreamingResponse(self._simulations.card_disputes)

    @cached_property
    def physical_cards(self) -> AsyncPhysicalCardsResourceWithStreamingResponse:
        return AsyncPhysicalCardsResourceWithStreamingResponse(self._simulations.physical_cards)

    @cached_property
    def digital_wallet_token_requests(self) -> AsyncDigitalWalletTokenRequestsResourceWithStreamingResponse:
        return AsyncDigitalWalletTokenRequestsResourceWithStreamingResponse(
            self._simulations.digital_wallet_token_requests
        )

    @cached_property
    def pending_transactions(self) -> AsyncPendingTransactionsResourceWithStreamingResponse:
        return AsyncPendingTransactionsResourceWithStreamingResponse(self._simulations.pending_transactions)

    @cached_property
    def account_transfers(self) -> AsyncAccountTransfersResourceWithStreamingResponse:
        return AsyncAccountTransfersResourceWithStreamingResponse(self._simulations.account_transfers)

    @cached_property
    def ach_transfers(self) -> AsyncACHTransfersResourceWithStreamingResponse:
        return AsyncACHTransfersResourceWithStreamingResponse(self._simulations.ach_transfers)

    @cached_property
    def inbound_ach_transfers(self) -> AsyncInboundACHTransfersResourceWithStreamingResponse:
        return AsyncInboundACHTransfersResourceWithStreamingResponse(self._simulations.inbound_ach_transfers)

    @cached_property
    def wire_transfers(self) -> AsyncWireTransfersResourceWithStreamingResponse:
        return AsyncWireTransfersResourceWithStreamingResponse(self._simulations.wire_transfers)

    @cached_property
    def inbound_wire_transfers(self) -> AsyncInboundWireTransfersResourceWithStreamingResponse:
        return AsyncInboundWireTransfersResourceWithStreamingResponse(self._simulations.inbound_wire_transfers)

    @cached_property
    def wire_drawdown_requests(self) -> AsyncWireDrawdownRequestsResourceWithStreamingResponse:
        return AsyncWireDrawdownRequestsResourceWithStreamingResponse(self._simulations.wire_drawdown_requests)

    @cached_property
    def inbound_wire_drawdown_requests(self) -> AsyncInboundWireDrawdownRequestsResourceWithStreamingResponse:
        return AsyncInboundWireDrawdownRequestsResourceWithStreamingResponse(
            self._simulations.inbound_wire_drawdown_requests
        )

    @cached_property
    def check_transfers(self) -> AsyncCheckTransfersResourceWithStreamingResponse:
        return AsyncCheckTransfersResourceWithStreamingResponse(self._simulations.check_transfers)

    @cached_property
    def inbound_check_deposits(self) -> AsyncInboundCheckDepositsResourceWithStreamingResponse:
        return AsyncInboundCheckDepositsResourceWithStreamingResponse(self._simulations.inbound_check_deposits)

    @cached_property
    def real_time_payments_transfers(self) -> AsyncRealTimePaymentsTransfersResourceWithStreamingResponse:
        return AsyncRealTimePaymentsTransfersResourceWithStreamingResponse(
            self._simulations.real_time_payments_transfers
        )

    @cached_property
    def inbound_real_time_payments_transfers(
        self,
    ) -> AsyncInboundRealTimePaymentsTransfersResourceWithStreamingResponse:
        return AsyncInboundRealTimePaymentsTransfersResourceWithStreamingResponse(
            self._simulations.inbound_real_time_payments_transfers
        )

    @cached_property
    def check_deposits(self) -> AsyncCheckDepositsResourceWithStreamingResponse:
        return AsyncCheckDepositsResourceWithStreamingResponse(self._simulations.check_deposits)

    @cached_property
    def inbound_mail_items(self) -> AsyncInboundMailItemsResourceWithStreamingResponse:
        return AsyncInboundMailItemsResourceWithStreamingResponse(self._simulations.inbound_mail_items)

    @cached_property
    def programs(self) -> AsyncProgramsResourceWithStreamingResponse:
        return AsyncProgramsResourceWithStreamingResponse(self._simulations.programs)

    @cached_property
    def account_statements(self) -> AsyncAccountStatementsResourceWithStreamingResponse:
        return AsyncAccountStatementsResourceWithStreamingResponse(self._simulations.account_statements)

    @cached_property
    def documents(self) -> AsyncDocumentsResourceWithStreamingResponse:
        return AsyncDocumentsResourceWithStreamingResponse(self._simulations.documents)

    @cached_property
    def card_tokens(self) -> AsyncCardTokensResourceWithStreamingResponse:
        return AsyncCardTokensResourceWithStreamingResponse(self._simulations.card_tokens)
