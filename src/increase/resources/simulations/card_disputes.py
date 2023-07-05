# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from ...types import CardDispute
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.simulations import card_dispute_action_params

__all__ = ["CardDisputes", "AsyncCardDisputes"]


class CardDisputes(SyncAPIResource):
    def action(
        self,
        card_dispute_id: str,
        *,
        status: Literal["accepted", "rejected"],
        explanation: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardDispute:
        """
        After a [Card Dispute](#card-disputes) is created in production, the dispute
        will be reviewed. Since no review happens in sandbox, this endpoint simulates
        moving a Card Dispute into a rejected or accepted state. A Card Dispute can only
        be actioned one time and must have a status of `pending_reviewing`.

        Args:
          card_dispute_id: The dispute you would like to action.

          status: The status to move the dispute to.

              - `accepted` - The Card Dispute has been accepted and your funds have been
                returned.
              - `rejected` - The Card Dispute has been rejected.

          explanation: Why the dispute was rejected. Not required for accepting disputes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/simulations/card_disputes/{card_dispute_id}/action",
            body=maybe_transform(
                {
                    "status": status,
                    "explanation": explanation,
                },
                card_dispute_action_params.CardDisputeActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardDispute,
        )


class AsyncCardDisputes(AsyncAPIResource):
    async def action(
        self,
        card_dispute_id: str,
        *,
        status: Literal["accepted", "rejected"],
        explanation: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> CardDispute:
        """
        After a [Card Dispute](#card-disputes) is created in production, the dispute
        will be reviewed. Since no review happens in sandbox, this endpoint simulates
        moving a Card Dispute into a rejected or accepted state. A Card Dispute can only
        be actioned one time and must have a status of `pending_reviewing`.

        Args:
          card_dispute_id: The dispute you would like to action.

          status: The status to move the dispute to.

              - `accepted` - The Card Dispute has been accepted and your funds have been
                returned.
              - `rejected` - The Card Dispute has been rejected.

          explanation: Why the dispute was rejected. Not required for accepting disputes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/simulations/card_disputes/{card_dispute_id}/action",
            body=maybe_transform(
                {
                    "status": status,
                    "explanation": explanation,
                },
                card_dispute_action_params.CardDisputeActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardDispute,
        )
