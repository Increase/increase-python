# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from ..._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations.transaction import Transaction
from ...types.simulations.card_authorize_params import CardAuthorizeParams
from ...types.simulations.card_settlement_params import CardSettlementParams
from ...types.simulations.card_authorization_simulation import (
    CardAuthorizationSimulation,
)

__all__ = ["Cards", "AsyncCards"]


class Cards(SyncAPIResource):
    def authorize(
        self,
        body: CardAuthorizeParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CardAuthorizationSimulation:
        """Simulates activity on a Card."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/simulations/card_authorizations",
            body=maybe_transform(body, CardAuthorizeParams),
            options=options,
            cast_to=CardAuthorizationSimulation,
        )

    def settlement(
        self,
        body: CardSettlementParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Transaction:
        """Simulates the settlement of an authorization by a card acquirer."""
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/simulations/card_settlements",
            body=maybe_transform(body, CardSettlementParams),
            options=options,
            cast_to=Transaction,
        )


class AsyncCards(AsyncAPIResource):
    async def authorize(
        self,
        body: CardAuthorizeParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> CardAuthorizationSimulation:
        """Simulates activity on a Card."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/simulations/card_authorizations",
            body=maybe_transform(body, CardAuthorizeParams),
            options=options,
            cast_to=CardAuthorizationSimulation,
        )

    async def settlement(
        self,
        body: CardSettlementParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Transaction:
        """Simulates the settlement of an authorization by a card acquirer."""
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/simulations/card_settlements",
            body=maybe_transform(body, CardSettlementParams),
            options=options,
            cast_to=Transaction,
        )
