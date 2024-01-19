# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    AsyncTransport,
    RequestOptions,
)
from ._utils import (
    is_given,
    is_mapping,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import IncreaseError, APIStatusError
from ._base_client import (
    DEFAULT_LIMITS,
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    SyncHttpxClientWrapper,
    AsyncHttpxClientWrapper,
)

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
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
    accounts: resources.Accounts
    account_numbers: resources.AccountNumbers
    bookkeeping_accounts: resources.BookkeepingAccounts
    bookkeeping_entry_sets: resources.BookkeepingEntrySets
    bookkeeping_entries: resources.BookkeepingEntries
    real_time_decisions: resources.RealTimeDecisions
    real_time_payments_transfers: resources.RealTimePaymentsTransfers
    cards: resources.Cards
    card_disputes: resources.CardDisputes
    card_profiles: resources.CardProfiles
    card_purchase_supplements: resources.CardPurchaseSupplements
    external_accounts: resources.ExternalAccounts
    exports: resources.Exports
    digital_wallet_tokens: resources.DigitalWalletTokens
    transactions: resources.Transactions
    pending_transactions: resources.PendingTransactions
    programs: resources.Programs
    declined_transactions: resources.DeclinedTransactions
    account_transfers: resources.AccountTransfers
    ach_transfers: resources.ACHTransfers
    ach_prenotifications: resources.ACHPrenotifications
    documents: resources.Documents
    wire_transfers: resources.WireTransfers
    check_transfers: resources.CheckTransfers
    entities: resources.Entities
    inbound_ach_transfers: resources.InboundACHTransfers
    inbound_wire_drawdown_requests: resources.InboundWireDrawdownRequests
    wire_drawdown_requests: resources.WireDrawdownRequests
    events: resources.Events
    event_subscriptions: resources.EventSubscriptions
    files: resources.Files
    groups: resources.Groups
    oauth_connections: resources.OAuthConnections
    check_deposits: resources.CheckDeposits
    routing_numbers: resources.RoutingNumbers
    account_statements: resources.AccountStatements
    simulations: resources.Simulations
    physical_cards: resources.PhysicalCards
    card_payments: resources.CardPayments
    proof_of_authorization_requests: resources.ProofOfAuthorizationRequests
    proof_of_authorization_request_submissions: resources.ProofOfAuthorizationRequestSubmissions
    intrafi: resources.Intrafi
    real_time_payments_request_for_payments: resources.RealTimePaymentsRequestForPayments
    webhooks: resources.Webhooks
    oauth_tokens: resources.OAuthTokens
    inbound_wire_transfers: resources.InboundWireTransfers
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
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Transport | None = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: ProxiesTypes | None = None,
        # See httpx documentation for [limits](https://www.python-httpx.org/advanced/#pool-limit-configuration)
        connection_pool_limits: httpx.Limits | None = None,
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
        """Construct a new synchronous increase client instance.

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
            transport=transport,
            proxies=proxies,
            limits=connection_pool_limits,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

        self.accounts = resources.Accounts(self)
        self.account_numbers = resources.AccountNumbers(self)
        self.bookkeeping_accounts = resources.BookkeepingAccounts(self)
        self.bookkeeping_entry_sets = resources.BookkeepingEntrySets(self)
        self.bookkeeping_entries = resources.BookkeepingEntries(self)
        self.real_time_decisions = resources.RealTimeDecisions(self)
        self.real_time_payments_transfers = resources.RealTimePaymentsTransfers(self)
        self.cards = resources.Cards(self)
        self.card_disputes = resources.CardDisputes(self)
        self.card_profiles = resources.CardProfiles(self)
        self.card_purchase_supplements = resources.CardPurchaseSupplements(self)
        self.external_accounts = resources.ExternalAccounts(self)
        self.exports = resources.Exports(self)
        self.digital_wallet_tokens = resources.DigitalWalletTokens(self)
        self.transactions = resources.Transactions(self)
        self.pending_transactions = resources.PendingTransactions(self)
        self.programs = resources.Programs(self)
        self.declined_transactions = resources.DeclinedTransactions(self)
        self.account_transfers = resources.AccountTransfers(self)
        self.ach_transfers = resources.ACHTransfers(self)
        self.ach_prenotifications = resources.ACHPrenotifications(self)
        self.documents = resources.Documents(self)
        self.wire_transfers = resources.WireTransfers(self)
        self.check_transfers = resources.CheckTransfers(self)
        self.entities = resources.Entities(self)
        self.inbound_ach_transfers = resources.InboundACHTransfers(self)
        self.inbound_wire_drawdown_requests = resources.InboundWireDrawdownRequests(self)
        self.wire_drawdown_requests = resources.WireDrawdownRequests(self)
        self.events = resources.Events(self)
        self.event_subscriptions = resources.EventSubscriptions(self)
        self.files = resources.Files(self)
        self.groups = resources.Groups(self)
        self.oauth_connections = resources.OAuthConnections(self)
        self.check_deposits = resources.CheckDeposits(self)
        self.routing_numbers = resources.RoutingNumbers(self)
        self.account_statements = resources.AccountStatements(self)
        self.simulations = resources.Simulations(self)
        self.physical_cards = resources.PhysicalCards(self)
        self.card_payments = resources.CardPayments(self)
        self.proof_of_authorization_requests = resources.ProofOfAuthorizationRequests(self)
        self.proof_of_authorization_request_submissions = resources.ProofOfAuthorizationRequestSubmissions(self)
        self.intrafi = resources.Intrafi(self)
        self.real_time_payments_request_for_payments = resources.RealTimePaymentsRequestForPayments(self)
        self.webhooks = resources.Webhooks(self)
        self.oauth_tokens = resources.OAuthTokens(self)
        self.inbound_wire_transfers = resources.InboundWireTransfers(self)
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
        connection_pool_limits: httpx.Limits | None = None,
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

        if connection_pool_limits is not None:
            if http_client is not None:
                raise ValueError("The 'http_client' argument is mutually exclusive with 'connection_pool_limits'")

            if not isinstance(self._client, SyncHttpxClientWrapper):
                raise ValueError(
                    "A custom HTTP client has been set and is mutually exclusive with the 'connection_pool_limits' argument"
                )

            http_client = None
        else:
            if self._limits is not DEFAULT_LIMITS:
                connection_pool_limits = self._limits
            else:
                connection_pool_limits = None

            http_client = http_client or self._client

        return self.__class__(
            api_key=api_key or self.api_key,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            connection_pool_limits=connection_pool_limits,
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

        if type_ == "idempotency_conflict_error":
            return _exceptions.IdempotencyConflictError(err_msg, response=response, body=body)

        if type_ == "invalid_operation_error":
            return _exceptions.InvalidOperationError(err_msg, response=response, body=body)

        if type_ == "unique_identifier_already_exists_error":
            return _exceptions.UniqueIdentifierAlreadyExistsError(err_msg, response=response, body=body)

        if type_ == "idempotency_unprocessable_error":
            return _exceptions.IdempotencyUnprocessableError(err_msg, response=response, body=body)

        if type_ == "rate_limited_error":
            return _exceptions.RateLimitedError(err_msg, response=response, body=body)

        if type_ == "internal_server_error":
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        if response.status_code == 500 or response.status_code >= 500:
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
    accounts: resources.AsyncAccounts
    account_numbers: resources.AsyncAccountNumbers
    bookkeeping_accounts: resources.AsyncBookkeepingAccounts
    bookkeeping_entry_sets: resources.AsyncBookkeepingEntrySets
    bookkeeping_entries: resources.AsyncBookkeepingEntries
    real_time_decisions: resources.AsyncRealTimeDecisions
    real_time_payments_transfers: resources.AsyncRealTimePaymentsTransfers
    cards: resources.AsyncCards
    card_disputes: resources.AsyncCardDisputes
    card_profiles: resources.AsyncCardProfiles
    card_purchase_supplements: resources.AsyncCardPurchaseSupplements
    external_accounts: resources.AsyncExternalAccounts
    exports: resources.AsyncExports
    digital_wallet_tokens: resources.AsyncDigitalWalletTokens
    transactions: resources.AsyncTransactions
    pending_transactions: resources.AsyncPendingTransactions
    programs: resources.AsyncPrograms
    declined_transactions: resources.AsyncDeclinedTransactions
    account_transfers: resources.AsyncAccountTransfers
    ach_transfers: resources.AsyncACHTransfers
    ach_prenotifications: resources.AsyncACHPrenotifications
    documents: resources.AsyncDocuments
    wire_transfers: resources.AsyncWireTransfers
    check_transfers: resources.AsyncCheckTransfers
    entities: resources.AsyncEntities
    inbound_ach_transfers: resources.AsyncInboundACHTransfers
    inbound_wire_drawdown_requests: resources.AsyncInboundWireDrawdownRequests
    wire_drawdown_requests: resources.AsyncWireDrawdownRequests
    events: resources.AsyncEvents
    event_subscriptions: resources.AsyncEventSubscriptions
    files: resources.AsyncFiles
    groups: resources.AsyncGroups
    oauth_connections: resources.AsyncOAuthConnections
    check_deposits: resources.AsyncCheckDeposits
    routing_numbers: resources.AsyncRoutingNumbers
    account_statements: resources.AsyncAccountStatements
    simulations: resources.AsyncSimulations
    physical_cards: resources.AsyncPhysicalCards
    card_payments: resources.AsyncCardPayments
    proof_of_authorization_requests: resources.AsyncProofOfAuthorizationRequests
    proof_of_authorization_request_submissions: resources.AsyncProofOfAuthorizationRequestSubmissions
    intrafi: resources.AsyncIntrafi
    real_time_payments_request_for_payments: resources.AsyncRealTimePaymentsRequestForPayments
    webhooks: resources.AsyncWebhooks
    oauth_tokens: resources.AsyncOAuthTokens
    inbound_wire_transfers: resources.AsyncInboundWireTransfers
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
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: AsyncTransport | None = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: ProxiesTypes | None = None,
        # See httpx documentation for [limits](https://www.python-httpx.org/advanced/#pool-limit-configuration)
        connection_pool_limits: httpx.Limits | None = None,
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
        """Construct a new async increase client instance.

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
            transport=transport,
            proxies=proxies,
            limits=connection_pool_limits,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

        self.accounts = resources.AsyncAccounts(self)
        self.account_numbers = resources.AsyncAccountNumbers(self)
        self.bookkeeping_accounts = resources.AsyncBookkeepingAccounts(self)
        self.bookkeeping_entry_sets = resources.AsyncBookkeepingEntrySets(self)
        self.bookkeeping_entries = resources.AsyncBookkeepingEntries(self)
        self.real_time_decisions = resources.AsyncRealTimeDecisions(self)
        self.real_time_payments_transfers = resources.AsyncRealTimePaymentsTransfers(self)
        self.cards = resources.AsyncCards(self)
        self.card_disputes = resources.AsyncCardDisputes(self)
        self.card_profiles = resources.AsyncCardProfiles(self)
        self.card_purchase_supplements = resources.AsyncCardPurchaseSupplements(self)
        self.external_accounts = resources.AsyncExternalAccounts(self)
        self.exports = resources.AsyncExports(self)
        self.digital_wallet_tokens = resources.AsyncDigitalWalletTokens(self)
        self.transactions = resources.AsyncTransactions(self)
        self.pending_transactions = resources.AsyncPendingTransactions(self)
        self.programs = resources.AsyncPrograms(self)
        self.declined_transactions = resources.AsyncDeclinedTransactions(self)
        self.account_transfers = resources.AsyncAccountTransfers(self)
        self.ach_transfers = resources.AsyncACHTransfers(self)
        self.ach_prenotifications = resources.AsyncACHPrenotifications(self)
        self.documents = resources.AsyncDocuments(self)
        self.wire_transfers = resources.AsyncWireTransfers(self)
        self.check_transfers = resources.AsyncCheckTransfers(self)
        self.entities = resources.AsyncEntities(self)
        self.inbound_ach_transfers = resources.AsyncInboundACHTransfers(self)
        self.inbound_wire_drawdown_requests = resources.AsyncInboundWireDrawdownRequests(self)
        self.wire_drawdown_requests = resources.AsyncWireDrawdownRequests(self)
        self.events = resources.AsyncEvents(self)
        self.event_subscriptions = resources.AsyncEventSubscriptions(self)
        self.files = resources.AsyncFiles(self)
        self.groups = resources.AsyncGroups(self)
        self.oauth_connections = resources.AsyncOAuthConnections(self)
        self.check_deposits = resources.AsyncCheckDeposits(self)
        self.routing_numbers = resources.AsyncRoutingNumbers(self)
        self.account_statements = resources.AsyncAccountStatements(self)
        self.simulations = resources.AsyncSimulations(self)
        self.physical_cards = resources.AsyncPhysicalCards(self)
        self.card_payments = resources.AsyncCardPayments(self)
        self.proof_of_authorization_requests = resources.AsyncProofOfAuthorizationRequests(self)
        self.proof_of_authorization_request_submissions = resources.AsyncProofOfAuthorizationRequestSubmissions(self)
        self.intrafi = resources.AsyncIntrafi(self)
        self.real_time_payments_request_for_payments = resources.AsyncRealTimePaymentsRequestForPayments(self)
        self.webhooks = resources.AsyncWebhooks(self)
        self.oauth_tokens = resources.AsyncOAuthTokens(self)
        self.inbound_wire_transfers = resources.AsyncInboundWireTransfers(self)
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
        connection_pool_limits: httpx.Limits | None = None,
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

        if connection_pool_limits is not None:
            if http_client is not None:
                raise ValueError("The 'http_client' argument is mutually exclusive with 'connection_pool_limits'")

            if not isinstance(self._client, AsyncHttpxClientWrapper):
                raise ValueError(
                    "A custom HTTP client has been set and is mutually exclusive with the 'connection_pool_limits' argument"
                )

            http_client = None
        else:
            if self._limits is not DEFAULT_LIMITS:
                connection_pool_limits = self._limits
            else:
                connection_pool_limits = None

            http_client = http_client or self._client

        return self.__class__(
            api_key=api_key or self.api_key,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            connection_pool_limits=connection_pool_limits,
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

        if type_ == "idempotency_conflict_error":
            return _exceptions.IdempotencyConflictError(err_msg, response=response, body=body)

        if type_ == "invalid_operation_error":
            return _exceptions.InvalidOperationError(err_msg, response=response, body=body)

        if type_ == "unique_identifier_already_exists_error":
            return _exceptions.UniqueIdentifierAlreadyExistsError(err_msg, response=response, body=body)

        if type_ == "idempotency_unprocessable_error":
            return _exceptions.IdempotencyUnprocessableError(err_msg, response=response, body=body)

        if type_ == "rate_limited_error":
            return _exceptions.RateLimitedError(err_msg, response=response, body=body)

        if type_ == "internal_server_error":
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        if response.status_code == 500 or response.status_code >= 500:
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
        self.accounts = resources.AccountsWithRawResponse(client.accounts)
        self.account_numbers = resources.AccountNumbersWithRawResponse(client.account_numbers)
        self.bookkeeping_accounts = resources.BookkeepingAccountsWithRawResponse(client.bookkeeping_accounts)
        self.bookkeeping_entry_sets = resources.BookkeepingEntrySetsWithRawResponse(client.bookkeeping_entry_sets)
        self.bookkeeping_entries = resources.BookkeepingEntriesWithRawResponse(client.bookkeeping_entries)
        self.real_time_decisions = resources.RealTimeDecisionsWithRawResponse(client.real_time_decisions)
        self.real_time_payments_transfers = resources.RealTimePaymentsTransfersWithRawResponse(
            client.real_time_payments_transfers
        )
        self.cards = resources.CardsWithRawResponse(client.cards)
        self.card_disputes = resources.CardDisputesWithRawResponse(client.card_disputes)
        self.card_profiles = resources.CardProfilesWithRawResponse(client.card_profiles)
        self.card_purchase_supplements = resources.CardPurchaseSupplementsWithRawResponse(
            client.card_purchase_supplements
        )
        self.external_accounts = resources.ExternalAccountsWithRawResponse(client.external_accounts)
        self.exports = resources.ExportsWithRawResponse(client.exports)
        self.digital_wallet_tokens = resources.DigitalWalletTokensWithRawResponse(client.digital_wallet_tokens)
        self.transactions = resources.TransactionsWithRawResponse(client.transactions)
        self.pending_transactions = resources.PendingTransactionsWithRawResponse(client.pending_transactions)
        self.programs = resources.ProgramsWithRawResponse(client.programs)
        self.declined_transactions = resources.DeclinedTransactionsWithRawResponse(client.declined_transactions)
        self.account_transfers = resources.AccountTransfersWithRawResponse(client.account_transfers)
        self.ach_transfers = resources.ACHTransfersWithRawResponse(client.ach_transfers)
        self.ach_prenotifications = resources.ACHPrenotificationsWithRawResponse(client.ach_prenotifications)
        self.documents = resources.DocumentsWithRawResponse(client.documents)
        self.wire_transfers = resources.WireTransfersWithRawResponse(client.wire_transfers)
        self.check_transfers = resources.CheckTransfersWithRawResponse(client.check_transfers)
        self.entities = resources.EntitiesWithRawResponse(client.entities)
        self.inbound_ach_transfers = resources.InboundACHTransfersWithRawResponse(client.inbound_ach_transfers)
        self.inbound_wire_drawdown_requests = resources.InboundWireDrawdownRequestsWithRawResponse(
            client.inbound_wire_drawdown_requests
        )
        self.wire_drawdown_requests = resources.WireDrawdownRequestsWithRawResponse(client.wire_drawdown_requests)
        self.events = resources.EventsWithRawResponse(client.events)
        self.event_subscriptions = resources.EventSubscriptionsWithRawResponse(client.event_subscriptions)
        self.files = resources.FilesWithRawResponse(client.files)
        self.groups = resources.GroupsWithRawResponse(client.groups)
        self.oauth_connections = resources.OAuthConnectionsWithRawResponse(client.oauth_connections)
        self.check_deposits = resources.CheckDepositsWithRawResponse(client.check_deposits)
        self.routing_numbers = resources.RoutingNumbersWithRawResponse(client.routing_numbers)
        self.account_statements = resources.AccountStatementsWithRawResponse(client.account_statements)
        self.simulations = resources.SimulationsWithRawResponse(client.simulations)
        self.physical_cards = resources.PhysicalCardsWithRawResponse(client.physical_cards)
        self.card_payments = resources.CardPaymentsWithRawResponse(client.card_payments)
        self.proof_of_authorization_requests = resources.ProofOfAuthorizationRequestsWithRawResponse(
            client.proof_of_authorization_requests
        )
        self.proof_of_authorization_request_submissions = (
            resources.ProofOfAuthorizationRequestSubmissionsWithRawResponse(
                client.proof_of_authorization_request_submissions
            )
        )
        self.intrafi = resources.IntrafiWithRawResponse(client.intrafi)
        self.real_time_payments_request_for_payments = resources.RealTimePaymentsRequestForPaymentsWithRawResponse(
            client.real_time_payments_request_for_payments
        )
        self.oauth_tokens = resources.OAuthTokensWithRawResponse(client.oauth_tokens)
        self.inbound_wire_transfers = resources.InboundWireTransfersWithRawResponse(client.inbound_wire_transfers)


class AsyncIncreaseWithRawResponse:
    def __init__(self, client: AsyncIncrease) -> None:
        self.accounts = resources.AsyncAccountsWithRawResponse(client.accounts)
        self.account_numbers = resources.AsyncAccountNumbersWithRawResponse(client.account_numbers)
        self.bookkeeping_accounts = resources.AsyncBookkeepingAccountsWithRawResponse(client.bookkeeping_accounts)
        self.bookkeeping_entry_sets = resources.AsyncBookkeepingEntrySetsWithRawResponse(client.bookkeeping_entry_sets)
        self.bookkeeping_entries = resources.AsyncBookkeepingEntriesWithRawResponse(client.bookkeeping_entries)
        self.real_time_decisions = resources.AsyncRealTimeDecisionsWithRawResponse(client.real_time_decisions)
        self.real_time_payments_transfers = resources.AsyncRealTimePaymentsTransfersWithRawResponse(
            client.real_time_payments_transfers
        )
        self.cards = resources.AsyncCardsWithRawResponse(client.cards)
        self.card_disputes = resources.AsyncCardDisputesWithRawResponse(client.card_disputes)
        self.card_profiles = resources.AsyncCardProfilesWithRawResponse(client.card_profiles)
        self.card_purchase_supplements = resources.AsyncCardPurchaseSupplementsWithRawResponse(
            client.card_purchase_supplements
        )
        self.external_accounts = resources.AsyncExternalAccountsWithRawResponse(client.external_accounts)
        self.exports = resources.AsyncExportsWithRawResponse(client.exports)
        self.digital_wallet_tokens = resources.AsyncDigitalWalletTokensWithRawResponse(client.digital_wallet_tokens)
        self.transactions = resources.AsyncTransactionsWithRawResponse(client.transactions)
        self.pending_transactions = resources.AsyncPendingTransactionsWithRawResponse(client.pending_transactions)
        self.programs = resources.AsyncProgramsWithRawResponse(client.programs)
        self.declined_transactions = resources.AsyncDeclinedTransactionsWithRawResponse(client.declined_transactions)
        self.account_transfers = resources.AsyncAccountTransfersWithRawResponse(client.account_transfers)
        self.ach_transfers = resources.AsyncACHTransfersWithRawResponse(client.ach_transfers)
        self.ach_prenotifications = resources.AsyncACHPrenotificationsWithRawResponse(client.ach_prenotifications)
        self.documents = resources.AsyncDocumentsWithRawResponse(client.documents)
        self.wire_transfers = resources.AsyncWireTransfersWithRawResponse(client.wire_transfers)
        self.check_transfers = resources.AsyncCheckTransfersWithRawResponse(client.check_transfers)
        self.entities = resources.AsyncEntitiesWithRawResponse(client.entities)
        self.inbound_ach_transfers = resources.AsyncInboundACHTransfersWithRawResponse(client.inbound_ach_transfers)
        self.inbound_wire_drawdown_requests = resources.AsyncInboundWireDrawdownRequestsWithRawResponse(
            client.inbound_wire_drawdown_requests
        )
        self.wire_drawdown_requests = resources.AsyncWireDrawdownRequestsWithRawResponse(client.wire_drawdown_requests)
        self.events = resources.AsyncEventsWithRawResponse(client.events)
        self.event_subscriptions = resources.AsyncEventSubscriptionsWithRawResponse(client.event_subscriptions)
        self.files = resources.AsyncFilesWithRawResponse(client.files)
        self.groups = resources.AsyncGroupsWithRawResponse(client.groups)
        self.oauth_connections = resources.AsyncOAuthConnectionsWithRawResponse(client.oauth_connections)
        self.check_deposits = resources.AsyncCheckDepositsWithRawResponse(client.check_deposits)
        self.routing_numbers = resources.AsyncRoutingNumbersWithRawResponse(client.routing_numbers)
        self.account_statements = resources.AsyncAccountStatementsWithRawResponse(client.account_statements)
        self.simulations = resources.AsyncSimulationsWithRawResponse(client.simulations)
        self.physical_cards = resources.AsyncPhysicalCardsWithRawResponse(client.physical_cards)
        self.card_payments = resources.AsyncCardPaymentsWithRawResponse(client.card_payments)
        self.proof_of_authorization_requests = resources.AsyncProofOfAuthorizationRequestsWithRawResponse(
            client.proof_of_authorization_requests
        )
        self.proof_of_authorization_request_submissions = (
            resources.AsyncProofOfAuthorizationRequestSubmissionsWithRawResponse(
                client.proof_of_authorization_request_submissions
            )
        )
        self.intrafi = resources.AsyncIntrafiWithRawResponse(client.intrafi)
        self.real_time_payments_request_for_payments = resources.AsyncRealTimePaymentsRequestForPaymentsWithRawResponse(
            client.real_time_payments_request_for_payments
        )
        self.oauth_tokens = resources.AsyncOAuthTokensWithRawResponse(client.oauth_tokens)
        self.inbound_wire_transfers = resources.AsyncInboundWireTransfersWithRawResponse(client.inbound_wire_transfers)


class IncreaseWithStreamedResponse:
    def __init__(self, client: Increase) -> None:
        self.accounts = resources.AccountsWithStreamingResponse(client.accounts)
        self.account_numbers = resources.AccountNumbersWithStreamingResponse(client.account_numbers)
        self.bookkeeping_accounts = resources.BookkeepingAccountsWithStreamingResponse(client.bookkeeping_accounts)
        self.bookkeeping_entry_sets = resources.BookkeepingEntrySetsWithStreamingResponse(client.bookkeeping_entry_sets)
        self.bookkeeping_entries = resources.BookkeepingEntriesWithStreamingResponse(client.bookkeeping_entries)
        self.real_time_decisions = resources.RealTimeDecisionsWithStreamingResponse(client.real_time_decisions)
        self.real_time_payments_transfers = resources.RealTimePaymentsTransfersWithStreamingResponse(
            client.real_time_payments_transfers
        )
        self.cards = resources.CardsWithStreamingResponse(client.cards)
        self.card_disputes = resources.CardDisputesWithStreamingResponse(client.card_disputes)
        self.card_profiles = resources.CardProfilesWithStreamingResponse(client.card_profiles)
        self.card_purchase_supplements = resources.CardPurchaseSupplementsWithStreamingResponse(
            client.card_purchase_supplements
        )
        self.external_accounts = resources.ExternalAccountsWithStreamingResponse(client.external_accounts)
        self.exports = resources.ExportsWithStreamingResponse(client.exports)
        self.digital_wallet_tokens = resources.DigitalWalletTokensWithStreamingResponse(client.digital_wallet_tokens)
        self.transactions = resources.TransactionsWithStreamingResponse(client.transactions)
        self.pending_transactions = resources.PendingTransactionsWithStreamingResponse(client.pending_transactions)
        self.programs = resources.ProgramsWithStreamingResponse(client.programs)
        self.declined_transactions = resources.DeclinedTransactionsWithStreamingResponse(client.declined_transactions)
        self.account_transfers = resources.AccountTransfersWithStreamingResponse(client.account_transfers)
        self.ach_transfers = resources.ACHTransfersWithStreamingResponse(client.ach_transfers)
        self.ach_prenotifications = resources.ACHPrenotificationsWithStreamingResponse(client.ach_prenotifications)
        self.documents = resources.DocumentsWithStreamingResponse(client.documents)
        self.wire_transfers = resources.WireTransfersWithStreamingResponse(client.wire_transfers)
        self.check_transfers = resources.CheckTransfersWithStreamingResponse(client.check_transfers)
        self.entities = resources.EntitiesWithStreamingResponse(client.entities)
        self.inbound_ach_transfers = resources.InboundACHTransfersWithStreamingResponse(client.inbound_ach_transfers)
        self.inbound_wire_drawdown_requests = resources.InboundWireDrawdownRequestsWithStreamingResponse(
            client.inbound_wire_drawdown_requests
        )
        self.wire_drawdown_requests = resources.WireDrawdownRequestsWithStreamingResponse(client.wire_drawdown_requests)
        self.events = resources.EventsWithStreamingResponse(client.events)
        self.event_subscriptions = resources.EventSubscriptionsWithStreamingResponse(client.event_subscriptions)
        self.files = resources.FilesWithStreamingResponse(client.files)
        self.groups = resources.GroupsWithStreamingResponse(client.groups)
        self.oauth_connections = resources.OAuthConnectionsWithStreamingResponse(client.oauth_connections)
        self.check_deposits = resources.CheckDepositsWithStreamingResponse(client.check_deposits)
        self.routing_numbers = resources.RoutingNumbersWithStreamingResponse(client.routing_numbers)
        self.account_statements = resources.AccountStatementsWithStreamingResponse(client.account_statements)
        self.simulations = resources.SimulationsWithStreamingResponse(client.simulations)
        self.physical_cards = resources.PhysicalCardsWithStreamingResponse(client.physical_cards)
        self.card_payments = resources.CardPaymentsWithStreamingResponse(client.card_payments)
        self.proof_of_authorization_requests = resources.ProofOfAuthorizationRequestsWithStreamingResponse(
            client.proof_of_authorization_requests
        )
        self.proof_of_authorization_request_submissions = (
            resources.ProofOfAuthorizationRequestSubmissionsWithStreamingResponse(
                client.proof_of_authorization_request_submissions
            )
        )
        self.intrafi = resources.IntrafiWithStreamingResponse(client.intrafi)
        self.real_time_payments_request_for_payments = (
            resources.RealTimePaymentsRequestForPaymentsWithStreamingResponse(
                client.real_time_payments_request_for_payments
            )
        )
        self.oauth_tokens = resources.OAuthTokensWithStreamingResponse(client.oauth_tokens)
        self.inbound_wire_transfers = resources.InboundWireTransfersWithStreamingResponse(client.inbound_wire_transfers)


class AsyncIncreaseWithStreamedResponse:
    def __init__(self, client: AsyncIncrease) -> None:
        self.accounts = resources.AsyncAccountsWithStreamingResponse(client.accounts)
        self.account_numbers = resources.AsyncAccountNumbersWithStreamingResponse(client.account_numbers)
        self.bookkeeping_accounts = resources.AsyncBookkeepingAccountsWithStreamingResponse(client.bookkeeping_accounts)
        self.bookkeeping_entry_sets = resources.AsyncBookkeepingEntrySetsWithStreamingResponse(
            client.bookkeeping_entry_sets
        )
        self.bookkeeping_entries = resources.AsyncBookkeepingEntriesWithStreamingResponse(client.bookkeeping_entries)
        self.real_time_decisions = resources.AsyncRealTimeDecisionsWithStreamingResponse(client.real_time_decisions)
        self.real_time_payments_transfers = resources.AsyncRealTimePaymentsTransfersWithStreamingResponse(
            client.real_time_payments_transfers
        )
        self.cards = resources.AsyncCardsWithStreamingResponse(client.cards)
        self.card_disputes = resources.AsyncCardDisputesWithStreamingResponse(client.card_disputes)
        self.card_profiles = resources.AsyncCardProfilesWithStreamingResponse(client.card_profiles)
        self.card_purchase_supplements = resources.AsyncCardPurchaseSupplementsWithStreamingResponse(
            client.card_purchase_supplements
        )
        self.external_accounts = resources.AsyncExternalAccountsWithStreamingResponse(client.external_accounts)
        self.exports = resources.AsyncExportsWithStreamingResponse(client.exports)
        self.digital_wallet_tokens = resources.AsyncDigitalWalletTokensWithStreamingResponse(
            client.digital_wallet_tokens
        )
        self.transactions = resources.AsyncTransactionsWithStreamingResponse(client.transactions)
        self.pending_transactions = resources.AsyncPendingTransactionsWithStreamingResponse(client.pending_transactions)
        self.programs = resources.AsyncProgramsWithStreamingResponse(client.programs)
        self.declined_transactions = resources.AsyncDeclinedTransactionsWithStreamingResponse(
            client.declined_transactions
        )
        self.account_transfers = resources.AsyncAccountTransfersWithStreamingResponse(client.account_transfers)
        self.ach_transfers = resources.AsyncACHTransfersWithStreamingResponse(client.ach_transfers)
        self.ach_prenotifications = resources.AsyncACHPrenotificationsWithStreamingResponse(client.ach_prenotifications)
        self.documents = resources.AsyncDocumentsWithStreamingResponse(client.documents)
        self.wire_transfers = resources.AsyncWireTransfersWithStreamingResponse(client.wire_transfers)
        self.check_transfers = resources.AsyncCheckTransfersWithStreamingResponse(client.check_transfers)
        self.entities = resources.AsyncEntitiesWithStreamingResponse(client.entities)
        self.inbound_ach_transfers = resources.AsyncInboundACHTransfersWithStreamingResponse(
            client.inbound_ach_transfers
        )
        self.inbound_wire_drawdown_requests = resources.AsyncInboundWireDrawdownRequestsWithStreamingResponse(
            client.inbound_wire_drawdown_requests
        )
        self.wire_drawdown_requests = resources.AsyncWireDrawdownRequestsWithStreamingResponse(
            client.wire_drawdown_requests
        )
        self.events = resources.AsyncEventsWithStreamingResponse(client.events)
        self.event_subscriptions = resources.AsyncEventSubscriptionsWithStreamingResponse(client.event_subscriptions)
        self.files = resources.AsyncFilesWithStreamingResponse(client.files)
        self.groups = resources.AsyncGroupsWithStreamingResponse(client.groups)
        self.oauth_connections = resources.AsyncOAuthConnectionsWithStreamingResponse(client.oauth_connections)
        self.check_deposits = resources.AsyncCheckDepositsWithStreamingResponse(client.check_deposits)
        self.routing_numbers = resources.AsyncRoutingNumbersWithStreamingResponse(client.routing_numbers)
        self.account_statements = resources.AsyncAccountStatementsWithStreamingResponse(client.account_statements)
        self.simulations = resources.AsyncSimulationsWithStreamingResponse(client.simulations)
        self.physical_cards = resources.AsyncPhysicalCardsWithStreamingResponse(client.physical_cards)
        self.card_payments = resources.AsyncCardPaymentsWithStreamingResponse(client.card_payments)
        self.proof_of_authorization_requests = resources.AsyncProofOfAuthorizationRequestsWithStreamingResponse(
            client.proof_of_authorization_requests
        )
        self.proof_of_authorization_request_submissions = (
            resources.AsyncProofOfAuthorizationRequestSubmissionsWithStreamingResponse(
                client.proof_of_authorization_request_submissions
            )
        )
        self.intrafi = resources.AsyncIntrafiWithStreamingResponse(client.intrafi)
        self.real_time_payments_request_for_payments = (
            resources.AsyncRealTimePaymentsRequestForPaymentsWithStreamingResponse(
                client.real_time_payments_request_for_payments
            )
        )
        self.oauth_tokens = resources.AsyncOAuthTokensWithStreamingResponse(client.oauth_tokens)
        self.inbound_wire_transfers = resources.AsyncInboundWireTransfersWithStreamingResponse(
            client.inbound_wire_transfers
        )


Client = Increase

AsyncClient = AsyncIncrease
