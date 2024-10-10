# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "RealTimeDecisionActionParams",
    "CardAuthentication",
    "CardAuthenticationChallenge",
    "CardAuthorization",
    "DigitalWalletAuthentication",
    "DigitalWalletAuthenticationSuccess",
    "DigitalWalletToken",
    "DigitalWalletTokenApproval",
    "DigitalWalletTokenDecline",
]


class RealTimeDecisionActionParams(TypedDict, total=False):
    card_authentication: CardAuthentication
    """
    If the Real-Time Decision relates to a 3DS card authentication attempt, this
    object contains your response to the authentication.
    """

    card_authentication_challenge: CardAuthenticationChallenge
    """
    If the Real-Time Decision relates to 3DS card authentication challenge delivery,
    this object contains your response.
    """

    card_authorization: CardAuthorization
    """
    If the Real-Time Decision relates to a card authorization attempt, this object
    contains your response to the authorization.
    """

    digital_wallet_authentication: DigitalWalletAuthentication
    """
    If the Real-Time Decision relates to a digital wallet authentication attempt,
    this object contains your response to the authentication.
    """

    digital_wallet_token: DigitalWalletToken
    """
    If the Real-Time Decision relates to a digital wallet token provisioning
    attempt, this object contains your response to the attempt.
    """


class CardAuthentication(TypedDict, total=False):
    decision: Required[Literal["approve", "challenge", "deny"]]
    """Whether the card authentication attempt should be approved or declined.

    - `approve` - Approve the authentication attempt without triggering a challenge.
    - `challenge` - Request further validation before approving the authentication
      attempt.
    - `deny` - Deny the authentication attempt.
    """


class CardAuthenticationChallenge(TypedDict, total=False):
    result: Required[Literal["success", "failure"]]
    """
    Whether the card authentication challenge was successfully delivered to the
    cardholder.

    - `success` - Your application successfully delivered the one-time code to the
      cardholder.
    - `failure` - Your application was unable to deliver the one-time code to the
      cardholder.
    """


class CardAuthorization(TypedDict, total=False):
    decision: Required[Literal["approve", "decline"]]
    """Whether the card authorization should be approved or declined.

    - `approve` - Approve the authorization.
    - `decline` - Decline the authorization.
    """


class DigitalWalletAuthenticationSuccess(TypedDict, total=False):
    email: str
    """The email address that was used to verify the cardholder via one-time passcode."""

    phone: str
    """
    The phone number that was used to verify the cardholder via one-time passcode
    over SMS.
    """


class DigitalWalletAuthentication(TypedDict, total=False):
    result: Required[Literal["success", "failure"]]
    """Whether your application was able to deliver the one-time passcode.

    - `success` - Your application successfully delivered the one-time passcode to
      the cardholder.
    - `failure` - Your application failed to deliver the one-time passcode to the
      cardholder.
    """

    success: DigitalWalletAuthenticationSuccess


class DigitalWalletTokenApproval(TypedDict, total=False):
    email: str
    """
    An email address that can be used to verify the cardholder via one-time
    passcode.
    """

    phone: str
    """
    A phone number that can be used to verify the cardholder via one-time passcode
    over SMS.
    """


class DigitalWalletTokenDecline(TypedDict, total=False):
    reason: str
    """Why the tokenization attempt was declined.

    This is for logging purposes only and is not displayed to the end-user.
    """


class DigitalWalletToken(TypedDict, total=False):
    approval: DigitalWalletTokenApproval
    """
    If your application approves the provisioning attempt, this contains metadata
    about the digital wallet token that will be generated.
    """

    decline: DigitalWalletTokenDecline
    """
    If your application declines the provisioning attempt, this contains details
    about the decline.
    """
