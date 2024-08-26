# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
    accounts: resources.AccountsResource
    account_numbers: resources.AccountNumbersResource
    cards: resources.CardsResource
    card_payments: resources.CardPaymentsResource
    card_purchase_supplements: resources.CardPurchaseSupplementsResource
    card_disputes: resources.CardDisputesResource
    physical_cards: resources.PhysicalCardsResource
    digital_card_profiles: resources.DigitalCardProfilesResource
    physical_card_profiles: resources.PhysicalCardProfilesResource
    digital_wallet_tokens: resources.DigitalWalletTokensResource
    transactions: resources.TransactionsResource
    pending_transactions: resources.PendingTransactionsResource
    declined_transactions: resources.DeclinedTransactionsResource
    account_transfers: resources.AccountTransfersResource
    ach_transfers: resources.ACHTransfersResource
    ach_prenotifications: resources.ACHPrenotificationsResource
    inbound_ach_transfers: resources.InboundACHTransfersResource
    wire_transfers: resources.WireTransfersResource
    inbound_wire_transfers: resources.InboundWireTransfersResource
    wire_drawdown_requests: resources.WireDrawdownRequestsResource
    inbound_wire_drawdown_requests: resources.InboundWireDrawdownRequestsResource
    check_transfers: resources.CheckTransfersResource
    inbound_check_deposits: resources.InboundCheckDepositsResource
    real_time_payments_transfers: resources.RealTimePaymentsTransfersResource
    inbound_real_time_payments_transfers: resources.InboundRealTimePaymentsTransfersResource
    check_deposits: resources.CheckDepositsResource
    lockboxes: resources.LockboxesResource
    inbound_mail_items: resources.InboundMailItemsResource
    routing_numbers: resources.RoutingNumbersResource
    external_accounts: resources.ExternalAccountsResource
    entities: resources.EntitiesResource
    supplemental_documents: resources.SupplementalDocumentsResource
    programs: resources.ProgramsResource
    proof_of_authorization_requests: resources.ProofOfAuthorizationRequestsResource
    proof_of_authorization_request_submissions: resources.ProofOfAuthorizationRequestSubmissionsResource
    account_statements: resources.AccountStatementsResource
    files: resources.FilesResource
    documents: resources.DocumentsResource
    exports: resources.ExportsResource
    events: resources.EventsResource
    event_subscriptions: resources.EventSubscriptionsResource
    real_time_decisions: resources.RealTimeDecisionsResource
    bookkeeping_accounts: resources.BookkeepingAccountsResource
    bookkeeping_entry_sets: resources.BookkeepingEntrySetsResource
    bookkeeping_entries: resources.BookkeepingEntriesResource
    groups: resources.GroupsResource
    oauth_connections: resources.OAuthConnectionsResource
    oauth_tokens: resources.OAuthTokensResource
    intrafi_account_enrollments: resources.IntrafiAccountEnrollmentsResource
    intrafi_balances: resources.IntrafiBalancesResource
    intrafi_exclusions: resources.IntrafiExclusionsResource
    real_time_payments_request_for_payments: resources.RealTimePaymentsRequestForPaymentsResource
    simulations: resources.SimulationsResource
    webhooks: resources.Webhooks
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
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

        self.accounts = resources.AccountsResource(self)
        self.account_numbers = resources.AccountNumbersResource(self)
        self.cards = resources.CardsResource(self)
        self.card_payments = resources.CardPaymentsResource(self)
        self.card_purchase_supplements = resources.CardPurchaseSupplementsResource(self)
        self.card_disputes = resources.CardDisputesResource(self)
        self.physical_cards = resources.PhysicalCardsResource(self)
        self.digital_card_profiles = resources.DigitalCardProfilesResource(self)
        self.physical_card_profiles = resources.PhysicalCardProfilesResource(self)
        self.digital_wallet_tokens = resources.DigitalWalletTokensResource(self)
        self.transactions = resources.TransactionsResource(self)
        self.pending_transactions = resources.PendingTransactionsResource(self)
        self.declined_transactions = resources.DeclinedTransactionsResource(self)
        self.account_transfers = resources.AccountTransfersResource(self)
        self.ach_transfers = resources.ACHTransfersResource(self)
        self.ach_prenotifications = resources.ACHPrenotificationsResource(self)
        self.inbound_ach_transfers = resources.InboundACHTransfersResource(self)
        self.wire_transfers = resources.WireTransfersResource(self)
        self.inbound_wire_transfers = resources.InboundWireTransfersResource(self)
        self.wire_drawdown_requests = resources.WireDrawdownRequestsResource(self)
        self.inbound_wire_drawdown_requests = resources.InboundWireDrawdownRequestsResource(self)
        self.check_transfers = resources.CheckTransfersResource(self)
        self.inbound_check_deposits = resources.InboundCheckDepositsResource(self)
        self.real_time_payments_transfers = resources.RealTimePaymentsTransfersResource(self)
        self.inbound_real_time_payments_transfers = resources.InboundRealTimePaymentsTransfersResource(self)
        self.check_deposits = resources.CheckDepositsResource(self)
        self.lockboxes = resources.LockboxesResource(self)
        self.inbound_mail_items = resources.InboundMailItemsResource(self)
        self.routing_numbers = resources.RoutingNumbersResource(self)
        self.external_accounts = resources.ExternalAccountsResource(self)
        self.entities = resources.EntitiesResource(self)
        self.supplemental_documents = resources.SupplementalDocumentsResource(self)
        self.programs = resources.ProgramsResource(self)
        self.proof_of_authorization_requests = resources.ProofOfAuthorizationRequestsResource(self)
        self.proof_of_authorization_request_submissions = resources.ProofOfAuthorizationRequestSubmissionsResource(self)
        self.account_statements = resources.AccountStatementsResource(self)
        self.files = resources.FilesResource(self)
        self.documents = resources.DocumentsResource(self)
        self.exports = resources.ExportsResource(self)
        self.events = resources.EventsResource(self)
        self.event_subscriptions = resources.EventSubscriptionsResource(self)
        self.real_time_decisions = resources.RealTimeDecisionsResource(self)
        self.bookkeeping_accounts = resources.BookkeepingAccountsResource(self)
        self.bookkeeping_entry_sets = resources.BookkeepingEntrySetsResource(self)
        self.bookkeeping_entries = resources.BookkeepingEntriesResource(self)
        self.groups = resources.GroupsResource(self)
        self.oauth_connections = resources.OAuthConnectionsResource(self)
        self.oauth_tokens = resources.OAuthTokensResource(self)
        self.intrafi_account_enrollments = resources.IntrafiAccountEnrollmentsResource(self)
        self.intrafi_balances = resources.IntrafiBalancesResource(self)
        self.intrafi_exclusions = resources.IntrafiExclusionsResource(self)
        self.real_time_payments_request_for_payments = resources.RealTimePaymentsRequestForPaymentsResource(self)
        self.simulations = resources.SimulationsResource(self)
        self.webhooks = resources.Webhooks(self)
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
    accounts: resources.AsyncAccountsResource
    account_numbers: resources.AsyncAccountNumbersResource
    cards: resources.AsyncCardsResource
    card_payments: resources.AsyncCardPaymentsResource
    card_purchase_supplements: resources.AsyncCardPurchaseSupplementsResource
    card_disputes: resources.AsyncCardDisputesResource
    physical_cards: resources.AsyncPhysicalCardsResource
    digital_card_profiles: resources.AsyncDigitalCardProfilesResource
    physical_card_profiles: resources.AsyncPhysicalCardProfilesResource
    digital_wallet_tokens: resources.AsyncDigitalWalletTokensResource
    transactions: resources.AsyncTransactionsResource
    pending_transactions: resources.AsyncPendingTransactionsResource
    declined_transactions: resources.AsyncDeclinedTransactionsResource
    account_transfers: resources.AsyncAccountTransfersResource
    ach_transfers: resources.AsyncACHTransfersResource
    ach_prenotifications: resources.AsyncACHPrenotificationsResource
    inbound_ach_transfers: resources.AsyncInboundACHTransfersResource
    wire_transfers: resources.AsyncWireTransfersResource
    inbound_wire_transfers: resources.AsyncInboundWireTransfersResource
    wire_drawdown_requests: resources.AsyncWireDrawdownRequestsResource
    inbound_wire_drawdown_requests: resources.AsyncInboundWireDrawdownRequestsResource
    check_transfers: resources.AsyncCheckTransfersResource
    inbound_check_deposits: resources.AsyncInboundCheckDepositsResource
    real_time_payments_transfers: resources.AsyncRealTimePaymentsTransfersResource
    inbound_real_time_payments_transfers: resources.AsyncInboundRealTimePaymentsTransfersResource
    check_deposits: resources.AsyncCheckDepositsResource
    lockboxes: resources.AsyncLockboxesResource
    inbound_mail_items: resources.AsyncInboundMailItemsResource
    routing_numbers: resources.AsyncRoutingNumbersResource
    external_accounts: resources.AsyncExternalAccountsResource
    entities: resources.AsyncEntitiesResource
    supplemental_documents: resources.AsyncSupplementalDocumentsResource
    programs: resources.AsyncProgramsResource
    proof_of_authorization_requests: resources.AsyncProofOfAuthorizationRequestsResource
    proof_of_authorization_request_submissions: resources.AsyncProofOfAuthorizationRequestSubmissionsResource
    account_statements: resources.AsyncAccountStatementsResource
    files: resources.AsyncFilesResource
    documents: resources.AsyncDocumentsResource
    exports: resources.AsyncExportsResource
    events: resources.AsyncEventsResource
    event_subscriptions: resources.AsyncEventSubscriptionsResource
    real_time_decisions: resources.AsyncRealTimeDecisionsResource
    bookkeeping_accounts: resources.AsyncBookkeepingAccountsResource
    bookkeeping_entry_sets: resources.AsyncBookkeepingEntrySetsResource
    bookkeeping_entries: resources.AsyncBookkeepingEntriesResource
    groups: resources.AsyncGroupsResource
    oauth_connections: resources.AsyncOAuthConnectionsResource
    oauth_tokens: resources.AsyncOAuthTokensResource
    intrafi_account_enrollments: resources.AsyncIntrafiAccountEnrollmentsResource
    intrafi_balances: resources.AsyncIntrafiBalancesResource
    intrafi_exclusions: resources.AsyncIntrafiExclusionsResource
    real_time_payments_request_for_payments: resources.AsyncRealTimePaymentsRequestForPaymentsResource
    simulations: resources.AsyncSimulationsResource
    webhooks: resources.AsyncWebhooks
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
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

        self.accounts = resources.AsyncAccountsResource(self)
        self.account_numbers = resources.AsyncAccountNumbersResource(self)
        self.cards = resources.AsyncCardsResource(self)
        self.card_payments = resources.AsyncCardPaymentsResource(self)
        self.card_purchase_supplements = resources.AsyncCardPurchaseSupplementsResource(self)
        self.card_disputes = resources.AsyncCardDisputesResource(self)
        self.physical_cards = resources.AsyncPhysicalCardsResource(self)
        self.digital_card_profiles = resources.AsyncDigitalCardProfilesResource(self)
        self.physical_card_profiles = resources.AsyncPhysicalCardProfilesResource(self)
        self.digital_wallet_tokens = resources.AsyncDigitalWalletTokensResource(self)
        self.transactions = resources.AsyncTransactionsResource(self)
        self.pending_transactions = resources.AsyncPendingTransactionsResource(self)
        self.declined_transactions = resources.AsyncDeclinedTransactionsResource(self)
        self.account_transfers = resources.AsyncAccountTransfersResource(self)
        self.ach_transfers = resources.AsyncACHTransfersResource(self)
        self.ach_prenotifications = resources.AsyncACHPrenotificationsResource(self)
        self.inbound_ach_transfers = resources.AsyncInboundACHTransfersResource(self)
        self.wire_transfers = resources.AsyncWireTransfersResource(self)
        self.inbound_wire_transfers = resources.AsyncInboundWireTransfersResource(self)
        self.wire_drawdown_requests = resources.AsyncWireDrawdownRequestsResource(self)
        self.inbound_wire_drawdown_requests = resources.AsyncInboundWireDrawdownRequestsResource(self)
        self.check_transfers = resources.AsyncCheckTransfersResource(self)
        self.inbound_check_deposits = resources.AsyncInboundCheckDepositsResource(self)
        self.real_time_payments_transfers = resources.AsyncRealTimePaymentsTransfersResource(self)
        self.inbound_real_time_payments_transfers = resources.AsyncInboundRealTimePaymentsTransfersResource(self)
        self.check_deposits = resources.AsyncCheckDepositsResource(self)
        self.lockboxes = resources.AsyncLockboxesResource(self)
        self.inbound_mail_items = resources.AsyncInboundMailItemsResource(self)
        self.routing_numbers = resources.AsyncRoutingNumbersResource(self)
        self.external_accounts = resources.AsyncExternalAccountsResource(self)
        self.entities = resources.AsyncEntitiesResource(self)
        self.supplemental_documents = resources.AsyncSupplementalDocumentsResource(self)
        self.programs = resources.AsyncProgramsResource(self)
        self.proof_of_authorization_requests = resources.AsyncProofOfAuthorizationRequestsResource(self)
        self.proof_of_authorization_request_submissions = resources.AsyncProofOfAuthorizationRequestSubmissionsResource(
            self
        )
        self.account_statements = resources.AsyncAccountStatementsResource(self)
        self.files = resources.AsyncFilesResource(self)
        self.documents = resources.AsyncDocumentsResource(self)
        self.exports = resources.AsyncExportsResource(self)
        self.events = resources.AsyncEventsResource(self)
        self.event_subscriptions = resources.AsyncEventSubscriptionsResource(self)
        self.real_time_decisions = resources.AsyncRealTimeDecisionsResource(self)
        self.bookkeeping_accounts = resources.AsyncBookkeepingAccountsResource(self)
        self.bookkeeping_entry_sets = resources.AsyncBookkeepingEntrySetsResource(self)
        self.bookkeeping_entries = resources.AsyncBookkeepingEntriesResource(self)
        self.groups = resources.AsyncGroupsResource(self)
        self.oauth_connections = resources.AsyncOAuthConnectionsResource(self)
        self.oauth_tokens = resources.AsyncOAuthTokensResource(self)
        self.intrafi_account_enrollments = resources.AsyncIntrafiAccountEnrollmentsResource(self)
        self.intrafi_balances = resources.AsyncIntrafiBalancesResource(self)
        self.intrafi_exclusions = resources.AsyncIntrafiExclusionsResource(self)
        self.real_time_payments_request_for_payments = resources.AsyncRealTimePaymentsRequestForPaymentsResource(self)
        self.simulations = resources.AsyncSimulationsResource(self)
        self.webhooks = resources.AsyncWebhooks(self)
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
        self.accounts = resources.AccountsResourceWithRawResponse(client.accounts)
        self.account_numbers = resources.AccountNumbersResourceWithRawResponse(client.account_numbers)
        self.cards = resources.CardsResourceWithRawResponse(client.cards)
        self.card_payments = resources.CardPaymentsResourceWithRawResponse(client.card_payments)
        self.card_purchase_supplements = resources.CardPurchaseSupplementsResourceWithRawResponse(
            client.card_purchase_supplements
        )
        self.card_disputes = resources.CardDisputesResourceWithRawResponse(client.card_disputes)
        self.physical_cards = resources.PhysicalCardsResourceWithRawResponse(client.physical_cards)
        self.digital_card_profiles = resources.DigitalCardProfilesResourceWithRawResponse(client.digital_card_profiles)
        self.physical_card_profiles = resources.PhysicalCardProfilesResourceWithRawResponse(
            client.physical_card_profiles
        )
        self.digital_wallet_tokens = resources.DigitalWalletTokensResourceWithRawResponse(client.digital_wallet_tokens)
        self.transactions = resources.TransactionsResourceWithRawResponse(client.transactions)
        self.pending_transactions = resources.PendingTransactionsResourceWithRawResponse(client.pending_transactions)
        self.declined_transactions = resources.DeclinedTransactionsResourceWithRawResponse(client.declined_transactions)
        self.account_transfers = resources.AccountTransfersResourceWithRawResponse(client.account_transfers)
        self.ach_transfers = resources.ACHTransfersResourceWithRawResponse(client.ach_transfers)
        self.ach_prenotifications = resources.ACHPrenotificationsResourceWithRawResponse(client.ach_prenotifications)
        self.inbound_ach_transfers = resources.InboundACHTransfersResourceWithRawResponse(client.inbound_ach_transfers)
        self.wire_transfers = resources.WireTransfersResourceWithRawResponse(client.wire_transfers)
        self.inbound_wire_transfers = resources.InboundWireTransfersResourceWithRawResponse(
            client.inbound_wire_transfers
        )
        self.wire_drawdown_requests = resources.WireDrawdownRequestsResourceWithRawResponse(
            client.wire_drawdown_requests
        )
        self.inbound_wire_drawdown_requests = resources.InboundWireDrawdownRequestsResourceWithRawResponse(
            client.inbound_wire_drawdown_requests
        )
        self.check_transfers = resources.CheckTransfersResourceWithRawResponse(client.check_transfers)
        self.inbound_check_deposits = resources.InboundCheckDepositsResourceWithRawResponse(
            client.inbound_check_deposits
        )
        self.real_time_payments_transfers = resources.RealTimePaymentsTransfersResourceWithRawResponse(
            client.real_time_payments_transfers
        )
        self.inbound_real_time_payments_transfers = resources.InboundRealTimePaymentsTransfersResourceWithRawResponse(
            client.inbound_real_time_payments_transfers
        )
        self.check_deposits = resources.CheckDepositsResourceWithRawResponse(client.check_deposits)
        self.lockboxes = resources.LockboxesResourceWithRawResponse(client.lockboxes)
        self.inbound_mail_items = resources.InboundMailItemsResourceWithRawResponse(client.inbound_mail_items)
        self.routing_numbers = resources.RoutingNumbersResourceWithRawResponse(client.routing_numbers)
        self.external_accounts = resources.ExternalAccountsResourceWithRawResponse(client.external_accounts)
        self.entities = resources.EntitiesResourceWithRawResponse(client.entities)
        self.supplemental_documents = resources.SupplementalDocumentsResourceWithRawResponse(
            client.supplemental_documents
        )
        self.programs = resources.ProgramsResourceWithRawResponse(client.programs)
        self.proof_of_authorization_requests = resources.ProofOfAuthorizationRequestsResourceWithRawResponse(
            client.proof_of_authorization_requests
        )
        self.proof_of_authorization_request_submissions = (
            resources.ProofOfAuthorizationRequestSubmissionsResourceWithRawResponse(
                client.proof_of_authorization_request_submissions
            )
        )
        self.account_statements = resources.AccountStatementsResourceWithRawResponse(client.account_statements)
        self.files = resources.FilesResourceWithRawResponse(client.files)
        self.documents = resources.DocumentsResourceWithRawResponse(client.documents)
        self.exports = resources.ExportsResourceWithRawResponse(client.exports)
        self.events = resources.EventsResourceWithRawResponse(client.events)
        self.event_subscriptions = resources.EventSubscriptionsResourceWithRawResponse(client.event_subscriptions)
        self.real_time_decisions = resources.RealTimeDecisionsResourceWithRawResponse(client.real_time_decisions)
        self.bookkeeping_accounts = resources.BookkeepingAccountsResourceWithRawResponse(client.bookkeeping_accounts)
        self.bookkeeping_entry_sets = resources.BookkeepingEntrySetsResourceWithRawResponse(
            client.bookkeeping_entry_sets
        )
        self.bookkeeping_entries = resources.BookkeepingEntriesResourceWithRawResponse(client.bookkeeping_entries)
        self.groups = resources.GroupsResourceWithRawResponse(client.groups)
        self.oauth_connections = resources.OAuthConnectionsResourceWithRawResponse(client.oauth_connections)
        self.oauth_tokens = resources.OAuthTokensResourceWithRawResponse(client.oauth_tokens)
        self.intrafi_account_enrollments = resources.IntrafiAccountEnrollmentsResourceWithRawResponse(
            client.intrafi_account_enrollments
        )
        self.intrafi_balances = resources.IntrafiBalancesResourceWithRawResponse(client.intrafi_balances)
        self.intrafi_exclusions = resources.IntrafiExclusionsResourceWithRawResponse(client.intrafi_exclusions)
        self.real_time_payments_request_for_payments = (
            resources.RealTimePaymentsRequestForPaymentsResourceWithRawResponse(
                client.real_time_payments_request_for_payments
            )
        )
        self.simulations = resources.SimulationsResourceWithRawResponse(client.simulations)


class AsyncIncreaseWithRawResponse:
    def __init__(self, client: AsyncIncrease) -> None:
        self.accounts = resources.AsyncAccountsResourceWithRawResponse(client.accounts)
        self.account_numbers = resources.AsyncAccountNumbersResourceWithRawResponse(client.account_numbers)
        self.cards = resources.AsyncCardsResourceWithRawResponse(client.cards)
        self.card_payments = resources.AsyncCardPaymentsResourceWithRawResponse(client.card_payments)
        self.card_purchase_supplements = resources.AsyncCardPurchaseSupplementsResourceWithRawResponse(
            client.card_purchase_supplements
        )
        self.card_disputes = resources.AsyncCardDisputesResourceWithRawResponse(client.card_disputes)
        self.physical_cards = resources.AsyncPhysicalCardsResourceWithRawResponse(client.physical_cards)
        self.digital_card_profiles = resources.AsyncDigitalCardProfilesResourceWithRawResponse(
            client.digital_card_profiles
        )
        self.physical_card_profiles = resources.AsyncPhysicalCardProfilesResourceWithRawResponse(
            client.physical_card_profiles
        )
        self.digital_wallet_tokens = resources.AsyncDigitalWalletTokensResourceWithRawResponse(
            client.digital_wallet_tokens
        )
        self.transactions = resources.AsyncTransactionsResourceWithRawResponse(client.transactions)
        self.pending_transactions = resources.AsyncPendingTransactionsResourceWithRawResponse(
            client.pending_transactions
        )
        self.declined_transactions = resources.AsyncDeclinedTransactionsResourceWithRawResponse(
            client.declined_transactions
        )
        self.account_transfers = resources.AsyncAccountTransfersResourceWithRawResponse(client.account_transfers)
        self.ach_transfers = resources.AsyncACHTransfersResourceWithRawResponse(client.ach_transfers)
        self.ach_prenotifications = resources.AsyncACHPrenotificationsResourceWithRawResponse(
            client.ach_prenotifications
        )
        self.inbound_ach_transfers = resources.AsyncInboundACHTransfersResourceWithRawResponse(
            client.inbound_ach_transfers
        )
        self.wire_transfers = resources.AsyncWireTransfersResourceWithRawResponse(client.wire_transfers)
        self.inbound_wire_transfers = resources.AsyncInboundWireTransfersResourceWithRawResponse(
            client.inbound_wire_transfers
        )
        self.wire_drawdown_requests = resources.AsyncWireDrawdownRequestsResourceWithRawResponse(
            client.wire_drawdown_requests
        )
        self.inbound_wire_drawdown_requests = resources.AsyncInboundWireDrawdownRequestsResourceWithRawResponse(
            client.inbound_wire_drawdown_requests
        )
        self.check_transfers = resources.AsyncCheckTransfersResourceWithRawResponse(client.check_transfers)
        self.inbound_check_deposits = resources.AsyncInboundCheckDepositsResourceWithRawResponse(
            client.inbound_check_deposits
        )
        self.real_time_payments_transfers = resources.AsyncRealTimePaymentsTransfersResourceWithRawResponse(
            client.real_time_payments_transfers
        )
        self.inbound_real_time_payments_transfers = (
            resources.AsyncInboundRealTimePaymentsTransfersResourceWithRawResponse(
                client.inbound_real_time_payments_transfers
            )
        )
        self.check_deposits = resources.AsyncCheckDepositsResourceWithRawResponse(client.check_deposits)
        self.lockboxes = resources.AsyncLockboxesResourceWithRawResponse(client.lockboxes)
        self.inbound_mail_items = resources.AsyncInboundMailItemsResourceWithRawResponse(client.inbound_mail_items)
        self.routing_numbers = resources.AsyncRoutingNumbersResourceWithRawResponse(client.routing_numbers)
        self.external_accounts = resources.AsyncExternalAccountsResourceWithRawResponse(client.external_accounts)
        self.entities = resources.AsyncEntitiesResourceWithRawResponse(client.entities)
        self.supplemental_documents = resources.AsyncSupplementalDocumentsResourceWithRawResponse(
            client.supplemental_documents
        )
        self.programs = resources.AsyncProgramsResourceWithRawResponse(client.programs)
        self.proof_of_authorization_requests = resources.AsyncProofOfAuthorizationRequestsResourceWithRawResponse(
            client.proof_of_authorization_requests
        )
        self.proof_of_authorization_request_submissions = (
            resources.AsyncProofOfAuthorizationRequestSubmissionsResourceWithRawResponse(
                client.proof_of_authorization_request_submissions
            )
        )
        self.account_statements = resources.AsyncAccountStatementsResourceWithRawResponse(client.account_statements)
        self.files = resources.AsyncFilesResourceWithRawResponse(client.files)
        self.documents = resources.AsyncDocumentsResourceWithRawResponse(client.documents)
        self.exports = resources.AsyncExportsResourceWithRawResponse(client.exports)
        self.events = resources.AsyncEventsResourceWithRawResponse(client.events)
        self.event_subscriptions = resources.AsyncEventSubscriptionsResourceWithRawResponse(client.event_subscriptions)
        self.real_time_decisions = resources.AsyncRealTimeDecisionsResourceWithRawResponse(client.real_time_decisions)
        self.bookkeeping_accounts = resources.AsyncBookkeepingAccountsResourceWithRawResponse(
            client.bookkeeping_accounts
        )
        self.bookkeeping_entry_sets = resources.AsyncBookkeepingEntrySetsResourceWithRawResponse(
            client.bookkeeping_entry_sets
        )
        self.bookkeeping_entries = resources.AsyncBookkeepingEntriesResourceWithRawResponse(client.bookkeeping_entries)
        self.groups = resources.AsyncGroupsResourceWithRawResponse(client.groups)
        self.oauth_connections = resources.AsyncOAuthConnectionsResourceWithRawResponse(client.oauth_connections)
        self.oauth_tokens = resources.AsyncOAuthTokensResourceWithRawResponse(client.oauth_tokens)
        self.intrafi_account_enrollments = resources.AsyncIntrafiAccountEnrollmentsResourceWithRawResponse(
            client.intrafi_account_enrollments
        )
        self.intrafi_balances = resources.AsyncIntrafiBalancesResourceWithRawResponse(client.intrafi_balances)
        self.intrafi_exclusions = resources.AsyncIntrafiExclusionsResourceWithRawResponse(client.intrafi_exclusions)
        self.real_time_payments_request_for_payments = (
            resources.AsyncRealTimePaymentsRequestForPaymentsResourceWithRawResponse(
                client.real_time_payments_request_for_payments
            )
        )
        self.simulations = resources.AsyncSimulationsResourceWithRawResponse(client.simulations)


class IncreaseWithStreamedResponse:
    def __init__(self, client: Increase) -> None:
        self.accounts = resources.AccountsResourceWithStreamingResponse(client.accounts)
        self.account_numbers = resources.AccountNumbersResourceWithStreamingResponse(client.account_numbers)
        self.cards = resources.CardsResourceWithStreamingResponse(client.cards)
        self.card_payments = resources.CardPaymentsResourceWithStreamingResponse(client.card_payments)
        self.card_purchase_supplements = resources.CardPurchaseSupplementsResourceWithStreamingResponse(
            client.card_purchase_supplements
        )
        self.card_disputes = resources.CardDisputesResourceWithStreamingResponse(client.card_disputes)
        self.physical_cards = resources.PhysicalCardsResourceWithStreamingResponse(client.physical_cards)
        self.digital_card_profiles = resources.DigitalCardProfilesResourceWithStreamingResponse(
            client.digital_card_profiles
        )
        self.physical_card_profiles = resources.PhysicalCardProfilesResourceWithStreamingResponse(
            client.physical_card_profiles
        )
        self.digital_wallet_tokens = resources.DigitalWalletTokensResourceWithStreamingResponse(
            client.digital_wallet_tokens
        )
        self.transactions = resources.TransactionsResourceWithStreamingResponse(client.transactions)
        self.pending_transactions = resources.PendingTransactionsResourceWithStreamingResponse(
            client.pending_transactions
        )
        self.declined_transactions = resources.DeclinedTransactionsResourceWithStreamingResponse(
            client.declined_transactions
        )
        self.account_transfers = resources.AccountTransfersResourceWithStreamingResponse(client.account_transfers)
        self.ach_transfers = resources.ACHTransfersResourceWithStreamingResponse(client.ach_transfers)
        self.ach_prenotifications = resources.ACHPrenotificationsResourceWithStreamingResponse(
            client.ach_prenotifications
        )
        self.inbound_ach_transfers = resources.InboundACHTransfersResourceWithStreamingResponse(
            client.inbound_ach_transfers
        )
        self.wire_transfers = resources.WireTransfersResourceWithStreamingResponse(client.wire_transfers)
        self.inbound_wire_transfers = resources.InboundWireTransfersResourceWithStreamingResponse(
            client.inbound_wire_transfers
        )
        self.wire_drawdown_requests = resources.WireDrawdownRequestsResourceWithStreamingResponse(
            client.wire_drawdown_requests
        )
        self.inbound_wire_drawdown_requests = resources.InboundWireDrawdownRequestsResourceWithStreamingResponse(
            client.inbound_wire_drawdown_requests
        )
        self.check_transfers = resources.CheckTransfersResourceWithStreamingResponse(client.check_transfers)
        self.inbound_check_deposits = resources.InboundCheckDepositsResourceWithStreamingResponse(
            client.inbound_check_deposits
        )
        self.real_time_payments_transfers = resources.RealTimePaymentsTransfersResourceWithStreamingResponse(
            client.real_time_payments_transfers
        )
        self.inbound_real_time_payments_transfers = (
            resources.InboundRealTimePaymentsTransfersResourceWithStreamingResponse(
                client.inbound_real_time_payments_transfers
            )
        )
        self.check_deposits = resources.CheckDepositsResourceWithStreamingResponse(client.check_deposits)
        self.lockboxes = resources.LockboxesResourceWithStreamingResponse(client.lockboxes)
        self.inbound_mail_items = resources.InboundMailItemsResourceWithStreamingResponse(client.inbound_mail_items)
        self.routing_numbers = resources.RoutingNumbersResourceWithStreamingResponse(client.routing_numbers)
        self.external_accounts = resources.ExternalAccountsResourceWithStreamingResponse(client.external_accounts)
        self.entities = resources.EntitiesResourceWithStreamingResponse(client.entities)
        self.supplemental_documents = resources.SupplementalDocumentsResourceWithStreamingResponse(
            client.supplemental_documents
        )
        self.programs = resources.ProgramsResourceWithStreamingResponse(client.programs)
        self.proof_of_authorization_requests = resources.ProofOfAuthorizationRequestsResourceWithStreamingResponse(
            client.proof_of_authorization_requests
        )
        self.proof_of_authorization_request_submissions = (
            resources.ProofOfAuthorizationRequestSubmissionsResourceWithStreamingResponse(
                client.proof_of_authorization_request_submissions
            )
        )
        self.account_statements = resources.AccountStatementsResourceWithStreamingResponse(client.account_statements)
        self.files = resources.FilesResourceWithStreamingResponse(client.files)
        self.documents = resources.DocumentsResourceWithStreamingResponse(client.documents)
        self.exports = resources.ExportsResourceWithStreamingResponse(client.exports)
        self.events = resources.EventsResourceWithStreamingResponse(client.events)
        self.event_subscriptions = resources.EventSubscriptionsResourceWithStreamingResponse(client.event_subscriptions)
        self.real_time_decisions = resources.RealTimeDecisionsResourceWithStreamingResponse(client.real_time_decisions)
        self.bookkeeping_accounts = resources.BookkeepingAccountsResourceWithStreamingResponse(
            client.bookkeeping_accounts
        )
        self.bookkeeping_entry_sets = resources.BookkeepingEntrySetsResourceWithStreamingResponse(
            client.bookkeeping_entry_sets
        )
        self.bookkeeping_entries = resources.BookkeepingEntriesResourceWithStreamingResponse(client.bookkeeping_entries)
        self.groups = resources.GroupsResourceWithStreamingResponse(client.groups)
        self.oauth_connections = resources.OAuthConnectionsResourceWithStreamingResponse(client.oauth_connections)
        self.oauth_tokens = resources.OAuthTokensResourceWithStreamingResponse(client.oauth_tokens)
        self.intrafi_account_enrollments = resources.IntrafiAccountEnrollmentsResourceWithStreamingResponse(
            client.intrafi_account_enrollments
        )
        self.intrafi_balances = resources.IntrafiBalancesResourceWithStreamingResponse(client.intrafi_balances)
        self.intrafi_exclusions = resources.IntrafiExclusionsResourceWithStreamingResponse(client.intrafi_exclusions)
        self.real_time_payments_request_for_payments = (
            resources.RealTimePaymentsRequestForPaymentsResourceWithStreamingResponse(
                client.real_time_payments_request_for_payments
            )
        )
        self.simulations = resources.SimulationsResourceWithStreamingResponse(client.simulations)


class AsyncIncreaseWithStreamedResponse:
    def __init__(self, client: AsyncIncrease) -> None:
        self.accounts = resources.AsyncAccountsResourceWithStreamingResponse(client.accounts)
        self.account_numbers = resources.AsyncAccountNumbersResourceWithStreamingResponse(client.account_numbers)
        self.cards = resources.AsyncCardsResourceWithStreamingResponse(client.cards)
        self.card_payments = resources.AsyncCardPaymentsResourceWithStreamingResponse(client.card_payments)
        self.card_purchase_supplements = resources.AsyncCardPurchaseSupplementsResourceWithStreamingResponse(
            client.card_purchase_supplements
        )
        self.card_disputes = resources.AsyncCardDisputesResourceWithStreamingResponse(client.card_disputes)
        self.physical_cards = resources.AsyncPhysicalCardsResourceWithStreamingResponse(client.physical_cards)
        self.digital_card_profiles = resources.AsyncDigitalCardProfilesResourceWithStreamingResponse(
            client.digital_card_profiles
        )
        self.physical_card_profiles = resources.AsyncPhysicalCardProfilesResourceWithStreamingResponse(
            client.physical_card_profiles
        )
        self.digital_wallet_tokens = resources.AsyncDigitalWalletTokensResourceWithStreamingResponse(
            client.digital_wallet_tokens
        )
        self.transactions = resources.AsyncTransactionsResourceWithStreamingResponse(client.transactions)
        self.pending_transactions = resources.AsyncPendingTransactionsResourceWithStreamingResponse(
            client.pending_transactions
        )
        self.declined_transactions = resources.AsyncDeclinedTransactionsResourceWithStreamingResponse(
            client.declined_transactions
        )
        self.account_transfers = resources.AsyncAccountTransfersResourceWithStreamingResponse(client.account_transfers)
        self.ach_transfers = resources.AsyncACHTransfersResourceWithStreamingResponse(client.ach_transfers)
        self.ach_prenotifications = resources.AsyncACHPrenotificationsResourceWithStreamingResponse(
            client.ach_prenotifications
        )
        self.inbound_ach_transfers = resources.AsyncInboundACHTransfersResourceWithStreamingResponse(
            client.inbound_ach_transfers
        )
        self.wire_transfers = resources.AsyncWireTransfersResourceWithStreamingResponse(client.wire_transfers)
        self.inbound_wire_transfers = resources.AsyncInboundWireTransfersResourceWithStreamingResponse(
            client.inbound_wire_transfers
        )
        self.wire_drawdown_requests = resources.AsyncWireDrawdownRequestsResourceWithStreamingResponse(
            client.wire_drawdown_requests
        )
        self.inbound_wire_drawdown_requests = resources.AsyncInboundWireDrawdownRequestsResourceWithStreamingResponse(
            client.inbound_wire_drawdown_requests
        )
        self.check_transfers = resources.AsyncCheckTransfersResourceWithStreamingResponse(client.check_transfers)
        self.inbound_check_deposits = resources.AsyncInboundCheckDepositsResourceWithStreamingResponse(
            client.inbound_check_deposits
        )
        self.real_time_payments_transfers = resources.AsyncRealTimePaymentsTransfersResourceWithStreamingResponse(
            client.real_time_payments_transfers
        )
        self.inbound_real_time_payments_transfers = (
            resources.AsyncInboundRealTimePaymentsTransfersResourceWithStreamingResponse(
                client.inbound_real_time_payments_transfers
            )
        )
        self.check_deposits = resources.AsyncCheckDepositsResourceWithStreamingResponse(client.check_deposits)
        self.lockboxes = resources.AsyncLockboxesResourceWithStreamingResponse(client.lockboxes)
        self.inbound_mail_items = resources.AsyncInboundMailItemsResourceWithStreamingResponse(
            client.inbound_mail_items
        )
        self.routing_numbers = resources.AsyncRoutingNumbersResourceWithStreamingResponse(client.routing_numbers)
        self.external_accounts = resources.AsyncExternalAccountsResourceWithStreamingResponse(client.external_accounts)
        self.entities = resources.AsyncEntitiesResourceWithStreamingResponse(client.entities)
        self.supplemental_documents = resources.AsyncSupplementalDocumentsResourceWithStreamingResponse(
            client.supplemental_documents
        )
        self.programs = resources.AsyncProgramsResourceWithStreamingResponse(client.programs)
        self.proof_of_authorization_requests = resources.AsyncProofOfAuthorizationRequestsResourceWithStreamingResponse(
            client.proof_of_authorization_requests
        )
        self.proof_of_authorization_request_submissions = (
            resources.AsyncProofOfAuthorizationRequestSubmissionsResourceWithStreamingResponse(
                client.proof_of_authorization_request_submissions
            )
        )
        self.account_statements = resources.AsyncAccountStatementsResourceWithStreamingResponse(
            client.account_statements
        )
        self.files = resources.AsyncFilesResourceWithStreamingResponse(client.files)
        self.documents = resources.AsyncDocumentsResourceWithStreamingResponse(client.documents)
        self.exports = resources.AsyncExportsResourceWithStreamingResponse(client.exports)
        self.events = resources.AsyncEventsResourceWithStreamingResponse(client.events)
        self.event_subscriptions = resources.AsyncEventSubscriptionsResourceWithStreamingResponse(
            client.event_subscriptions
        )
        self.real_time_decisions = resources.AsyncRealTimeDecisionsResourceWithStreamingResponse(
            client.real_time_decisions
        )
        self.bookkeeping_accounts = resources.AsyncBookkeepingAccountsResourceWithStreamingResponse(
            client.bookkeeping_accounts
        )
        self.bookkeeping_entry_sets = resources.AsyncBookkeepingEntrySetsResourceWithStreamingResponse(
            client.bookkeeping_entry_sets
        )
        self.bookkeeping_entries = resources.AsyncBookkeepingEntriesResourceWithStreamingResponse(
            client.bookkeeping_entries
        )
        self.groups = resources.AsyncGroupsResourceWithStreamingResponse(client.groups)
        self.oauth_connections = resources.AsyncOAuthConnectionsResourceWithStreamingResponse(client.oauth_connections)
        self.oauth_tokens = resources.AsyncOAuthTokensResourceWithStreamingResponse(client.oauth_tokens)
        self.intrafi_account_enrollments = resources.AsyncIntrafiAccountEnrollmentsResourceWithStreamingResponse(
            client.intrafi_account_enrollments
        )
        self.intrafi_balances = resources.AsyncIntrafiBalancesResourceWithStreamingResponse(client.intrafi_balances)
        self.intrafi_exclusions = resources.AsyncIntrafiExclusionsResourceWithStreamingResponse(
            client.intrafi_exclusions
        )
        self.real_time_payments_request_for_payments = (
            resources.AsyncRealTimePaymentsRequestForPaymentsResourceWithStreamingResponse(
                client.real_time_payments_request_for_payments
            )
        )
        self.simulations = resources.AsyncSimulationsResourceWithStreamingResponse(client.simulations)


Client = Increase

AsyncClient = AsyncIncrease
