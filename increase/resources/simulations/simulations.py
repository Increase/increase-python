# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal

from ..._utils import extract_files, maybe_transform, required_args, deprecated_positional_args, deepcopy_minimal
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, UnknownResponse, FileTypes
from ..._base_client import AsyncPaginator, make_request_options, strip_not_given
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import SyncAPIClient, AsyncAPIClient
from ...types import shared_params

from .account_transfers import AccountTransfers, AsyncAccountTransfers
from .account_statements import AccountStatements, AsyncAccountStatements
from .ach_transfers import ACHTransfers, AsyncACHTransfers
from .check_transfers import CheckTransfers, AsyncCheckTransfers
from .digital_wallet_token_requests import DigitalWalletTokenRequests, AsyncDigitalWalletTokenRequests
from .check_deposits import CheckDeposits, AsyncCheckDeposits
from .wire_transfers import WireTransfers, AsyncWireTransfers
from .cards import Cards, AsyncCards
from .real_time_payments_transfers import RealTimePaymentsTransfers, AsyncRealTimePaymentsTransfers
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from ..._client import AsyncIncrease, Increase

__all__ = ["Simulations", "AsyncSimulations"]

class Simulations(SyncAPIResource):
    account_transfers: AccountTransfers
    account_statements: AccountStatements
    ach_transfers: ACHTransfers
    check_transfers: CheckTransfers
    digital_wallet_token_requests: DigitalWalletTokenRequests
    check_deposits: CheckDeposits
    wire_transfers: WireTransfers
    cards: Cards
    real_time_payments_transfers: RealTimePaymentsTransfers

    def __init__(self, client: Increase) -> None:
        super().__init__(client)
        self.account_transfers = AccountTransfers(client)
        self.account_statements = AccountStatements(client)
        self.ach_transfers = ACHTransfers(client)
        self.check_transfers = CheckTransfers(client)
        self.digital_wallet_token_requests = DigitalWalletTokenRequests(client)
        self.check_deposits = CheckDeposits(client)
        self.wire_transfers = WireTransfers(client)
        self.cards = Cards(client)
        self.real_time_payments_transfers = RealTimePaymentsTransfers(client)

class AsyncSimulations(AsyncAPIResource):
    account_transfers: AsyncAccountTransfers
    account_statements: AsyncAccountStatements
    ach_transfers: AsyncACHTransfers
    check_transfers: AsyncCheckTransfers
    digital_wallet_token_requests: AsyncDigitalWalletTokenRequests
    check_deposits: AsyncCheckDeposits
    wire_transfers: AsyncWireTransfers
    cards: AsyncCards
    real_time_payments_transfers: AsyncRealTimePaymentsTransfers

    def __init__(self, client: AsyncIncrease) -> None:
        super().__init__(client)
        self.account_transfers = AsyncAccountTransfers(client)
        self.account_statements = AsyncAccountStatements(client)
        self.ach_transfers = AsyncACHTransfers(client)
        self.check_transfers = AsyncCheckTransfers(client)
        self.digital_wallet_token_requests = AsyncDigitalWalletTokenRequests(client)
        self.check_deposits = AsyncCheckDeposits(client)
        self.wire_transfers = AsyncWireTransfers(client)
        self.cards = AsyncCards(client)
        self.real_time_payments_transfers = AsyncRealTimePaymentsTransfers(client)