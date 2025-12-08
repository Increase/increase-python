# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CardPushTransferCreateParams", "PresentmentAmount"]


class CardPushTransferCreateParams(TypedDict, total=False):
    business_application_identifier: Required[
        Literal[
            "account_to_account",
            "business_to_business",
            "money_transfer_bank_initiated",
            "non_card_bill_payment",
            "consumer_bill_payment",
            "card_bill_payment",
            "funds_disbursement",
            "funds_transfer",
            "loyalty_and_offers",
            "merchant_disbursement",
            "merchant_payment",
            "person_to_person",
            "top_up",
            "wallet_transfer",
        ]
    ]
    """
    The Business Application Identifier describes the type of transaction being
    performed. Your program must be approved for the specified Business Application
    Identifier in order to use it.

    - `account_to_account` - Account to Account
    - `business_to_business` - Business to Business
    - `money_transfer_bank_initiated` - Money Transfer Bank Initiated
    - `non_card_bill_payment` - Non-Card Bill Payment
    - `consumer_bill_payment` - Consumer Bill Payment
    - `card_bill_payment` - Card Bill Payment
    - `funds_disbursement` - Funds Disbursement
    - `funds_transfer` - Funds Transfer
    - `loyalty_and_offers` - Loyalty and Offers
    - `merchant_disbursement` - Merchant Disbursement
    - `merchant_payment` - Merchant Payment
    - `person_to_person` - Person to Person
    - `top_up` - Top Up
    - `wallet_transfer` - Wallet Transfer
    """

    card_token_id: Required[str]
    """
    The Increase identifier for the Card Token that represents the card number
    you're pushing funds to.
    """

    merchant_category_code: Required[str]
    """
    The merchant category code (MCC) of the merchant (generally your business)
    sending the transfer. This is a four-digit code that describes the type of
    business or service provided by the merchant. Your program must be approved for
    the specified MCC in order to use it.
    """

    merchant_city_name: Required[str]
    """The city name of the merchant (generally your business) sending the transfer."""

    merchant_name: Required[str]
    """The merchant name shows up as the statement descriptor for the transfer.

    This is typically the name of your business or organization.
    """

    merchant_name_prefix: Required[str]
    """
    For certain Business Application Identifiers, the statement descriptor is
    `merchant_name_prefix*sender_name`, where the `merchant_name_prefix` is a one to
    four character prefix that identifies the merchant.
    """

    merchant_postal_code: Required[str]
    """The postal code of the merchant (generally your business) sending the transfer."""

    merchant_state: Required[str]
    """The state of the merchant (generally your business) sending the transfer."""

    presentment_amount: Required[PresentmentAmount]
    """The amount to transfer.

    The receiving bank will convert this to the cardholder's currency. The amount
    that is applied to your Increase account matches the currency of your account.
    """

    recipient_name: Required[str]
    """The name of the funds recipient."""

    sender_address_city: Required[str]
    """The city of the sender."""

    sender_address_line1: Required[str]
    """The address line 1 of the sender."""

    sender_address_postal_code: Required[str]
    """The postal code of the sender."""

    sender_address_state: Required[str]
    """The state of the sender."""

    sender_name: Required[str]
    """The name of the funds originator."""

    source_account_number_id: Required[str]
    """The identifier of the Account Number from which to send the transfer."""

    require_approval: bool
    """Whether the transfer requires explicit approval via the dashboard or API."""


class PresentmentAmount(TypedDict, total=False):
    """The amount to transfer.

    The receiving bank will convert this to the cardholder's currency. The amount that is applied to your Increase account matches the currency of your account.
    """

    currency: Required[
        Literal[
            "AFN",
            "EUR",
            "ALL",
            "DZD",
            "USD",
            "AOA",
            "ARS",
            "AMD",
            "AWG",
            "AUD",
            "AZN",
            "BSD",
            "BHD",
            "BDT",
            "BBD",
            "BYN",
            "BZD",
            "BMD",
            "INR",
            "BTN",
            "BOB",
            "BOV",
            "BAM",
            "BWP",
            "NOK",
            "BRL",
            "BND",
            "BGN",
            "BIF",
            "CVE",
            "KHR",
            "CAD",
            "KYD",
            "CLP",
            "CLF",
            "CNY",
            "COP",
            "COU",
            "KMF",
            "CDF",
            "NZD",
            "CRC",
            "CUP",
            "CZK",
            "DKK",
            "DJF",
            "DOP",
            "EGP",
            "SVC",
            "ERN",
            "SZL",
            "ETB",
            "FKP",
            "FJD",
            "GMD",
            "GEL",
            "GHS",
            "GIP",
            "GTQ",
            "GBP",
            "GNF",
            "GYD",
            "HTG",
            "HNL",
            "HKD",
            "HUF",
            "ISK",
            "IDR",
            "IRR",
            "IQD",
            "ILS",
            "JMD",
            "JPY",
            "JOD",
            "KZT",
            "KES",
            "KPW",
            "KRW",
            "KWD",
            "KGS",
            "LAK",
            "LBP",
            "LSL",
            "ZAR",
            "LRD",
            "LYD",
            "CHF",
            "MOP",
            "MKD",
            "MGA",
            "MWK",
            "MYR",
            "MVR",
            "MRU",
            "MUR",
            "MXN",
            "MXV",
            "MDL",
            "MNT",
            "MAD",
            "MZN",
            "MMK",
            "NAD",
            "NPR",
            "NIO",
            "NGN",
            "OMR",
            "PKR",
            "PAB",
            "PGK",
            "PYG",
            "PEN",
            "PHP",
            "PLN",
            "QAR",
            "RON",
            "RUB",
            "RWF",
            "SHP",
            "WST",
            "STN",
            "SAR",
            "RSD",
            "SCR",
            "SLE",
            "SGD",
            "SBD",
            "SOS",
            "SSP",
            "LKR",
            "SDG",
            "SRD",
            "SEK",
            "CHE",
            "CHW",
            "SYP",
            "TWD",
            "TJS",
            "TZS",
            "THB",
            "TOP",
            "TTD",
            "TND",
            "TRY",
            "TMT",
            "UGX",
            "UAH",
            "AED",
            "USN",
            "UYU",
            "UYI",
            "UYW",
            "UZS",
            "VUV",
            "VES",
            "VED",
            "VND",
            "YER",
            "ZMW",
            "ZWG",
        ]
    ]
    """The ISO 4217 currency code representing the currency of the amount.

    - `AFN` - AFN
    - `EUR` - EUR
    - `ALL` - ALL
    - `DZD` - DZD
    - `USD` - USD
    - `AOA` - AOA
    - `ARS` - ARS
    - `AMD` - AMD
    - `AWG` - AWG
    - `AUD` - AUD
    - `AZN` - AZN
    - `BSD` - BSD
    - `BHD` - BHD
    - `BDT` - BDT
    - `BBD` - BBD
    - `BYN` - BYN
    - `BZD` - BZD
    - `BMD` - BMD
    - `INR` - INR
    - `BTN` - BTN
    - `BOB` - BOB
    - `BOV` - BOV
    - `BAM` - BAM
    - `BWP` - BWP
    - `NOK` - NOK
    - `BRL` - BRL
    - `BND` - BND
    - `BGN` - BGN
    - `BIF` - BIF
    - `CVE` - CVE
    - `KHR` - KHR
    - `CAD` - CAD
    - `KYD` - KYD
    - `CLP` - CLP
    - `CLF` - CLF
    - `CNY` - CNY
    - `COP` - COP
    - `COU` - COU
    - `KMF` - KMF
    - `CDF` - CDF
    - `NZD` - NZD
    - `CRC` - CRC
    - `CUP` - CUP
    - `CZK` - CZK
    - `DKK` - DKK
    - `DJF` - DJF
    - `DOP` - DOP
    - `EGP` - EGP
    - `SVC` - SVC
    - `ERN` - ERN
    - `SZL` - SZL
    - `ETB` - ETB
    - `FKP` - FKP
    - `FJD` - FJD
    - `GMD` - GMD
    - `GEL` - GEL
    - `GHS` - GHS
    - `GIP` - GIP
    - `GTQ` - GTQ
    - `GBP` - GBP
    - `GNF` - GNF
    - `GYD` - GYD
    - `HTG` - HTG
    - `HNL` - HNL
    - `HKD` - HKD
    - `HUF` - HUF
    - `ISK` - ISK
    - `IDR` - IDR
    - `IRR` - IRR
    - `IQD` - IQD
    - `ILS` - ILS
    - `JMD` - JMD
    - `JPY` - JPY
    - `JOD` - JOD
    - `KZT` - KZT
    - `KES` - KES
    - `KPW` - KPW
    - `KRW` - KRW
    - `KWD` - KWD
    - `KGS` - KGS
    - `LAK` - LAK
    - `LBP` - LBP
    - `LSL` - LSL
    - `ZAR` - ZAR
    - `LRD` - LRD
    - `LYD` - LYD
    - `CHF` - CHF
    - `MOP` - MOP
    - `MKD` - MKD
    - `MGA` - MGA
    - `MWK` - MWK
    - `MYR` - MYR
    - `MVR` - MVR
    - `MRU` - MRU
    - `MUR` - MUR
    - `MXN` - MXN
    - `MXV` - MXV
    - `MDL` - MDL
    - `MNT` - MNT
    - `MAD` - MAD
    - `MZN` - MZN
    - `MMK` - MMK
    - `NAD` - NAD
    - `NPR` - NPR
    - `NIO` - NIO
    - `NGN` - NGN
    - `OMR` - OMR
    - `PKR` - PKR
    - `PAB` - PAB
    - `PGK` - PGK
    - `PYG` - PYG
    - `PEN` - PEN
    - `PHP` - PHP
    - `PLN` - PLN
    - `QAR` - QAR
    - `RON` - RON
    - `RUB` - RUB
    - `RWF` - RWF
    - `SHP` - SHP
    - `WST` - WST
    - `STN` - STN
    - `SAR` - SAR
    - `RSD` - RSD
    - `SCR` - SCR
    - `SLE` - SLE
    - `SGD` - SGD
    - `SBD` - SBD
    - `SOS` - SOS
    - `SSP` - SSP
    - `LKR` - LKR
    - `SDG` - SDG
    - `SRD` - SRD
    - `SEK` - SEK
    - `CHE` - CHE
    - `CHW` - CHW
    - `SYP` - SYP
    - `TWD` - TWD
    - `TJS` - TJS
    - `TZS` - TZS
    - `THB` - THB
    - `TOP` - TOP
    - `TTD` - TTD
    - `TND` - TND
    - `TRY` - TRY
    - `TMT` - TMT
    - `UGX` - UGX
    - `UAH` - UAH
    - `AED` - AED
    - `USN` - USN
    - `UYU` - UYU
    - `UYI` - UYI
    - `UYW` - UYW
    - `UZS` - UZS
    - `VUV` - VUV
    - `VES` - VES
    - `VED` - VED
    - `VND` - VND
    - `YER` - YER
    - `ZMW` - ZMW
    - `ZWG` - ZWG
    """

    value: Required[str]
    """The amount value as a decimal string in the currency's major unit.

    For example, for USD, '1234.56' represents 1234 dollars and 56 cents. For JPY,
    '1234' represents 1234 yen. A currency with minor units requires at least one
    decimal place and supports up to the number of decimal places defined by the
    currency's minor units. A currency without minor units does not support any
    decimal places.
    """
