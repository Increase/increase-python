# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Dict, Union, Mapping, Optional
from typing_extensions import Literal

import httpx

from . import resources
from . import _exceptions as exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_mapping
from ._version import __version__
from ._streaming import Stream as Stream
from ._streaming import AsyncStream as AsyncStream
from ._base_client import (
    DEFAULT_LIMITS,
    DEFAULT_TIMEOUT,
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
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
    balance_lookups: resources.BalanceLookups
    cards: resources.Cards
    card_disputes: resources.CardDisputes
    card_profiles: resources.CardProfiles
    external_accounts: resources.ExternalAccounts
    exports: resources.Exports
    digital_wallet_tokens: resources.DigitalWalletTokens
    transactions: resources.Transactions
    pending_transactions: resources.PendingTransactions
    programs: resources.Programs
    declined_transactions: resources.DeclinedTransactions
    limits: resources.Limits
    account_transfers: resources.AccountTransfers
    ach_transfers: resources.ACHTransfers
    inbound_ach_transfer_returns: resources.InboundACHTransferReturns
    ach_prenotifications: resources.ACHPrenotifications
    documents: resources.Documents
    wire_transfers: resources.WireTransfers
    check_transfers: resources.CheckTransfers
    entities: resources.Entities
    inbound_wire_drawdown_requests: resources.InboundWireDrawdownRequests
    wire_drawdown_requests: resources.WireDrawdownRequests
    events: resources.Events
    event_subscriptions: resources.EventSubscriptions
    files: resources.Files
    groups: resources.Groups
    oauth_connections: resources.OauthConnections
    check_deposits: resources.CheckDeposits
    routing_numbers: resources.RoutingNumbers
    account_statements: resources.AccountStatements
    simulations: resources.Simulations

    # client options
    api_key: str

    _environment: Literal["production", "sandbox"]

    def __init__(
        self,
        *,
        environment: Literal["production", "sandbox"] = "production",
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Optional[Transport] = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: Optional[ProxiesTypes] = None,
        # See httpx documentation for [limits](https://www.python-httpx.org/advanced/#pool-limit-configuration)
        connection_pool_limits: httpx.Limits | None = DEFAULT_LIMITS,
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

        This automatically infers the `api_key` argument from the `INCREASE_API_KEY` environment variable if it is not provided.
        """
        api_key = api_key or os.environ.get("INCREASE_API_KEY", "")
        if not api_key:
            raise Exception(
                "The api_key client option must be set either by passing api_key to the client or by setting the INCREASE_API_KEY environment variable"
            )

        self._environment = environment

        if base_url is None:
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            transport=transport,
            proxies=proxies,
            limits=connection_pool_limits,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.api_key = api_key

        self._idempotency_header = "Idempotency-Key"

        self.accounts = resources.Accounts(self)
        self.account_numbers = resources.AccountNumbers(self)
        self.bookkeeping_accounts = resources.BookkeepingAccounts(self)
        self.bookkeeping_entry_sets = resources.BookkeepingEntrySets(self)
        self.bookkeeping_entries = resources.BookkeepingEntries(self)
        self.real_time_decisions = resources.RealTimeDecisions(self)
        self.real_time_payments_transfers = resources.RealTimePaymentsTransfers(self)
        self.balance_lookups = resources.BalanceLookups(self)
        self.cards = resources.Cards(self)
        self.card_disputes = resources.CardDisputes(self)
        self.card_profiles = resources.CardProfiles(self)
        self.external_accounts = resources.ExternalAccounts(self)
        self.exports = resources.Exports(self)
        self.digital_wallet_tokens = resources.DigitalWalletTokens(self)
        self.transactions = resources.Transactions(self)
        self.pending_transactions = resources.PendingTransactions(self)
        self.programs = resources.Programs(self)
        self.declined_transactions = resources.DeclinedTransactions(self)
        self.limits = resources.Limits(self)
        self.account_transfers = resources.AccountTransfers(self)
        self.ach_transfers = resources.ACHTransfers(self)
        self.inbound_ach_transfer_returns = resources.InboundACHTransferReturns(self)
        self.ach_prenotifications = resources.ACHPrenotifications(self)
        self.documents = resources.Documents(self)
        self.wire_transfers = resources.WireTransfers(self)
        self.check_transfers = resources.CheckTransfers(self)
        self.entities = resources.Entities(self)
        self.inbound_wire_drawdown_requests = resources.InboundWireDrawdownRequests(self)
        self.wire_drawdown_requests = resources.WireDrawdownRequests(self)
        self.events = resources.Events(self)
        self.event_subscriptions = resources.EventSubscriptions(self)
        self.files = resources.Files(self)
        self.groups = resources.Groups(self)
        self.oauth_connections = resources.OauthConnections(self)
        self.check_deposits = resources.CheckDeposits(self)
        self.routing_numbers = resources.RoutingNumbers(self)
        self.account_statements = resources.AccountStatements(self)
        self.simulations = resources.Simulations(self)

    @property
    def qs(self) -> Querystring:
        return Querystring(nested_format="dots", array_format="comma")

    @property
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "sandbox"] | None = None,
        base_url: str | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        connection_pool_limits: httpx.Limits | NotGiven = NOT_GIVEN,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
    ) -> Increase:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.

        It should be noted that this does not share the underlying httpx client class which may lead
        to performance issues.
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

        # TODO: share the same httpx client between instances
        return self.__class__(
            base_url=base_url or str(self.base_url),
            environment=environment or self._environment,
            api_key=api_key or self.api_key,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            connection_pool_limits=self._limits
            if isinstance(connection_pool_limits, NotGiven)
            else connection_pool_limits,
            max_retries=self.max_retries if isinstance(max_retries, NotGiven) else max_retries,
            default_headers=headers,
            default_query=params,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        request: httpx.Request,
        response: httpx.Response,
    ) -> exceptions.APIStatusError:
        if not is_mapping(body):
            return super()._make_status_error(err_msg, request=request, response=response, body=body)

        type_ = body.get("type")
        if type_ == "invalid_parameters_error":
            return exceptions.InvalidParametersError(err_msg, request=request, response=response, body=body)

        if type_ == "malformed_request_error":
            return exceptions.MalformedRequestError(err_msg, request=request, response=response, body=body)

        if type_ == "invalid_api_key_error":
            return exceptions.InvalidAPIKeyError(err_msg, request=request, response=response, body=body)

        if type_ == "environment_mismatch_error":
            return exceptions.EnvironmentMismatchError(err_msg, request=request, response=response, body=body)

        if type_ == "insufficient_permissions_error":
            return exceptions.InsufficientPermissionsError(err_msg, request=request, response=response, body=body)

        if type_ == "private_feature_error":
            return exceptions.PrivateFeatureError(err_msg, request=request, response=response, body=body)

        if type_ == "api_method_not_found_error":
            return exceptions.APIMethodNotFoundError(err_msg, request=request, response=response, body=body)

        if type_ == "object_not_found_error":
            return exceptions.ObjectNotFoundError(err_msg, request=request, response=response, body=body)

        if type_ == "idempotency_conflict_error":
            return exceptions.IdempotencyConflictError(err_msg, request=request, response=response, body=body)

        if type_ == "invalid_operation_error":
            return exceptions.InvalidOperationError(err_msg, request=request, response=response, body=body)

        if type_ == "unique_identifier_already_exists_error":
            return exceptions.UniqueIdentifierAlreadyExistsError(err_msg, request=request, response=response, body=body)

        if type_ == "idempotency_unprocessable_error":
            return exceptions.IdempotencyUnprocessableError(err_msg, request=request, response=response, body=body)

        if type_ == "rate_limited_error":
            return exceptions.RateLimitedError(err_msg, request=request, response=response, body=body)

        if type_ == "internal_server_error":
            return exceptions.InternalServerError(err_msg, request=request, response=response, body=body)
        if response.status_code == 500:
            return exceptions.InternalServerError(
                err_msg,
                request=request,
                response=response,
                body={
                    "detail": None,
                    "status": 500,
                    "title": "",
                    "type": "internal_server_error",
                },
            )
        return super()._make_status_error(err_msg, request=request, response=response, body=body)


class AsyncIncrease(AsyncAPIClient):
    accounts: resources.AsyncAccounts
    account_numbers: resources.AsyncAccountNumbers
    bookkeeping_accounts: resources.AsyncBookkeepingAccounts
    bookkeeping_entry_sets: resources.AsyncBookkeepingEntrySets
    bookkeeping_entries: resources.AsyncBookkeepingEntries
    real_time_decisions: resources.AsyncRealTimeDecisions
    real_time_payments_transfers: resources.AsyncRealTimePaymentsTransfers
    balance_lookups: resources.AsyncBalanceLookups
    cards: resources.AsyncCards
    card_disputes: resources.AsyncCardDisputes
    card_profiles: resources.AsyncCardProfiles
    external_accounts: resources.AsyncExternalAccounts
    exports: resources.AsyncExports
    digital_wallet_tokens: resources.AsyncDigitalWalletTokens
    transactions: resources.AsyncTransactions
    pending_transactions: resources.AsyncPendingTransactions
    programs: resources.AsyncPrograms
    declined_transactions: resources.AsyncDeclinedTransactions
    limits: resources.AsyncLimits
    account_transfers: resources.AsyncAccountTransfers
    ach_transfers: resources.AsyncACHTransfers
    inbound_ach_transfer_returns: resources.AsyncInboundACHTransferReturns
    ach_prenotifications: resources.AsyncACHPrenotifications
    documents: resources.AsyncDocuments
    wire_transfers: resources.AsyncWireTransfers
    check_transfers: resources.AsyncCheckTransfers
    entities: resources.AsyncEntities
    inbound_wire_drawdown_requests: resources.AsyncInboundWireDrawdownRequests
    wire_drawdown_requests: resources.AsyncWireDrawdownRequests
    events: resources.AsyncEvents
    event_subscriptions: resources.AsyncEventSubscriptions
    files: resources.AsyncFiles
    groups: resources.AsyncGroups
    oauth_connections: resources.AsyncOauthConnections
    check_deposits: resources.AsyncCheckDeposits
    routing_numbers: resources.AsyncRoutingNumbers
    account_statements: resources.AsyncAccountStatements
    simulations: resources.AsyncSimulations

    # client options
    api_key: str

    _environment: Literal["production", "sandbox"]

    def __init__(
        self,
        *,
        environment: Literal["production", "sandbox"] = "production",
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Optional[Transport] = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: Optional[ProxiesTypes] = None,
        # See httpx documentation for [limits](https://www.python-httpx.org/advanced/#pool-limit-configuration)
        connection_pool_limits: httpx.Limits | None = DEFAULT_LIMITS,
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

        This automatically infers the `api_key` argument from the `INCREASE_API_KEY` environment variable if it is not provided.
        """
        api_key = api_key or os.environ.get("INCREASE_API_KEY", "")
        if not api_key:
            raise Exception(
                "The api_key client option must be set either by passing api_key to the client or by setting the INCREASE_API_KEY environment variable"
            )

        self._environment = environment

        if base_url is None:
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            transport=transport,
            proxies=proxies,
            limits=connection_pool_limits,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.api_key = api_key

        self._idempotency_header = "Idempotency-Key"

        self.accounts = resources.AsyncAccounts(self)
        self.account_numbers = resources.AsyncAccountNumbers(self)
        self.bookkeeping_accounts = resources.AsyncBookkeepingAccounts(self)
        self.bookkeeping_entry_sets = resources.AsyncBookkeepingEntrySets(self)
        self.bookkeeping_entries = resources.AsyncBookkeepingEntries(self)
        self.real_time_decisions = resources.AsyncRealTimeDecisions(self)
        self.real_time_payments_transfers = resources.AsyncRealTimePaymentsTransfers(self)
        self.balance_lookups = resources.AsyncBalanceLookups(self)
        self.cards = resources.AsyncCards(self)
        self.card_disputes = resources.AsyncCardDisputes(self)
        self.card_profiles = resources.AsyncCardProfiles(self)
        self.external_accounts = resources.AsyncExternalAccounts(self)
        self.exports = resources.AsyncExports(self)
        self.digital_wallet_tokens = resources.AsyncDigitalWalletTokens(self)
        self.transactions = resources.AsyncTransactions(self)
        self.pending_transactions = resources.AsyncPendingTransactions(self)
        self.programs = resources.AsyncPrograms(self)
        self.declined_transactions = resources.AsyncDeclinedTransactions(self)
        self.limits = resources.AsyncLimits(self)
        self.account_transfers = resources.AsyncAccountTransfers(self)
        self.ach_transfers = resources.AsyncACHTransfers(self)
        self.inbound_ach_transfer_returns = resources.AsyncInboundACHTransferReturns(self)
        self.ach_prenotifications = resources.AsyncACHPrenotifications(self)
        self.documents = resources.AsyncDocuments(self)
        self.wire_transfers = resources.AsyncWireTransfers(self)
        self.check_transfers = resources.AsyncCheckTransfers(self)
        self.entities = resources.AsyncEntities(self)
        self.inbound_wire_drawdown_requests = resources.AsyncInboundWireDrawdownRequests(self)
        self.wire_drawdown_requests = resources.AsyncWireDrawdownRequests(self)
        self.events = resources.AsyncEvents(self)
        self.event_subscriptions = resources.AsyncEventSubscriptions(self)
        self.files = resources.AsyncFiles(self)
        self.groups = resources.AsyncGroups(self)
        self.oauth_connections = resources.AsyncOauthConnections(self)
        self.check_deposits = resources.AsyncCheckDeposits(self)
        self.routing_numbers = resources.AsyncRoutingNumbers(self)
        self.account_statements = resources.AsyncAccountStatements(self)
        self.simulations = resources.AsyncSimulations(self)

    @property
    def qs(self) -> Querystring:
        return Querystring(nested_format="dots", array_format="comma")

    @property
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "sandbox"] | None = None,
        base_url: str | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        connection_pool_limits: httpx.Limits | NotGiven = NOT_GIVEN,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
    ) -> AsyncIncrease:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.

        It should be noted that this does not share the underlying httpx client class which may lead
        to performance issues.
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

        # TODO: share the same httpx client between instances
        return self.__class__(
            base_url=base_url or str(self.base_url),
            environment=environment or self._environment,
            api_key=api_key or self.api_key,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            connection_pool_limits=self._limits
            if isinstance(connection_pool_limits, NotGiven)
            else connection_pool_limits,
            max_retries=self.max_retries if isinstance(max_retries, NotGiven) else max_retries,
            default_headers=headers,
            default_query=params,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        request: httpx.Request,
        response: httpx.Response,
    ) -> exceptions.APIStatusError:
        if not is_mapping(body):
            return super()._make_status_error(err_msg, request=request, response=response, body=body)

        type_ = body.get("type")
        if type_ == "invalid_parameters_error":
            return exceptions.InvalidParametersError(err_msg, request=request, response=response, body=body)

        if type_ == "malformed_request_error":
            return exceptions.MalformedRequestError(err_msg, request=request, response=response, body=body)

        if type_ == "invalid_api_key_error":
            return exceptions.InvalidAPIKeyError(err_msg, request=request, response=response, body=body)

        if type_ == "environment_mismatch_error":
            return exceptions.EnvironmentMismatchError(err_msg, request=request, response=response, body=body)

        if type_ == "insufficient_permissions_error":
            return exceptions.InsufficientPermissionsError(err_msg, request=request, response=response, body=body)

        if type_ == "private_feature_error":
            return exceptions.PrivateFeatureError(err_msg, request=request, response=response, body=body)

        if type_ == "api_method_not_found_error":
            return exceptions.APIMethodNotFoundError(err_msg, request=request, response=response, body=body)

        if type_ == "object_not_found_error":
            return exceptions.ObjectNotFoundError(err_msg, request=request, response=response, body=body)

        if type_ == "idempotency_conflict_error":
            return exceptions.IdempotencyConflictError(err_msg, request=request, response=response, body=body)

        if type_ == "invalid_operation_error":
            return exceptions.InvalidOperationError(err_msg, request=request, response=response, body=body)

        if type_ == "unique_identifier_already_exists_error":
            return exceptions.UniqueIdentifierAlreadyExistsError(err_msg, request=request, response=response, body=body)

        if type_ == "idempotency_unprocessable_error":
            return exceptions.IdempotencyUnprocessableError(err_msg, request=request, response=response, body=body)

        if type_ == "rate_limited_error":
            return exceptions.RateLimitedError(err_msg, request=request, response=response, body=body)

        if type_ == "internal_server_error":
            return exceptions.InternalServerError(err_msg, request=request, response=response, body=body)
        if response.status_code == 500:
            return exceptions.InternalServerError(
                err_msg,
                request=request,
                response=response,
                body={
                    "detail": None,
                    "status": 500,
                    "title": "",
                    "type": "internal_server_error",
                },
            )
        return super()._make_status_error(err_msg, request=request, response=response, body=body)


Client = Increase

AsyncClient = AsyncIncrease
