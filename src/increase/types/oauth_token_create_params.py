# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OAuthTokenCreateParams"]


class OAuthTokenCreateParams(TypedDict, total=False):
    grant_type: Required[Literal["authorization_code", "production_token"]]
    """The credential you request in exchange for the code.

    - `authorization_code` - An OAuth authorization code.
    - `production_token` - An OAuth production token.
    """

    client_id: str
    """The public identifier for your application."""

    client_secret: str
    """The secret that confirms you own the application.

    This is redundent given that the request is made with your API key but it's a
    required component of OAuth 2.0.
    """

    code: str
    """
    The authorization code generated by the user and given to you as a query
    parameter.
    """

    production_token: str
    """The production token you want to exchange for a sandbox token.

    This is only available in Sandbox. Set `grant_type` to `production_token` to use
    this parameter.
    """
