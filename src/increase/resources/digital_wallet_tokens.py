# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import DigitalWalletToken, digital_wallet_token_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["DigitalWalletTokens", "AsyncDigitalWalletTokens"]


class DigitalWalletTokens(SyncAPIResource):
    def retrieve(
        self,
        digital_wallet_token_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> DigitalWalletToken:
        """Retrieve a Digital Wallet Token"""
        return self._get(
            f"/digital_wallet_tokens/{digital_wallet_token_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=DigitalWalletToken,
        )

    def list(
        self,
        *,
        card_id: str | NotGiven = NOT_GIVEN,
        created_at: digital_wallet_token_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[DigitalWalletToken]:
        """
        List Digital Wallet Tokens

        Args:
          card_id: Filter Digital Wallet Tokens to ones belonging to the specified Card.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/digital_wallet_tokens",
            page=SyncPage[DigitalWalletToken],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "card_id": card_id,
                        "created_at": created_at,
                    },
                    digital_wallet_token_list_params.DigitalWalletTokenListParams,
                ),
            ),
            model=DigitalWalletToken,
        )


class AsyncDigitalWalletTokens(AsyncAPIResource):
    async def retrieve(
        self,
        digital_wallet_token_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> DigitalWalletToken:
        """Retrieve a Digital Wallet Token"""
        return await self._get(
            f"/digital_wallet_tokens/{digital_wallet_token_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=DigitalWalletToken,
        )

    def list(
        self,
        *,
        card_id: str | NotGiven = NOT_GIVEN,
        created_at: digital_wallet_token_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[DigitalWalletToken, AsyncPage[DigitalWalletToken]]:
        """
        List Digital Wallet Tokens

        Args:
          card_id: Filter Digital Wallet Tokens to ones belonging to the specified Card.

          cursor: Return the page of entries after this one.

          limit: Limit the size of the list that is returned. The default (and maximum) is 100
              objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/digital_wallet_tokens",
            page=AsyncPage[DigitalWalletToken],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "card_id": card_id,
                        "created_at": created_at,
                    },
                    digital_wallet_token_list_params.DigitalWalletTokenListParams,
                ),
            ),
            model=DigitalWalletToken,
        )
