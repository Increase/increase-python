# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..types import shared
from .._models import BaseModel

__all__ = [
    "RealTimeDecision",
    "CardAuthorization",
    "CardAuthorizationNetworkDetails",
    "CardAuthorizationNetworkDetailsVisa",
    "CardAuthorizationRequestDetails",
    "CardAuthorizationRequestDetailsIncrementalAuthorization",
    "DigitalWalletAuthentication",
    "DigitalWalletToken",
]


class CardAuthorizationNetworkDetailsVisa(BaseModel):
    electronic_commerce_indicator: Optional[
        Literal[
            "mail_phone_order",
            "recurring",
            "installment",
            "unknown_mail_phone_order",
            "secure_electronic_commerce",
            "non_authenticated_security_transaction_at_3ds_capable_merchant",
            "non_authenticated_security_transaction",
            "non_secure_transaction",
        ]
    ]
    """
    For electronic commerce transactions, this identifies the level of security used
    in obtaining the customer's payment credential. For mail or telephone order
    transactions, identifies the type of mail or telephone order.

    - `mail_phone_order` - Single transaction of a mail/phone order: Use to indicate
      that the transaction is a mail/phone order purchase, not a recurring
      transaction or installment payment. For domestic transactions in the US
      region, this value may also indicate one bill payment transaction in the
      card-present or card-absent environments.
    - `recurring` - Recurring transaction: Payment indicator used to indicate a
      recurring transaction that originates from an acquirer in the US region.
    - `installment` - Installment payment: Payment indicator used to indicate one
      purchase of goods or services that is billed to the account in multiple
      charges over a period of time agreed upon by the cardholder and merchant from
      transactions that originate from an acquirer in the US region.
    - `unknown_mail_phone_order` - Unknown classification: other mail order: Use to
      indicate that the type of mail/telephone order is unknown.
    - `secure_electronic_commerce` - Secure electronic commerce transaction: Use to
      indicate that the electronic commerce transaction has been authenticated using
      e.g., 3-D Secure
    - `non_authenticated_security_transaction_at_3ds_capable_merchant` -
      Non-authenticated security transaction at a 3-D Secure-capable merchant, and
      merchant attempted to authenticate the cardholder using 3-D Secure: Use to
      identify an electronic commerce transaction where the merchant attempted to
      authenticate the cardholder using 3-D Secure, but was unable to complete the
      authentication because the issuer or cardholder does not participate in the
      3-D Secure program.
    - `non_authenticated_security_transaction` - Non-authenticated security
      transaction: Use to identify an electronic commerce transaction that uses data
      encryption for security however , cardholder authentication is not performed
      using 3-D Secure.
    - `non_secure_transaction` - Non-secure transaction: Use to identify an
      electronic commerce transaction that has no data protection.
    """

    point_of_service_entry_mode: Optional[shared.PointOfServiceEntryMode]
    """
    The method used to enter the cardholder's primary account number and card
    expiration date
    """


class CardAuthorizationNetworkDetails(BaseModel):
    category: Literal["visa"]
    """The payment network used to process this card authorization

    - `visa` - Visa
    """

    visa: Optional[CardAuthorizationNetworkDetailsVisa]
    """Fields specific to the `visa` network"""


class CardAuthorizationRequestDetailsIncrementalAuthorization(BaseModel):
    card_payment_id: str
    """The card payment for this authorization and increment."""

    original_card_authorization_id: str
    """
    The identifier of the card authorization this request is attempting to
    increment.
    """


class CardAuthorizationRequestDetails(BaseModel):
    category: Literal["initial_authorization", "incremental_authorization"]
    """
    The type of this request (e.g., an initial authorization or an incremental
    authorization.)

    - `initial_authorization` - A regular, standalone authorization.
    - `incremental_authorization` - An incremental request to increase the amount of
      an existing authorization.
    """

    incremental_authorization: Optional[CardAuthorizationRequestDetailsIncrementalAuthorization]
    """Fields specific to the categorty `incremental_authorization`."""

    initial_authorization: Optional[object]
    """Fields specific to the category `initial_authorization`."""


class CardAuthorization(BaseModel):
    account_id: str
    """The identifier of the Account the authorization will debit."""

    card_id: str
    """The identifier of the Card that is being authorized."""

    decision: Optional[Literal["approve", "decline"]]
    """Whether or not the authorization was approved.

    - `approve` - Approve the authorization.
    - `decline` - Decline the authorization.
    """

    merchant_acceptor_id: str
    """
    The merchant identifier (commonly abbreviated as MID) of the merchant the card
    is transacting with.
    """

    merchant_category_code: Optional[str]
    """
    The Merchant Category Code (commonly abbreviated as MCC) of the merchant the
    card is transacting with.
    """

    merchant_city: Optional[str]
    """The city the merchant resides in."""

    merchant_country: Optional[str]
    """The country the merchant resides in."""

    merchant_descriptor: str
    """The merchant descriptor of the merchant the card is transacting with."""

    network_details: CardAuthorizationNetworkDetails
    """Fields specific to the `network`"""

    physical_card_id: Optional[str]
    """
    If the authorization was made in-person with a physical card, the Physical Card
    that was used.
    """

    presentment_amount: int
    """
    The amount of the attempted authorization in the currency the card user sees at
    the time of purchase, in the minor unit of that currency. For dollars, for
    example, this is cents.
    """

    presentment_currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the currency the
    user sees at the time of purchase.
    """

    request_details: CardAuthorizationRequestDetails
    """Fields specific to the type of request, such as an incremental authorization."""

    settlement_amount: int
    """The amount of the attempted authorization in the currency it will be settled in.

    This currency is the same as that of the Account the card belongs to.
    """

    settlement_currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the currency the
    transaction will be settled in.
    """


class DigitalWalletAuthentication(BaseModel):
    card_id: str
    """The identifier of the Card that is being tokenized."""

    channel: Literal["sms", "email"]
    """The channel to send the card user their one-time passcode.

    - `sms` - Send one-time passcodes over SMS.
    - `email` - Send one-time passcodes over email.
    """

    digital_wallet: Literal["apple_pay", "google_pay"]
    """The digital wallet app being used.

    - `apple_pay` - Apple Pay
    - `google_pay` - Google Pay
    """

    email: Optional[str]
    """The email to send the one-time passcode to if `channel` is equal to `email`."""

    one_time_passcode: str
    """The one-time passcode to send the card user."""

    phone: Optional[str]
    """
    The phone number to send the one-time passcode to if `channel` is equal to
    `sms`.
    """

    result: Optional[Literal["success", "failure"]]
    """Whether your application successfully delivered the one-time passcode.

    - `success` - Your application successfully delivered the one-time passcode to
      the cardholder.
    - `failure` - Your application failed to deliver the one-time passcode to the
      cardholder.
    """


class DigitalWalletToken(BaseModel):
    card_id: str
    """The identifier of the Card that is being tokenized."""

    card_profile_id: Optional[str]
    """The identifier of the Card Profile that was set via the real time decision.

    This will be null until the real time decision is responded to or if the real
    time decision did not set a card profile.
    """

    decision: Optional[Literal["approve", "decline"]]
    """Whether or not the provisioning request was approved.

    This will be null until the real time decision is responded to.

    - `approve` - Approve the provisioning request.
    - `decline` - Decline the provisioning request.
    """

    digital_wallet: Literal["apple_pay", "google_pay"]
    """The digital wallet app being used.

    - `apple_pay` - Apple Pay
    - `google_pay` - Google Pay
    """


class RealTimeDecision(BaseModel):
    id: str
    """The Real-Time Decision identifier."""

    card_authorization: Optional[CardAuthorization]
    """Fields related to a card authorization."""

    category: Literal[
        "card_authorization_requested", "digital_wallet_token_requested", "digital_wallet_authentication_requested"
    ]
    """The category of the Real-Time Decision.

    - `card_authorization_requested` - A card is being authorized.
    - `digital_wallet_token_requested` - A card is being loaded into a digital
      wallet.
    - `digital_wallet_authentication_requested` - A card is being loaded into a
      digital wallet and requires cardholder authentication.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Real-Time Decision was created.
    """

    digital_wallet_authentication: Optional[DigitalWalletAuthentication]
    """Fields related to a digital wallet authentication attempt."""

    digital_wallet_token: Optional[DigitalWalletToken]
    """Fields related to a digital wallet token provisioning attempt."""

    status: Literal["pending", "responded", "timed_out"]
    """The status of the Real-Time Decision.

    - `pending` - The decision is pending action via real-time webhook.
    - `responded` - Your webhook actioned the real-time decision.
    - `timed_out` - Your webhook failed to respond to the authorization in time.
    """

    timeout_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    your application can no longer respond to the Real-Time Decision.
    """

    type: Literal["real_time_decision"]
    """A constant representing the object's type.

    For this resource it will always be `real_time_decision`.
    """
