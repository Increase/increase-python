# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ... import _legacy_response
from .cards import (
    Cards,
    AsyncCards,
    CardsWithRawResponse,
    AsyncCardsWithRawResponse,
    CardsWithStreamingResponse,
    AsyncCardsWithStreamingResponse,
)
from ...types import (
    simulation_card_reversals_params,
    simulation_card_increments_params,
    simulation_card_fuel_confirmations_params,
    simulation_card_authorization_expirations_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
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
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
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
from ..._base_client import (
    make_request_options,
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
from ...types.card_payment import CardPayment
from .inbound_check_deposits import (
    InboundCheckDeposits,
    AsyncInboundCheckDeposits,
    InboundCheckDepositsWithRawResponse,
    AsyncInboundCheckDepositsWithRawResponse,
    InboundCheckDepositsWithStreamingResponse,
    AsyncInboundCheckDepositsWithStreamingResponse,
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
    def inbound_check_deposits(self) -> InboundCheckDeposits:
        return InboundCheckDeposits(self._client)

    @cached_property
    def with_raw_response(self) -> SimulationsWithRawResponse:
        return SimulationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulationsWithStreamingResponse:
        return SimulationsWithStreamingResponse(self)

    def card_authorization_expirations(
        self,
        *,
        card_payment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """
        Simulates expiring a card authorization immediately.

        Args:
          card_payment_id: The identifier of the Card Payment to expire.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/card_authorization_expirations",
            body=maybe_transform(
                {"card_payment_id": card_payment_id},
                simulation_card_authorization_expirations_params.SimulationCardAuthorizationExpirationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPayment,
        )

    def card_fuel_confirmations(
        self,
        *,
        amount: int,
        card_payment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """Simulates the fuel confirmation of an authorization by a card acquirer.

        This
        happens asynchronously right after a fuel pump transaction is completed. A fuel
        confirmation can only happen once per authorization.

        Args:
          amount: The amount of the fuel_confirmation in minor units in the card authorization's
              currency.

          card_payment_id: The identifier of the Card Payment to create a fuel_confirmation on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/card_fuel_confirmations",
            body=maybe_transform(
                {
                    "amount": amount,
                    "card_payment_id": card_payment_id,
                },
                simulation_card_fuel_confirmations_params.SimulationCardFuelConfirmationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPayment,
        )

    def card_increments(
        self,
        *,
        amount: int,
        card_payment_id: str,
        event_subscription_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """Simulates the increment of an authorization by a card acquirer.

        An authorization
        can be incremented multiple times.

        Args:
          amount: The amount of the increment in minor units in the card authorization's currency.

          card_payment_id: The identifier of the Card Payment to create a increment on.

          event_subscription_id: The identifier of the Event Subscription to use. If provided, will override the
              default real time event subscription. Because you can only create one real time
              decision event subscription, you can use this field to route events to any
              specified event subscription for testing purposes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/card_increments",
            body=maybe_transform(
                {
                    "amount": amount,
                    "card_payment_id": card_payment_id,
                    "event_subscription_id": event_subscription_id,
                },
                simulation_card_increments_params.SimulationCardIncrementsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPayment,
        )

    def card_reversals(
        self,
        *,
        card_payment_id: str,
        amount: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """Simulates the reversal of an authorization by a card acquirer.

        An authorization
        can be partially reversed multiple times, up until the total authorized amount.
        Marks the pending transaction as complete if the authorization is fully
        reversed.

        Args:
          card_payment_id: The identifier of the Card Payment to create a reversal on.

          amount: The amount of the reversal in minor units in the card authorization's currency.
              This defaults to the authorization amount.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/simulations/card_reversals",
            body=maybe_transform(
                {
                    "card_payment_id": card_payment_id,
                    "amount": amount,
                },
                simulation_card_reversals_params.SimulationCardReversalsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPayment,
        )


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
    def inbound_check_deposits(self) -> AsyncInboundCheckDeposits:
        return AsyncInboundCheckDeposits(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSimulationsWithRawResponse:
        return AsyncSimulationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulationsWithStreamingResponse:
        return AsyncSimulationsWithStreamingResponse(self)

    async def card_authorization_expirations(
        self,
        *,
        card_payment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """
        Simulates expiring a card authorization immediately.

        Args:
          card_payment_id: The identifier of the Card Payment to expire.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/card_authorization_expirations",
            body=await async_maybe_transform(
                {"card_payment_id": card_payment_id},
                simulation_card_authorization_expirations_params.SimulationCardAuthorizationExpirationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPayment,
        )

    async def card_fuel_confirmations(
        self,
        *,
        amount: int,
        card_payment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """Simulates the fuel confirmation of an authorization by a card acquirer.

        This
        happens asynchronously right after a fuel pump transaction is completed. A fuel
        confirmation can only happen once per authorization.

        Args:
          amount: The amount of the fuel_confirmation in minor units in the card authorization's
              currency.

          card_payment_id: The identifier of the Card Payment to create a fuel_confirmation on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/card_fuel_confirmations",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "card_payment_id": card_payment_id,
                },
                simulation_card_fuel_confirmations_params.SimulationCardFuelConfirmationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPayment,
        )

    async def card_increments(
        self,
        *,
        amount: int,
        card_payment_id: str,
        event_subscription_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """Simulates the increment of an authorization by a card acquirer.

        An authorization
        can be incremented multiple times.

        Args:
          amount: The amount of the increment in minor units in the card authorization's currency.

          card_payment_id: The identifier of the Card Payment to create a increment on.

          event_subscription_id: The identifier of the Event Subscription to use. If provided, will override the
              default real time event subscription. Because you can only create one real time
              decision event subscription, you can use this field to route events to any
              specified event subscription for testing purposes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/card_increments",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "card_payment_id": card_payment_id,
                    "event_subscription_id": event_subscription_id,
                },
                simulation_card_increments_params.SimulationCardIncrementsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPayment,
        )

    async def card_reversals(
        self,
        *,
        card_payment_id: str,
        amount: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardPayment:
        """Simulates the reversal of an authorization by a card acquirer.

        An authorization
        can be partially reversed multiple times, up until the total authorized amount.
        Marks the pending transaction as complete if the authorization is fully
        reversed.

        Args:
          card_payment_id: The identifier of the Card Payment to create a reversal on.

          amount: The amount of the reversal in minor units in the card authorization's currency.
              This defaults to the authorization amount.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/simulations/card_reversals",
            body=await async_maybe_transform(
                {
                    "card_payment_id": card_payment_id,
                    "amount": amount,
                },
                simulation_card_reversals_params.SimulationCardReversalsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardPayment,
        )


class SimulationsWithRawResponse:
    def __init__(self, simulations: Simulations) -> None:
        self._simulations = simulations

        self.card_authorization_expirations = _legacy_response.to_raw_response_wrapper(
            simulations.card_authorization_expirations,
        )
        self.card_fuel_confirmations = _legacy_response.to_raw_response_wrapper(
            simulations.card_fuel_confirmations,
        )
        self.card_increments = _legacy_response.to_raw_response_wrapper(
            simulations.card_increments,
        )
        self.card_reversals = _legacy_response.to_raw_response_wrapper(
            simulations.card_reversals,
        )

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

    @cached_property
    def inbound_check_deposits(self) -> InboundCheckDepositsWithRawResponse:
        return InboundCheckDepositsWithRawResponse(self._simulations.inbound_check_deposits)


class AsyncSimulationsWithRawResponse:
    def __init__(self, simulations: AsyncSimulations) -> None:
        self._simulations = simulations

        self.card_authorization_expirations = _legacy_response.async_to_raw_response_wrapper(
            simulations.card_authorization_expirations,
        )
        self.card_fuel_confirmations = _legacy_response.async_to_raw_response_wrapper(
            simulations.card_fuel_confirmations,
        )
        self.card_increments = _legacy_response.async_to_raw_response_wrapper(
            simulations.card_increments,
        )
        self.card_reversals = _legacy_response.async_to_raw_response_wrapper(
            simulations.card_reversals,
        )

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

    @cached_property
    def inbound_check_deposits(self) -> AsyncInboundCheckDepositsWithRawResponse:
        return AsyncInboundCheckDepositsWithRawResponse(self._simulations.inbound_check_deposits)


class SimulationsWithStreamingResponse:
    def __init__(self, simulations: Simulations) -> None:
        self._simulations = simulations

        self.card_authorization_expirations = to_streamed_response_wrapper(
            simulations.card_authorization_expirations,
        )
        self.card_fuel_confirmations = to_streamed_response_wrapper(
            simulations.card_fuel_confirmations,
        )
        self.card_increments = to_streamed_response_wrapper(
            simulations.card_increments,
        )
        self.card_reversals = to_streamed_response_wrapper(
            simulations.card_reversals,
        )

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

    @cached_property
    def inbound_check_deposits(self) -> InboundCheckDepositsWithStreamingResponse:
        return InboundCheckDepositsWithStreamingResponse(self._simulations.inbound_check_deposits)


class AsyncSimulationsWithStreamingResponse:
    def __init__(self, simulations: AsyncSimulations) -> None:
        self._simulations = simulations

        self.card_authorization_expirations = async_to_streamed_response_wrapper(
            simulations.card_authorization_expirations,
        )
        self.card_fuel_confirmations = async_to_streamed_response_wrapper(
            simulations.card_fuel_confirmations,
        )
        self.card_increments = async_to_streamed_response_wrapper(
            simulations.card_increments,
        )
        self.card_reversals = async_to_streamed_response_wrapper(
            simulations.card_reversals,
        )

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

    @cached_property
    def inbound_check_deposits(self) -> AsyncInboundCheckDepositsWithStreamingResponse:
        return AsyncInboundCheckDepositsWithStreamingResponse(self._simulations.inbound_check_deposits)
