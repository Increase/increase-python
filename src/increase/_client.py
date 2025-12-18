# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import IncreaseError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources.cards import (
        CardsResource,
        AsyncCardsResource,
        CardsResourceWithRawResponse,
        AsyncCardsResourceWithRawResponse,
        CardsResourceWithStreamingResponse,
        AsyncCardsResourceWithStreamingResponse,
    )
    from .resources.files import (
        FilesResource,
        AsyncFilesResource,
        FilesResourceWithRawResponse,
        AsyncFilesResourceWithRawResponse,
        FilesResourceWithStreamingResponse,
        AsyncFilesResourceWithStreamingResponse,
    )
    from .resources.events import (
        EventsResource,
        AsyncEventsResource,
        EventsResourceWithRawResponse,
        AsyncEventsResourceWithRawResponse,
        EventsResourceWithStreamingResponse,
        AsyncEventsResourceWithStreamingResponse,
    )
    from .resources.groups import (
        GroupsResource,
        AsyncGroupsResource,
        GroupsResourceWithRawResponse,
        AsyncGroupsResourceWithRawResponse,
        GroupsResourceWithStreamingResponse,
        AsyncGroupsResourceWithStreamingResponse,
    )
    from .resources.exports import (
        ExportsResource,
        AsyncExportsResource,
        ExportsResourceWithRawResponse,
        AsyncExportsResourceWithRawResponse,
        ExportsResourceWithStreamingResponse,
        AsyncExportsResourceWithStreamingResponse,
    )
    from .resources.accounts import (
        AccountsResource,
        AsyncAccountsResource,
        AccountsResourceWithRawResponse,
        AsyncAccountsResourceWithRawResponse,
        AccountsResourceWithStreamingResponse,
        AsyncAccountsResourceWithStreamingResponse,
    )
    from .resources.entities import (
        EntitiesResource,
        AsyncEntitiesResource,
        EntitiesResourceWithRawResponse,
        AsyncEntitiesResourceWithRawResponse,
        EntitiesResourceWithStreamingResponse,
        AsyncEntitiesResourceWithStreamingResponse,
    )
    from .resources.programs import (
        ProgramsResource,
        AsyncProgramsResource,
        ProgramsResourceWithRawResponse,
        AsyncProgramsResourceWithRawResponse,
        ProgramsResourceWithStreamingResponse,
        AsyncProgramsResourceWithStreamingResponse,
    )
    from .resources.webhooks import Webhooks, AsyncWebhooks
    from .resources.lockboxes import (
        LockboxesResource,
        AsyncLockboxesResource,
        LockboxesResourceWithRawResponse,
        AsyncLockboxesResourceWithRawResponse,
        LockboxesResourceWithStreamingResponse,
        AsyncLockboxesResourceWithStreamingResponse,
    )
    from .resources.file_links import (
        FileLinksResource,
        AsyncFileLinksResource,
        FileLinksResourceWithRawResponse,
        AsyncFileLinksResourceWithRawResponse,
        FileLinksResourceWithStreamingResponse,
        AsyncFileLinksResourceWithStreamingResponse,
    )
    from .resources.card_tokens import (
        CardTokensResource,
        AsyncCardTokensResource,
        CardTokensResourceWithRawResponse,
        AsyncCardTokensResourceWithRawResponse,
        CardTokensResourceWithStreamingResponse,
        AsyncCardTokensResourceWithStreamingResponse,
    )
    from .resources.oauth_tokens import (
        OAuthTokensResource,
        AsyncOAuthTokensResource,
        OAuthTokensResourceWithRawResponse,
        AsyncOAuthTokensResourceWithRawResponse,
        OAuthTokensResourceWithStreamingResponse,
        AsyncOAuthTokensResourceWithStreamingResponse,
    )
    from .resources.transactions import (
        TransactionsResource,
        AsyncTransactionsResource,
        TransactionsResourceWithRawResponse,
        AsyncTransactionsResourceWithRawResponse,
        TransactionsResourceWithStreamingResponse,
        AsyncTransactionsResourceWithStreamingResponse,
    )
    from .resources.ach_transfers import (
        ACHTransfersResource,
        AsyncACHTransfersResource,
        ACHTransfersResourceWithRawResponse,
        AsyncACHTransfersResourceWithRawResponse,
        ACHTransfersResourceWithStreamingResponse,
        AsyncACHTransfersResourceWithStreamingResponse,
    )
    from .resources.card_disputes import (
        CardDisputesResource,
        AsyncCardDisputesResource,
        CardDisputesResourceWithRawResponse,
        AsyncCardDisputesResourceWithRawResponse,
        CardDisputesResourceWithStreamingResponse,
        AsyncCardDisputesResourceWithStreamingResponse,
    )
    from .resources.card_payments import (
        CardPaymentsResource,
        AsyncCardPaymentsResource,
        CardPaymentsResourceWithRawResponse,
        AsyncCardPaymentsResourceWithRawResponse,
        CardPaymentsResourceWithStreamingResponse,
        AsyncCardPaymentsResourceWithStreamingResponse,
    )
    from .resources.check_deposits import (
        CheckDepositsResource,
        AsyncCheckDepositsResource,
        CheckDepositsResourceWithRawResponse,
        AsyncCheckDepositsResourceWithRawResponse,
        CheckDepositsResourceWithStreamingResponse,
        AsyncCheckDepositsResourceWithStreamingResponse,
    )
    from .resources.physical_cards import (
        PhysicalCardsResource,
        AsyncPhysicalCardsResource,
        PhysicalCardsResourceWithRawResponse,
        AsyncPhysicalCardsResourceWithRawResponse,
        PhysicalCardsResourceWithStreamingResponse,
        AsyncPhysicalCardsResourceWithStreamingResponse,
    )
    from .resources.wire_transfers import (
        WireTransfersResource,
        AsyncWireTransfersResource,
        WireTransfersResourceWithRawResponse,
        AsyncWireTransfersResourceWithRawResponse,
        WireTransfersResourceWithStreamingResponse,
        AsyncWireTransfersResourceWithStreamingResponse,
    )
    from .resources.account_numbers import (
        AccountNumbersResource,
        AsyncAccountNumbersResource,
        AccountNumbersResourceWithRawResponse,
        AsyncAccountNumbersResourceWithRawResponse,
        AccountNumbersResourceWithStreamingResponse,
        AsyncAccountNumbersResourceWithStreamingResponse,
    )
    from .resources.check_transfers import (
        CheckTransfersResource,
        AsyncCheckTransfersResource,
        CheckTransfersResourceWithRawResponse,
        AsyncCheckTransfersResourceWithRawResponse,
        CheckTransfersResourceWithStreamingResponse,
        AsyncCheckTransfersResourceWithStreamingResponse,
    )
    from .resources.routing_numbers import (
        RoutingNumbersResource,
        AsyncRoutingNumbersResource,
        RoutingNumbersResourceWithRawResponse,
        AsyncRoutingNumbersResourceWithRawResponse,
        RoutingNumbersResourceWithStreamingResponse,
        AsyncRoutingNumbersResourceWithStreamingResponse,
    )
    from .resources.card_validations import (
        CardValidationsResource,
        AsyncCardValidationsResource,
        CardValidationsResourceWithRawResponse,
        AsyncCardValidationsResourceWithRawResponse,
        CardValidationsResourceWithStreamingResponse,
        AsyncCardValidationsResourceWithStreamingResponse,
    )
    from .resources.fednow_transfers import (
        FednowTransfersResource,
        AsyncFednowTransfersResource,
        FednowTransfersResourceWithRawResponse,
        AsyncFednowTransfersResourceWithRawResponse,
        FednowTransfersResourceWithStreamingResponse,
        AsyncFednowTransfersResourceWithStreamingResponse,
    )
    from .resources.intrafi_balances import (
        IntrafiBalancesResource,
        AsyncIntrafiBalancesResource,
        IntrafiBalancesResourceWithRawResponse,
        AsyncIntrafiBalancesResourceWithRawResponse,
        IntrafiBalancesResourceWithStreamingResponse,
        AsyncIntrafiBalancesResourceWithStreamingResponse,
    )
    from .resources.account_transfers import (
        AccountTransfersResource,
        AsyncAccountTransfersResource,
        AccountTransfersResourceWithRawResponse,
        AsyncAccountTransfersResourceWithRawResponse,
        AccountTransfersResourceWithStreamingResponse,
        AsyncAccountTransfersResourceWithStreamingResponse,
    )
    from .resources.external_accounts import (
        ExternalAccountsResource,
        AsyncExternalAccountsResource,
        ExternalAccountsResourceWithRawResponse,
        AsyncExternalAccountsResourceWithRawResponse,
        ExternalAccountsResourceWithStreamingResponse,
        AsyncExternalAccountsResourceWithStreamingResponse,
    )
    from .resources.oauth_connections import (
        OAuthConnectionsResource,
        AsyncOAuthConnectionsResource,
        OAuthConnectionsResourceWithRawResponse,
        AsyncOAuthConnectionsResourceWithRawResponse,
        OAuthConnectionsResourceWithStreamingResponse,
        AsyncOAuthConnectionsResourceWithStreamingResponse,
    )
    from .resources.account_statements import (
        AccountStatementsResource,
        AsyncAccountStatementsResource,
        AccountStatementsResourceWithRawResponse,
        AsyncAccountStatementsResourceWithRawResponse,
        AccountStatementsResourceWithStreamingResponse,
        AsyncAccountStatementsResourceWithStreamingResponse,
    )
    from .resources.inbound_mail_items import (
        InboundMailItemsResource,
        AsyncInboundMailItemsResource,
        InboundMailItemsResourceWithRawResponse,
        AsyncInboundMailItemsResourceWithRawResponse,
        InboundMailItemsResourceWithStreamingResponse,
        AsyncInboundMailItemsResourceWithStreamingResponse,
    )
    from .resources.intrafi_exclusions import (
        IntrafiExclusionsResource,
        AsyncIntrafiExclusionsResource,
        IntrafiExclusionsResourceWithRawResponse,
        AsyncIntrafiExclusionsResourceWithRawResponse,
        IntrafiExclusionsResourceWithStreamingResponse,
        AsyncIntrafiExclusionsResourceWithStreamingResponse,
    )
    from .resources.oauth_applications import (
        OAuthApplicationsResource,
        AsyncOAuthApplicationsResource,
        OAuthApplicationsResourceWithRawResponse,
        AsyncOAuthApplicationsResourceWithRawResponse,
        OAuthApplicationsResourceWithStreamingResponse,
        AsyncOAuthApplicationsResourceWithStreamingResponse,
    )
    from .resources.bookkeeping_entries import (
        BookkeepingEntriesResource,
        AsyncBookkeepingEntriesResource,
        BookkeepingEntriesResourceWithRawResponse,
        AsyncBookkeepingEntriesResourceWithRawResponse,
        BookkeepingEntriesResourceWithStreamingResponse,
        AsyncBookkeepingEntriesResourceWithStreamingResponse,
    )
    from .resources.card_push_transfers import (
        CardPushTransfersResource,
        AsyncCardPushTransfersResource,
        CardPushTransfersResourceWithRawResponse,
        AsyncCardPushTransfersResourceWithRawResponse,
        CardPushTransfersResourceWithStreamingResponse,
        AsyncCardPushTransfersResourceWithStreamingResponse,
    )
    from .resources.event_subscriptions import (
        EventSubscriptionsResource,
        AsyncEventSubscriptionsResource,
        EventSubscriptionsResourceWithRawResponse,
        AsyncEventSubscriptionsResourceWithRawResponse,
        EventSubscriptionsResourceWithStreamingResponse,
        AsyncEventSubscriptionsResourceWithStreamingResponse,
    )
    from .resources.real_time_decisions import (
        RealTimeDecisionsResource,
        AsyncRealTimeDecisionsResource,
        RealTimeDecisionsResourceWithRawResponse,
        AsyncRealTimeDecisionsResourceWithRawResponse,
        RealTimeDecisionsResourceWithStreamingResponse,
        AsyncRealTimeDecisionsResourceWithStreamingResponse,
    )
    from .resources.ach_prenotifications import (
        ACHPrenotificationsResource,
        AsyncACHPrenotificationsResource,
        ACHPrenotificationsResourceWithRawResponse,
        AsyncACHPrenotificationsResourceWithRawResponse,
        ACHPrenotificationsResourceWithStreamingResponse,
        AsyncACHPrenotificationsResourceWithStreamingResponse,
    )
    from .resources.bookkeeping_accounts import (
        BookkeepingAccountsResource,
        AsyncBookkeepingAccountsResource,
        BookkeepingAccountsResourceWithRawResponse,
        AsyncBookkeepingAccountsResourceWithRawResponse,
        BookkeepingAccountsResourceWithStreamingResponse,
        AsyncBookkeepingAccountsResourceWithStreamingResponse,
    )
    from .resources.pending_transactions import (
        PendingTransactionsResource,
        AsyncPendingTransactionsResource,
        PendingTransactionsResourceWithRawResponse,
        AsyncPendingTransactionsResourceWithRawResponse,
        PendingTransactionsResourceWithStreamingResponse,
        AsyncPendingTransactionsResourceWithStreamingResponse,
    )
    from .resources.declined_transactions import (
        DeclinedTransactionsResource,
        AsyncDeclinedTransactionsResource,
        DeclinedTransactionsResourceWithRawResponse,
        AsyncDeclinedTransactionsResourceWithRawResponse,
        DeclinedTransactionsResourceWithStreamingResponse,
        AsyncDeclinedTransactionsResourceWithStreamingResponse,
    )
    from .resources.digital_card_profiles import (
        DigitalCardProfilesResource,
        AsyncDigitalCardProfilesResource,
        DigitalCardProfilesResourceWithRawResponse,
        AsyncDigitalCardProfilesResourceWithRawResponse,
        DigitalCardProfilesResourceWithStreamingResponse,
        AsyncDigitalCardProfilesResourceWithStreamingResponse,
    )
    from .resources.digital_wallet_tokens import (
        DigitalWalletTokensResource,
        AsyncDigitalWalletTokensResource,
        DigitalWalletTokensResourceWithRawResponse,
        AsyncDigitalWalletTokensResourceWithRawResponse,
        DigitalWalletTokensResourceWithStreamingResponse,
        AsyncDigitalWalletTokensResourceWithStreamingResponse,
    )
    from .resources.inbound_ach_transfers import (
        InboundACHTransfersResource,
        AsyncInboundACHTransfersResource,
        InboundACHTransfersResourceWithRawResponse,
        AsyncInboundACHTransfersResourceWithRawResponse,
        InboundACHTransfersResourceWithStreamingResponse,
        AsyncInboundACHTransfersResourceWithStreamingResponse,
    )
    from .resources.bookkeeping_entry_sets import (
        BookkeepingEntrySetsResource,
        AsyncBookkeepingEntrySetsResource,
        BookkeepingEntrySetsResourceWithRawResponse,
        AsyncBookkeepingEntrySetsResourceWithRawResponse,
        BookkeepingEntrySetsResourceWithStreamingResponse,
        AsyncBookkeepingEntrySetsResourceWithStreamingResponse,
    )
    from .resources.inbound_check_deposits import (
        InboundCheckDepositsResource,
        AsyncInboundCheckDepositsResource,
        InboundCheckDepositsResourceWithRawResponse,
        AsyncInboundCheckDepositsResourceWithRawResponse,
        InboundCheckDepositsResourceWithStreamingResponse,
        AsyncInboundCheckDepositsResourceWithStreamingResponse,
    )
    from .resources.inbound_wire_transfers import (
        InboundWireTransfersResource,
        AsyncInboundWireTransfersResource,
        InboundWireTransfersResourceWithRawResponse,
        AsyncInboundWireTransfersResourceWithRawResponse,
        InboundWireTransfersResourceWithStreamingResponse,
        AsyncInboundWireTransfersResourceWithStreamingResponse,
    )
    from .resources.physical_card_profiles import (
        PhysicalCardProfilesResource,
        AsyncPhysicalCardProfilesResource,
        PhysicalCardProfilesResourceWithRawResponse,
        AsyncPhysicalCardProfilesResourceWithRawResponse,
        PhysicalCardProfilesResourceWithStreamingResponse,
        AsyncPhysicalCardProfilesResourceWithStreamingResponse,
    )
    from .resources.supplemental_documents import (
        SupplementalDocumentsResource,
        AsyncSupplementalDocumentsResource,
        SupplementalDocumentsResourceWithRawResponse,
        AsyncSupplementalDocumentsResourceWithRawResponse,
        SupplementalDocumentsResourceWithStreamingResponse,
        AsyncSupplementalDocumentsResourceWithStreamingResponse,
    )
    from .resources.wire_drawdown_requests import (
        WireDrawdownRequestsResource,
        AsyncWireDrawdownRequestsResource,
        WireDrawdownRequestsResourceWithRawResponse,
        AsyncWireDrawdownRequestsResourceWithRawResponse,
        WireDrawdownRequestsResourceWithStreamingResponse,
        AsyncWireDrawdownRequestsResourceWithStreamingResponse,
    )
    from .resources.simulations.simulations import (
        SimulationsResource,
        AsyncSimulationsResource,
        SimulationsResourceWithRawResponse,
        AsyncSimulationsResourceWithRawResponse,
        SimulationsResourceWithStreamingResponse,
        AsyncSimulationsResourceWithStreamingResponse,
    )
    from .resources.inbound_fednow_transfers import (
        InboundFednowTransfersResource,
        AsyncInboundFednowTransfersResource,
        InboundFednowTransfersResourceWithRawResponse,
        AsyncInboundFednowTransfersResourceWithRawResponse,
        InboundFednowTransfersResourceWithStreamingResponse,
        AsyncInboundFednowTransfersResourceWithStreamingResponse,
    )
    from .resources.card_purchase_supplements import (
        CardPurchaseSupplementsResource,
        AsyncCardPurchaseSupplementsResource,
        CardPurchaseSupplementsResourceWithRawResponse,
        AsyncCardPurchaseSupplementsResourceWithRawResponse,
        CardPurchaseSupplementsResourceWithStreamingResponse,
        AsyncCardPurchaseSupplementsResourceWithStreamingResponse,
    )
    from .resources.intrafi_account_enrollments import (
        IntrafiAccountEnrollmentsResource,
        AsyncIntrafiAccountEnrollmentsResource,
        IntrafiAccountEnrollmentsResourceWithRawResponse,
        AsyncIntrafiAccountEnrollmentsResourceWithRawResponse,
        IntrafiAccountEnrollmentsResourceWithStreamingResponse,
        AsyncIntrafiAccountEnrollmentsResourceWithStreamingResponse,
    )
    from .resources.real_time_payments_transfers import (
        RealTimePaymentsTransfersResource,
        AsyncRealTimePaymentsTransfersResource,
        RealTimePaymentsTransfersResourceWithRawResponse,
        AsyncRealTimePaymentsTransfersResourceWithRawResponse,
        RealTimePaymentsTransfersResourceWithStreamingResponse,
        AsyncRealTimePaymentsTransfersResourceWithStreamingResponse,
    )
    from .resources.inbound_wire_drawdown_requests import (
        InboundWireDrawdownRequestsResource,
        AsyncInboundWireDrawdownRequestsResource,
        InboundWireDrawdownRequestsResourceWithRawResponse,
        AsyncInboundWireDrawdownRequestsResourceWithRawResponse,
        InboundWireDrawdownRequestsResourceWithStreamingResponse,
        AsyncInboundWireDrawdownRequestsResourceWithStreamingResponse,
    )
    from .resources.inbound_real_time_payments_transfers import (
        InboundRealTimePaymentsTransfersResource,
        AsyncInboundRealTimePaymentsTransfersResource,
        InboundRealTimePaymentsTransfersResourceWithRawResponse,
        AsyncInboundRealTimePaymentsTransfersResourceWithRawResponse,
        InboundRealTimePaymentsTransfersResourceWithStreamingResponse,
        AsyncInboundRealTimePaymentsTransfersResourceWithStreamingResponse,
    )

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Increase",
    "AsyncIncrease",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.increase.com",
    "sandbox": "https://sandbox.increase.com",
}


class Increase(SyncAPIClient):
    # client options
    api_key: str
    webhook_secret: str | None

    _environment: Literal["production", "sandbox"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        environment: Literal["production", "sandbox"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Increase client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `INCREASE_API_KEY`
        - `webhook_secret` from `INCREASE_WEBHOOK_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("INCREASE_API_KEY")
        if api_key is None:
            raise IncreaseError(
                "The api_key client option must be set either by passing api_key to the client or by setting the INCREASE_API_KEY environment variable"
            )
        self.api_key = api_key

        if webhook_secret is None:
            webhook_secret = os.environ.get("INCREASE_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret

        self._environment = environment

        base_url_env = os.environ.get("INCREASE_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `INCREASE_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

    @cached_property
    def accounts(self) -> AccountsResource:
        from .resources.accounts import AccountsResource

        return AccountsResource(self)

    @cached_property
    def account_numbers(self) -> AccountNumbersResource:
        from .resources.account_numbers import AccountNumbersResource

        return AccountNumbersResource(self)

    @cached_property
    def account_transfers(self) -> AccountTransfersResource:
        from .resources.account_transfers import AccountTransfersResource

        return AccountTransfersResource(self)

    @cached_property
    def cards(self) -> CardsResource:
        from .resources.cards import CardsResource

        return CardsResource(self)

    @cached_property
    def card_payments(self) -> CardPaymentsResource:
        from .resources.card_payments import CardPaymentsResource

        return CardPaymentsResource(self)

    @cached_property
    def card_purchase_supplements(self) -> CardPurchaseSupplementsResource:
        from .resources.card_purchase_supplements import CardPurchaseSupplementsResource

        return CardPurchaseSupplementsResource(self)

    @cached_property
    def card_disputes(self) -> CardDisputesResource:
        from .resources.card_disputes import CardDisputesResource

        return CardDisputesResource(self)

    @cached_property
    def physical_cards(self) -> PhysicalCardsResource:
        from .resources.physical_cards import PhysicalCardsResource

        return PhysicalCardsResource(self)

    @cached_property
    def digital_card_profiles(self) -> DigitalCardProfilesResource:
        from .resources.digital_card_profiles import DigitalCardProfilesResource

        return DigitalCardProfilesResource(self)

    @cached_property
    def physical_card_profiles(self) -> PhysicalCardProfilesResource:
        from .resources.physical_card_profiles import PhysicalCardProfilesResource

        return PhysicalCardProfilesResource(self)

    @cached_property
    def digital_wallet_tokens(self) -> DigitalWalletTokensResource:
        from .resources.digital_wallet_tokens import DigitalWalletTokensResource

        return DigitalWalletTokensResource(self)

    @cached_property
    def transactions(self) -> TransactionsResource:
        from .resources.transactions import TransactionsResource

        return TransactionsResource(self)

    @cached_property
    def pending_transactions(self) -> PendingTransactionsResource:
        from .resources.pending_transactions import PendingTransactionsResource

        return PendingTransactionsResource(self)

    @cached_property
    def declined_transactions(self) -> DeclinedTransactionsResource:
        from .resources.declined_transactions import DeclinedTransactionsResource

        return DeclinedTransactionsResource(self)

    @cached_property
    def ach_transfers(self) -> ACHTransfersResource:
        from .resources.ach_transfers import ACHTransfersResource

        return ACHTransfersResource(self)

    @cached_property
    def ach_prenotifications(self) -> ACHPrenotificationsResource:
        from .resources.ach_prenotifications import ACHPrenotificationsResource

        return ACHPrenotificationsResource(self)

    @cached_property
    def inbound_ach_transfers(self) -> InboundACHTransfersResource:
        from .resources.inbound_ach_transfers import InboundACHTransfersResource

        return InboundACHTransfersResource(self)

    @cached_property
    def wire_transfers(self) -> WireTransfersResource:
        from .resources.wire_transfers import WireTransfersResource

        return WireTransfersResource(self)

    @cached_property
    def inbound_wire_transfers(self) -> InboundWireTransfersResource:
        from .resources.inbound_wire_transfers import InboundWireTransfersResource

        return InboundWireTransfersResource(self)

    @cached_property
    def wire_drawdown_requests(self) -> WireDrawdownRequestsResource:
        from .resources.wire_drawdown_requests import WireDrawdownRequestsResource

        return WireDrawdownRequestsResource(self)

    @cached_property
    def inbound_wire_drawdown_requests(self) -> InboundWireDrawdownRequestsResource:
        from .resources.inbound_wire_drawdown_requests import InboundWireDrawdownRequestsResource

        return InboundWireDrawdownRequestsResource(self)

    @cached_property
    def check_transfers(self) -> CheckTransfersResource:
        from .resources.check_transfers import CheckTransfersResource

        return CheckTransfersResource(self)

    @cached_property
    def inbound_check_deposits(self) -> InboundCheckDepositsResource:
        from .resources.inbound_check_deposits import InboundCheckDepositsResource

        return InboundCheckDepositsResource(self)

    @cached_property
    def real_time_payments_transfers(self) -> RealTimePaymentsTransfersResource:
        from .resources.real_time_payments_transfers import RealTimePaymentsTransfersResource

        return RealTimePaymentsTransfersResource(self)

    @cached_property
    def inbound_real_time_payments_transfers(self) -> InboundRealTimePaymentsTransfersResource:
        from .resources.inbound_real_time_payments_transfers import InboundRealTimePaymentsTransfersResource

        return InboundRealTimePaymentsTransfersResource(self)

    @cached_property
    def fednow_transfers(self) -> FednowTransfersResource:
        from .resources.fednow_transfers import FednowTransfersResource

        return FednowTransfersResource(self)

    @cached_property
    def inbound_fednow_transfers(self) -> InboundFednowTransfersResource:
        from .resources.inbound_fednow_transfers import InboundFednowTransfersResource

        return InboundFednowTransfersResource(self)

    @cached_property
    def check_deposits(self) -> CheckDepositsResource:
        from .resources.check_deposits import CheckDepositsResource

        return CheckDepositsResource(self)

    @cached_property
    def lockboxes(self) -> LockboxesResource:
        from .resources.lockboxes import LockboxesResource

        return LockboxesResource(self)

    @cached_property
    def inbound_mail_items(self) -> InboundMailItemsResource:
        from .resources.inbound_mail_items import InboundMailItemsResource

        return InboundMailItemsResource(self)

    @cached_property
    def routing_numbers(self) -> RoutingNumbersResource:
        from .resources.routing_numbers import RoutingNumbersResource

        return RoutingNumbersResource(self)

    @cached_property
    def external_accounts(self) -> ExternalAccountsResource:
        from .resources.external_accounts import ExternalAccountsResource

        return ExternalAccountsResource(self)

    @cached_property
    def entities(self) -> EntitiesResource:
        from .resources.entities import EntitiesResource

        return EntitiesResource(self)

    @cached_property
    def supplemental_documents(self) -> SupplementalDocumentsResource:
        from .resources.supplemental_documents import SupplementalDocumentsResource

        return SupplementalDocumentsResource(self)

    @cached_property
    def programs(self) -> ProgramsResource:
        from .resources.programs import ProgramsResource

        return ProgramsResource(self)

    @cached_property
    def account_statements(self) -> AccountStatementsResource:
        from .resources.account_statements import AccountStatementsResource

        return AccountStatementsResource(self)

    @cached_property
    def files(self) -> FilesResource:
        from .resources.files import FilesResource

        return FilesResource(self)

    @cached_property
    def file_links(self) -> FileLinksResource:
        from .resources.file_links import FileLinksResource

        return FileLinksResource(self)

    @cached_property
    def exports(self) -> ExportsResource:
        from .resources.exports import ExportsResource

        return ExportsResource(self)

    @cached_property
    def events(self) -> EventsResource:
        from .resources.events import EventsResource

        return EventsResource(self)

    @cached_property
    def event_subscriptions(self) -> EventSubscriptionsResource:
        from .resources.event_subscriptions import EventSubscriptionsResource

        return EventSubscriptionsResource(self)

    @cached_property
    def real_time_decisions(self) -> RealTimeDecisionsResource:
        from .resources.real_time_decisions import RealTimeDecisionsResource

        return RealTimeDecisionsResource(self)

    @cached_property
    def bookkeeping_accounts(self) -> BookkeepingAccountsResource:
        from .resources.bookkeeping_accounts import BookkeepingAccountsResource

        return BookkeepingAccountsResource(self)

    @cached_property
    def bookkeeping_entry_sets(self) -> BookkeepingEntrySetsResource:
        from .resources.bookkeeping_entry_sets import BookkeepingEntrySetsResource

        return BookkeepingEntrySetsResource(self)

    @cached_property
    def bookkeeping_entries(self) -> BookkeepingEntriesResource:
        from .resources.bookkeeping_entries import BookkeepingEntriesResource

        return BookkeepingEntriesResource(self)

    @cached_property
    def groups(self) -> GroupsResource:
        from .resources.groups import GroupsResource

        return GroupsResource(self)

    @cached_property
    def oauth_applications(self) -> OAuthApplicationsResource:
        from .resources.oauth_applications import OAuthApplicationsResource

        return OAuthApplicationsResource(self)

    @cached_property
    def oauth_connections(self) -> OAuthConnectionsResource:
        from .resources.oauth_connections import OAuthConnectionsResource

        return OAuthConnectionsResource(self)

    @cached_property
    def oauth_tokens(self) -> OAuthTokensResource:
        from .resources.oauth_tokens import OAuthTokensResource

        return OAuthTokensResource(self)

    @cached_property
    def intrafi_account_enrollments(self) -> IntrafiAccountEnrollmentsResource:
        from .resources.intrafi_account_enrollments import IntrafiAccountEnrollmentsResource

        return IntrafiAccountEnrollmentsResource(self)

    @cached_property
    def intrafi_balances(self) -> IntrafiBalancesResource:
        from .resources.intrafi_balances import IntrafiBalancesResource

        return IntrafiBalancesResource(self)

    @cached_property
    def intrafi_exclusions(self) -> IntrafiExclusionsResource:
        from .resources.intrafi_exclusions import IntrafiExclusionsResource

        return IntrafiExclusionsResource(self)

    @cached_property
    def card_tokens(self) -> CardTokensResource:
        from .resources.card_tokens import CardTokensResource

        return CardTokensResource(self)

    @cached_property
    def card_push_transfers(self) -> CardPushTransfersResource:
        from .resources.card_push_transfers import CardPushTransfersResource

        return CardPushTransfersResource(self)

    @cached_property
    def card_validations(self) -> CardValidationsResource:
        from .resources.card_validations import CardValidationsResource

        return CardValidationsResource(self)

    @cached_property
    def simulations(self) -> SimulationsResource:
        from .resources.simulations import SimulationsResource

        return SimulationsResource(self)

    @cached_property
    def webhooks(self) -> Webhooks:
        from .resources.webhooks import Webhooks

        return Webhooks(self)

    @cached_property
    def with_raw_response(self) -> IncreaseWithRawResponse:
        return IncreaseWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IncreaseWithStreamedResponse:
        return IncreaseWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(nested_format="dots", array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        environment: Literal["production", "sandbox"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        type_ = body.get("type") if is_mapping(body) else None
        if type_ == "invalid_parameters_error":
            return _exceptions.InvalidParametersError(err_msg, response=response, body=body)

        if type_ == "malformed_request_error":
            return _exceptions.MalformedRequestError(err_msg, response=response, body=body)

        if type_ == "invalid_api_key_error":
            return _exceptions.InvalidAPIKeyError(err_msg, response=response, body=body)

        if type_ == "environment_mismatch_error":
            return _exceptions.EnvironmentMismatchError(err_msg, response=response, body=body)

        if type_ == "insufficient_permissions_error":
            return _exceptions.InsufficientPermissionsError(err_msg, response=response, body=body)

        if type_ == "private_feature_error":
            return _exceptions.PrivateFeatureError(err_msg, response=response, body=body)

        if type_ == "api_method_not_found_error":
            return _exceptions.APIMethodNotFoundError(err_msg, response=response, body=body)

        if type_ == "object_not_found_error":
            return _exceptions.ObjectNotFoundError(err_msg, response=response, body=body)

        if type_ == "idempotency_key_already_used_error":
            return _exceptions.IdempotencyKeyAlreadyUsedError(err_msg, response=response, body=body)

        if type_ == "invalid_operation_error":
            return _exceptions.InvalidOperationError(err_msg, response=response, body=body)

        if type_ == "rate_limited_error":
            return _exceptions.RateLimitedError(err_msg, response=response, body=body)

        if type_ == "internal_server_error":
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(
                err_msg,
                response=response,
                body={
                    "detail": None,
                    "status": 500,
                    "title": "",
                    "type": "internal_server_error",
                },
            )

        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncIncrease(AsyncAPIClient):
    # client options
    api_key: str
    webhook_secret: str | None

    _environment: Literal["production", "sandbox"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        environment: Literal["production", "sandbox"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncIncrease client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `INCREASE_API_KEY`
        - `webhook_secret` from `INCREASE_WEBHOOK_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("INCREASE_API_KEY")
        if api_key is None:
            raise IncreaseError(
                "The api_key client option must be set either by passing api_key to the client or by setting the INCREASE_API_KEY environment variable"
            )
        self.api_key = api_key

        if webhook_secret is None:
            webhook_secret = os.environ.get("INCREASE_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret

        self._environment = environment

        base_url_env = os.environ.get("INCREASE_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `INCREASE_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        from .resources.accounts import AsyncAccountsResource

        return AsyncAccountsResource(self)

    @cached_property
    def account_numbers(self) -> AsyncAccountNumbersResource:
        from .resources.account_numbers import AsyncAccountNumbersResource

        return AsyncAccountNumbersResource(self)

    @cached_property
    def account_transfers(self) -> AsyncAccountTransfersResource:
        from .resources.account_transfers import AsyncAccountTransfersResource

        return AsyncAccountTransfersResource(self)

    @cached_property
    def cards(self) -> AsyncCardsResource:
        from .resources.cards import AsyncCardsResource

        return AsyncCardsResource(self)

    @cached_property
    def card_payments(self) -> AsyncCardPaymentsResource:
        from .resources.card_payments import AsyncCardPaymentsResource

        return AsyncCardPaymentsResource(self)

    @cached_property
    def card_purchase_supplements(self) -> AsyncCardPurchaseSupplementsResource:
        from .resources.card_purchase_supplements import AsyncCardPurchaseSupplementsResource

        return AsyncCardPurchaseSupplementsResource(self)

    @cached_property
    def card_disputes(self) -> AsyncCardDisputesResource:
        from .resources.card_disputes import AsyncCardDisputesResource

        return AsyncCardDisputesResource(self)

    @cached_property
    def physical_cards(self) -> AsyncPhysicalCardsResource:
        from .resources.physical_cards import AsyncPhysicalCardsResource

        return AsyncPhysicalCardsResource(self)

    @cached_property
    def digital_card_profiles(self) -> AsyncDigitalCardProfilesResource:
        from .resources.digital_card_profiles import AsyncDigitalCardProfilesResource

        return AsyncDigitalCardProfilesResource(self)

    @cached_property
    def physical_card_profiles(self) -> AsyncPhysicalCardProfilesResource:
        from .resources.physical_card_profiles import AsyncPhysicalCardProfilesResource

        return AsyncPhysicalCardProfilesResource(self)

    @cached_property
    def digital_wallet_tokens(self) -> AsyncDigitalWalletTokensResource:
        from .resources.digital_wallet_tokens import AsyncDigitalWalletTokensResource

        return AsyncDigitalWalletTokensResource(self)

    @cached_property
    def transactions(self) -> AsyncTransactionsResource:
        from .resources.transactions import AsyncTransactionsResource

        return AsyncTransactionsResource(self)

    @cached_property
    def pending_transactions(self) -> AsyncPendingTransactionsResource:
        from .resources.pending_transactions import AsyncPendingTransactionsResource

        return AsyncPendingTransactionsResource(self)

    @cached_property
    def declined_transactions(self) -> AsyncDeclinedTransactionsResource:
        from .resources.declined_transactions import AsyncDeclinedTransactionsResource

        return AsyncDeclinedTransactionsResource(self)

    @cached_property
    def ach_transfers(self) -> AsyncACHTransfersResource:
        from .resources.ach_transfers import AsyncACHTransfersResource

        return AsyncACHTransfersResource(self)

    @cached_property
    def ach_prenotifications(self) -> AsyncACHPrenotificationsResource:
        from .resources.ach_prenotifications import AsyncACHPrenotificationsResource

        return AsyncACHPrenotificationsResource(self)

    @cached_property
    def inbound_ach_transfers(self) -> AsyncInboundACHTransfersResource:
        from .resources.inbound_ach_transfers import AsyncInboundACHTransfersResource

        return AsyncInboundACHTransfersResource(self)

    @cached_property
    def wire_transfers(self) -> AsyncWireTransfersResource:
        from .resources.wire_transfers import AsyncWireTransfersResource

        return AsyncWireTransfersResource(self)

    @cached_property
    def inbound_wire_transfers(self) -> AsyncInboundWireTransfersResource:
        from .resources.inbound_wire_transfers import AsyncInboundWireTransfersResource

        return AsyncInboundWireTransfersResource(self)

    @cached_property
    def wire_drawdown_requests(self) -> AsyncWireDrawdownRequestsResource:
        from .resources.wire_drawdown_requests import AsyncWireDrawdownRequestsResource

        return AsyncWireDrawdownRequestsResource(self)

    @cached_property
    def inbound_wire_drawdown_requests(self) -> AsyncInboundWireDrawdownRequestsResource:
        from .resources.inbound_wire_drawdown_requests import AsyncInboundWireDrawdownRequestsResource

        return AsyncInboundWireDrawdownRequestsResource(self)

    @cached_property
    def check_transfers(self) -> AsyncCheckTransfersResource:
        from .resources.check_transfers import AsyncCheckTransfersResource

        return AsyncCheckTransfersResource(self)

    @cached_property
    def inbound_check_deposits(self) -> AsyncInboundCheckDepositsResource:
        from .resources.inbound_check_deposits import AsyncInboundCheckDepositsResource

        return AsyncInboundCheckDepositsResource(self)

    @cached_property
    def real_time_payments_transfers(self) -> AsyncRealTimePaymentsTransfersResource:
        from .resources.real_time_payments_transfers import AsyncRealTimePaymentsTransfersResource

        return AsyncRealTimePaymentsTransfersResource(self)

    @cached_property
    def inbound_real_time_payments_transfers(self) -> AsyncInboundRealTimePaymentsTransfersResource:
        from .resources.inbound_real_time_payments_transfers import AsyncInboundRealTimePaymentsTransfersResource

        return AsyncInboundRealTimePaymentsTransfersResource(self)

    @cached_property
    def fednow_transfers(self) -> AsyncFednowTransfersResource:
        from .resources.fednow_transfers import AsyncFednowTransfersResource

        return AsyncFednowTransfersResource(self)

    @cached_property
    def inbound_fednow_transfers(self) -> AsyncInboundFednowTransfersResource:
        from .resources.inbound_fednow_transfers import AsyncInboundFednowTransfersResource

        return AsyncInboundFednowTransfersResource(self)

    @cached_property
    def check_deposits(self) -> AsyncCheckDepositsResource:
        from .resources.check_deposits import AsyncCheckDepositsResource

        return AsyncCheckDepositsResource(self)

    @cached_property
    def lockboxes(self) -> AsyncLockboxesResource:
        from .resources.lockboxes import AsyncLockboxesResource

        return AsyncLockboxesResource(self)

    @cached_property
    def inbound_mail_items(self) -> AsyncInboundMailItemsResource:
        from .resources.inbound_mail_items import AsyncInboundMailItemsResource

        return AsyncInboundMailItemsResource(self)

    @cached_property
    def routing_numbers(self) -> AsyncRoutingNumbersResource:
        from .resources.routing_numbers import AsyncRoutingNumbersResource

        return AsyncRoutingNumbersResource(self)

    @cached_property
    def external_accounts(self) -> AsyncExternalAccountsResource:
        from .resources.external_accounts import AsyncExternalAccountsResource

        return AsyncExternalAccountsResource(self)

    @cached_property
    def entities(self) -> AsyncEntitiesResource:
        from .resources.entities import AsyncEntitiesResource

        return AsyncEntitiesResource(self)

    @cached_property
    def supplemental_documents(self) -> AsyncSupplementalDocumentsResource:
        from .resources.supplemental_documents import AsyncSupplementalDocumentsResource

        return AsyncSupplementalDocumentsResource(self)

    @cached_property
    def programs(self) -> AsyncProgramsResource:
        from .resources.programs import AsyncProgramsResource

        return AsyncProgramsResource(self)

    @cached_property
    def account_statements(self) -> AsyncAccountStatementsResource:
        from .resources.account_statements import AsyncAccountStatementsResource

        return AsyncAccountStatementsResource(self)

    @cached_property
    def files(self) -> AsyncFilesResource:
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

    @cached_property
    def file_links(self) -> AsyncFileLinksResource:
        from .resources.file_links import AsyncFileLinksResource

        return AsyncFileLinksResource(self)

    @cached_property
    def exports(self) -> AsyncExportsResource:
        from .resources.exports import AsyncExportsResource

        return AsyncExportsResource(self)

    @cached_property
    def events(self) -> AsyncEventsResource:
        from .resources.events import AsyncEventsResource

        return AsyncEventsResource(self)

    @cached_property
    def event_subscriptions(self) -> AsyncEventSubscriptionsResource:
        from .resources.event_subscriptions import AsyncEventSubscriptionsResource

        return AsyncEventSubscriptionsResource(self)

    @cached_property
    def real_time_decisions(self) -> AsyncRealTimeDecisionsResource:
        from .resources.real_time_decisions import AsyncRealTimeDecisionsResource

        return AsyncRealTimeDecisionsResource(self)

    @cached_property
    def bookkeeping_accounts(self) -> AsyncBookkeepingAccountsResource:
        from .resources.bookkeeping_accounts import AsyncBookkeepingAccountsResource

        return AsyncBookkeepingAccountsResource(self)

    @cached_property
    def bookkeeping_entry_sets(self) -> AsyncBookkeepingEntrySetsResource:
        from .resources.bookkeeping_entry_sets import AsyncBookkeepingEntrySetsResource

        return AsyncBookkeepingEntrySetsResource(self)

    @cached_property
    def bookkeeping_entries(self) -> AsyncBookkeepingEntriesResource:
        from .resources.bookkeeping_entries import AsyncBookkeepingEntriesResource

        return AsyncBookkeepingEntriesResource(self)

    @cached_property
    def groups(self) -> AsyncGroupsResource:
        from .resources.groups import AsyncGroupsResource

        return AsyncGroupsResource(self)

    @cached_property
    def oauth_applications(self) -> AsyncOAuthApplicationsResource:
        from .resources.oauth_applications import AsyncOAuthApplicationsResource

        return AsyncOAuthApplicationsResource(self)

    @cached_property
    def oauth_connections(self) -> AsyncOAuthConnectionsResource:
        from .resources.oauth_connections import AsyncOAuthConnectionsResource

        return AsyncOAuthConnectionsResource(self)

    @cached_property
    def oauth_tokens(self) -> AsyncOAuthTokensResource:
        from .resources.oauth_tokens import AsyncOAuthTokensResource

        return AsyncOAuthTokensResource(self)

    @cached_property
    def intrafi_account_enrollments(self) -> AsyncIntrafiAccountEnrollmentsResource:
        from .resources.intrafi_account_enrollments import AsyncIntrafiAccountEnrollmentsResource

        return AsyncIntrafiAccountEnrollmentsResource(self)

    @cached_property
    def intrafi_balances(self) -> AsyncIntrafiBalancesResource:
        from .resources.intrafi_balances import AsyncIntrafiBalancesResource

        return AsyncIntrafiBalancesResource(self)

    @cached_property
    def intrafi_exclusions(self) -> AsyncIntrafiExclusionsResource:
        from .resources.intrafi_exclusions import AsyncIntrafiExclusionsResource

        return AsyncIntrafiExclusionsResource(self)

    @cached_property
    def card_tokens(self) -> AsyncCardTokensResource:
        from .resources.card_tokens import AsyncCardTokensResource

        return AsyncCardTokensResource(self)

    @cached_property
    def card_push_transfers(self) -> AsyncCardPushTransfersResource:
        from .resources.card_push_transfers import AsyncCardPushTransfersResource

        return AsyncCardPushTransfersResource(self)

    @cached_property
    def card_validations(self) -> AsyncCardValidationsResource:
        from .resources.card_validations import AsyncCardValidationsResource

        return AsyncCardValidationsResource(self)

    @cached_property
    def simulations(self) -> AsyncSimulationsResource:
        from .resources.simulations import AsyncSimulationsResource

        return AsyncSimulationsResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooks:
        from .resources.webhooks import AsyncWebhooks

        return AsyncWebhooks(self)

    @cached_property
    def with_raw_response(self) -> AsyncIncreaseWithRawResponse:
        return AsyncIncreaseWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIncreaseWithStreamedResponse:
        return AsyncIncreaseWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(nested_format="dots", array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        environment: Literal["production", "sandbox"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        type_ = body.get("type") if is_mapping(body) else None
        if type_ == "invalid_parameters_error":
            return _exceptions.InvalidParametersError(err_msg, response=response, body=body)

        if type_ == "malformed_request_error":
            return _exceptions.MalformedRequestError(err_msg, response=response, body=body)

        if type_ == "invalid_api_key_error":
            return _exceptions.InvalidAPIKeyError(err_msg, response=response, body=body)

        if type_ == "environment_mismatch_error":
            return _exceptions.EnvironmentMismatchError(err_msg, response=response, body=body)

        if type_ == "insufficient_permissions_error":
            return _exceptions.InsufficientPermissionsError(err_msg, response=response, body=body)

        if type_ == "private_feature_error":
            return _exceptions.PrivateFeatureError(err_msg, response=response, body=body)

        if type_ == "api_method_not_found_error":
            return _exceptions.APIMethodNotFoundError(err_msg, response=response, body=body)

        if type_ == "object_not_found_error":
            return _exceptions.ObjectNotFoundError(err_msg, response=response, body=body)

        if type_ == "idempotency_key_already_used_error":
            return _exceptions.IdempotencyKeyAlreadyUsedError(err_msg, response=response, body=body)

        if type_ == "invalid_operation_error":
            return _exceptions.InvalidOperationError(err_msg, response=response, body=body)

        if type_ == "rate_limited_error":
            return _exceptions.RateLimitedError(err_msg, response=response, body=body)

        if type_ == "internal_server_error":
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(
                err_msg,
                response=response,
                body={
                    "detail": None,
                    "status": 500,
                    "title": "",
                    "type": "internal_server_error",
                },
            )

        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class IncreaseWithRawResponse:
    _client: Increase

    def __init__(self, client: Increase) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        from .resources.accounts import AccountsResourceWithRawResponse

        return AccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def account_numbers(self) -> AccountNumbersResourceWithRawResponse:
        from .resources.account_numbers import AccountNumbersResourceWithRawResponse

        return AccountNumbersResourceWithRawResponse(self._client.account_numbers)

    @cached_property
    def account_transfers(self) -> AccountTransfersResourceWithRawResponse:
        from .resources.account_transfers import AccountTransfersResourceWithRawResponse

        return AccountTransfersResourceWithRawResponse(self._client.account_transfers)

    @cached_property
    def cards(self) -> CardsResourceWithRawResponse:
        from .resources.cards import CardsResourceWithRawResponse

        return CardsResourceWithRawResponse(self._client.cards)

    @cached_property
    def card_payments(self) -> CardPaymentsResourceWithRawResponse:
        from .resources.card_payments import CardPaymentsResourceWithRawResponse

        return CardPaymentsResourceWithRawResponse(self._client.card_payments)

    @cached_property
    def card_purchase_supplements(self) -> CardPurchaseSupplementsResourceWithRawResponse:
        from .resources.card_purchase_supplements import CardPurchaseSupplementsResourceWithRawResponse

        return CardPurchaseSupplementsResourceWithRawResponse(self._client.card_purchase_supplements)

    @cached_property
    def card_disputes(self) -> CardDisputesResourceWithRawResponse:
        from .resources.card_disputes import CardDisputesResourceWithRawResponse

        return CardDisputesResourceWithRawResponse(self._client.card_disputes)

    @cached_property
    def physical_cards(self) -> PhysicalCardsResourceWithRawResponse:
        from .resources.physical_cards import PhysicalCardsResourceWithRawResponse

        return PhysicalCardsResourceWithRawResponse(self._client.physical_cards)

    @cached_property
    def digital_card_profiles(self) -> DigitalCardProfilesResourceWithRawResponse:
        from .resources.digital_card_profiles import DigitalCardProfilesResourceWithRawResponse

        return DigitalCardProfilesResourceWithRawResponse(self._client.digital_card_profiles)

    @cached_property
    def physical_card_profiles(self) -> PhysicalCardProfilesResourceWithRawResponse:
        from .resources.physical_card_profiles import PhysicalCardProfilesResourceWithRawResponse

        return PhysicalCardProfilesResourceWithRawResponse(self._client.physical_card_profiles)

    @cached_property
    def digital_wallet_tokens(self) -> DigitalWalletTokensResourceWithRawResponse:
        from .resources.digital_wallet_tokens import DigitalWalletTokensResourceWithRawResponse

        return DigitalWalletTokensResourceWithRawResponse(self._client.digital_wallet_tokens)

    @cached_property
    def transactions(self) -> TransactionsResourceWithRawResponse:
        from .resources.transactions import TransactionsResourceWithRawResponse

        return TransactionsResourceWithRawResponse(self._client.transactions)

    @cached_property
    def pending_transactions(self) -> PendingTransactionsResourceWithRawResponse:
        from .resources.pending_transactions import PendingTransactionsResourceWithRawResponse

        return PendingTransactionsResourceWithRawResponse(self._client.pending_transactions)

    @cached_property
    def declined_transactions(self) -> DeclinedTransactionsResourceWithRawResponse:
        from .resources.declined_transactions import DeclinedTransactionsResourceWithRawResponse

        return DeclinedTransactionsResourceWithRawResponse(self._client.declined_transactions)

    @cached_property
    def ach_transfers(self) -> ACHTransfersResourceWithRawResponse:
        from .resources.ach_transfers import ACHTransfersResourceWithRawResponse

        return ACHTransfersResourceWithRawResponse(self._client.ach_transfers)

    @cached_property
    def ach_prenotifications(self) -> ACHPrenotificationsResourceWithRawResponse:
        from .resources.ach_prenotifications import ACHPrenotificationsResourceWithRawResponse

        return ACHPrenotificationsResourceWithRawResponse(self._client.ach_prenotifications)

    @cached_property
    def inbound_ach_transfers(self) -> InboundACHTransfersResourceWithRawResponse:
        from .resources.inbound_ach_transfers import InboundACHTransfersResourceWithRawResponse

        return InboundACHTransfersResourceWithRawResponse(self._client.inbound_ach_transfers)

    @cached_property
    def wire_transfers(self) -> WireTransfersResourceWithRawResponse:
        from .resources.wire_transfers import WireTransfersResourceWithRawResponse

        return WireTransfersResourceWithRawResponse(self._client.wire_transfers)

    @cached_property
    def inbound_wire_transfers(self) -> InboundWireTransfersResourceWithRawResponse:
        from .resources.inbound_wire_transfers import InboundWireTransfersResourceWithRawResponse

        return InboundWireTransfersResourceWithRawResponse(self._client.inbound_wire_transfers)

    @cached_property
    def wire_drawdown_requests(self) -> WireDrawdownRequestsResourceWithRawResponse:
        from .resources.wire_drawdown_requests import WireDrawdownRequestsResourceWithRawResponse

        return WireDrawdownRequestsResourceWithRawResponse(self._client.wire_drawdown_requests)

    @cached_property
    def inbound_wire_drawdown_requests(
        self,
    ) -> InboundWireDrawdownRequestsResourceWithRawResponse:
        from .resources.inbound_wire_drawdown_requests import InboundWireDrawdownRequestsResourceWithRawResponse

        return InboundWireDrawdownRequestsResourceWithRawResponse(self._client.inbound_wire_drawdown_requests)

    @cached_property
    def check_transfers(self) -> CheckTransfersResourceWithRawResponse:
        from .resources.check_transfers import CheckTransfersResourceWithRawResponse

        return CheckTransfersResourceWithRawResponse(self._client.check_transfers)

    @cached_property
    def inbound_check_deposits(self) -> InboundCheckDepositsResourceWithRawResponse:
        from .resources.inbound_check_deposits import InboundCheckDepositsResourceWithRawResponse

        return InboundCheckDepositsResourceWithRawResponse(self._client.inbound_check_deposits)

    @cached_property
    def real_time_payments_transfers(
        self,
    ) -> RealTimePaymentsTransfersResourceWithRawResponse:
        from .resources.real_time_payments_transfers import RealTimePaymentsTransfersResourceWithRawResponse

        return RealTimePaymentsTransfersResourceWithRawResponse(self._client.real_time_payments_transfers)

    @cached_property
    def inbound_real_time_payments_transfers(
        self,
    ) -> InboundRealTimePaymentsTransfersResourceWithRawResponse:
        from .resources.inbound_real_time_payments_transfers import (
            InboundRealTimePaymentsTransfersResourceWithRawResponse,
        )

        return InboundRealTimePaymentsTransfersResourceWithRawResponse(
            self._client.inbound_real_time_payments_transfers
        )

    @cached_property
    def fednow_transfers(self) -> FednowTransfersResourceWithRawResponse:
        from .resources.fednow_transfers import FednowTransfersResourceWithRawResponse

        return FednowTransfersResourceWithRawResponse(self._client.fednow_transfers)

    @cached_property
    def inbound_fednow_transfers(self) -> InboundFednowTransfersResourceWithRawResponse:
        from .resources.inbound_fednow_transfers import InboundFednowTransfersResourceWithRawResponse

        return InboundFednowTransfersResourceWithRawResponse(self._client.inbound_fednow_transfers)

    @cached_property
    def check_deposits(self) -> CheckDepositsResourceWithRawResponse:
        from .resources.check_deposits import CheckDepositsResourceWithRawResponse

        return CheckDepositsResourceWithRawResponse(self._client.check_deposits)

    @cached_property
    def lockboxes(self) -> LockboxesResourceWithRawResponse:
        from .resources.lockboxes import LockboxesResourceWithRawResponse

        return LockboxesResourceWithRawResponse(self._client.lockboxes)

    @cached_property
    def inbound_mail_items(self) -> InboundMailItemsResourceWithRawResponse:
        from .resources.inbound_mail_items import InboundMailItemsResourceWithRawResponse

        return InboundMailItemsResourceWithRawResponse(self._client.inbound_mail_items)

    @cached_property
    def routing_numbers(self) -> RoutingNumbersResourceWithRawResponse:
        from .resources.routing_numbers import RoutingNumbersResourceWithRawResponse

        return RoutingNumbersResourceWithRawResponse(self._client.routing_numbers)

    @cached_property
    def external_accounts(self) -> ExternalAccountsResourceWithRawResponse:
        from .resources.external_accounts import ExternalAccountsResourceWithRawResponse

        return ExternalAccountsResourceWithRawResponse(self._client.external_accounts)

    @cached_property
    def entities(self) -> EntitiesResourceWithRawResponse:
        from .resources.entities import EntitiesResourceWithRawResponse

        return EntitiesResourceWithRawResponse(self._client.entities)

    @cached_property
    def supplemental_documents(self) -> SupplementalDocumentsResourceWithRawResponse:
        from .resources.supplemental_documents import SupplementalDocumentsResourceWithRawResponse

        return SupplementalDocumentsResourceWithRawResponse(self._client.supplemental_documents)

    @cached_property
    def programs(self) -> ProgramsResourceWithRawResponse:
        from .resources.programs import ProgramsResourceWithRawResponse

        return ProgramsResourceWithRawResponse(self._client.programs)

    @cached_property
    def account_statements(self) -> AccountStatementsResourceWithRawResponse:
        from .resources.account_statements import AccountStatementsResourceWithRawResponse

        return AccountStatementsResourceWithRawResponse(self._client.account_statements)

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)

    @cached_property
    def file_links(self) -> FileLinksResourceWithRawResponse:
        from .resources.file_links import FileLinksResourceWithRawResponse

        return FileLinksResourceWithRawResponse(self._client.file_links)

    @cached_property
    def exports(self) -> ExportsResourceWithRawResponse:
        from .resources.exports import ExportsResourceWithRawResponse

        return ExportsResourceWithRawResponse(self._client.exports)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        from .resources.events import EventsResourceWithRawResponse

        return EventsResourceWithRawResponse(self._client.events)

    @cached_property
    def event_subscriptions(self) -> EventSubscriptionsResourceWithRawResponse:
        from .resources.event_subscriptions import EventSubscriptionsResourceWithRawResponse

        return EventSubscriptionsResourceWithRawResponse(self._client.event_subscriptions)

    @cached_property
    def real_time_decisions(self) -> RealTimeDecisionsResourceWithRawResponse:
        from .resources.real_time_decisions import RealTimeDecisionsResourceWithRawResponse

        return RealTimeDecisionsResourceWithRawResponse(self._client.real_time_decisions)

    @cached_property
    def bookkeeping_accounts(self) -> BookkeepingAccountsResourceWithRawResponse:
        from .resources.bookkeeping_accounts import BookkeepingAccountsResourceWithRawResponse

        return BookkeepingAccountsResourceWithRawResponse(self._client.bookkeeping_accounts)

    @cached_property
    def bookkeeping_entry_sets(self) -> BookkeepingEntrySetsResourceWithRawResponse:
        from .resources.bookkeeping_entry_sets import BookkeepingEntrySetsResourceWithRawResponse

        return BookkeepingEntrySetsResourceWithRawResponse(self._client.bookkeeping_entry_sets)

    @cached_property
    def bookkeeping_entries(self) -> BookkeepingEntriesResourceWithRawResponse:
        from .resources.bookkeeping_entries import BookkeepingEntriesResourceWithRawResponse

        return BookkeepingEntriesResourceWithRawResponse(self._client.bookkeeping_entries)

    @cached_property
    def groups(self) -> GroupsResourceWithRawResponse:
        from .resources.groups import GroupsResourceWithRawResponse

        return GroupsResourceWithRawResponse(self._client.groups)

    @cached_property
    def oauth_applications(self) -> OAuthApplicationsResourceWithRawResponse:
        from .resources.oauth_applications import OAuthApplicationsResourceWithRawResponse

        return OAuthApplicationsResourceWithRawResponse(self._client.oauth_applications)

    @cached_property
    def oauth_connections(self) -> OAuthConnectionsResourceWithRawResponse:
        from .resources.oauth_connections import OAuthConnectionsResourceWithRawResponse

        return OAuthConnectionsResourceWithRawResponse(self._client.oauth_connections)

    @cached_property
    def oauth_tokens(self) -> OAuthTokensResourceWithRawResponse:
        from .resources.oauth_tokens import OAuthTokensResourceWithRawResponse

        return OAuthTokensResourceWithRawResponse(self._client.oauth_tokens)

    @cached_property
    def intrafi_account_enrollments(
        self,
    ) -> IntrafiAccountEnrollmentsResourceWithRawResponse:
        from .resources.intrafi_account_enrollments import IntrafiAccountEnrollmentsResourceWithRawResponse

        return IntrafiAccountEnrollmentsResourceWithRawResponse(self._client.intrafi_account_enrollments)

    @cached_property
    def intrafi_balances(self) -> IntrafiBalancesResourceWithRawResponse:
        from .resources.intrafi_balances import IntrafiBalancesResourceWithRawResponse

        return IntrafiBalancesResourceWithRawResponse(self._client.intrafi_balances)

    @cached_property
    def intrafi_exclusions(self) -> IntrafiExclusionsResourceWithRawResponse:
        from .resources.intrafi_exclusions import IntrafiExclusionsResourceWithRawResponse

        return IntrafiExclusionsResourceWithRawResponse(self._client.intrafi_exclusions)

    @cached_property
    def card_tokens(self) -> CardTokensResourceWithRawResponse:
        from .resources.card_tokens import CardTokensResourceWithRawResponse

        return CardTokensResourceWithRawResponse(self._client.card_tokens)

    @cached_property
    def card_push_transfers(self) -> CardPushTransfersResourceWithRawResponse:
        from .resources.card_push_transfers import CardPushTransfersResourceWithRawResponse

        return CardPushTransfersResourceWithRawResponse(self._client.card_push_transfers)

    @cached_property
    def card_validations(self) -> CardValidationsResourceWithRawResponse:
        from .resources.card_validations import CardValidationsResourceWithRawResponse

        return CardValidationsResourceWithRawResponse(self._client.card_validations)

    @cached_property
    def simulations(self) -> SimulationsResourceWithRawResponse:
        from .resources.simulations import SimulationsResourceWithRawResponse

        return SimulationsResourceWithRawResponse(self._client.simulations)


class AsyncIncreaseWithRawResponse:
    _client: AsyncIncrease

    def __init__(self, client: AsyncIncrease) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        from .resources.accounts import AsyncAccountsResourceWithRawResponse

        return AsyncAccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def account_numbers(self) -> AsyncAccountNumbersResourceWithRawResponse:
        from .resources.account_numbers import AsyncAccountNumbersResourceWithRawResponse

        return AsyncAccountNumbersResourceWithRawResponse(self._client.account_numbers)

    @cached_property
    def account_transfers(self) -> AsyncAccountTransfersResourceWithRawResponse:
        from .resources.account_transfers import AsyncAccountTransfersResourceWithRawResponse

        return AsyncAccountTransfersResourceWithRawResponse(self._client.account_transfers)

    @cached_property
    def cards(self) -> AsyncCardsResourceWithRawResponse:
        from .resources.cards import AsyncCardsResourceWithRawResponse

        return AsyncCardsResourceWithRawResponse(self._client.cards)

    @cached_property
    def card_payments(self) -> AsyncCardPaymentsResourceWithRawResponse:
        from .resources.card_payments import AsyncCardPaymentsResourceWithRawResponse

        return AsyncCardPaymentsResourceWithRawResponse(self._client.card_payments)

    @cached_property
    def card_purchase_supplements(
        self,
    ) -> AsyncCardPurchaseSupplementsResourceWithRawResponse:
        from .resources.card_purchase_supplements import AsyncCardPurchaseSupplementsResourceWithRawResponse

        return AsyncCardPurchaseSupplementsResourceWithRawResponse(self._client.card_purchase_supplements)

    @cached_property
    def card_disputes(self) -> AsyncCardDisputesResourceWithRawResponse:
        from .resources.card_disputes import AsyncCardDisputesResourceWithRawResponse

        return AsyncCardDisputesResourceWithRawResponse(self._client.card_disputes)

    @cached_property
    def physical_cards(self) -> AsyncPhysicalCardsResourceWithRawResponse:
        from .resources.physical_cards import AsyncPhysicalCardsResourceWithRawResponse

        return AsyncPhysicalCardsResourceWithRawResponse(self._client.physical_cards)

    @cached_property
    def digital_card_profiles(self) -> AsyncDigitalCardProfilesResourceWithRawResponse:
        from .resources.digital_card_profiles import AsyncDigitalCardProfilesResourceWithRawResponse

        return AsyncDigitalCardProfilesResourceWithRawResponse(self._client.digital_card_profiles)

    @cached_property
    def physical_card_profiles(self) -> AsyncPhysicalCardProfilesResourceWithRawResponse:
        from .resources.physical_card_profiles import AsyncPhysicalCardProfilesResourceWithRawResponse

        return AsyncPhysicalCardProfilesResourceWithRawResponse(self._client.physical_card_profiles)

    @cached_property
    def digital_wallet_tokens(self) -> AsyncDigitalWalletTokensResourceWithRawResponse:
        from .resources.digital_wallet_tokens import AsyncDigitalWalletTokensResourceWithRawResponse

        return AsyncDigitalWalletTokensResourceWithRawResponse(self._client.digital_wallet_tokens)

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithRawResponse:
        from .resources.transactions import AsyncTransactionsResourceWithRawResponse

        return AsyncTransactionsResourceWithRawResponse(self._client.transactions)

    @cached_property
    def pending_transactions(self) -> AsyncPendingTransactionsResourceWithRawResponse:
        from .resources.pending_transactions import AsyncPendingTransactionsResourceWithRawResponse

        return AsyncPendingTransactionsResourceWithRawResponse(self._client.pending_transactions)

    @cached_property
    def declined_transactions(self) -> AsyncDeclinedTransactionsResourceWithRawResponse:
        from .resources.declined_transactions import AsyncDeclinedTransactionsResourceWithRawResponse

        return AsyncDeclinedTransactionsResourceWithRawResponse(self._client.declined_transactions)

    @cached_property
    def ach_transfers(self) -> AsyncACHTransfersResourceWithRawResponse:
        from .resources.ach_transfers import AsyncACHTransfersResourceWithRawResponse

        return AsyncACHTransfersResourceWithRawResponse(self._client.ach_transfers)

    @cached_property
    def ach_prenotifications(self) -> AsyncACHPrenotificationsResourceWithRawResponse:
        from .resources.ach_prenotifications import AsyncACHPrenotificationsResourceWithRawResponse

        return AsyncACHPrenotificationsResourceWithRawResponse(self._client.ach_prenotifications)

    @cached_property
    def inbound_ach_transfers(self) -> AsyncInboundACHTransfersResourceWithRawResponse:
        from .resources.inbound_ach_transfers import AsyncInboundACHTransfersResourceWithRawResponse

        return AsyncInboundACHTransfersResourceWithRawResponse(self._client.inbound_ach_transfers)

    @cached_property
    def wire_transfers(self) -> AsyncWireTransfersResourceWithRawResponse:
        from .resources.wire_transfers import AsyncWireTransfersResourceWithRawResponse

        return AsyncWireTransfersResourceWithRawResponse(self._client.wire_transfers)

    @cached_property
    def inbound_wire_transfers(self) -> AsyncInboundWireTransfersResourceWithRawResponse:
        from .resources.inbound_wire_transfers import AsyncInboundWireTransfersResourceWithRawResponse

        return AsyncInboundWireTransfersResourceWithRawResponse(self._client.inbound_wire_transfers)

    @cached_property
    def wire_drawdown_requests(self) -> AsyncWireDrawdownRequestsResourceWithRawResponse:
        from .resources.wire_drawdown_requests import AsyncWireDrawdownRequestsResourceWithRawResponse

        return AsyncWireDrawdownRequestsResourceWithRawResponse(self._client.wire_drawdown_requests)

    @cached_property
    def inbound_wire_drawdown_requests(
        self,
    ) -> AsyncInboundWireDrawdownRequestsResourceWithRawResponse:
        from .resources.inbound_wire_drawdown_requests import AsyncInboundWireDrawdownRequestsResourceWithRawResponse

        return AsyncInboundWireDrawdownRequestsResourceWithRawResponse(self._client.inbound_wire_drawdown_requests)

    @cached_property
    def check_transfers(self) -> AsyncCheckTransfersResourceWithRawResponse:
        from .resources.check_transfers import AsyncCheckTransfersResourceWithRawResponse

        return AsyncCheckTransfersResourceWithRawResponse(self._client.check_transfers)

    @cached_property
    def inbound_check_deposits(self) -> AsyncInboundCheckDepositsResourceWithRawResponse:
        from .resources.inbound_check_deposits import AsyncInboundCheckDepositsResourceWithRawResponse

        return AsyncInboundCheckDepositsResourceWithRawResponse(self._client.inbound_check_deposits)

    @cached_property
    def real_time_payments_transfers(
        self,
    ) -> AsyncRealTimePaymentsTransfersResourceWithRawResponse:
        from .resources.real_time_payments_transfers import AsyncRealTimePaymentsTransfersResourceWithRawResponse

        return AsyncRealTimePaymentsTransfersResourceWithRawResponse(self._client.real_time_payments_transfers)

    @cached_property
    def inbound_real_time_payments_transfers(
        self,
    ) -> AsyncInboundRealTimePaymentsTransfersResourceWithRawResponse:
        from .resources.inbound_real_time_payments_transfers import (
            AsyncInboundRealTimePaymentsTransfersResourceWithRawResponse,
        )

        return AsyncInboundRealTimePaymentsTransfersResourceWithRawResponse(
            self._client.inbound_real_time_payments_transfers
        )

    @cached_property
    def fednow_transfers(self) -> AsyncFednowTransfersResourceWithRawResponse:
        from .resources.fednow_transfers import AsyncFednowTransfersResourceWithRawResponse

        return AsyncFednowTransfersResourceWithRawResponse(self._client.fednow_transfers)

    @cached_property
    def inbound_fednow_transfers(self) -> AsyncInboundFednowTransfersResourceWithRawResponse:
        from .resources.inbound_fednow_transfers import AsyncInboundFednowTransfersResourceWithRawResponse

        return AsyncInboundFednowTransfersResourceWithRawResponse(self._client.inbound_fednow_transfers)

    @cached_property
    def check_deposits(self) -> AsyncCheckDepositsResourceWithRawResponse:
        from .resources.check_deposits import AsyncCheckDepositsResourceWithRawResponse

        return AsyncCheckDepositsResourceWithRawResponse(self._client.check_deposits)

    @cached_property
    def lockboxes(self) -> AsyncLockboxesResourceWithRawResponse:
        from .resources.lockboxes import AsyncLockboxesResourceWithRawResponse

        return AsyncLockboxesResourceWithRawResponse(self._client.lockboxes)

    @cached_property
    def inbound_mail_items(self) -> AsyncInboundMailItemsResourceWithRawResponse:
        from .resources.inbound_mail_items import AsyncInboundMailItemsResourceWithRawResponse

        return AsyncInboundMailItemsResourceWithRawResponse(self._client.inbound_mail_items)

    @cached_property
    def routing_numbers(self) -> AsyncRoutingNumbersResourceWithRawResponse:
        from .resources.routing_numbers import AsyncRoutingNumbersResourceWithRawResponse

        return AsyncRoutingNumbersResourceWithRawResponse(self._client.routing_numbers)

    @cached_property
    def external_accounts(self) -> AsyncExternalAccountsResourceWithRawResponse:
        from .resources.external_accounts import AsyncExternalAccountsResourceWithRawResponse

        return AsyncExternalAccountsResourceWithRawResponse(self._client.external_accounts)

    @cached_property
    def entities(self) -> AsyncEntitiesResourceWithRawResponse:
        from .resources.entities import AsyncEntitiesResourceWithRawResponse

        return AsyncEntitiesResourceWithRawResponse(self._client.entities)

    @cached_property
    def supplemental_documents(self) -> AsyncSupplementalDocumentsResourceWithRawResponse:
        from .resources.supplemental_documents import AsyncSupplementalDocumentsResourceWithRawResponse

        return AsyncSupplementalDocumentsResourceWithRawResponse(self._client.supplemental_documents)

    @cached_property
    def programs(self) -> AsyncProgramsResourceWithRawResponse:
        from .resources.programs import AsyncProgramsResourceWithRawResponse

        return AsyncProgramsResourceWithRawResponse(self._client.programs)

    @cached_property
    def account_statements(self) -> AsyncAccountStatementsResourceWithRawResponse:
        from .resources.account_statements import AsyncAccountStatementsResourceWithRawResponse

        return AsyncAccountStatementsResourceWithRawResponse(self._client.account_statements)

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)

    @cached_property
    def file_links(self) -> AsyncFileLinksResourceWithRawResponse:
        from .resources.file_links import AsyncFileLinksResourceWithRawResponse

        return AsyncFileLinksResourceWithRawResponse(self._client.file_links)

    @cached_property
    def exports(self) -> AsyncExportsResourceWithRawResponse:
        from .resources.exports import AsyncExportsResourceWithRawResponse

        return AsyncExportsResourceWithRawResponse(self._client.exports)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        from .resources.events import AsyncEventsResourceWithRawResponse

        return AsyncEventsResourceWithRawResponse(self._client.events)

    @cached_property
    def event_subscriptions(self) -> AsyncEventSubscriptionsResourceWithRawResponse:
        from .resources.event_subscriptions import AsyncEventSubscriptionsResourceWithRawResponse

        return AsyncEventSubscriptionsResourceWithRawResponse(self._client.event_subscriptions)

    @cached_property
    def real_time_decisions(self) -> AsyncRealTimeDecisionsResourceWithRawResponse:
        from .resources.real_time_decisions import AsyncRealTimeDecisionsResourceWithRawResponse

        return AsyncRealTimeDecisionsResourceWithRawResponse(self._client.real_time_decisions)

    @cached_property
    def bookkeeping_accounts(self) -> AsyncBookkeepingAccountsResourceWithRawResponse:
        from .resources.bookkeeping_accounts import AsyncBookkeepingAccountsResourceWithRawResponse

        return AsyncBookkeepingAccountsResourceWithRawResponse(self._client.bookkeeping_accounts)

    @cached_property
    def bookkeeping_entry_sets(self) -> AsyncBookkeepingEntrySetsResourceWithRawResponse:
        from .resources.bookkeeping_entry_sets import AsyncBookkeepingEntrySetsResourceWithRawResponse

        return AsyncBookkeepingEntrySetsResourceWithRawResponse(self._client.bookkeeping_entry_sets)

    @cached_property
    def bookkeeping_entries(self) -> AsyncBookkeepingEntriesResourceWithRawResponse:
        from .resources.bookkeeping_entries import AsyncBookkeepingEntriesResourceWithRawResponse

        return AsyncBookkeepingEntriesResourceWithRawResponse(self._client.bookkeeping_entries)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithRawResponse:
        from .resources.groups import AsyncGroupsResourceWithRawResponse

        return AsyncGroupsResourceWithRawResponse(self._client.groups)

    @cached_property
    def oauth_applications(self) -> AsyncOAuthApplicationsResourceWithRawResponse:
        from .resources.oauth_applications import AsyncOAuthApplicationsResourceWithRawResponse

        return AsyncOAuthApplicationsResourceWithRawResponse(self._client.oauth_applications)

    @cached_property
    def oauth_connections(self) -> AsyncOAuthConnectionsResourceWithRawResponse:
        from .resources.oauth_connections import AsyncOAuthConnectionsResourceWithRawResponse

        return AsyncOAuthConnectionsResourceWithRawResponse(self._client.oauth_connections)

    @cached_property
    def oauth_tokens(self) -> AsyncOAuthTokensResourceWithRawResponse:
        from .resources.oauth_tokens import AsyncOAuthTokensResourceWithRawResponse

        return AsyncOAuthTokensResourceWithRawResponse(self._client.oauth_tokens)

    @cached_property
    def intrafi_account_enrollments(
        self,
    ) -> AsyncIntrafiAccountEnrollmentsResourceWithRawResponse:
        from .resources.intrafi_account_enrollments import AsyncIntrafiAccountEnrollmentsResourceWithRawResponse

        return AsyncIntrafiAccountEnrollmentsResourceWithRawResponse(self._client.intrafi_account_enrollments)

    @cached_property
    def intrafi_balances(self) -> AsyncIntrafiBalancesResourceWithRawResponse:
        from .resources.intrafi_balances import AsyncIntrafiBalancesResourceWithRawResponse

        return AsyncIntrafiBalancesResourceWithRawResponse(self._client.intrafi_balances)

    @cached_property
    def intrafi_exclusions(self) -> AsyncIntrafiExclusionsResourceWithRawResponse:
        from .resources.intrafi_exclusions import AsyncIntrafiExclusionsResourceWithRawResponse

        return AsyncIntrafiExclusionsResourceWithRawResponse(self._client.intrafi_exclusions)

    @cached_property
    def card_tokens(self) -> AsyncCardTokensResourceWithRawResponse:
        from .resources.card_tokens import AsyncCardTokensResourceWithRawResponse

        return AsyncCardTokensResourceWithRawResponse(self._client.card_tokens)

    @cached_property
    def card_push_transfers(self) -> AsyncCardPushTransfersResourceWithRawResponse:
        from .resources.card_push_transfers import AsyncCardPushTransfersResourceWithRawResponse

        return AsyncCardPushTransfersResourceWithRawResponse(self._client.card_push_transfers)

    @cached_property
    def card_validations(self) -> AsyncCardValidationsResourceWithRawResponse:
        from .resources.card_validations import AsyncCardValidationsResourceWithRawResponse

        return AsyncCardValidationsResourceWithRawResponse(self._client.card_validations)

    @cached_property
    def simulations(self) -> AsyncSimulationsResourceWithRawResponse:
        from .resources.simulations import AsyncSimulationsResourceWithRawResponse

        return AsyncSimulationsResourceWithRawResponse(self._client.simulations)


class IncreaseWithStreamedResponse:
    _client: Increase

    def __init__(self, client: Increase) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        from .resources.accounts import AccountsResourceWithStreamingResponse

        return AccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def account_numbers(self) -> AccountNumbersResourceWithStreamingResponse:
        from .resources.account_numbers import AccountNumbersResourceWithStreamingResponse

        return AccountNumbersResourceWithStreamingResponse(self._client.account_numbers)

    @cached_property
    def account_transfers(self) -> AccountTransfersResourceWithStreamingResponse:
        from .resources.account_transfers import AccountTransfersResourceWithStreamingResponse

        return AccountTransfersResourceWithStreamingResponse(self._client.account_transfers)

    @cached_property
    def cards(self) -> CardsResourceWithStreamingResponse:
        from .resources.cards import CardsResourceWithStreamingResponse

        return CardsResourceWithStreamingResponse(self._client.cards)

    @cached_property
    def card_payments(self) -> CardPaymentsResourceWithStreamingResponse:
        from .resources.card_payments import CardPaymentsResourceWithStreamingResponse

        return CardPaymentsResourceWithStreamingResponse(self._client.card_payments)

    @cached_property
    def card_purchase_supplements(
        self,
    ) -> CardPurchaseSupplementsResourceWithStreamingResponse:
        from .resources.card_purchase_supplements import CardPurchaseSupplementsResourceWithStreamingResponse

        return CardPurchaseSupplementsResourceWithStreamingResponse(self._client.card_purchase_supplements)

    @cached_property
    def card_disputes(self) -> CardDisputesResourceWithStreamingResponse:
        from .resources.card_disputes import CardDisputesResourceWithStreamingResponse

        return CardDisputesResourceWithStreamingResponse(self._client.card_disputes)

    @cached_property
    def physical_cards(self) -> PhysicalCardsResourceWithStreamingResponse:
        from .resources.physical_cards import PhysicalCardsResourceWithStreamingResponse

        return PhysicalCardsResourceWithStreamingResponse(self._client.physical_cards)

    @cached_property
    def digital_card_profiles(self) -> DigitalCardProfilesResourceWithStreamingResponse:
        from .resources.digital_card_profiles import DigitalCardProfilesResourceWithStreamingResponse

        return DigitalCardProfilesResourceWithStreamingResponse(self._client.digital_card_profiles)

    @cached_property
    def physical_card_profiles(self) -> PhysicalCardProfilesResourceWithStreamingResponse:
        from .resources.physical_card_profiles import PhysicalCardProfilesResourceWithStreamingResponse

        return PhysicalCardProfilesResourceWithStreamingResponse(self._client.physical_card_profiles)

    @cached_property
    def digital_wallet_tokens(self) -> DigitalWalletTokensResourceWithStreamingResponse:
        from .resources.digital_wallet_tokens import DigitalWalletTokensResourceWithStreamingResponse

        return DigitalWalletTokensResourceWithStreamingResponse(self._client.digital_wallet_tokens)

    @cached_property
    def transactions(self) -> TransactionsResourceWithStreamingResponse:
        from .resources.transactions import TransactionsResourceWithStreamingResponse

        return TransactionsResourceWithStreamingResponse(self._client.transactions)

    @cached_property
    def pending_transactions(self) -> PendingTransactionsResourceWithStreamingResponse:
        from .resources.pending_transactions import PendingTransactionsResourceWithStreamingResponse

        return PendingTransactionsResourceWithStreamingResponse(self._client.pending_transactions)

    @cached_property
    def declined_transactions(self) -> DeclinedTransactionsResourceWithStreamingResponse:
        from .resources.declined_transactions import DeclinedTransactionsResourceWithStreamingResponse

        return DeclinedTransactionsResourceWithStreamingResponse(self._client.declined_transactions)

    @cached_property
    def ach_transfers(self) -> ACHTransfersResourceWithStreamingResponse:
        from .resources.ach_transfers import ACHTransfersResourceWithStreamingResponse

        return ACHTransfersResourceWithStreamingResponse(self._client.ach_transfers)

    @cached_property
    def ach_prenotifications(self) -> ACHPrenotificationsResourceWithStreamingResponse:
        from .resources.ach_prenotifications import ACHPrenotificationsResourceWithStreamingResponse

        return ACHPrenotificationsResourceWithStreamingResponse(self._client.ach_prenotifications)

    @cached_property
    def inbound_ach_transfers(self) -> InboundACHTransfersResourceWithStreamingResponse:
        from .resources.inbound_ach_transfers import InboundACHTransfersResourceWithStreamingResponse

        return InboundACHTransfersResourceWithStreamingResponse(self._client.inbound_ach_transfers)

    @cached_property
    def wire_transfers(self) -> WireTransfersResourceWithStreamingResponse:
        from .resources.wire_transfers import WireTransfersResourceWithStreamingResponse

        return WireTransfersResourceWithStreamingResponse(self._client.wire_transfers)

    @cached_property
    def inbound_wire_transfers(self) -> InboundWireTransfersResourceWithStreamingResponse:
        from .resources.inbound_wire_transfers import InboundWireTransfersResourceWithStreamingResponse

        return InboundWireTransfersResourceWithStreamingResponse(self._client.inbound_wire_transfers)

    @cached_property
    def wire_drawdown_requests(self) -> WireDrawdownRequestsResourceWithStreamingResponse:
        from .resources.wire_drawdown_requests import WireDrawdownRequestsResourceWithStreamingResponse

        return WireDrawdownRequestsResourceWithStreamingResponse(self._client.wire_drawdown_requests)

    @cached_property
    def inbound_wire_drawdown_requests(
        self,
    ) -> InboundWireDrawdownRequestsResourceWithStreamingResponse:
        from .resources.inbound_wire_drawdown_requests import InboundWireDrawdownRequestsResourceWithStreamingResponse

        return InboundWireDrawdownRequestsResourceWithStreamingResponse(self._client.inbound_wire_drawdown_requests)

    @cached_property
    def check_transfers(self) -> CheckTransfersResourceWithStreamingResponse:
        from .resources.check_transfers import CheckTransfersResourceWithStreamingResponse

        return CheckTransfersResourceWithStreamingResponse(self._client.check_transfers)

    @cached_property
    def inbound_check_deposits(self) -> InboundCheckDepositsResourceWithStreamingResponse:
        from .resources.inbound_check_deposits import InboundCheckDepositsResourceWithStreamingResponse

        return InboundCheckDepositsResourceWithStreamingResponse(self._client.inbound_check_deposits)

    @cached_property
    def real_time_payments_transfers(
        self,
    ) -> RealTimePaymentsTransfersResourceWithStreamingResponse:
        from .resources.real_time_payments_transfers import RealTimePaymentsTransfersResourceWithStreamingResponse

        return RealTimePaymentsTransfersResourceWithStreamingResponse(self._client.real_time_payments_transfers)

    @cached_property
    def inbound_real_time_payments_transfers(
        self,
    ) -> InboundRealTimePaymentsTransfersResourceWithStreamingResponse:
        from .resources.inbound_real_time_payments_transfers import (
            InboundRealTimePaymentsTransfersResourceWithStreamingResponse,
        )

        return InboundRealTimePaymentsTransfersResourceWithStreamingResponse(
            self._client.inbound_real_time_payments_transfers
        )

    @cached_property
    def fednow_transfers(self) -> FednowTransfersResourceWithStreamingResponse:
        from .resources.fednow_transfers import FednowTransfersResourceWithStreamingResponse

        return FednowTransfersResourceWithStreamingResponse(self._client.fednow_transfers)

    @cached_property
    def inbound_fednow_transfers(self) -> InboundFednowTransfersResourceWithStreamingResponse:
        from .resources.inbound_fednow_transfers import InboundFednowTransfersResourceWithStreamingResponse

        return InboundFednowTransfersResourceWithStreamingResponse(self._client.inbound_fednow_transfers)

    @cached_property
    def check_deposits(self) -> CheckDepositsResourceWithStreamingResponse:
        from .resources.check_deposits import CheckDepositsResourceWithStreamingResponse

        return CheckDepositsResourceWithStreamingResponse(self._client.check_deposits)

    @cached_property
    def lockboxes(self) -> LockboxesResourceWithStreamingResponse:
        from .resources.lockboxes import LockboxesResourceWithStreamingResponse

        return LockboxesResourceWithStreamingResponse(self._client.lockboxes)

    @cached_property
    def inbound_mail_items(self) -> InboundMailItemsResourceWithStreamingResponse:
        from .resources.inbound_mail_items import InboundMailItemsResourceWithStreamingResponse

        return InboundMailItemsResourceWithStreamingResponse(self._client.inbound_mail_items)

    @cached_property
    def routing_numbers(self) -> RoutingNumbersResourceWithStreamingResponse:
        from .resources.routing_numbers import RoutingNumbersResourceWithStreamingResponse

        return RoutingNumbersResourceWithStreamingResponse(self._client.routing_numbers)

    @cached_property
    def external_accounts(self) -> ExternalAccountsResourceWithStreamingResponse:
        from .resources.external_accounts import ExternalAccountsResourceWithStreamingResponse

        return ExternalAccountsResourceWithStreamingResponse(self._client.external_accounts)

    @cached_property
    def entities(self) -> EntitiesResourceWithStreamingResponse:
        from .resources.entities import EntitiesResourceWithStreamingResponse

        return EntitiesResourceWithStreamingResponse(self._client.entities)

    @cached_property
    def supplemental_documents(self) -> SupplementalDocumentsResourceWithStreamingResponse:
        from .resources.supplemental_documents import SupplementalDocumentsResourceWithStreamingResponse

        return SupplementalDocumentsResourceWithStreamingResponse(self._client.supplemental_documents)

    @cached_property
    def programs(self) -> ProgramsResourceWithStreamingResponse:
        from .resources.programs import ProgramsResourceWithStreamingResponse

        return ProgramsResourceWithStreamingResponse(self._client.programs)

    @cached_property
    def account_statements(self) -> AccountStatementsResourceWithStreamingResponse:
        from .resources.account_statements import AccountStatementsResourceWithStreamingResponse

        return AccountStatementsResourceWithStreamingResponse(self._client.account_statements)

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def file_links(self) -> FileLinksResourceWithStreamingResponse:
        from .resources.file_links import FileLinksResourceWithStreamingResponse

        return FileLinksResourceWithStreamingResponse(self._client.file_links)

    @cached_property
    def exports(self) -> ExportsResourceWithStreamingResponse:
        from .resources.exports import ExportsResourceWithStreamingResponse

        return ExportsResourceWithStreamingResponse(self._client.exports)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        from .resources.events import EventsResourceWithStreamingResponse

        return EventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def event_subscriptions(self) -> EventSubscriptionsResourceWithStreamingResponse:
        from .resources.event_subscriptions import EventSubscriptionsResourceWithStreamingResponse

        return EventSubscriptionsResourceWithStreamingResponse(self._client.event_subscriptions)

    @cached_property
    def real_time_decisions(self) -> RealTimeDecisionsResourceWithStreamingResponse:
        from .resources.real_time_decisions import RealTimeDecisionsResourceWithStreamingResponse

        return RealTimeDecisionsResourceWithStreamingResponse(self._client.real_time_decisions)

    @cached_property
    def bookkeeping_accounts(self) -> BookkeepingAccountsResourceWithStreamingResponse:
        from .resources.bookkeeping_accounts import BookkeepingAccountsResourceWithStreamingResponse

        return BookkeepingAccountsResourceWithStreamingResponse(self._client.bookkeeping_accounts)

    @cached_property
    def bookkeeping_entry_sets(self) -> BookkeepingEntrySetsResourceWithStreamingResponse:
        from .resources.bookkeeping_entry_sets import BookkeepingEntrySetsResourceWithStreamingResponse

        return BookkeepingEntrySetsResourceWithStreamingResponse(self._client.bookkeeping_entry_sets)

    @cached_property
    def bookkeeping_entries(self) -> BookkeepingEntriesResourceWithStreamingResponse:
        from .resources.bookkeeping_entries import BookkeepingEntriesResourceWithStreamingResponse

        return BookkeepingEntriesResourceWithStreamingResponse(self._client.bookkeeping_entries)

    @cached_property
    def groups(self) -> GroupsResourceWithStreamingResponse:
        from .resources.groups import GroupsResourceWithStreamingResponse

        return GroupsResourceWithStreamingResponse(self._client.groups)

    @cached_property
    def oauth_applications(self) -> OAuthApplicationsResourceWithStreamingResponse:
        from .resources.oauth_applications import OAuthApplicationsResourceWithStreamingResponse

        return OAuthApplicationsResourceWithStreamingResponse(self._client.oauth_applications)

    @cached_property
    def oauth_connections(self) -> OAuthConnectionsResourceWithStreamingResponse:
        from .resources.oauth_connections import OAuthConnectionsResourceWithStreamingResponse

        return OAuthConnectionsResourceWithStreamingResponse(self._client.oauth_connections)

    @cached_property
    def oauth_tokens(self) -> OAuthTokensResourceWithStreamingResponse:
        from .resources.oauth_tokens import OAuthTokensResourceWithStreamingResponse

        return OAuthTokensResourceWithStreamingResponse(self._client.oauth_tokens)

    @cached_property
    def intrafi_account_enrollments(
        self,
    ) -> IntrafiAccountEnrollmentsResourceWithStreamingResponse:
        from .resources.intrafi_account_enrollments import IntrafiAccountEnrollmentsResourceWithStreamingResponse

        return IntrafiAccountEnrollmentsResourceWithStreamingResponse(self._client.intrafi_account_enrollments)

    @cached_property
    def intrafi_balances(self) -> IntrafiBalancesResourceWithStreamingResponse:
        from .resources.intrafi_balances import IntrafiBalancesResourceWithStreamingResponse

        return IntrafiBalancesResourceWithStreamingResponse(self._client.intrafi_balances)

    @cached_property
    def intrafi_exclusions(self) -> IntrafiExclusionsResourceWithStreamingResponse:
        from .resources.intrafi_exclusions import IntrafiExclusionsResourceWithStreamingResponse

        return IntrafiExclusionsResourceWithStreamingResponse(self._client.intrafi_exclusions)

    @cached_property
    def card_tokens(self) -> CardTokensResourceWithStreamingResponse:
        from .resources.card_tokens import CardTokensResourceWithStreamingResponse

        return CardTokensResourceWithStreamingResponse(self._client.card_tokens)

    @cached_property
    def card_push_transfers(self) -> CardPushTransfersResourceWithStreamingResponse:
        from .resources.card_push_transfers import CardPushTransfersResourceWithStreamingResponse

        return CardPushTransfersResourceWithStreamingResponse(self._client.card_push_transfers)

    @cached_property
    def card_validations(self) -> CardValidationsResourceWithStreamingResponse:
        from .resources.card_validations import CardValidationsResourceWithStreamingResponse

        return CardValidationsResourceWithStreamingResponse(self._client.card_validations)

    @cached_property
    def simulations(self) -> SimulationsResourceWithStreamingResponse:
        from .resources.simulations import SimulationsResourceWithStreamingResponse

        return SimulationsResourceWithStreamingResponse(self._client.simulations)


class AsyncIncreaseWithStreamedResponse:
    _client: AsyncIncrease

    def __init__(self, client: AsyncIncrease) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        from .resources.accounts import AsyncAccountsResourceWithStreamingResponse

        return AsyncAccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def account_numbers(self) -> AsyncAccountNumbersResourceWithStreamingResponse:
        from .resources.account_numbers import AsyncAccountNumbersResourceWithStreamingResponse

        return AsyncAccountNumbersResourceWithStreamingResponse(self._client.account_numbers)

    @cached_property
    def account_transfers(self) -> AsyncAccountTransfersResourceWithStreamingResponse:
        from .resources.account_transfers import AsyncAccountTransfersResourceWithStreamingResponse

        return AsyncAccountTransfersResourceWithStreamingResponse(self._client.account_transfers)

    @cached_property
    def cards(self) -> AsyncCardsResourceWithStreamingResponse:
        from .resources.cards import AsyncCardsResourceWithStreamingResponse

        return AsyncCardsResourceWithStreamingResponse(self._client.cards)

    @cached_property
    def card_payments(self) -> AsyncCardPaymentsResourceWithStreamingResponse:
        from .resources.card_payments import AsyncCardPaymentsResourceWithStreamingResponse

        return AsyncCardPaymentsResourceWithStreamingResponse(self._client.card_payments)

    @cached_property
    def card_purchase_supplements(
        self,
    ) -> AsyncCardPurchaseSupplementsResourceWithStreamingResponse:
        from .resources.card_purchase_supplements import AsyncCardPurchaseSupplementsResourceWithStreamingResponse

        return AsyncCardPurchaseSupplementsResourceWithStreamingResponse(self._client.card_purchase_supplements)

    @cached_property
    def card_disputes(self) -> AsyncCardDisputesResourceWithStreamingResponse:
        from .resources.card_disputes import AsyncCardDisputesResourceWithStreamingResponse

        return AsyncCardDisputesResourceWithStreamingResponse(self._client.card_disputes)

    @cached_property
    def physical_cards(self) -> AsyncPhysicalCardsResourceWithStreamingResponse:
        from .resources.physical_cards import AsyncPhysicalCardsResourceWithStreamingResponse

        return AsyncPhysicalCardsResourceWithStreamingResponse(self._client.physical_cards)

    @cached_property
    def digital_card_profiles(self) -> AsyncDigitalCardProfilesResourceWithStreamingResponse:
        from .resources.digital_card_profiles import AsyncDigitalCardProfilesResourceWithStreamingResponse

        return AsyncDigitalCardProfilesResourceWithStreamingResponse(self._client.digital_card_profiles)

    @cached_property
    def physical_card_profiles(self) -> AsyncPhysicalCardProfilesResourceWithStreamingResponse:
        from .resources.physical_card_profiles import AsyncPhysicalCardProfilesResourceWithStreamingResponse

        return AsyncPhysicalCardProfilesResourceWithStreamingResponse(self._client.physical_card_profiles)

    @cached_property
    def digital_wallet_tokens(self) -> AsyncDigitalWalletTokensResourceWithStreamingResponse:
        from .resources.digital_wallet_tokens import AsyncDigitalWalletTokensResourceWithStreamingResponse

        return AsyncDigitalWalletTokensResourceWithStreamingResponse(self._client.digital_wallet_tokens)

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithStreamingResponse:
        from .resources.transactions import AsyncTransactionsResourceWithStreamingResponse

        return AsyncTransactionsResourceWithStreamingResponse(self._client.transactions)

    @cached_property
    def pending_transactions(self) -> AsyncPendingTransactionsResourceWithStreamingResponse:
        from .resources.pending_transactions import AsyncPendingTransactionsResourceWithStreamingResponse

        return AsyncPendingTransactionsResourceWithStreamingResponse(self._client.pending_transactions)

    @cached_property
    def declined_transactions(self) -> AsyncDeclinedTransactionsResourceWithStreamingResponse:
        from .resources.declined_transactions import AsyncDeclinedTransactionsResourceWithStreamingResponse

        return AsyncDeclinedTransactionsResourceWithStreamingResponse(self._client.declined_transactions)

    @cached_property
    def ach_transfers(self) -> AsyncACHTransfersResourceWithStreamingResponse:
        from .resources.ach_transfers import AsyncACHTransfersResourceWithStreamingResponse

        return AsyncACHTransfersResourceWithStreamingResponse(self._client.ach_transfers)

    @cached_property
    def ach_prenotifications(self) -> AsyncACHPrenotificationsResourceWithStreamingResponse:
        from .resources.ach_prenotifications import AsyncACHPrenotificationsResourceWithStreamingResponse

        return AsyncACHPrenotificationsResourceWithStreamingResponse(self._client.ach_prenotifications)

    @cached_property
    def inbound_ach_transfers(self) -> AsyncInboundACHTransfersResourceWithStreamingResponse:
        from .resources.inbound_ach_transfers import AsyncInboundACHTransfersResourceWithStreamingResponse

        return AsyncInboundACHTransfersResourceWithStreamingResponse(self._client.inbound_ach_transfers)

    @cached_property
    def wire_transfers(self) -> AsyncWireTransfersResourceWithStreamingResponse:
        from .resources.wire_transfers import AsyncWireTransfersResourceWithStreamingResponse

        return AsyncWireTransfersResourceWithStreamingResponse(self._client.wire_transfers)

    @cached_property
    def inbound_wire_transfers(self) -> AsyncInboundWireTransfersResourceWithStreamingResponse:
        from .resources.inbound_wire_transfers import AsyncInboundWireTransfersResourceWithStreamingResponse

        return AsyncInboundWireTransfersResourceWithStreamingResponse(self._client.inbound_wire_transfers)

    @cached_property
    def wire_drawdown_requests(self) -> AsyncWireDrawdownRequestsResourceWithStreamingResponse:
        from .resources.wire_drawdown_requests import AsyncWireDrawdownRequestsResourceWithStreamingResponse

        return AsyncWireDrawdownRequestsResourceWithStreamingResponse(self._client.wire_drawdown_requests)

    @cached_property
    def inbound_wire_drawdown_requests(
        self,
    ) -> AsyncInboundWireDrawdownRequestsResourceWithStreamingResponse:
        from .resources.inbound_wire_drawdown_requests import (
            AsyncInboundWireDrawdownRequestsResourceWithStreamingResponse,
        )

        return AsyncInboundWireDrawdownRequestsResourceWithStreamingResponse(
            self._client.inbound_wire_drawdown_requests
        )

    @cached_property
    def check_transfers(self) -> AsyncCheckTransfersResourceWithStreamingResponse:
        from .resources.check_transfers import AsyncCheckTransfersResourceWithStreamingResponse

        return AsyncCheckTransfersResourceWithStreamingResponse(self._client.check_transfers)

    @cached_property
    def inbound_check_deposits(self) -> AsyncInboundCheckDepositsResourceWithStreamingResponse:
        from .resources.inbound_check_deposits import AsyncInboundCheckDepositsResourceWithStreamingResponse

        return AsyncInboundCheckDepositsResourceWithStreamingResponse(self._client.inbound_check_deposits)

    @cached_property
    def real_time_payments_transfers(
        self,
    ) -> AsyncRealTimePaymentsTransfersResourceWithStreamingResponse:
        from .resources.real_time_payments_transfers import AsyncRealTimePaymentsTransfersResourceWithStreamingResponse

        return AsyncRealTimePaymentsTransfersResourceWithStreamingResponse(self._client.real_time_payments_transfers)

    @cached_property
    def inbound_real_time_payments_transfers(
        self,
    ) -> AsyncInboundRealTimePaymentsTransfersResourceWithStreamingResponse:
        from .resources.inbound_real_time_payments_transfers import (
            AsyncInboundRealTimePaymentsTransfersResourceWithStreamingResponse,
        )

        return AsyncInboundRealTimePaymentsTransfersResourceWithStreamingResponse(
            self._client.inbound_real_time_payments_transfers
        )

    @cached_property
    def fednow_transfers(self) -> AsyncFednowTransfersResourceWithStreamingResponse:
        from .resources.fednow_transfers import AsyncFednowTransfersResourceWithStreamingResponse

        return AsyncFednowTransfersResourceWithStreamingResponse(self._client.fednow_transfers)

    @cached_property
    def inbound_fednow_transfers(
        self,
    ) -> AsyncInboundFednowTransfersResourceWithStreamingResponse:
        from .resources.inbound_fednow_transfers import AsyncInboundFednowTransfersResourceWithStreamingResponse

        return AsyncInboundFednowTransfersResourceWithStreamingResponse(self._client.inbound_fednow_transfers)

    @cached_property
    def check_deposits(self) -> AsyncCheckDepositsResourceWithStreamingResponse:
        from .resources.check_deposits import AsyncCheckDepositsResourceWithStreamingResponse

        return AsyncCheckDepositsResourceWithStreamingResponse(self._client.check_deposits)

    @cached_property
    def lockboxes(self) -> AsyncLockboxesResourceWithStreamingResponse:
        from .resources.lockboxes import AsyncLockboxesResourceWithStreamingResponse

        return AsyncLockboxesResourceWithStreamingResponse(self._client.lockboxes)

    @cached_property
    def inbound_mail_items(self) -> AsyncInboundMailItemsResourceWithStreamingResponse:
        from .resources.inbound_mail_items import AsyncInboundMailItemsResourceWithStreamingResponse

        return AsyncInboundMailItemsResourceWithStreamingResponse(self._client.inbound_mail_items)

    @cached_property
    def routing_numbers(self) -> AsyncRoutingNumbersResourceWithStreamingResponse:
        from .resources.routing_numbers import AsyncRoutingNumbersResourceWithStreamingResponse

        return AsyncRoutingNumbersResourceWithStreamingResponse(self._client.routing_numbers)

    @cached_property
    def external_accounts(self) -> AsyncExternalAccountsResourceWithStreamingResponse:
        from .resources.external_accounts import AsyncExternalAccountsResourceWithStreamingResponse

        return AsyncExternalAccountsResourceWithStreamingResponse(self._client.external_accounts)

    @cached_property
    def entities(self) -> AsyncEntitiesResourceWithStreamingResponse:
        from .resources.entities import AsyncEntitiesResourceWithStreamingResponse

        return AsyncEntitiesResourceWithStreamingResponse(self._client.entities)

    @cached_property
    def supplemental_documents(self) -> AsyncSupplementalDocumentsResourceWithStreamingResponse:
        from .resources.supplemental_documents import AsyncSupplementalDocumentsResourceWithStreamingResponse

        return AsyncSupplementalDocumentsResourceWithStreamingResponse(self._client.supplemental_documents)

    @cached_property
    def programs(self) -> AsyncProgramsResourceWithStreamingResponse:
        from .resources.programs import AsyncProgramsResourceWithStreamingResponse

        return AsyncProgramsResourceWithStreamingResponse(self._client.programs)

    @cached_property
    def account_statements(self) -> AsyncAccountStatementsResourceWithStreamingResponse:
        from .resources.account_statements import AsyncAccountStatementsResourceWithStreamingResponse

        return AsyncAccountStatementsResourceWithStreamingResponse(self._client.account_statements)

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def file_links(self) -> AsyncFileLinksResourceWithStreamingResponse:
        from .resources.file_links import AsyncFileLinksResourceWithStreamingResponse

        return AsyncFileLinksResourceWithStreamingResponse(self._client.file_links)

    @cached_property
    def exports(self) -> AsyncExportsResourceWithStreamingResponse:
        from .resources.exports import AsyncExportsResourceWithStreamingResponse

        return AsyncExportsResourceWithStreamingResponse(self._client.exports)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        from .resources.events import AsyncEventsResourceWithStreamingResponse

        return AsyncEventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def event_subscriptions(self) -> AsyncEventSubscriptionsResourceWithStreamingResponse:
        from .resources.event_subscriptions import AsyncEventSubscriptionsResourceWithStreamingResponse

        return AsyncEventSubscriptionsResourceWithStreamingResponse(self._client.event_subscriptions)

    @cached_property
    def real_time_decisions(self) -> AsyncRealTimeDecisionsResourceWithStreamingResponse:
        from .resources.real_time_decisions import AsyncRealTimeDecisionsResourceWithStreamingResponse

        return AsyncRealTimeDecisionsResourceWithStreamingResponse(self._client.real_time_decisions)

    @cached_property
    def bookkeeping_accounts(self) -> AsyncBookkeepingAccountsResourceWithStreamingResponse:
        from .resources.bookkeeping_accounts import AsyncBookkeepingAccountsResourceWithStreamingResponse

        return AsyncBookkeepingAccountsResourceWithStreamingResponse(self._client.bookkeeping_accounts)

    @cached_property
    def bookkeeping_entry_sets(self) -> AsyncBookkeepingEntrySetsResourceWithStreamingResponse:
        from .resources.bookkeeping_entry_sets import AsyncBookkeepingEntrySetsResourceWithStreamingResponse

        return AsyncBookkeepingEntrySetsResourceWithStreamingResponse(self._client.bookkeeping_entry_sets)

    @cached_property
    def bookkeeping_entries(self) -> AsyncBookkeepingEntriesResourceWithStreamingResponse:
        from .resources.bookkeeping_entries import AsyncBookkeepingEntriesResourceWithStreamingResponse

        return AsyncBookkeepingEntriesResourceWithStreamingResponse(self._client.bookkeeping_entries)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithStreamingResponse:
        from .resources.groups import AsyncGroupsResourceWithStreamingResponse

        return AsyncGroupsResourceWithStreamingResponse(self._client.groups)

    @cached_property
    def oauth_applications(self) -> AsyncOAuthApplicationsResourceWithStreamingResponse:
        from .resources.oauth_applications import AsyncOAuthApplicationsResourceWithStreamingResponse

        return AsyncOAuthApplicationsResourceWithStreamingResponse(self._client.oauth_applications)

    @cached_property
    def oauth_connections(self) -> AsyncOAuthConnectionsResourceWithStreamingResponse:
        from .resources.oauth_connections import AsyncOAuthConnectionsResourceWithStreamingResponse

        return AsyncOAuthConnectionsResourceWithStreamingResponse(self._client.oauth_connections)

    @cached_property
    def oauth_tokens(self) -> AsyncOAuthTokensResourceWithStreamingResponse:
        from .resources.oauth_tokens import AsyncOAuthTokensResourceWithStreamingResponse

        return AsyncOAuthTokensResourceWithStreamingResponse(self._client.oauth_tokens)

    @cached_property
    def intrafi_account_enrollments(
        self,
    ) -> AsyncIntrafiAccountEnrollmentsResourceWithStreamingResponse:
        from .resources.intrafi_account_enrollments import AsyncIntrafiAccountEnrollmentsResourceWithStreamingResponse

        return AsyncIntrafiAccountEnrollmentsResourceWithStreamingResponse(self._client.intrafi_account_enrollments)

    @cached_property
    def intrafi_balances(self) -> AsyncIntrafiBalancesResourceWithStreamingResponse:
        from .resources.intrafi_balances import AsyncIntrafiBalancesResourceWithStreamingResponse

        return AsyncIntrafiBalancesResourceWithStreamingResponse(self._client.intrafi_balances)

    @cached_property
    def intrafi_exclusions(self) -> AsyncIntrafiExclusionsResourceWithStreamingResponse:
        from .resources.intrafi_exclusions import AsyncIntrafiExclusionsResourceWithStreamingResponse

        return AsyncIntrafiExclusionsResourceWithStreamingResponse(self._client.intrafi_exclusions)

    @cached_property
    def card_tokens(self) -> AsyncCardTokensResourceWithStreamingResponse:
        from .resources.card_tokens import AsyncCardTokensResourceWithStreamingResponse

        return AsyncCardTokensResourceWithStreamingResponse(self._client.card_tokens)

    @cached_property
    def card_push_transfers(self) -> AsyncCardPushTransfersResourceWithStreamingResponse:
        from .resources.card_push_transfers import AsyncCardPushTransfersResourceWithStreamingResponse

        return AsyncCardPushTransfersResourceWithStreamingResponse(self._client.card_push_transfers)

    @cached_property
    def card_validations(self) -> AsyncCardValidationsResourceWithStreamingResponse:
        from .resources.card_validations import AsyncCardValidationsResourceWithStreamingResponse

        return AsyncCardValidationsResourceWithStreamingResponse(self._client.card_validations)

    @cached_property
    def simulations(self) -> AsyncSimulationsResourceWithStreamingResponse:
        from .resources.simulations import AsyncSimulationsResourceWithStreamingResponse

        return AsyncSimulationsResourceWithStreamingResponse(self._client.simulations)


Client = Increase

AsyncClient = AsyncIncrease
