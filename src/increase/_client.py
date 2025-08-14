# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    is_mapping,
    get_async_library,
)
from ._version import __version__
from .resources import (
    cards,
    files,
    events,
    groups,
    exports,
    accounts,
    entities,
    programs,
    webhooks,
    documents,
    lockboxes,
    file_links,
    card_tokens,
    oauth_tokens,
    transactions,
    ach_transfers,
    card_disputes,
    card_payments,
    check_deposits,
    physical_cards,
    wire_transfers,
    account_numbers,
    check_transfers,
    routing_numbers,
    card_validations,
    intrafi_balances,
    account_transfers,
    external_accounts,
    oauth_connections,
    account_statements,
    inbound_mail_items,
    intrafi_exclusions,
    oauth_applications,
    bookkeeping_entries,
    card_push_transfers,
    event_subscriptions,
    real_time_decisions,
    ach_prenotifications,
    bookkeeping_accounts,
    pending_transactions,
    declined_transactions,
    digital_card_profiles,
    digital_wallet_tokens,
    inbound_ach_transfers,
    bookkeeping_entry_sets,
    inbound_check_deposits,
    inbound_wire_transfers,
    physical_card_profiles,
    supplemental_documents,
    wire_drawdown_requests,
    card_purchase_supplements,
    intrafi_account_enrollments,
    real_time_payments_transfers,
    inbound_wire_drawdown_requests,
    inbound_real_time_payments_transfers,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import IncreaseError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.simulations import simulations

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
    accounts: accounts.AccountsResource
    account_numbers: account_numbers.AccountNumbersResource
    cards: cards.CardsResource
    card_payments: card_payments.CardPaymentsResource
    card_purchase_supplements: card_purchase_supplements.CardPurchaseSupplementsResource
    card_disputes: card_disputes.CardDisputesResource
    physical_cards: physical_cards.PhysicalCardsResource
    digital_card_profiles: digital_card_profiles.DigitalCardProfilesResource
    physical_card_profiles: physical_card_profiles.PhysicalCardProfilesResource
    digital_wallet_tokens: digital_wallet_tokens.DigitalWalletTokensResource
    transactions: transactions.TransactionsResource
    pending_transactions: pending_transactions.PendingTransactionsResource
    declined_transactions: declined_transactions.DeclinedTransactionsResource
    account_transfers: account_transfers.AccountTransfersResource
    ach_transfers: ach_transfers.ACHTransfersResource
    ach_prenotifications: ach_prenotifications.ACHPrenotificationsResource
    inbound_ach_transfers: inbound_ach_transfers.InboundACHTransfersResource
    wire_transfers: wire_transfers.WireTransfersResource
    inbound_wire_transfers: inbound_wire_transfers.InboundWireTransfersResource
    wire_drawdown_requests: wire_drawdown_requests.WireDrawdownRequestsResource
    inbound_wire_drawdown_requests: inbound_wire_drawdown_requests.InboundWireDrawdownRequestsResource
    check_transfers: check_transfers.CheckTransfersResource
    inbound_check_deposits: inbound_check_deposits.InboundCheckDepositsResource
    real_time_payments_transfers: real_time_payments_transfers.RealTimePaymentsTransfersResource
    inbound_real_time_payments_transfers: inbound_real_time_payments_transfers.InboundRealTimePaymentsTransfersResource
    check_deposits: check_deposits.CheckDepositsResource
    lockboxes: lockboxes.LockboxesResource
    inbound_mail_items: inbound_mail_items.InboundMailItemsResource
    routing_numbers: routing_numbers.RoutingNumbersResource
    external_accounts: external_accounts.ExternalAccountsResource
    entities: entities.EntitiesResource
    supplemental_documents: supplemental_documents.SupplementalDocumentsResource
    programs: programs.ProgramsResource
    account_statements: account_statements.AccountStatementsResource
    files: files.FilesResource
    file_links: file_links.FileLinksResource
    documents: documents.DocumentsResource
    exports: exports.ExportsResource
    events: events.EventsResource
    event_subscriptions: event_subscriptions.EventSubscriptionsResource
    real_time_decisions: real_time_decisions.RealTimeDecisionsResource
    bookkeeping_accounts: bookkeeping_accounts.BookkeepingAccountsResource
    bookkeeping_entry_sets: bookkeeping_entry_sets.BookkeepingEntrySetsResource
    bookkeeping_entries: bookkeeping_entries.BookkeepingEntriesResource
    groups: groups.GroupsResource
    oauth_applications: oauth_applications.OAuthApplicationsResource
    oauth_connections: oauth_connections.OAuthConnectionsResource
    oauth_tokens: oauth_tokens.OAuthTokensResource
    intrafi_account_enrollments: intrafi_account_enrollments.IntrafiAccountEnrollmentsResource
    intrafi_balances: intrafi_balances.IntrafiBalancesResource
    intrafi_exclusions: intrafi_exclusions.IntrafiExclusionsResource
    card_tokens: card_tokens.CardTokensResource
    card_push_transfers: card_push_transfers.CardPushTransfersResource
    card_validations: card_validations.CardValidationsResource
    simulations: simulations.SimulationsResource
    webhooks: webhooks.Webhooks
    with_raw_response: IncreaseWithRawResponse
    with_streaming_response: IncreaseWithStreamedResponse

    # client options
    api_key: str
    webhook_secret: str | None

    _environment: Literal["production", "sandbox"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        environment: Literal["production", "sandbox"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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

        self.accounts = accounts.AccountsResource(self)
        self.account_numbers = account_numbers.AccountNumbersResource(self)
        self.cards = cards.CardsResource(self)
        self.card_payments = card_payments.CardPaymentsResource(self)
        self.card_purchase_supplements = card_purchase_supplements.CardPurchaseSupplementsResource(self)
        self.card_disputes = card_disputes.CardDisputesResource(self)
        self.physical_cards = physical_cards.PhysicalCardsResource(self)
        self.digital_card_profiles = digital_card_profiles.DigitalCardProfilesResource(self)
        self.physical_card_profiles = physical_card_profiles.PhysicalCardProfilesResource(self)
        self.digital_wallet_tokens = digital_wallet_tokens.DigitalWalletTokensResource(self)
        self.transactions = transactions.TransactionsResource(self)
        self.pending_transactions = pending_transactions.PendingTransactionsResource(self)
        self.declined_transactions = declined_transactions.DeclinedTransactionsResource(self)
        self.account_transfers = account_transfers.AccountTransfersResource(self)
        self.ach_transfers = ach_transfers.ACHTransfersResource(self)
        self.ach_prenotifications = ach_prenotifications.ACHPrenotificationsResource(self)
        self.inbound_ach_transfers = inbound_ach_transfers.InboundACHTransfersResource(self)
        self.wire_transfers = wire_transfers.WireTransfersResource(self)
        self.inbound_wire_transfers = inbound_wire_transfers.InboundWireTransfersResource(self)
        self.wire_drawdown_requests = wire_drawdown_requests.WireDrawdownRequestsResource(self)
        self.inbound_wire_drawdown_requests = inbound_wire_drawdown_requests.InboundWireDrawdownRequestsResource(self)
        self.check_transfers = check_transfers.CheckTransfersResource(self)
        self.inbound_check_deposits = inbound_check_deposits.InboundCheckDepositsResource(self)
        self.real_time_payments_transfers = real_time_payments_transfers.RealTimePaymentsTransfersResource(self)
        self.inbound_real_time_payments_transfers = (
            inbound_real_time_payments_transfers.InboundRealTimePaymentsTransfersResource(self)
        )
        self.check_deposits = check_deposits.CheckDepositsResource(self)
        self.lockboxes = lockboxes.LockboxesResource(self)
        self.inbound_mail_items = inbound_mail_items.InboundMailItemsResource(self)
        self.routing_numbers = routing_numbers.RoutingNumbersResource(self)
        self.external_accounts = external_accounts.ExternalAccountsResource(self)
        self.entities = entities.EntitiesResource(self)
        self.supplemental_documents = supplemental_documents.SupplementalDocumentsResource(self)
        self.programs = programs.ProgramsResource(self)
        self.account_statements = account_statements.AccountStatementsResource(self)
        self.files = files.FilesResource(self)
        self.file_links = file_links.FileLinksResource(self)
        self.documents = documents.DocumentsResource(self)
        self.exports = exports.ExportsResource(self)
        self.events = events.EventsResource(self)
        self.event_subscriptions = event_subscriptions.EventSubscriptionsResource(self)
        self.real_time_decisions = real_time_decisions.RealTimeDecisionsResource(self)
        self.bookkeeping_accounts = bookkeeping_accounts.BookkeepingAccountsResource(self)
        self.bookkeeping_entry_sets = bookkeeping_entry_sets.BookkeepingEntrySetsResource(self)
        self.bookkeeping_entries = bookkeeping_entries.BookkeepingEntriesResource(self)
        self.groups = groups.GroupsResource(self)
        self.oauth_applications = oauth_applications.OAuthApplicationsResource(self)
        self.oauth_connections = oauth_connections.OAuthConnectionsResource(self)
        self.oauth_tokens = oauth_tokens.OAuthTokensResource(self)
        self.intrafi_account_enrollments = intrafi_account_enrollments.IntrafiAccountEnrollmentsResource(self)
        self.intrafi_balances = intrafi_balances.IntrafiBalancesResource(self)
        self.intrafi_exclusions = intrafi_exclusions.IntrafiExclusionsResource(self)
        self.card_tokens = card_tokens.CardTokensResource(self)
        self.card_push_transfers = card_push_transfers.CardPushTransfersResource(self)
        self.card_validations = card_validations.CardValidationsResource(self)
        self.simulations = simulations.SimulationsResource(self)
        self.webhooks = webhooks.Webhooks(self)
        self.with_raw_response = IncreaseWithRawResponse(self)
        self.with_streaming_response = IncreaseWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
    accounts: accounts.AsyncAccountsResource
    account_numbers: account_numbers.AsyncAccountNumbersResource
    cards: cards.AsyncCardsResource
    card_payments: card_payments.AsyncCardPaymentsResource
    card_purchase_supplements: card_purchase_supplements.AsyncCardPurchaseSupplementsResource
    card_disputes: card_disputes.AsyncCardDisputesResource
    physical_cards: physical_cards.AsyncPhysicalCardsResource
    digital_card_profiles: digital_card_profiles.AsyncDigitalCardProfilesResource
    physical_card_profiles: physical_card_profiles.AsyncPhysicalCardProfilesResource
    digital_wallet_tokens: digital_wallet_tokens.AsyncDigitalWalletTokensResource
    transactions: transactions.AsyncTransactionsResource
    pending_transactions: pending_transactions.AsyncPendingTransactionsResource
    declined_transactions: declined_transactions.AsyncDeclinedTransactionsResource
    account_transfers: account_transfers.AsyncAccountTransfersResource
    ach_transfers: ach_transfers.AsyncACHTransfersResource
    ach_prenotifications: ach_prenotifications.AsyncACHPrenotificationsResource
    inbound_ach_transfers: inbound_ach_transfers.AsyncInboundACHTransfersResource
    wire_transfers: wire_transfers.AsyncWireTransfersResource
    inbound_wire_transfers: inbound_wire_transfers.AsyncInboundWireTransfersResource
    wire_drawdown_requests: wire_drawdown_requests.AsyncWireDrawdownRequestsResource
    inbound_wire_drawdown_requests: inbound_wire_drawdown_requests.AsyncInboundWireDrawdownRequestsResource
    check_transfers: check_transfers.AsyncCheckTransfersResource
    inbound_check_deposits: inbound_check_deposits.AsyncInboundCheckDepositsResource
    real_time_payments_transfers: real_time_payments_transfers.AsyncRealTimePaymentsTransfersResource
    inbound_real_time_payments_transfers: (
        inbound_real_time_payments_transfers.AsyncInboundRealTimePaymentsTransfersResource
    )
    check_deposits: check_deposits.AsyncCheckDepositsResource
    lockboxes: lockboxes.AsyncLockboxesResource
    inbound_mail_items: inbound_mail_items.AsyncInboundMailItemsResource
    routing_numbers: routing_numbers.AsyncRoutingNumbersResource
    external_accounts: external_accounts.AsyncExternalAccountsResource
    entities: entities.AsyncEntitiesResource
    supplemental_documents: supplemental_documents.AsyncSupplementalDocumentsResource
    programs: programs.AsyncProgramsResource
    account_statements: account_statements.AsyncAccountStatementsResource
    files: files.AsyncFilesResource
    file_links: file_links.AsyncFileLinksResource
    documents: documents.AsyncDocumentsResource
    exports: exports.AsyncExportsResource
    events: events.AsyncEventsResource
    event_subscriptions: event_subscriptions.AsyncEventSubscriptionsResource
    real_time_decisions: real_time_decisions.AsyncRealTimeDecisionsResource
    bookkeeping_accounts: bookkeeping_accounts.AsyncBookkeepingAccountsResource
    bookkeeping_entry_sets: bookkeeping_entry_sets.AsyncBookkeepingEntrySetsResource
    bookkeeping_entries: bookkeeping_entries.AsyncBookkeepingEntriesResource
    groups: groups.AsyncGroupsResource
    oauth_applications: oauth_applications.AsyncOAuthApplicationsResource
    oauth_connections: oauth_connections.AsyncOAuthConnectionsResource
    oauth_tokens: oauth_tokens.AsyncOAuthTokensResource
    intrafi_account_enrollments: intrafi_account_enrollments.AsyncIntrafiAccountEnrollmentsResource
    intrafi_balances: intrafi_balances.AsyncIntrafiBalancesResource
    intrafi_exclusions: intrafi_exclusions.AsyncIntrafiExclusionsResource
    card_tokens: card_tokens.AsyncCardTokensResource
    card_push_transfers: card_push_transfers.AsyncCardPushTransfersResource
    card_validations: card_validations.AsyncCardValidationsResource
    simulations: simulations.AsyncSimulationsResource
    webhooks: webhooks.AsyncWebhooks
    with_raw_response: AsyncIncreaseWithRawResponse
    with_streaming_response: AsyncIncreaseWithStreamedResponse

    # client options
    api_key: str
    webhook_secret: str | None

    _environment: Literal["production", "sandbox"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        environment: Literal["production", "sandbox"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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

        self.accounts = accounts.AsyncAccountsResource(self)
        self.account_numbers = account_numbers.AsyncAccountNumbersResource(self)
        self.cards = cards.AsyncCardsResource(self)
        self.card_payments = card_payments.AsyncCardPaymentsResource(self)
        self.card_purchase_supplements = card_purchase_supplements.AsyncCardPurchaseSupplementsResource(self)
        self.card_disputes = card_disputes.AsyncCardDisputesResource(self)
        self.physical_cards = physical_cards.AsyncPhysicalCardsResource(self)
        self.digital_card_profiles = digital_card_profiles.AsyncDigitalCardProfilesResource(self)
        self.physical_card_profiles = physical_card_profiles.AsyncPhysicalCardProfilesResource(self)
        self.digital_wallet_tokens = digital_wallet_tokens.AsyncDigitalWalletTokensResource(self)
        self.transactions = transactions.AsyncTransactionsResource(self)
        self.pending_transactions = pending_transactions.AsyncPendingTransactionsResource(self)
        self.declined_transactions = declined_transactions.AsyncDeclinedTransactionsResource(self)
        self.account_transfers = account_transfers.AsyncAccountTransfersResource(self)
        self.ach_transfers = ach_transfers.AsyncACHTransfersResource(self)
        self.ach_prenotifications = ach_prenotifications.AsyncACHPrenotificationsResource(self)
        self.inbound_ach_transfers = inbound_ach_transfers.AsyncInboundACHTransfersResource(self)
        self.wire_transfers = wire_transfers.AsyncWireTransfersResource(self)
        self.inbound_wire_transfers = inbound_wire_transfers.AsyncInboundWireTransfersResource(self)
        self.wire_drawdown_requests = wire_drawdown_requests.AsyncWireDrawdownRequestsResource(self)
        self.inbound_wire_drawdown_requests = inbound_wire_drawdown_requests.AsyncInboundWireDrawdownRequestsResource(
            self
        )
        self.check_transfers = check_transfers.AsyncCheckTransfersResource(self)
        self.inbound_check_deposits = inbound_check_deposits.AsyncInboundCheckDepositsResource(self)
        self.real_time_payments_transfers = real_time_payments_transfers.AsyncRealTimePaymentsTransfersResource(self)
        self.inbound_real_time_payments_transfers = (
            inbound_real_time_payments_transfers.AsyncInboundRealTimePaymentsTransfersResource(self)
        )
        self.check_deposits = check_deposits.AsyncCheckDepositsResource(self)
        self.lockboxes = lockboxes.AsyncLockboxesResource(self)
        self.inbound_mail_items = inbound_mail_items.AsyncInboundMailItemsResource(self)
        self.routing_numbers = routing_numbers.AsyncRoutingNumbersResource(self)
        self.external_accounts = external_accounts.AsyncExternalAccountsResource(self)
        self.entities = entities.AsyncEntitiesResource(self)
        self.supplemental_documents = supplemental_documents.AsyncSupplementalDocumentsResource(self)
        self.programs = programs.AsyncProgramsResource(self)
        self.account_statements = account_statements.AsyncAccountStatementsResource(self)
        self.files = files.AsyncFilesResource(self)
        self.file_links = file_links.AsyncFileLinksResource(self)
        self.documents = documents.AsyncDocumentsResource(self)
        self.exports = exports.AsyncExportsResource(self)
        self.events = events.AsyncEventsResource(self)
        self.event_subscriptions = event_subscriptions.AsyncEventSubscriptionsResource(self)
        self.real_time_decisions = real_time_decisions.AsyncRealTimeDecisionsResource(self)
        self.bookkeeping_accounts = bookkeeping_accounts.AsyncBookkeepingAccountsResource(self)
        self.bookkeeping_entry_sets = bookkeeping_entry_sets.AsyncBookkeepingEntrySetsResource(self)
        self.bookkeeping_entries = bookkeeping_entries.AsyncBookkeepingEntriesResource(self)
        self.groups = groups.AsyncGroupsResource(self)
        self.oauth_applications = oauth_applications.AsyncOAuthApplicationsResource(self)
        self.oauth_connections = oauth_connections.AsyncOAuthConnectionsResource(self)
        self.oauth_tokens = oauth_tokens.AsyncOAuthTokensResource(self)
        self.intrafi_account_enrollments = intrafi_account_enrollments.AsyncIntrafiAccountEnrollmentsResource(self)
        self.intrafi_balances = intrafi_balances.AsyncIntrafiBalancesResource(self)
        self.intrafi_exclusions = intrafi_exclusions.AsyncIntrafiExclusionsResource(self)
        self.card_tokens = card_tokens.AsyncCardTokensResource(self)
        self.card_push_transfers = card_push_transfers.AsyncCardPushTransfersResource(self)
        self.card_validations = card_validations.AsyncCardValidationsResource(self)
        self.simulations = simulations.AsyncSimulationsResource(self)
        self.webhooks = webhooks.AsyncWebhooks(self)
        self.with_raw_response = AsyncIncreaseWithRawResponse(self)
        self.with_streaming_response = AsyncIncreaseWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
    def __init__(self, client: Increase) -> None:
        self.accounts = accounts.AccountsResourceWithRawResponse(client.accounts)
        self.account_numbers = account_numbers.AccountNumbersResourceWithRawResponse(client.account_numbers)
        self.cards = cards.CardsResourceWithRawResponse(client.cards)
        self.card_payments = card_payments.CardPaymentsResourceWithRawResponse(client.card_payments)
        self.card_purchase_supplements = card_purchase_supplements.CardPurchaseSupplementsResourceWithRawResponse(
            client.card_purchase_supplements
        )
        self.card_disputes = card_disputes.CardDisputesResourceWithRawResponse(client.card_disputes)
        self.physical_cards = physical_cards.PhysicalCardsResourceWithRawResponse(client.physical_cards)
        self.digital_card_profiles = digital_card_profiles.DigitalCardProfilesResourceWithRawResponse(
            client.digital_card_profiles
        )
        self.physical_card_profiles = physical_card_profiles.PhysicalCardProfilesResourceWithRawResponse(
            client.physical_card_profiles
        )
        self.digital_wallet_tokens = digital_wallet_tokens.DigitalWalletTokensResourceWithRawResponse(
            client.digital_wallet_tokens
        )
        self.transactions = transactions.TransactionsResourceWithRawResponse(client.transactions)
        self.pending_transactions = pending_transactions.PendingTransactionsResourceWithRawResponse(
            client.pending_transactions
        )
        self.declined_transactions = declined_transactions.DeclinedTransactionsResourceWithRawResponse(
            client.declined_transactions
        )
        self.account_transfers = account_transfers.AccountTransfersResourceWithRawResponse(client.account_transfers)
        self.ach_transfers = ach_transfers.ACHTransfersResourceWithRawResponse(client.ach_transfers)
        self.ach_prenotifications = ach_prenotifications.ACHPrenotificationsResourceWithRawResponse(
            client.ach_prenotifications
        )
        self.inbound_ach_transfers = inbound_ach_transfers.InboundACHTransfersResourceWithRawResponse(
            client.inbound_ach_transfers
        )
        self.wire_transfers = wire_transfers.WireTransfersResourceWithRawResponse(client.wire_transfers)
        self.inbound_wire_transfers = inbound_wire_transfers.InboundWireTransfersResourceWithRawResponse(
            client.inbound_wire_transfers
        )
        self.wire_drawdown_requests = wire_drawdown_requests.WireDrawdownRequestsResourceWithRawResponse(
            client.wire_drawdown_requests
        )
        self.inbound_wire_drawdown_requests = (
            inbound_wire_drawdown_requests.InboundWireDrawdownRequestsResourceWithRawResponse(
                client.inbound_wire_drawdown_requests
            )
        )
        self.check_transfers = check_transfers.CheckTransfersResourceWithRawResponse(client.check_transfers)
        self.inbound_check_deposits = inbound_check_deposits.InboundCheckDepositsResourceWithRawResponse(
            client.inbound_check_deposits
        )
        self.real_time_payments_transfers = (
            real_time_payments_transfers.RealTimePaymentsTransfersResourceWithRawResponse(
                client.real_time_payments_transfers
            )
        )
        self.inbound_real_time_payments_transfers = (
            inbound_real_time_payments_transfers.InboundRealTimePaymentsTransfersResourceWithRawResponse(
                client.inbound_real_time_payments_transfers
            )
        )
        self.check_deposits = check_deposits.CheckDepositsResourceWithRawResponse(client.check_deposits)
        self.lockboxes = lockboxes.LockboxesResourceWithRawResponse(client.lockboxes)
        self.inbound_mail_items = inbound_mail_items.InboundMailItemsResourceWithRawResponse(client.inbound_mail_items)
        self.routing_numbers = routing_numbers.RoutingNumbersResourceWithRawResponse(client.routing_numbers)
        self.external_accounts = external_accounts.ExternalAccountsResourceWithRawResponse(client.external_accounts)
        self.entities = entities.EntitiesResourceWithRawResponse(client.entities)
        self.supplemental_documents = supplemental_documents.SupplementalDocumentsResourceWithRawResponse(
            client.supplemental_documents
        )
        self.programs = programs.ProgramsResourceWithRawResponse(client.programs)
        self.account_statements = account_statements.AccountStatementsResourceWithRawResponse(client.account_statements)
        self.files = files.FilesResourceWithRawResponse(client.files)
        self.file_links = file_links.FileLinksResourceWithRawResponse(client.file_links)
        self.documents = documents.DocumentsResourceWithRawResponse(client.documents)
        self.exports = exports.ExportsResourceWithRawResponse(client.exports)
        self.events = events.EventsResourceWithRawResponse(client.events)
        self.event_subscriptions = event_subscriptions.EventSubscriptionsResourceWithRawResponse(
            client.event_subscriptions
        )
        self.real_time_decisions = real_time_decisions.RealTimeDecisionsResourceWithRawResponse(
            client.real_time_decisions
        )
        self.bookkeeping_accounts = bookkeeping_accounts.BookkeepingAccountsResourceWithRawResponse(
            client.bookkeeping_accounts
        )
        self.bookkeeping_entry_sets = bookkeeping_entry_sets.BookkeepingEntrySetsResourceWithRawResponse(
            client.bookkeeping_entry_sets
        )
        self.bookkeeping_entries = bookkeeping_entries.BookkeepingEntriesResourceWithRawResponse(
            client.bookkeeping_entries
        )
        self.groups = groups.GroupsResourceWithRawResponse(client.groups)
        self.oauth_applications = oauth_applications.OAuthApplicationsResourceWithRawResponse(client.oauth_applications)
        self.oauth_connections = oauth_connections.OAuthConnectionsResourceWithRawResponse(client.oauth_connections)
        self.oauth_tokens = oauth_tokens.OAuthTokensResourceWithRawResponse(client.oauth_tokens)
        self.intrafi_account_enrollments = intrafi_account_enrollments.IntrafiAccountEnrollmentsResourceWithRawResponse(
            client.intrafi_account_enrollments
        )
        self.intrafi_balances = intrafi_balances.IntrafiBalancesResourceWithRawResponse(client.intrafi_balances)
        self.intrafi_exclusions = intrafi_exclusions.IntrafiExclusionsResourceWithRawResponse(client.intrafi_exclusions)
        self.card_tokens = card_tokens.CardTokensResourceWithRawResponse(client.card_tokens)
        self.card_push_transfers = card_push_transfers.CardPushTransfersResourceWithRawResponse(
            client.card_push_transfers
        )
        self.card_validations = card_validations.CardValidationsResourceWithRawResponse(client.card_validations)
        self.simulations = simulations.SimulationsResourceWithRawResponse(client.simulations)


class AsyncIncreaseWithRawResponse:
    def __init__(self, client: AsyncIncrease) -> None:
        self.accounts = accounts.AsyncAccountsResourceWithRawResponse(client.accounts)
        self.account_numbers = account_numbers.AsyncAccountNumbersResourceWithRawResponse(client.account_numbers)
        self.cards = cards.AsyncCardsResourceWithRawResponse(client.cards)
        self.card_payments = card_payments.AsyncCardPaymentsResourceWithRawResponse(client.card_payments)
        self.card_purchase_supplements = card_purchase_supplements.AsyncCardPurchaseSupplementsResourceWithRawResponse(
            client.card_purchase_supplements
        )
        self.card_disputes = card_disputes.AsyncCardDisputesResourceWithRawResponse(client.card_disputes)
        self.physical_cards = physical_cards.AsyncPhysicalCardsResourceWithRawResponse(client.physical_cards)
        self.digital_card_profiles = digital_card_profiles.AsyncDigitalCardProfilesResourceWithRawResponse(
            client.digital_card_profiles
        )
        self.physical_card_profiles = physical_card_profiles.AsyncPhysicalCardProfilesResourceWithRawResponse(
            client.physical_card_profiles
        )
        self.digital_wallet_tokens = digital_wallet_tokens.AsyncDigitalWalletTokensResourceWithRawResponse(
            client.digital_wallet_tokens
        )
        self.transactions = transactions.AsyncTransactionsResourceWithRawResponse(client.transactions)
        self.pending_transactions = pending_transactions.AsyncPendingTransactionsResourceWithRawResponse(
            client.pending_transactions
        )
        self.declined_transactions = declined_transactions.AsyncDeclinedTransactionsResourceWithRawResponse(
            client.declined_transactions
        )
        self.account_transfers = account_transfers.AsyncAccountTransfersResourceWithRawResponse(
            client.account_transfers
        )
        self.ach_transfers = ach_transfers.AsyncACHTransfersResourceWithRawResponse(client.ach_transfers)
        self.ach_prenotifications = ach_prenotifications.AsyncACHPrenotificationsResourceWithRawResponse(
            client.ach_prenotifications
        )
        self.inbound_ach_transfers = inbound_ach_transfers.AsyncInboundACHTransfersResourceWithRawResponse(
            client.inbound_ach_transfers
        )
        self.wire_transfers = wire_transfers.AsyncWireTransfersResourceWithRawResponse(client.wire_transfers)
        self.inbound_wire_transfers = inbound_wire_transfers.AsyncInboundWireTransfersResourceWithRawResponse(
            client.inbound_wire_transfers
        )
        self.wire_drawdown_requests = wire_drawdown_requests.AsyncWireDrawdownRequestsResourceWithRawResponse(
            client.wire_drawdown_requests
        )
        self.inbound_wire_drawdown_requests = (
            inbound_wire_drawdown_requests.AsyncInboundWireDrawdownRequestsResourceWithRawResponse(
                client.inbound_wire_drawdown_requests
            )
        )
        self.check_transfers = check_transfers.AsyncCheckTransfersResourceWithRawResponse(client.check_transfers)
        self.inbound_check_deposits = inbound_check_deposits.AsyncInboundCheckDepositsResourceWithRawResponse(
            client.inbound_check_deposits
        )
        self.real_time_payments_transfers = (
            real_time_payments_transfers.AsyncRealTimePaymentsTransfersResourceWithRawResponse(
                client.real_time_payments_transfers
            )
        )
        self.inbound_real_time_payments_transfers = (
            inbound_real_time_payments_transfers.AsyncInboundRealTimePaymentsTransfersResourceWithRawResponse(
                client.inbound_real_time_payments_transfers
            )
        )
        self.check_deposits = check_deposits.AsyncCheckDepositsResourceWithRawResponse(client.check_deposits)
        self.lockboxes = lockboxes.AsyncLockboxesResourceWithRawResponse(client.lockboxes)
        self.inbound_mail_items = inbound_mail_items.AsyncInboundMailItemsResourceWithRawResponse(
            client.inbound_mail_items
        )
        self.routing_numbers = routing_numbers.AsyncRoutingNumbersResourceWithRawResponse(client.routing_numbers)
        self.external_accounts = external_accounts.AsyncExternalAccountsResourceWithRawResponse(
            client.external_accounts
        )
        self.entities = entities.AsyncEntitiesResourceWithRawResponse(client.entities)
        self.supplemental_documents = supplemental_documents.AsyncSupplementalDocumentsResourceWithRawResponse(
            client.supplemental_documents
        )
        self.programs = programs.AsyncProgramsResourceWithRawResponse(client.programs)
        self.account_statements = account_statements.AsyncAccountStatementsResourceWithRawResponse(
            client.account_statements
        )
        self.files = files.AsyncFilesResourceWithRawResponse(client.files)
        self.file_links = file_links.AsyncFileLinksResourceWithRawResponse(client.file_links)
        self.documents = documents.AsyncDocumentsResourceWithRawResponse(client.documents)
        self.exports = exports.AsyncExportsResourceWithRawResponse(client.exports)
        self.events = events.AsyncEventsResourceWithRawResponse(client.events)
        self.event_subscriptions = event_subscriptions.AsyncEventSubscriptionsResourceWithRawResponse(
            client.event_subscriptions
        )
        self.real_time_decisions = real_time_decisions.AsyncRealTimeDecisionsResourceWithRawResponse(
            client.real_time_decisions
        )
        self.bookkeeping_accounts = bookkeeping_accounts.AsyncBookkeepingAccountsResourceWithRawResponse(
            client.bookkeeping_accounts
        )
        self.bookkeeping_entry_sets = bookkeeping_entry_sets.AsyncBookkeepingEntrySetsResourceWithRawResponse(
            client.bookkeeping_entry_sets
        )
        self.bookkeeping_entries = bookkeeping_entries.AsyncBookkeepingEntriesResourceWithRawResponse(
            client.bookkeeping_entries
        )
        self.groups = groups.AsyncGroupsResourceWithRawResponse(client.groups)
        self.oauth_applications = oauth_applications.AsyncOAuthApplicationsResourceWithRawResponse(
            client.oauth_applications
        )
        self.oauth_connections = oauth_connections.AsyncOAuthConnectionsResourceWithRawResponse(
            client.oauth_connections
        )
        self.oauth_tokens = oauth_tokens.AsyncOAuthTokensResourceWithRawResponse(client.oauth_tokens)
        self.intrafi_account_enrollments = (
            intrafi_account_enrollments.AsyncIntrafiAccountEnrollmentsResourceWithRawResponse(
                client.intrafi_account_enrollments
            )
        )
        self.intrafi_balances = intrafi_balances.AsyncIntrafiBalancesResourceWithRawResponse(client.intrafi_balances)
        self.intrafi_exclusions = intrafi_exclusions.AsyncIntrafiExclusionsResourceWithRawResponse(
            client.intrafi_exclusions
        )
        self.card_tokens = card_tokens.AsyncCardTokensResourceWithRawResponse(client.card_tokens)
        self.card_push_transfers = card_push_transfers.AsyncCardPushTransfersResourceWithRawResponse(
            client.card_push_transfers
        )
        self.card_validations = card_validations.AsyncCardValidationsResourceWithRawResponse(client.card_validations)
        self.simulations = simulations.AsyncSimulationsResourceWithRawResponse(client.simulations)


class IncreaseWithStreamedResponse:
    def __init__(self, client: Increase) -> None:
        self.accounts = accounts.AccountsResourceWithStreamingResponse(client.accounts)
        self.account_numbers = account_numbers.AccountNumbersResourceWithStreamingResponse(client.account_numbers)
        self.cards = cards.CardsResourceWithStreamingResponse(client.cards)
        self.card_payments = card_payments.CardPaymentsResourceWithStreamingResponse(client.card_payments)
        self.card_purchase_supplements = card_purchase_supplements.CardPurchaseSupplementsResourceWithStreamingResponse(
            client.card_purchase_supplements
        )
        self.card_disputes = card_disputes.CardDisputesResourceWithStreamingResponse(client.card_disputes)
        self.physical_cards = physical_cards.PhysicalCardsResourceWithStreamingResponse(client.physical_cards)
        self.digital_card_profiles = digital_card_profiles.DigitalCardProfilesResourceWithStreamingResponse(
            client.digital_card_profiles
        )
        self.physical_card_profiles = physical_card_profiles.PhysicalCardProfilesResourceWithStreamingResponse(
            client.physical_card_profiles
        )
        self.digital_wallet_tokens = digital_wallet_tokens.DigitalWalletTokensResourceWithStreamingResponse(
            client.digital_wallet_tokens
        )
        self.transactions = transactions.TransactionsResourceWithStreamingResponse(client.transactions)
        self.pending_transactions = pending_transactions.PendingTransactionsResourceWithStreamingResponse(
            client.pending_transactions
        )
        self.declined_transactions = declined_transactions.DeclinedTransactionsResourceWithStreamingResponse(
            client.declined_transactions
        )
        self.account_transfers = account_transfers.AccountTransfersResourceWithStreamingResponse(
            client.account_transfers
        )
        self.ach_transfers = ach_transfers.ACHTransfersResourceWithStreamingResponse(client.ach_transfers)
        self.ach_prenotifications = ach_prenotifications.ACHPrenotificationsResourceWithStreamingResponse(
            client.ach_prenotifications
        )
        self.inbound_ach_transfers = inbound_ach_transfers.InboundACHTransfersResourceWithStreamingResponse(
            client.inbound_ach_transfers
        )
        self.wire_transfers = wire_transfers.WireTransfersResourceWithStreamingResponse(client.wire_transfers)
        self.inbound_wire_transfers = inbound_wire_transfers.InboundWireTransfersResourceWithStreamingResponse(
            client.inbound_wire_transfers
        )
        self.wire_drawdown_requests = wire_drawdown_requests.WireDrawdownRequestsResourceWithStreamingResponse(
            client.wire_drawdown_requests
        )
        self.inbound_wire_drawdown_requests = (
            inbound_wire_drawdown_requests.InboundWireDrawdownRequestsResourceWithStreamingResponse(
                client.inbound_wire_drawdown_requests
            )
        )
        self.check_transfers = check_transfers.CheckTransfersResourceWithStreamingResponse(client.check_transfers)
        self.inbound_check_deposits = inbound_check_deposits.InboundCheckDepositsResourceWithStreamingResponse(
            client.inbound_check_deposits
        )
        self.real_time_payments_transfers = (
            real_time_payments_transfers.RealTimePaymentsTransfersResourceWithStreamingResponse(
                client.real_time_payments_transfers
            )
        )
        self.inbound_real_time_payments_transfers = (
            inbound_real_time_payments_transfers.InboundRealTimePaymentsTransfersResourceWithStreamingResponse(
                client.inbound_real_time_payments_transfers
            )
        )
        self.check_deposits = check_deposits.CheckDepositsResourceWithStreamingResponse(client.check_deposits)
        self.lockboxes = lockboxes.LockboxesResourceWithStreamingResponse(client.lockboxes)
        self.inbound_mail_items = inbound_mail_items.InboundMailItemsResourceWithStreamingResponse(
            client.inbound_mail_items
        )
        self.routing_numbers = routing_numbers.RoutingNumbersResourceWithStreamingResponse(client.routing_numbers)
        self.external_accounts = external_accounts.ExternalAccountsResourceWithStreamingResponse(
            client.external_accounts
        )
        self.entities = entities.EntitiesResourceWithStreamingResponse(client.entities)
        self.supplemental_documents = supplemental_documents.SupplementalDocumentsResourceWithStreamingResponse(
            client.supplemental_documents
        )
        self.programs = programs.ProgramsResourceWithStreamingResponse(client.programs)
        self.account_statements = account_statements.AccountStatementsResourceWithStreamingResponse(
            client.account_statements
        )
        self.files = files.FilesResourceWithStreamingResponse(client.files)
        self.file_links = file_links.FileLinksResourceWithStreamingResponse(client.file_links)
        self.documents = documents.DocumentsResourceWithStreamingResponse(client.documents)
        self.exports = exports.ExportsResourceWithStreamingResponse(client.exports)
        self.events = events.EventsResourceWithStreamingResponse(client.events)
        self.event_subscriptions = event_subscriptions.EventSubscriptionsResourceWithStreamingResponse(
            client.event_subscriptions
        )
        self.real_time_decisions = real_time_decisions.RealTimeDecisionsResourceWithStreamingResponse(
            client.real_time_decisions
        )
        self.bookkeeping_accounts = bookkeeping_accounts.BookkeepingAccountsResourceWithStreamingResponse(
            client.bookkeeping_accounts
        )
        self.bookkeeping_entry_sets = bookkeeping_entry_sets.BookkeepingEntrySetsResourceWithStreamingResponse(
            client.bookkeeping_entry_sets
        )
        self.bookkeeping_entries = bookkeeping_entries.BookkeepingEntriesResourceWithStreamingResponse(
            client.bookkeeping_entries
        )
        self.groups = groups.GroupsResourceWithStreamingResponse(client.groups)
        self.oauth_applications = oauth_applications.OAuthApplicationsResourceWithStreamingResponse(
            client.oauth_applications
        )
        self.oauth_connections = oauth_connections.OAuthConnectionsResourceWithStreamingResponse(
            client.oauth_connections
        )
        self.oauth_tokens = oauth_tokens.OAuthTokensResourceWithStreamingResponse(client.oauth_tokens)
        self.intrafi_account_enrollments = (
            intrafi_account_enrollments.IntrafiAccountEnrollmentsResourceWithStreamingResponse(
                client.intrafi_account_enrollments
            )
        )
        self.intrafi_balances = intrafi_balances.IntrafiBalancesResourceWithStreamingResponse(client.intrafi_balances)
        self.intrafi_exclusions = intrafi_exclusions.IntrafiExclusionsResourceWithStreamingResponse(
            client.intrafi_exclusions
        )
        self.card_tokens = card_tokens.CardTokensResourceWithStreamingResponse(client.card_tokens)
        self.card_push_transfers = card_push_transfers.CardPushTransfersResourceWithStreamingResponse(
            client.card_push_transfers
        )
        self.card_validations = card_validations.CardValidationsResourceWithStreamingResponse(client.card_validations)
        self.simulations = simulations.SimulationsResourceWithStreamingResponse(client.simulations)


class AsyncIncreaseWithStreamedResponse:
    def __init__(self, client: AsyncIncrease) -> None:
        self.accounts = accounts.AsyncAccountsResourceWithStreamingResponse(client.accounts)
        self.account_numbers = account_numbers.AsyncAccountNumbersResourceWithStreamingResponse(client.account_numbers)
        self.cards = cards.AsyncCardsResourceWithStreamingResponse(client.cards)
        self.card_payments = card_payments.AsyncCardPaymentsResourceWithStreamingResponse(client.card_payments)
        self.card_purchase_supplements = (
            card_purchase_supplements.AsyncCardPurchaseSupplementsResourceWithStreamingResponse(
                client.card_purchase_supplements
            )
        )
        self.card_disputes = card_disputes.AsyncCardDisputesResourceWithStreamingResponse(client.card_disputes)
        self.physical_cards = physical_cards.AsyncPhysicalCardsResourceWithStreamingResponse(client.physical_cards)
        self.digital_card_profiles = digital_card_profiles.AsyncDigitalCardProfilesResourceWithStreamingResponse(
            client.digital_card_profiles
        )
        self.physical_card_profiles = physical_card_profiles.AsyncPhysicalCardProfilesResourceWithStreamingResponse(
            client.physical_card_profiles
        )
        self.digital_wallet_tokens = digital_wallet_tokens.AsyncDigitalWalletTokensResourceWithStreamingResponse(
            client.digital_wallet_tokens
        )
        self.transactions = transactions.AsyncTransactionsResourceWithStreamingResponse(client.transactions)
        self.pending_transactions = pending_transactions.AsyncPendingTransactionsResourceWithStreamingResponse(
            client.pending_transactions
        )
        self.declined_transactions = declined_transactions.AsyncDeclinedTransactionsResourceWithStreamingResponse(
            client.declined_transactions
        )
        self.account_transfers = account_transfers.AsyncAccountTransfersResourceWithStreamingResponse(
            client.account_transfers
        )
        self.ach_transfers = ach_transfers.AsyncACHTransfersResourceWithStreamingResponse(client.ach_transfers)
        self.ach_prenotifications = ach_prenotifications.AsyncACHPrenotificationsResourceWithStreamingResponse(
            client.ach_prenotifications
        )
        self.inbound_ach_transfers = inbound_ach_transfers.AsyncInboundACHTransfersResourceWithStreamingResponse(
            client.inbound_ach_transfers
        )
        self.wire_transfers = wire_transfers.AsyncWireTransfersResourceWithStreamingResponse(client.wire_transfers)
        self.inbound_wire_transfers = inbound_wire_transfers.AsyncInboundWireTransfersResourceWithStreamingResponse(
            client.inbound_wire_transfers
        )
        self.wire_drawdown_requests = wire_drawdown_requests.AsyncWireDrawdownRequestsResourceWithStreamingResponse(
            client.wire_drawdown_requests
        )
        self.inbound_wire_drawdown_requests = (
            inbound_wire_drawdown_requests.AsyncInboundWireDrawdownRequestsResourceWithStreamingResponse(
                client.inbound_wire_drawdown_requests
            )
        )
        self.check_transfers = check_transfers.AsyncCheckTransfersResourceWithStreamingResponse(client.check_transfers)
        self.inbound_check_deposits = inbound_check_deposits.AsyncInboundCheckDepositsResourceWithStreamingResponse(
            client.inbound_check_deposits
        )
        self.real_time_payments_transfers = (
            real_time_payments_transfers.AsyncRealTimePaymentsTransfersResourceWithStreamingResponse(
                client.real_time_payments_transfers
            )
        )
        self.inbound_real_time_payments_transfers = (
            inbound_real_time_payments_transfers.AsyncInboundRealTimePaymentsTransfersResourceWithStreamingResponse(
                client.inbound_real_time_payments_transfers
            )
        )
        self.check_deposits = check_deposits.AsyncCheckDepositsResourceWithStreamingResponse(client.check_deposits)
        self.lockboxes = lockboxes.AsyncLockboxesResourceWithStreamingResponse(client.lockboxes)
        self.inbound_mail_items = inbound_mail_items.AsyncInboundMailItemsResourceWithStreamingResponse(
            client.inbound_mail_items
        )
        self.routing_numbers = routing_numbers.AsyncRoutingNumbersResourceWithStreamingResponse(client.routing_numbers)
        self.external_accounts = external_accounts.AsyncExternalAccountsResourceWithStreamingResponse(
            client.external_accounts
        )
        self.entities = entities.AsyncEntitiesResourceWithStreamingResponse(client.entities)
        self.supplemental_documents = supplemental_documents.AsyncSupplementalDocumentsResourceWithStreamingResponse(
            client.supplemental_documents
        )
        self.programs = programs.AsyncProgramsResourceWithStreamingResponse(client.programs)
        self.account_statements = account_statements.AsyncAccountStatementsResourceWithStreamingResponse(
            client.account_statements
        )
        self.files = files.AsyncFilesResourceWithStreamingResponse(client.files)
        self.file_links = file_links.AsyncFileLinksResourceWithStreamingResponse(client.file_links)
        self.documents = documents.AsyncDocumentsResourceWithStreamingResponse(client.documents)
        self.exports = exports.AsyncExportsResourceWithStreamingResponse(client.exports)
        self.events = events.AsyncEventsResourceWithStreamingResponse(client.events)
        self.event_subscriptions = event_subscriptions.AsyncEventSubscriptionsResourceWithStreamingResponse(
            client.event_subscriptions
        )
        self.real_time_decisions = real_time_decisions.AsyncRealTimeDecisionsResourceWithStreamingResponse(
            client.real_time_decisions
        )
        self.bookkeeping_accounts = bookkeeping_accounts.AsyncBookkeepingAccountsResourceWithStreamingResponse(
            client.bookkeeping_accounts
        )
        self.bookkeeping_entry_sets = bookkeeping_entry_sets.AsyncBookkeepingEntrySetsResourceWithStreamingResponse(
            client.bookkeeping_entry_sets
        )
        self.bookkeeping_entries = bookkeeping_entries.AsyncBookkeepingEntriesResourceWithStreamingResponse(
            client.bookkeeping_entries
        )
        self.groups = groups.AsyncGroupsResourceWithStreamingResponse(client.groups)
        self.oauth_applications = oauth_applications.AsyncOAuthApplicationsResourceWithStreamingResponse(
            client.oauth_applications
        )
        self.oauth_connections = oauth_connections.AsyncOAuthConnectionsResourceWithStreamingResponse(
            client.oauth_connections
        )
        self.oauth_tokens = oauth_tokens.AsyncOAuthTokensResourceWithStreamingResponse(client.oauth_tokens)
        self.intrafi_account_enrollments = (
            intrafi_account_enrollments.AsyncIntrafiAccountEnrollmentsResourceWithStreamingResponse(
                client.intrafi_account_enrollments
            )
        )
        self.intrafi_balances = intrafi_balances.AsyncIntrafiBalancesResourceWithStreamingResponse(
            client.intrafi_balances
        )
        self.intrafi_exclusions = intrafi_exclusions.AsyncIntrafiExclusionsResourceWithStreamingResponse(
            client.intrafi_exclusions
        )
        self.card_tokens = card_tokens.AsyncCardTokensResourceWithStreamingResponse(client.card_tokens)
        self.card_push_transfers = card_push_transfers.AsyncCardPushTransfersResourceWithStreamingResponse(
            client.card_push_transfers
        )
        self.card_validations = card_validations.AsyncCardValidationsResourceWithStreamingResponse(
            client.card_validations
        )
        self.simulations = simulations.AsyncSimulationsResourceWithStreamingResponse(client.simulations)


Client = Increase

AsyncClient = AsyncIncrease
