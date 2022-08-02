# File generated from our OpenAPI spec by Stainless.

import os
from typing import Dict, Union, Optional
from typing_extensions import Literal

from . import resources
from ._qs import Querystring
from ._types import Timeout, Transport, ProxiesTypes, RequestOptions
from ._version import __version__
from ._base_client import (
    DEFAULT_TIMEOUT,
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Increase",
    "AsyncIncrease",
    "Client",
    "AsyncClient",
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.increase.com",
    "sandbox": "https://sandbox.increase.com",
}


class Increase(SyncAPIClient):
    accounts: resources.Accounts
    account_numbers: resources.AccountNumbers
    cards: resources.Cards
    card_disputes: resources.CardDisputes
    transactions: resources.Transactions
    pending_transactions: resources.PendingTransactions
    declined_transactions: resources.DeclinedTransactions
    limits: resources.Limits
    account_transfers: resources.AccountTransfers
    ach_transfers: resources.ACHTransfers
    ach_prenotifications: resources.ACHPrenotifications
    wire_transfers: resources.WireTransfers
    check_transfers: resources.CheckTransfers
    entities: resources.Entities
    events: resources.Events
    event_subscriptions: resources.EventSubscriptions
    files: resources.Files
    groups: resources.Groups
    oauth_connections: resources.OauthConnections
    check_deposits: resources.CheckDeposits
    routing_numbers: resources.RoutingNumbers
    account_statements: resources.AccountStatements
    simulations: resources.Simulations

    def __init__(
        self,
        *,
        environment: Literal["production", "sandbox"] = "production",
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Optional[Transport] = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: Optional[ProxiesTypes] = None,
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
        api_key = api_key or os.environ.get("INCREASE_API_KEY", "")
        if not api_key:
            raise Exception("No API key provided")

        if base_url is None:
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            api_key=api_key,
            max_retries=max_retries,
            timeout=timeout,
            transport=transport,
            proxies=proxies,
            _strict_response_validation=_strict_response_validation,
        )

        self.accounts = resources.Accounts(self)
        self.account_numbers = resources.AccountNumbers(self)
        self.cards = resources.Cards(self)
        self.card_disputes = resources.CardDisputes(self)
        self.transactions = resources.Transactions(self)
        self.pending_transactions = resources.PendingTransactions(self)
        self.declined_transactions = resources.DeclinedTransactions(self)
        self.limits = resources.Limits(self)
        self.account_transfers = resources.AccountTransfers(self)
        self.ach_transfers = resources.ACHTransfers(self)
        self.ach_prenotifications = resources.ACHPrenotifications(self)
        self.wire_transfers = resources.WireTransfers(self)
        self.check_transfers = resources.CheckTransfers(self)
        self.entities = resources.Entities(self)
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
    def default_headers(self) -> Dict[str, str]:
        return {**super().default_headers, "Authorization": f"Bearer {self.api_key}"}


class AsyncIncrease(AsyncAPIClient):
    accounts: resources.AsyncAccounts
    account_numbers: resources.AsyncAccountNumbers
    cards: resources.AsyncCards
    card_disputes: resources.AsyncCardDisputes
    transactions: resources.AsyncTransactions
    pending_transactions: resources.AsyncPendingTransactions
    declined_transactions: resources.AsyncDeclinedTransactions
    limits: resources.AsyncLimits
    account_transfers: resources.AsyncAccountTransfers
    ach_transfers: resources.AsyncACHTransfers
    ach_prenotifications: resources.AsyncACHPrenotifications
    wire_transfers: resources.AsyncWireTransfers
    check_transfers: resources.AsyncCheckTransfers
    entities: resources.AsyncEntities
    events: resources.AsyncEvents
    event_subscriptions: resources.AsyncEventSubscriptions
    files: resources.AsyncFiles
    groups: resources.AsyncGroups
    oauth_connections: resources.AsyncOauthConnections
    check_deposits: resources.AsyncCheckDeposits
    routing_numbers: resources.AsyncRoutingNumbers
    account_statements: resources.AsyncAccountStatements
    simulations: resources.AsyncSimulations

    def __init__(
        self,
        *,
        environment: Literal["production", "sandbox"] = "production",
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Optional[Transport] = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: Optional[ProxiesTypes] = None,
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
        api_key = api_key or os.environ.get("INCREASE_API_KEY", "")
        if not api_key:
            raise Exception("No API key provided")

        if base_url is None:
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            api_key=api_key,
            max_retries=max_retries,
            timeout=timeout,
            transport=transport,
            proxies=proxies,
            _strict_response_validation=_strict_response_validation,
        )

        self.accounts = resources.AsyncAccounts(self)
        self.account_numbers = resources.AsyncAccountNumbers(self)
        self.cards = resources.AsyncCards(self)
        self.card_disputes = resources.AsyncCardDisputes(self)
        self.transactions = resources.AsyncTransactions(self)
        self.pending_transactions = resources.AsyncPendingTransactions(self)
        self.declined_transactions = resources.AsyncDeclinedTransactions(self)
        self.limits = resources.AsyncLimits(self)
        self.account_transfers = resources.AsyncAccountTransfers(self)
        self.ach_transfers = resources.AsyncACHTransfers(self)
        self.ach_prenotifications = resources.AsyncACHPrenotifications(self)
        self.wire_transfers = resources.AsyncWireTransfers(self)
        self.check_transfers = resources.AsyncCheckTransfers(self)
        self.entities = resources.AsyncEntities(self)
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
    def default_headers(self) -> Dict[str, str]:
        return {**super().default_headers, "Authorization": f"Bearer {self.api_key}"}


Client = Increase

AsyncClient = AsyncIncrease
