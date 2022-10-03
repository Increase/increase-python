# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.event_subscription import EventSubscription
from ..types.event_subscription_list_params import EventSubscriptionListParams
from ..types.event_subscription_create_params import EventSubscriptionCreateParams
from ..types.event_subscription_update_params import EventSubscriptionUpdateParams

__all__ = ["EventSubscriptions", "AsyncEventSubscriptions"]


class EventSubscriptions(SyncAPIResource):
    def create(
        self,
        body: EventSubscriptionCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> EventSubscription:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/event_subscriptions",
            body=maybe_transform(body, EventSubscriptionCreateParams),
            options=options,
            cast_to=EventSubscription,
        )

    def retrieve(
        self,
        event_subscription_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> EventSubscription:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/event_subscriptions/{event_subscription_id}",
            options=options,
            cast_to=EventSubscription,
        )

    def update(
        self,
        event_subscription_id: str,
        body: EventSubscriptionUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> EventSubscription:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._patch(
            f"/event_subscriptions/{event_subscription_id}",
            body=maybe_transform(body, EventSubscriptionUpdateParams),
            options=options,
            cast_to=EventSubscription,
        )

    def list(
        self,
        query: EventSubscriptionListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[EventSubscription]:
        options = make_request_options(
            headers, max_retries, timeout, maybe_transform(query, EventSubscriptionListParams)
        )
        return self._get_api_list(
            "/event_subscriptions",
            page=SyncPage[EventSubscription],
            options=options,
            model=EventSubscription,
        )


class AsyncEventSubscriptions(AsyncAPIResource):
    async def create(
        self,
        body: EventSubscriptionCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> EventSubscription:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/event_subscriptions",
            body=maybe_transform(body, EventSubscriptionCreateParams),
            options=options,
            cast_to=EventSubscription,
        )

    async def retrieve(
        self,
        event_subscription_id: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> EventSubscription:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/event_subscriptions/{event_subscription_id}",
            options=options,
            cast_to=EventSubscription,
        )

    async def update(
        self,
        event_subscription_id: str,
        body: EventSubscriptionUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> EventSubscription:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._patch(
            f"/event_subscriptions/{event_subscription_id}",
            body=maybe_transform(body, EventSubscriptionUpdateParams),
            options=options,
            cast_to=EventSubscription,
        )

    def list(
        self,
        query: EventSubscriptionListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[EventSubscription, AsyncPage[EventSubscription]]:
        options = make_request_options(
            headers, max_retries, timeout, maybe_transform(query, EventSubscriptionListParams)
        )
        return self._get_api_list(
            "/event_subscriptions",
            page=AsyncPage[EventSubscription],
            options=options,
            model=EventSubscription,
        )
