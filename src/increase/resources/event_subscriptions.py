# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import event_subscription_list_params, event_subscription_create_params, event_subscription_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.event_subscription import EventSubscription

__all__ = ["EventSubscriptionsResource", "AsyncEventSubscriptionsResource"]


class EventSubscriptionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return EventSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return EventSubscriptionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        url: str,
        oauth_connection_id: str | NotGiven = NOT_GIVEN,
        selected_event_category: Literal[
            "account.created",
            "account.updated",
            "account_number.created",
            "account_number.updated",
            "account_statement.created",
            "account_transfer.created",
            "account_transfer.updated",
            "ach_prenotification.created",
            "ach_prenotification.updated",
            "ach_transfer.created",
            "ach_transfer.updated",
            "bookkeeping_account.created",
            "bookkeeping_account.updated",
            "bookkeeping_entry_set.updated",
            "card.created",
            "card.updated",
            "card_payment.created",
            "card_payment.updated",
            "card_profile.created",
            "card_profile.updated",
            "card_dispute.created",
            "card_dispute.updated",
            "check_deposit.created",
            "check_deposit.updated",
            "check_transfer.created",
            "check_transfer.updated",
            "declined_transaction.created",
            "digital_card_profile.created",
            "digital_card_profile.updated",
            "digital_wallet_token.created",
            "digital_wallet_token.updated",
            "document.created",
            "entity.created",
            "entity.updated",
            "event_subscription.created",
            "event_subscription.updated",
            "export.created",
            "export.updated",
            "external_account.created",
            "external_account.updated",
            "file.created",
            "group.updated",
            "group.heartbeat",
            "inbound_ach_transfer.created",
            "inbound_ach_transfer.updated",
            "inbound_ach_transfer_return.created",
            "inbound_ach_transfer_return.updated",
            "inbound_check_deposit.created",
            "inbound_check_deposit.updated",
            "inbound_mail_item.created",
            "inbound_mail_item.updated",
            "inbound_real_time_payments_transfer.created",
            "inbound_real_time_payments_transfer.updated",
            "inbound_wire_drawdown_request.created",
            "inbound_wire_transfer.created",
            "inbound_wire_transfer.updated",
            "intrafi_account_enrollment.created",
            "intrafi_account_enrollment.updated",
            "intrafi_exclusion.created",
            "intrafi_exclusion.updated",
            "legacy_card_dispute.created",
            "legacy_card_dispute.updated",
            "lockbox.created",
            "lockbox.updated",
            "oauth_connection.created",
            "oauth_connection.deactivated",
            "outbound_card_push_transfer.created",
            "outbound_card_push_transfer.updated",
            "outbound_card_validation.created",
            "outbound_card_validation.updated",
            "card_push_transfer.created",
            "card_push_transfer.updated",
            "card_validation.created",
            "card_validation.updated",
            "pending_transaction.created",
            "pending_transaction.updated",
            "physical_card.created",
            "physical_card.updated",
            "physical_card_profile.created",
            "physical_card_profile.updated",
            "program.created",
            "program.updated",
            "proof_of_authorization_request.created",
            "proof_of_authorization_request.updated",
            "real_time_decision.card_authorization_requested",
            "real_time_decision.digital_wallet_token_requested",
            "real_time_decision.digital_wallet_authentication_requested",
            "real_time_decision.card_authentication_requested",
            "real_time_decision.card_authentication_challenge_requested",
            "real_time_payments_transfer.created",
            "real_time_payments_transfer.updated",
            "real_time_payments_request_for_payment.created",
            "real_time_payments_request_for_payment.updated",
            "swift_transfer.created",
            "swift_transfer.updated",
            "transaction.created",
            "wire_drawdown_request.created",
            "wire_drawdown_request.updated",
            "wire_transfer.created",
            "wire_transfer.updated",
        ]
        | NotGiven = NOT_GIVEN,
        shared_secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> EventSubscription:
        """
        Create an Event Subscription

        Args:
          url: The URL you'd like us to send webhooks to.

          oauth_connection_id: If specified, this subscription will only receive webhooks for Events associated
              with the specified OAuth Connection.

          selected_event_category: If specified, this subscription will only receive webhooks for Events with the
              specified `category`.

              - `account.created` - Occurs whenever an Account is created.
              - `account.updated` - Occurs whenever an Account is updated.
              - `account_number.created` - Occurs whenever an Account Number is created.
              - `account_number.updated` - Occurs whenever an Account Number is updated.
              - `account_statement.created` - Occurs whenever an Account Statement is created.
              - `account_transfer.created` - Occurs whenever an Account Transfer is created.
              - `account_transfer.updated` - Occurs whenever an Account Transfer is updated.
              - `ach_prenotification.created` - Occurs whenever an ACH Prenotification is
                created.
              - `ach_prenotification.updated` - Occurs whenever an ACH Prenotification is
                updated.
              - `ach_transfer.created` - Occurs whenever an ACH Transfer is created.
              - `ach_transfer.updated` - Occurs whenever an ACH Transfer is updated.
              - `bookkeeping_account.created` - Occurs whenever a Bookkeeping Account is
                created.
              - `bookkeeping_account.updated` - Occurs whenever a Bookkeeping Account is
                updated.
              - `bookkeeping_entry_set.updated` - Occurs whenever a Bookkeeping Entry Set is
                created.
              - `card.created` - Occurs whenever a Card is created.
              - `card.updated` - Occurs whenever a Card is updated.
              - `card_payment.created` - Occurs whenever a Card Payment is created.
              - `card_payment.updated` - Occurs whenever a Card Payment is updated.
              - `card_profile.created` - Occurs whenever a Card Profile is created.
              - `card_profile.updated` - Occurs whenever a Card Profile is updated.
              - `card_dispute.created` - Occurs whenever a Card Dispute is created.
              - `card_dispute.updated` - Occurs whenever a Card Dispute is updated.
              - `check_deposit.created` - Occurs whenever a Check Deposit is created.
              - `check_deposit.updated` - Occurs whenever a Check Deposit is updated.
              - `check_transfer.created` - Occurs whenever a Check Transfer is created.
              - `check_transfer.updated` - Occurs whenever a Check Transfer is updated.
              - `declined_transaction.created` - Occurs whenever a Declined Transaction is
                created.
              - `digital_card_profile.created` - Occurs whenever a Digital Card Profile is
                created.
              - `digital_card_profile.updated` - Occurs whenever a Digital Card Profile is
                updated.
              - `digital_wallet_token.created` - Occurs whenever a Digital Wallet Token is
                created.
              - `digital_wallet_token.updated` - Occurs whenever a Digital Wallet Token is
                updated.
              - `document.created` - Occurs whenever a Document is created.
              - `entity.created` - Occurs whenever an Entity is created.
              - `entity.updated` - Occurs whenever an Entity is updated.
              - `event_subscription.created` - Occurs whenever an Event Subscription is
                created.
              - `event_subscription.updated` - Occurs whenever an Event Subscription is
                updated.
              - `export.created` - Occurs whenever an Export is created.
              - `export.updated` - Occurs whenever an Export is updated.
              - `external_account.created` - Occurs whenever an External Account is created.
              - `external_account.updated` - Occurs whenever an External Account is updated.
              - `file.created` - Occurs whenever a File is created.
              - `group.updated` - Occurs whenever a Group is updated.
              - `group.heartbeat` - Increase may send webhooks with this category to see if a
                webhook endpoint is working properly.
              - `inbound_ach_transfer.created` - Occurs whenever an Inbound ACH Transfer is
                created.
              - `inbound_ach_transfer.updated` - Occurs whenever an Inbound ACH Transfer is
                updated.
              - `inbound_ach_transfer_return.created` - Occurs whenever an Inbound ACH
                Transfer Return is created.
              - `inbound_ach_transfer_return.updated` - Occurs whenever an Inbound ACH
                Transfer Return is updated.
              - `inbound_check_deposit.created` - Occurs whenever an Inbound Check Deposit is
                created.
              - `inbound_check_deposit.updated` - Occurs whenever an Inbound Check Deposit is
                updated.
              - `inbound_mail_item.created` - Occurs whenever an Inbound Mail Item is created.
              - `inbound_mail_item.updated` - Occurs whenever an Inbound Mail Item is updated.
              - `inbound_real_time_payments_transfer.created` - Occurs whenever an Inbound
                Real-Time Payments Transfer is created.
              - `inbound_real_time_payments_transfer.updated` - Occurs whenever an Inbound
                Real-Time Payments Transfer is updated.
              - `inbound_wire_drawdown_request.created` - Occurs whenever an Inbound Wire
                Drawdown Request is created.
              - `inbound_wire_transfer.created` - Occurs whenever an Inbound Wire Transfer is
                created.
              - `inbound_wire_transfer.updated` - Occurs whenever an Inbound Wire Transfer is
                updated.
              - `intrafi_account_enrollment.created` - Occurs whenever an IntraFi Account
                Enrollment is created.
              - `intrafi_account_enrollment.updated` - Occurs whenever an IntraFi Account
                Enrollment is updated.
              - `intrafi_exclusion.created` - Occurs whenever an IntraFi Exclusion is created.
              - `intrafi_exclusion.updated` - Occurs whenever an IntraFi Exclusion is updated.
              - `legacy_card_dispute.created` - Occurs whenever a Legacy Card Dispute is
                created.
              - `legacy_card_dispute.updated` - Occurs whenever a Legacy Card Dispute is
                updated.
              - `lockbox.created` - Occurs whenever a Lockbox is created.
              - `lockbox.updated` - Occurs whenever a Lockbox is updated.
              - `oauth_connection.created` - Occurs whenever an OAuth Connection is created.
              - `oauth_connection.deactivated` - Occurs whenever an OAuth Connection is
                deactivated.
              - `outbound_card_push_transfer.created` - Occurs whenever a Card Push Transfer
                is created.
              - `outbound_card_push_transfer.updated` - Occurs whenever a Card Push Transfer
                is updated.
              - `outbound_card_validation.created` - Occurs whenever a Card Validation is
                created.
              - `outbound_card_validation.updated` - Occurs whenever a Card Validation is
                updated.
              - `card_push_transfer.created` - Occurs whenever a Card Push Transfer is
                created.
              - `card_push_transfer.updated` - Occurs whenever a Card Push Transfer is
                updated.
              - `card_validation.created` - Occurs whenever a Card Validation is created.
              - `card_validation.updated` - Occurs whenever a Card Validation is updated.
              - `pending_transaction.created` - Occurs whenever a Pending Transaction is
                created.
              - `pending_transaction.updated` - Occurs whenever a Pending Transaction is
                updated.
              - `physical_card.created` - Occurs whenever a Physical Card is created.
              - `physical_card.updated` - Occurs whenever a Physical Card is updated.
              - `physical_card_profile.created` - Occurs whenever a Physical Card Profile is
                created.
              - `physical_card_profile.updated` - Occurs whenever a Physical Card Profile is
                updated.
              - `program.created` - Occurs whenever a Program is created.
              - `program.updated` - Occurs whenever a Program is updated.
              - `proof_of_authorization_request.created` - Occurs whenever a Proof of
                Authorization Request is created.
              - `proof_of_authorization_request.updated` - Occurs whenever a Proof of
                Authorization Request is updated.
              - `real_time_decision.card_authorization_requested` - Occurs whenever a
                Real-Time Decision is created in response to a card authorization.
              - `real_time_decision.digital_wallet_token_requested` - Occurs whenever a
                Real-Time Decision is created in response to a digital wallet provisioning
                attempt.
              - `real_time_decision.digital_wallet_authentication_requested` - Occurs whenever
                a Real-Time Decision is created in response to a digital wallet requiring
                two-factor authentication.
              - `real_time_decision.card_authentication_requested` - Occurs whenever a
                Real-Time Decision is created in response to 3DS authentication.
              - `real_time_decision.card_authentication_challenge_requested` - Occurs whenever
                a Real-Time Decision is created in response to 3DS authentication challenges.
              - `real_time_payments_transfer.created` - Occurs whenever a Real-Time Payments
                Transfer is created.
              - `real_time_payments_transfer.updated` - Occurs whenever a Real-Time Payments
                Transfer is updated.
              - `real_time_payments_request_for_payment.created` - Occurs whenever a Real-Time
                Payments Request for Payment is created.
              - `real_time_payments_request_for_payment.updated` - Occurs whenever a Real-Time
                Payments Request for Payment is updated.
              - `swift_transfer.created` - Occurs whenever a Swift Transfer is created.
              - `swift_transfer.updated` - Occurs whenever a Swift Transfer is updated.
              - `transaction.created` - Occurs whenever a Transaction is created.
              - `wire_drawdown_request.created` - Occurs whenever a Wire Drawdown Request is
                created.
              - `wire_drawdown_request.updated` - Occurs whenever a Wire Drawdown Request is
                updated.
              - `wire_transfer.created` - Occurs whenever a Wire Transfer is created.
              - `wire_transfer.updated` - Occurs whenever a Wire Transfer is updated.

          shared_secret: The key that will be used to sign webhooks. If no value is passed, a random
              string will be used as default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/event_subscriptions",
            body=maybe_transform(
                {
                    "url": url,
                    "oauth_connection_id": oauth_connection_id,
                    "selected_event_category": selected_event_category,
                    "shared_secret": shared_secret,
                },
                event_subscription_create_params.EventSubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EventSubscription,
        )

    def retrieve(
        self,
        event_subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventSubscription:
        """
        Retrieve an Event Subscription

        Args:
          event_subscription_id: The identifier of the Event Subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_id:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_id` but received {event_subscription_id!r}"
            )
        return self._get(
            f"/event_subscriptions/{event_subscription_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventSubscription,
        )

    def update(
        self,
        event_subscription_id: str,
        *,
        status: Literal["active", "disabled", "deleted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> EventSubscription:
        """
        Update an Event Subscription

        Args:
          event_subscription_id: The identifier of the Event Subscription.

          status: The status to update the Event Subscription with.

              - `active` - The subscription is active and Events will be delivered normally.
              - `disabled` - The subscription is temporarily disabled and Events will not be
                delivered.
              - `deleted` - The subscription is permanently disabled and Events will not be
                delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not event_subscription_id:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_id` but received {event_subscription_id!r}"
            )
        return self._patch(
            f"/event_subscriptions/{event_subscription_id}",
            body=maybe_transform({"status": status}, event_subscription_update_params.EventSubscriptionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EventSubscription,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[EventSubscription]:
        """
        List Event Subscriptions

        Args:
          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/event_subscriptions",
            page=SyncPage[EventSubscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    event_subscription_list_params.EventSubscriptionListParams,
                ),
            ),
            model=EventSubscription,
        )


class AsyncEventSubscriptionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Increase/increase-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Increase/increase-python#with_streaming_response
        """
        return AsyncEventSubscriptionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        url: str,
        oauth_connection_id: str | NotGiven = NOT_GIVEN,
        selected_event_category: Literal[
            "account.created",
            "account.updated",
            "account_number.created",
            "account_number.updated",
            "account_statement.created",
            "account_transfer.created",
            "account_transfer.updated",
            "ach_prenotification.created",
            "ach_prenotification.updated",
            "ach_transfer.created",
            "ach_transfer.updated",
            "bookkeeping_account.created",
            "bookkeeping_account.updated",
            "bookkeeping_entry_set.updated",
            "card.created",
            "card.updated",
            "card_payment.created",
            "card_payment.updated",
            "card_profile.created",
            "card_profile.updated",
            "card_dispute.created",
            "card_dispute.updated",
            "check_deposit.created",
            "check_deposit.updated",
            "check_transfer.created",
            "check_transfer.updated",
            "declined_transaction.created",
            "digital_card_profile.created",
            "digital_card_profile.updated",
            "digital_wallet_token.created",
            "digital_wallet_token.updated",
            "document.created",
            "entity.created",
            "entity.updated",
            "event_subscription.created",
            "event_subscription.updated",
            "export.created",
            "export.updated",
            "external_account.created",
            "external_account.updated",
            "file.created",
            "group.updated",
            "group.heartbeat",
            "inbound_ach_transfer.created",
            "inbound_ach_transfer.updated",
            "inbound_ach_transfer_return.created",
            "inbound_ach_transfer_return.updated",
            "inbound_check_deposit.created",
            "inbound_check_deposit.updated",
            "inbound_mail_item.created",
            "inbound_mail_item.updated",
            "inbound_real_time_payments_transfer.created",
            "inbound_real_time_payments_transfer.updated",
            "inbound_wire_drawdown_request.created",
            "inbound_wire_transfer.created",
            "inbound_wire_transfer.updated",
            "intrafi_account_enrollment.created",
            "intrafi_account_enrollment.updated",
            "intrafi_exclusion.created",
            "intrafi_exclusion.updated",
            "legacy_card_dispute.created",
            "legacy_card_dispute.updated",
            "lockbox.created",
            "lockbox.updated",
            "oauth_connection.created",
            "oauth_connection.deactivated",
            "outbound_card_push_transfer.created",
            "outbound_card_push_transfer.updated",
            "outbound_card_validation.created",
            "outbound_card_validation.updated",
            "card_push_transfer.created",
            "card_push_transfer.updated",
            "card_validation.created",
            "card_validation.updated",
            "pending_transaction.created",
            "pending_transaction.updated",
            "physical_card.created",
            "physical_card.updated",
            "physical_card_profile.created",
            "physical_card_profile.updated",
            "program.created",
            "program.updated",
            "proof_of_authorization_request.created",
            "proof_of_authorization_request.updated",
            "real_time_decision.card_authorization_requested",
            "real_time_decision.digital_wallet_token_requested",
            "real_time_decision.digital_wallet_authentication_requested",
            "real_time_decision.card_authentication_requested",
            "real_time_decision.card_authentication_challenge_requested",
            "real_time_payments_transfer.created",
            "real_time_payments_transfer.updated",
            "real_time_payments_request_for_payment.created",
            "real_time_payments_request_for_payment.updated",
            "swift_transfer.created",
            "swift_transfer.updated",
            "transaction.created",
            "wire_drawdown_request.created",
            "wire_drawdown_request.updated",
            "wire_transfer.created",
            "wire_transfer.updated",
        ]
        | NotGiven = NOT_GIVEN,
        shared_secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> EventSubscription:
        """
        Create an Event Subscription

        Args:
          url: The URL you'd like us to send webhooks to.

          oauth_connection_id: If specified, this subscription will only receive webhooks for Events associated
              with the specified OAuth Connection.

          selected_event_category: If specified, this subscription will only receive webhooks for Events with the
              specified `category`.

              - `account.created` - Occurs whenever an Account is created.
              - `account.updated` - Occurs whenever an Account is updated.
              - `account_number.created` - Occurs whenever an Account Number is created.
              - `account_number.updated` - Occurs whenever an Account Number is updated.
              - `account_statement.created` - Occurs whenever an Account Statement is created.
              - `account_transfer.created` - Occurs whenever an Account Transfer is created.
              - `account_transfer.updated` - Occurs whenever an Account Transfer is updated.
              - `ach_prenotification.created` - Occurs whenever an ACH Prenotification is
                created.
              - `ach_prenotification.updated` - Occurs whenever an ACH Prenotification is
                updated.
              - `ach_transfer.created` - Occurs whenever an ACH Transfer is created.
              - `ach_transfer.updated` - Occurs whenever an ACH Transfer is updated.
              - `bookkeeping_account.created` - Occurs whenever a Bookkeeping Account is
                created.
              - `bookkeeping_account.updated` - Occurs whenever a Bookkeeping Account is
                updated.
              - `bookkeeping_entry_set.updated` - Occurs whenever a Bookkeeping Entry Set is
                created.
              - `card.created` - Occurs whenever a Card is created.
              - `card.updated` - Occurs whenever a Card is updated.
              - `card_payment.created` - Occurs whenever a Card Payment is created.
              - `card_payment.updated` - Occurs whenever a Card Payment is updated.
              - `card_profile.created` - Occurs whenever a Card Profile is created.
              - `card_profile.updated` - Occurs whenever a Card Profile is updated.
              - `card_dispute.created` - Occurs whenever a Card Dispute is created.
              - `card_dispute.updated` - Occurs whenever a Card Dispute is updated.
              - `check_deposit.created` - Occurs whenever a Check Deposit is created.
              - `check_deposit.updated` - Occurs whenever a Check Deposit is updated.
              - `check_transfer.created` - Occurs whenever a Check Transfer is created.
              - `check_transfer.updated` - Occurs whenever a Check Transfer is updated.
              - `declined_transaction.created` - Occurs whenever a Declined Transaction is
                created.
              - `digital_card_profile.created` - Occurs whenever a Digital Card Profile is
                created.
              - `digital_card_profile.updated` - Occurs whenever a Digital Card Profile is
                updated.
              - `digital_wallet_token.created` - Occurs whenever a Digital Wallet Token is
                created.
              - `digital_wallet_token.updated` - Occurs whenever a Digital Wallet Token is
                updated.
              - `document.created` - Occurs whenever a Document is created.
              - `entity.created` - Occurs whenever an Entity is created.
              - `entity.updated` - Occurs whenever an Entity is updated.
              - `event_subscription.created` - Occurs whenever an Event Subscription is
                created.
              - `event_subscription.updated` - Occurs whenever an Event Subscription is
                updated.
              - `export.created` - Occurs whenever an Export is created.
              - `export.updated` - Occurs whenever an Export is updated.
              - `external_account.created` - Occurs whenever an External Account is created.
              - `external_account.updated` - Occurs whenever an External Account is updated.
              - `file.created` - Occurs whenever a File is created.
              - `group.updated` - Occurs whenever a Group is updated.
              - `group.heartbeat` - Increase may send webhooks with this category to see if a
                webhook endpoint is working properly.
              - `inbound_ach_transfer.created` - Occurs whenever an Inbound ACH Transfer is
                created.
              - `inbound_ach_transfer.updated` - Occurs whenever an Inbound ACH Transfer is
                updated.
              - `inbound_ach_transfer_return.created` - Occurs whenever an Inbound ACH
                Transfer Return is created.
              - `inbound_ach_transfer_return.updated` - Occurs whenever an Inbound ACH
                Transfer Return is updated.
              - `inbound_check_deposit.created` - Occurs whenever an Inbound Check Deposit is
                created.
              - `inbound_check_deposit.updated` - Occurs whenever an Inbound Check Deposit is
                updated.
              - `inbound_mail_item.created` - Occurs whenever an Inbound Mail Item is created.
              - `inbound_mail_item.updated` - Occurs whenever an Inbound Mail Item is updated.
              - `inbound_real_time_payments_transfer.created` - Occurs whenever an Inbound
                Real-Time Payments Transfer is created.
              - `inbound_real_time_payments_transfer.updated` - Occurs whenever an Inbound
                Real-Time Payments Transfer is updated.
              - `inbound_wire_drawdown_request.created` - Occurs whenever an Inbound Wire
                Drawdown Request is created.
              - `inbound_wire_transfer.created` - Occurs whenever an Inbound Wire Transfer is
                created.
              - `inbound_wire_transfer.updated` - Occurs whenever an Inbound Wire Transfer is
                updated.
              - `intrafi_account_enrollment.created` - Occurs whenever an IntraFi Account
                Enrollment is created.
              - `intrafi_account_enrollment.updated` - Occurs whenever an IntraFi Account
                Enrollment is updated.
              - `intrafi_exclusion.created` - Occurs whenever an IntraFi Exclusion is created.
              - `intrafi_exclusion.updated` - Occurs whenever an IntraFi Exclusion is updated.
              - `legacy_card_dispute.created` - Occurs whenever a Legacy Card Dispute is
                created.
              - `legacy_card_dispute.updated` - Occurs whenever a Legacy Card Dispute is
                updated.
              - `lockbox.created` - Occurs whenever a Lockbox is created.
              - `lockbox.updated` - Occurs whenever a Lockbox is updated.
              - `oauth_connection.created` - Occurs whenever an OAuth Connection is created.
              - `oauth_connection.deactivated` - Occurs whenever an OAuth Connection is
                deactivated.
              - `outbound_card_push_transfer.created` - Occurs whenever a Card Push Transfer
                is created.
              - `outbound_card_push_transfer.updated` - Occurs whenever a Card Push Transfer
                is updated.
              - `outbound_card_validation.created` - Occurs whenever a Card Validation is
                created.
              - `outbound_card_validation.updated` - Occurs whenever a Card Validation is
                updated.
              - `card_push_transfer.created` - Occurs whenever a Card Push Transfer is
                created.
              - `card_push_transfer.updated` - Occurs whenever a Card Push Transfer is
                updated.
              - `card_validation.created` - Occurs whenever a Card Validation is created.
              - `card_validation.updated` - Occurs whenever a Card Validation is updated.
              - `pending_transaction.created` - Occurs whenever a Pending Transaction is
                created.
              - `pending_transaction.updated` - Occurs whenever a Pending Transaction is
                updated.
              - `physical_card.created` - Occurs whenever a Physical Card is created.
              - `physical_card.updated` - Occurs whenever a Physical Card is updated.
              - `physical_card_profile.created` - Occurs whenever a Physical Card Profile is
                created.
              - `physical_card_profile.updated` - Occurs whenever a Physical Card Profile is
                updated.
              - `program.created` - Occurs whenever a Program is created.
              - `program.updated` - Occurs whenever a Program is updated.
              - `proof_of_authorization_request.created` - Occurs whenever a Proof of
                Authorization Request is created.
              - `proof_of_authorization_request.updated` - Occurs whenever a Proof of
                Authorization Request is updated.
              - `real_time_decision.card_authorization_requested` - Occurs whenever a
                Real-Time Decision is created in response to a card authorization.
              - `real_time_decision.digital_wallet_token_requested` - Occurs whenever a
                Real-Time Decision is created in response to a digital wallet provisioning
                attempt.
              - `real_time_decision.digital_wallet_authentication_requested` - Occurs whenever
                a Real-Time Decision is created in response to a digital wallet requiring
                two-factor authentication.
              - `real_time_decision.card_authentication_requested` - Occurs whenever a
                Real-Time Decision is created in response to 3DS authentication.
              - `real_time_decision.card_authentication_challenge_requested` - Occurs whenever
                a Real-Time Decision is created in response to 3DS authentication challenges.
              - `real_time_payments_transfer.created` - Occurs whenever a Real-Time Payments
                Transfer is created.
              - `real_time_payments_transfer.updated` - Occurs whenever a Real-Time Payments
                Transfer is updated.
              - `real_time_payments_request_for_payment.created` - Occurs whenever a Real-Time
                Payments Request for Payment is created.
              - `real_time_payments_request_for_payment.updated` - Occurs whenever a Real-Time
                Payments Request for Payment is updated.
              - `swift_transfer.created` - Occurs whenever a Swift Transfer is created.
              - `swift_transfer.updated` - Occurs whenever a Swift Transfer is updated.
              - `transaction.created` - Occurs whenever a Transaction is created.
              - `wire_drawdown_request.created` - Occurs whenever a Wire Drawdown Request is
                created.
              - `wire_drawdown_request.updated` - Occurs whenever a Wire Drawdown Request is
                updated.
              - `wire_transfer.created` - Occurs whenever a Wire Transfer is created.
              - `wire_transfer.updated` - Occurs whenever a Wire Transfer is updated.

          shared_secret: The key that will be used to sign webhooks. If no value is passed, a random
              string will be used as default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/event_subscriptions",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "oauth_connection_id": oauth_connection_id,
                    "selected_event_category": selected_event_category,
                    "shared_secret": shared_secret,
                },
                event_subscription_create_params.EventSubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EventSubscription,
        )

    async def retrieve(
        self,
        event_subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventSubscription:
        """
        Retrieve an Event Subscription

        Args:
          event_subscription_id: The identifier of the Event Subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_id:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_id` but received {event_subscription_id!r}"
            )
        return await self._get(
            f"/event_subscriptions/{event_subscription_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventSubscription,
        )

    async def update(
        self,
        event_subscription_id: str,
        *,
        status: Literal["active", "disabled", "deleted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> EventSubscription:
        """
        Update an Event Subscription

        Args:
          event_subscription_id: The identifier of the Event Subscription.

          status: The status to update the Event Subscription with.

              - `active` - The subscription is active and Events will be delivered normally.
              - `disabled` - The subscription is temporarily disabled and Events will not be
                delivered.
              - `deleted` - The subscription is permanently disabled and Events will not be
                delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not event_subscription_id:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_id` but received {event_subscription_id!r}"
            )
        return await self._patch(
            f"/event_subscriptions/{event_subscription_id}",
            body=await async_maybe_transform(
                {"status": status}, event_subscription_update_params.EventSubscriptionUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EventSubscription,
        )

    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EventSubscription, AsyncPage[EventSubscription]]:
        """
        List Event Subscriptions

        Args:
          cursor: Return the page of entries after this one.

          idempotency_key: Filter records to the one with the specified `idempotency_key` you chose for
              that object. This value is unique across Increase and is used to ensure that a
              request is only processed once. Learn more about
              [idempotency](https://increase.com/documentation/idempotency-keys).

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/event_subscriptions",
            page=AsyncPage[EventSubscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "idempotency_key": idempotency_key,
                        "limit": limit,
                    },
                    event_subscription_list_params.EventSubscriptionListParams,
                ),
            ),
            model=EventSubscription,
        )


class EventSubscriptionsResourceWithRawResponse:
    def __init__(self, event_subscriptions: EventSubscriptionsResource) -> None:
        self._event_subscriptions = event_subscriptions

        self.create = to_raw_response_wrapper(
            event_subscriptions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            event_subscriptions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            event_subscriptions.update,
        )
        self.list = to_raw_response_wrapper(
            event_subscriptions.list,
        )


class AsyncEventSubscriptionsResourceWithRawResponse:
    def __init__(self, event_subscriptions: AsyncEventSubscriptionsResource) -> None:
        self._event_subscriptions = event_subscriptions

        self.create = async_to_raw_response_wrapper(
            event_subscriptions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            event_subscriptions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            event_subscriptions.update,
        )
        self.list = async_to_raw_response_wrapper(
            event_subscriptions.list,
        )


class EventSubscriptionsResourceWithStreamingResponse:
    def __init__(self, event_subscriptions: EventSubscriptionsResource) -> None:
        self._event_subscriptions = event_subscriptions

        self.create = to_streamed_response_wrapper(
            event_subscriptions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            event_subscriptions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            event_subscriptions.update,
        )
        self.list = to_streamed_response_wrapper(
            event_subscriptions.list,
        )


class AsyncEventSubscriptionsResourceWithStreamingResponse:
    def __init__(self, event_subscriptions: AsyncEventSubscriptionsResource) -> None:
        self._event_subscriptions = event_subscriptions

        self.create = async_to_streamed_response_wrapper(
            event_subscriptions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            event_subscriptions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            event_subscriptions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            event_subscriptions.list,
        )
