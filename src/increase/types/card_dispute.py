# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "CardDispute",
    "Loss",
    "Visa",
    "VisaNetworkEvent",
    "VisaNetworkEventAttachmentFile",
    "VisaNetworkEventMerchantPrearbitrationReceived",
    "VisaNetworkEventMerchantPrearbitrationReceivedCardholderNoLongerDisputes",
    "VisaNetworkEventMerchantPrearbitrationReceivedCompellingEvidence",
    "VisaNetworkEventMerchantPrearbitrationReceivedCreditOrReversalProcessed",
    "VisaNetworkEventMerchantPrearbitrationReceivedDelayedChargeTransaction",
    "VisaNetworkEventMerchantPrearbitrationReceivedEvidenceOfImprint",
    "VisaNetworkEventMerchantPrearbitrationReceivedInvalidDispute",
    "VisaNetworkEventMerchantPrearbitrationReceivedNonFiatCurrencyOrNonFungibleTokenReceived",
    "VisaNetworkEventMerchantPrearbitrationReceivedPriorUndisputedNonFraudTransactions",
    "VisaNetworkEventRepresented",
    "VisaNetworkEventRepresentedCardholderNoLongerDisputes",
    "VisaNetworkEventRepresentedCreditOrReversalProcessed",
    "VisaNetworkEventRepresentedInvalidDispute",
    "VisaNetworkEventRepresentedNonFiatCurrencyOrNonFungibleTokenReceived",
    "VisaNetworkEventRepresentedProofOfCashDisbursement",
    "VisaNetworkEventRepresentedReversalIssued",
    "VisaUserSubmission",
    "VisaUserSubmissionAttachmentFile",
    "VisaUserSubmissionChargeback",
    "VisaUserSubmissionChargebackAuthorization",
    "VisaUserSubmissionChargebackConsumerCanceledMerchandise",
    "VisaUserSubmissionChargebackConsumerCanceledMerchandiseCardholderCancellation",
    "VisaUserSubmissionChargebackConsumerCanceledMerchandiseReturnAttempted",
    "VisaUserSubmissionChargebackConsumerCanceledMerchandiseReturned",
    "VisaUserSubmissionChargebackConsumerCanceledRecurringTransaction",
    "VisaUserSubmissionChargebackConsumerCanceledRecurringTransactionMerchantContactMethods",
    "VisaUserSubmissionChargebackConsumerCanceledServices",
    "VisaUserSubmissionChargebackConsumerCanceledServicesCardholderCancellation",
    "VisaUserSubmissionChargebackConsumerCanceledServicesGuaranteedReservation",
    "VisaUserSubmissionChargebackConsumerCounterfeitMerchandise",
    "VisaUserSubmissionChargebackConsumerCreditNotProcessed",
    "VisaUserSubmissionChargebackConsumerDamagedOrDefectiveMerchandise",
    "VisaUserSubmissionChargebackConsumerDamagedOrDefectiveMerchandiseReturnAttempted",
    "VisaUserSubmissionChargebackConsumerDamagedOrDefectiveMerchandiseReturned",
    "VisaUserSubmissionChargebackConsumerMerchandiseMisrepresentation",
    "VisaUserSubmissionChargebackConsumerMerchandiseMisrepresentationReturnAttempted",
    "VisaUserSubmissionChargebackConsumerMerchandiseMisrepresentationReturned",
    "VisaUserSubmissionChargebackConsumerMerchandiseNotAsDescribed",
    "VisaUserSubmissionChargebackConsumerMerchandiseNotAsDescribedReturnAttempted",
    "VisaUserSubmissionChargebackConsumerMerchandiseNotAsDescribedReturned",
    "VisaUserSubmissionChargebackConsumerMerchandiseNotReceived",
    "VisaUserSubmissionChargebackConsumerMerchandiseNotReceivedCardholderCancellationPriorToExpectedReceipt",
    "VisaUserSubmissionChargebackConsumerMerchandiseNotReceivedDelayed",
    "VisaUserSubmissionChargebackConsumerMerchandiseNotReceivedDelayedReturnAttempted",
    "VisaUserSubmissionChargebackConsumerMerchandiseNotReceivedDelayedReturned",
    "VisaUserSubmissionChargebackConsumerMerchandiseNotReceivedDeliveredToWrongLocation",
    "VisaUserSubmissionChargebackConsumerMerchandiseNotReceivedMerchantCancellation",
    "VisaUserSubmissionChargebackConsumerOriginalCreditTransactionNotAccepted",
    "VisaUserSubmissionChargebackConsumerQualityMerchandise",
    "VisaUserSubmissionChargebackConsumerQualityMerchandiseOngoingNegotiations",
    "VisaUserSubmissionChargebackConsumerQualityMerchandiseReturnAttempted",
    "VisaUserSubmissionChargebackConsumerQualityMerchandiseReturned",
    "VisaUserSubmissionChargebackConsumerQualityServices",
    "VisaUserSubmissionChargebackConsumerQualityServicesCardholderCancellation",
    "VisaUserSubmissionChargebackConsumerQualityServicesOngoingNegotiations",
    "VisaUserSubmissionChargebackConsumerServicesMisrepresentation",
    "VisaUserSubmissionChargebackConsumerServicesMisrepresentationCardholderCancellation",
    "VisaUserSubmissionChargebackConsumerServicesNotAsDescribed",
    "VisaUserSubmissionChargebackConsumerServicesNotAsDescribedCardholderCancellation",
    "VisaUserSubmissionChargebackConsumerServicesNotReceived",
    "VisaUserSubmissionChargebackConsumerServicesNotReceivedCardholderCancellationPriorToExpectedReceipt",
    "VisaUserSubmissionChargebackConsumerServicesNotReceivedMerchantCancellation",
    "VisaUserSubmissionChargebackFraud",
    "VisaUserSubmissionChargebackProcessingError",
    "VisaUserSubmissionChargebackProcessingErrorDuplicateTransaction",
    "VisaUserSubmissionChargebackProcessingErrorIncorrectAmount",
    "VisaUserSubmissionChargebackProcessingErrorPaidByOtherMeans",
    "VisaUserSubmissionMerchantPrearbitrationDecline",
    "VisaUserSubmissionUserPrearbitration",
    "VisaUserSubmissionUserPrearbitrationCategoryChange",
    "Win",
]


class Loss(BaseModel):
    lost_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Card Dispute was lost.
    """

    reason: Literal["user_withdrawn", "loss"]
    """The reason the Card Dispute was lost.

    - `user_withdrawn` - The user withdrew the Card Dispute.
    - `loss` - The Card Dispute was lost according to network rules.
    """


class VisaNetworkEventAttachmentFile(BaseModel):
    file_id: str
    """The ID of the file attached to the Card Dispute."""


class VisaNetworkEventMerchantPrearbitrationReceivedCardholderNoLongerDisputes(BaseModel):
    explanation: Optional[str] = None
    """
    Explanation for why the merchant believes the cardholder no longer disputes the
    transaction.
    """


class VisaNetworkEventMerchantPrearbitrationReceivedCompellingEvidence(BaseModel):
    category: Literal[
        "authorized_signer",
        "delivery",
        "delivery_at_place_of_employment",
        "digital_goods_download",
        "dynamic_currency_conversion_actively_chosen",
        "flight_manifest_and_purchase_itinerary",
        "household_member_signer",
        "legitimate_spend_across_payment_types_for_same_merchandise",
        "merchandise_use",
        "passenger_transport_ticket_use",
        "recurring_transaction_with_binding_contract_or_previous_undisputed_transaction",
        "signed_delivery_or_pickup_form",
        "signed_mail_order_phone_order_form",
        "travel_and_expense_loyalty_transaction",
        "travel_and_expense_subsequent_purchase",
    ]
    """The category of compelling evidence provided by the merchant.

    - `authorized_signer` - Authorized signer known by the cardholder.
    - `delivery` - Proof of delivery.
    - `delivery_at_place_of_employment` - Proof of delivery to cardholder at place
      of employment.
    - `digital_goods_download` - Proof of digital goods download.
    - `dynamic_currency_conversion_actively_chosen` - Dynamic Currency Conversion
      actively chosen by cardholder.
    - `flight_manifest_and_purchase_itinerary` - Flight manifest with corresponding
      purchase itinerary record.
    - `household_member_signer` - Signer is member of cardholder's household.
    - `legitimate_spend_across_payment_types_for_same_merchandise` - Legitimate
      spend across multiple payment types for same merchandise.
    - `merchandise_use` - Documentation to prove the cardholder is in possession of
      and/or using the merchandise.
    - `passenger_transport_ticket_use` - Passenger transport: proof ticket was
      received, scanned at gate or other transaction related to original (for
      example, frequent flyer miles.)
    - `recurring_transaction_with_binding_contract_or_previous_undisputed_transaction` -
      Recurring transaction with binding contract or previous undisputed recurring
      transactions and proof the cardholder is using the merchandise or service.
    - `signed_delivery_or_pickup_form` - Signed delivery form, or copy of/details of
      identification from cardholder as proof goods were picked up at merchant
      location.
    - `signed_mail_order_phone_order_form` - Signed Mail Order/Phone Order form.
    - `travel_and_expense_loyalty_transaction` - Travel & Expense: loyalty
      transactions related to purchase.
    - `travel_and_expense_subsequent_purchase` - Travel & Expense: subsequent
      purchases made throughout service period.
    """

    explanation: Optional[str] = None
    """Explanation of the compelling evidence provided by the merchant."""


class VisaNetworkEventMerchantPrearbitrationReceivedCreditOrReversalProcessed(BaseModel):
    amount: int
    """The amount of the credit or reversal in the minor unit of its currency.

    For dollars, for example, this is cents.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the credit or
    reversal's currency.
    """

    explanation: Optional[str] = None
    """Explanation for why the merchant believes the credit or reversal was processed."""

    processed_at: date
    """The date the credit or reversal was processed."""


class VisaNetworkEventMerchantPrearbitrationReceivedDelayedChargeTransaction(BaseModel):
    explanation: Optional[str] = None
    """Additional details about the delayed charge transaction."""


class VisaNetworkEventMerchantPrearbitrationReceivedEvidenceOfImprint(BaseModel):
    explanation: Optional[str] = None
    """Explanation of the evidence of imprint."""


class VisaNetworkEventMerchantPrearbitrationReceivedInvalidDispute(BaseModel):
    explanation: Optional[str] = None
    """Explanation for why the dispute is considered invalid by the merchant."""

    reason: Literal["other", "special_authorization_procedures_followed"]
    """The reason a merchant considers the dispute invalid.

    - `other` - Other.
    - `special_authorization_procedures_followed` - Special authorization procedures
      followed.
    """


class VisaNetworkEventMerchantPrearbitrationReceivedNonFiatCurrencyOrNonFungibleTokenReceived(BaseModel):
    blockchain_transaction_hash: str
    """Blockchain transaction hash."""

    destination_wallet_address: str
    """Destination wallet address."""

    prior_approved_transactions: Optional[str] = None
    """Prior approved transactions."""


class VisaNetworkEventMerchantPrearbitrationReceivedPriorUndisputedNonFraudTransactions(BaseModel):
    explanation: Optional[str] = None
    """
    Explanation of the prior undisputed non-fraud transactions provided by the
    merchant.
    """


class VisaNetworkEventMerchantPrearbitrationReceived(BaseModel):
    cardholder_no_longer_disputes: Optional[
        VisaNetworkEventMerchantPrearbitrationReceivedCardholderNoLongerDisputes
    ] = None
    """Cardholder no longer disputes details.

    Present if and only if `reason` is `cardholder_no_longer_disputes`.
    """

    compelling_evidence: Optional[VisaNetworkEventMerchantPrearbitrationReceivedCompellingEvidence] = None
    """Compelling evidence details.

    Present if and only if `reason` is `compelling_evidence`.
    """

    credit_or_reversal_processed: Optional[VisaNetworkEventMerchantPrearbitrationReceivedCreditOrReversalProcessed] = (
        None
    )
    """Credit or reversal processed details.

    Present if and only if `reason` is `credit_or_reversal_processed`.
    """

    delayed_charge_transaction: Optional[VisaNetworkEventMerchantPrearbitrationReceivedDelayedChargeTransaction] = None
    """Delayed charge transaction details.

    Present if and only if `reason` is `delayed_charge_transaction`.
    """

    evidence_of_imprint: Optional[VisaNetworkEventMerchantPrearbitrationReceivedEvidenceOfImprint] = None
    """Evidence of imprint details.

    Present if and only if `reason` is `evidence_of_imprint`.
    """

    invalid_dispute: Optional[VisaNetworkEventMerchantPrearbitrationReceivedInvalidDispute] = None
    """Invalid dispute details. Present if and only if `reason` is `invalid_dispute`."""

    non_fiat_currency_or_non_fungible_token_received: Optional[
        VisaNetworkEventMerchantPrearbitrationReceivedNonFiatCurrencyOrNonFungibleTokenReceived
    ] = None
    """Non-fiat currency or non-fungible token received details.

    Present if and only if `reason` is
    `non_fiat_currency_or_non_fungible_token_received`.
    """

    prior_undisputed_non_fraud_transactions: Optional[
        VisaNetworkEventMerchantPrearbitrationReceivedPriorUndisputedNonFraudTransactions
    ] = None
    """Prior undisputed non-fraud transactions details.

    Present if and only if `reason` is `prior_undisputed_non_fraud_transactions`.
    """

    reason: Literal[
        "cardholder_no_longer_disputes",
        "compelling_evidence",
        "credit_or_reversal_processed",
        "delayed_charge_transaction",
        "evidence_of_imprint",
        "invalid_dispute",
        "non_fiat_currency_or_non_fungible_token_received",
        "prior_undisputed_non_fraud_transactions",
    ]
    """The reason the merchant re-presented the dispute.

    - `cardholder_no_longer_disputes` - Cardholder no longer disputes the
      transaction.
    - `compelling_evidence` - Compelling evidence.
    - `credit_or_reversal_processed` - Credit or reversal was processed.
    - `delayed_charge_transaction` - Delayed charge transaction.
    - `evidence_of_imprint` - Evidence of imprint.
    - `invalid_dispute` - Invalid dispute.
    - `non_fiat_currency_or_non_fungible_token_received` - Non-fiat currency or
      non-fungible token was received by the cardholder.
    - `prior_undisputed_non_fraud_transactions` - Prior undisputed non-fraud
      transactions.
    """


class VisaNetworkEventRepresentedCardholderNoLongerDisputes(BaseModel):
    explanation: Optional[str] = None
    """
    Explanation for why the merchant believes the cardholder no longer disputes the
    transaction.
    """


class VisaNetworkEventRepresentedCreditOrReversalProcessed(BaseModel):
    amount: int
    """The amount of the credit or reversal in the minor unit of its currency.

    For dollars, for example, this is cents.
    """

    currency: str
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the credit or
    reversal's currency.
    """

    explanation: Optional[str] = None
    """Explanation for why the merchant believes the credit or reversal was processed."""

    processed_at: date
    """The date the credit or reversal was processed."""


class VisaNetworkEventRepresentedInvalidDispute(BaseModel):
    explanation: Optional[str] = None
    """Explanation for why the dispute is considered invalid by the merchant."""

    reason: Literal[
        "automatic_teller_machine_transaction_proof_provided",
        "balance_of_partial_prepayment_not_paid",
        "cardholder_canceled_before_expected_merchandise_receipt_date",
        "cardholder_canceled_before_expected_services_receipt_date",
        "cardholder_canceled_different_date",
        "cardholder_did_not_cancel_according_to_policy",
        "cardholder_received_merchandise",
        "country_code_correct",
        "credit_processed_correctly",
        "currency_correct",
        "dispute_is_for_quality",
        "dispute_is_for_visa_cash_back_transaction_portion",
        "disputed_amount_is_value_added_tax",
        "disputed_amount_is_value_added_tax_no_credit_receipt_provided",
        "limited_return_or_cancellation_policy_properly_disclosed",
        "merchandise_held_at_cardholder_customs_agency",
        "merchandise_matches_description",
        "merchandise_not_counterfeit",
        "merchandise_not_damaged",
        "merchandise_not_defective",
        "merchandise_provided_prior_to_cancellation_date",
        "merchandise_quality_matches_description",
        "merchandise_return_not_attempted",
        "merchant_not_notified_of_closed_account",
        "name_on_flight_manifest_matches_purchase",
        "no_credit_receipt_provided",
        "other",
        "processing_error_incorrect",
        "returned_mechandise_held_at_customs_agency_outside_merchant_country",
        "services_match_description",
        "services_provided_prior_to_cancellation_date",
        "services_used_after_cancellation_date",
        "terms_of_service_not_misrepresented",
        "transaction_code_correct",
    ]
    """The reason a merchant considers the dispute invalid.

    - `automatic_teller_machine_transaction_proof_provided` - Automatic Teller
      Machine (ATM) transaction proof provided.
    - `balance_of_partial_prepayment_not_paid` - Balance of partial prepayment not
      paid.
    - `cardholder_canceled_before_expected_merchandise_receipt_date` - Cardholder
      canceled before expected receipt date of the merchandise.
    - `cardholder_canceled_before_expected_services_receipt_date` - Cardholder
      canceled before expected receipt date of the services.
    - `cardholder_canceled_different_date` - Cardholder canceled on a different date
      than claimed.
    - `cardholder_did_not_cancel_according_to_policy` - Cardholder received did not
      cancel according to policy.
    - `cardholder_received_merchandise` - Cardholder received the merchandise.
    - `country_code_correct` - Country code is correct.
    - `credit_processed_correctly` - Credit was processed correctly.
    - `currency_correct` - Currency is correct.
    - `dispute_is_for_quality` - Dispute is for quality.
    - `dispute_is_for_visa_cash_back_transaction_portion` - Dispute is for Visa Cash
      Back transaction portion.
    - `disputed_amount_is_value_added_tax` - Disputed amount is Value Added Tax
      (VAT).
    - `disputed_amount_is_value_added_tax_no_credit_receipt_provided` - Disputed
      amount is Value Added Tax (VAT) but no credit receipt was provided by the
      cardholder.
    - `limited_return_or_cancellation_policy_properly_disclosed` - Limited return or
      cancellation policy was properly disclosed.
    - `merchandise_held_at_cardholder_customs_agency` - Merchandise held at
      cardholder customs agency.
    - `merchandise_matches_description` - Merchandise matches the merchant's
      description.
    - `merchandise_not_counterfeit` - Merchandise is not counterfeit.
    - `merchandise_not_damaged` - Merchandise is not damaged.
    - `merchandise_not_defective` - Merchandise is not defective.
    - `merchandise_provided_prior_to_cancellation_date` - Merchandise was provided
      prior to the cancellation date.
    - `merchandise_quality_matches_description` - Merchandise quality matches the
      merchant's description.
    - `merchandise_return_not_attempted` - Merchandise was not attempted returned to
      the merchant.
    - `merchant_not_notified_of_closed_account` - Merchant was not notified of the
      closed account.
    - `name_on_flight_manifest_matches_purchase` - Name on manifest of departed
      flight matches name on purchased itinerary.
    - `no_credit_receipt_provided` - No credit receipt was provided by the
      cardholder.
    - `other` - Other.
    - `processing_error_incorrect` - The claimed processing error did not occur.
    - `returned_mechandise_held_at_customs_agency_outside_merchant_country` -
      Returned merchandise held at customs agency outside the merchant's country.
    - `services_match_description` - Services match the merchant's description.
    - `services_provided_prior_to_cancellation_date` - Services were provided prior
      to the cancellation date.
    - `services_used_after_cancellation_date` - Services were used after the
      cancellation date and prior to the dispute submission date.
    - `terms_of_service_not_misrepresented` - Terms of service were not
      misrepresented.
    - `transaction_code_correct` - Transaction code is correct.
    """


class VisaNetworkEventRepresentedNonFiatCurrencyOrNonFungibleTokenReceived(BaseModel):
    blockchain_transaction_hash: str
    """Blockchain transaction hash."""

    destination_wallet_address: str
    """Destination wallet address."""

    prior_approved_transactions: Optional[str] = None
    """Prior approved transactions."""


class VisaNetworkEventRepresentedProofOfCashDisbursement(BaseModel):
    explanation: Optional[str] = None
    """
    Explanation for why the merchant believes the evidence provides proof of cash
    disbursement.
    """


class VisaNetworkEventRepresentedReversalIssued(BaseModel):
    explanation: Optional[str] = None
    """Explanation of the reversal issued by the merchant."""


class VisaNetworkEventRepresented(BaseModel):
    cardholder_no_longer_disputes: Optional[VisaNetworkEventRepresentedCardholderNoLongerDisputes] = None
    """Cardholder no longer disputes details.

    Present if and only if `reason` is `cardholder_no_longer_disputes`.
    """

    credit_or_reversal_processed: Optional[VisaNetworkEventRepresentedCreditOrReversalProcessed] = None
    """Credit or reversal processed details.

    Present if and only if `reason` is `credit_or_reversal_processed`.
    """

    invalid_dispute: Optional[VisaNetworkEventRepresentedInvalidDispute] = None
    """Invalid dispute details. Present if and only if `reason` is `invalid_dispute`."""

    non_fiat_currency_or_non_fungible_token_as_described: Optional[object] = None
    """Non-fiat currency or non-fungible token as described details.

    Present if and only if `reason` is
    `non_fiat_currency_or_non_fungible_token_as_described`.
    """

    non_fiat_currency_or_non_fungible_token_received: Optional[
        VisaNetworkEventRepresentedNonFiatCurrencyOrNonFungibleTokenReceived
    ] = None
    """Non-fiat currency or non-fungible token received details.

    Present if and only if `reason` is
    `non_fiat_currency_or_non_fungible_token_received`.
    """

    proof_of_cash_disbursement: Optional[VisaNetworkEventRepresentedProofOfCashDisbursement] = None
    """Proof of cash disbursement details.

    Present if and only if `reason` is `proof_of_cash_disbursement`.
    """

    reason: Literal[
        "cardholder_no_longer_disputes",
        "credit_or_reversal_processed",
        "invalid_dispute",
        "non_fiat_currency_or_non_fungible_token_as_described",
        "non_fiat_currency_or_non_fungible_token_received",
        "proof_of_cash_disbursement",
        "reversal_issued",
    ]
    """The reason the merchant re-presented the dispute.

    - `cardholder_no_longer_disputes` - Cardholder no longer disputes the
      transaction.
    - `credit_or_reversal_processed` - Credit or reversal was processed.
    - `invalid_dispute` - Invalid dispute.
    - `non_fiat_currency_or_non_fungible_token_as_described` - Non-fiat currency or
      non-fungible token is as described by the merchant.
    - `non_fiat_currency_or_non_fungible_token_received` - Non-fiat currency or
      non-fungible token was received by the cardholder.
    - `proof_of_cash_disbursement` - Proof of cash disbursement provided.
    - `reversal_issued` - Reversal issued by merchant.
    """

    reversal_issued: Optional[VisaNetworkEventRepresentedReversalIssued] = None
    """Reversal issued by merchant details.

    Present if and only if `reason` is `reversal_issued`.
    """


class VisaNetworkEvent(BaseModel):
    attachment_files: List[VisaNetworkEventAttachmentFile]
    """The files attached to the Visa Card Dispute User Submission."""

    category: Literal[
        "chargeback_accepted",
        "chargeback_submitted",
        "chargeback_timed_out",
        "merchant_prearbitration_decline_submitted",
        "merchant_prearbitration_received",
        "merchant_prearbitration_timed_out",
        "represented",
        "representment_timed_out",
        "user_prearbitration_accepted",
        "user_prearbitration_declined",
        "user_prearbitration_submitted",
        "user_prearbitration_timed_out",
        "user_withdrawal_submitted",
    ]
    """The category of the user submission.

    We may add additional possible values for this enum over time; your application
    should be able to handle such additions gracefully.

    - `chargeback_accepted` - Card Dispute Chargeback Accepted Visa Network Event:
      details will be under the `chargeback_accepted` object.
    - `chargeback_submitted` - Card Dispute Chargeback Submitted Visa Network Event:
      details will be under the `chargeback_submitted` object.
    - `chargeback_timed_out` - Card Dispute Chargeback Timed Out Visa Network Event:
      details will be under the `chargeback_timed_out` object.
    - `merchant_prearbitration_decline_submitted` - Card Dispute Merchant
      Pre-Arbitration Decline Submitted Visa Network Event: details will be under
      the `merchant_prearbitration_decline_submitted` object.
    - `merchant_prearbitration_received` - Card Dispute Merchant Pre-Arbitration
      Received Visa Network Event: details will be under the
      `merchant_prearbitration_received` object.
    - `merchant_prearbitration_timed_out` - Card Dispute Merchant Pre-Arbitration
      Timed Out Visa Network Event: details will be under the
      `merchant_prearbitration_timed_out` object.
    - `represented` - Card Dispute Re-presented Visa Network Event: details will be
      under the `represented` object.
    - `representment_timed_out` - Card Dispute Re-presentment Timed Out Visa Network
      Event: details will be under the `representment_timed_out` object.
    - `user_prearbitration_accepted` - Card Dispute User Pre-Arbitration Accepted
      Visa Network Event: details will be under the `user_prearbitration_accepted`
      object.
    - `user_prearbitration_declined` - Card Dispute User Pre-Arbitration Declined
      Visa Network Event: details will be under the `user_prearbitration_declined`
      object.
    - `user_prearbitration_submitted` - Card Dispute User Pre-Arbitration Submitted
      Visa Network Event: details will be under the `user_prearbitration_submitted`
      object.
    - `user_prearbitration_timed_out` - Card Dispute User Pre-Arbitration Timed Out
      Visa Network Event: details will be under the `user_prearbitration_timed_out`
      object.
    - `user_withdrawal_submitted` - Card Dispute User Withdrawal Submitted Visa
      Network Event: details will be under the `user_withdrawal_submitted` object.
    """

    chargeback_accepted: Optional[object] = None
    """A Card Dispute Chargeback Accepted Visa Network Event object.

    This field will be present in the JSON response if and only if `category` is
    equal to `chargeback_accepted`. Contains the details specific to a chargeback
    accepted Visa Card Dispute Network Event, which represents that a chargeback has
    been accepted by the merchant.
    """

    chargeback_submitted: Optional[object] = None
    """A Card Dispute Chargeback Submitted Visa Network Event object.

    This field will be present in the JSON response if and only if `category` is
    equal to `chargeback_submitted`. Contains the details specific to a chargeback
    submitted Visa Card Dispute Network Event, which represents that a chargeback
    has been submitted to the network.
    """

    chargeback_timed_out: Optional[object] = None
    """A Card Dispute Chargeback Timed Out Visa Network Event object.

    This field will be present in the JSON response if and only if `category` is
    equal to `chargeback_timed_out`. Contains the details specific to a chargeback
    timed out Visa Card Dispute Network Event, which represents that the chargeback
    has timed out in the user's favor.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Visa Card Dispute Network Event was created.
    """

    dispute_financial_transaction_id: Optional[str] = None
    """The dispute financial transaction that resulted from the network event, if any."""

    merchant_prearbitration_decline_submitted: Optional[object] = None
    """
    A Card Dispute Merchant Pre-Arbitration Decline Submitted Visa Network Event
    object. This field will be present in the JSON response if and only if
    `category` is equal to `merchant_prearbitration_decline_submitted`. Contains the
    details specific to a merchant prearbitration decline submitted Visa Card
    Dispute Network Event, which represents that the user has declined the
    merchant's request for a prearbitration request decision in their favor.
    """

    merchant_prearbitration_received: Optional[VisaNetworkEventMerchantPrearbitrationReceived] = None
    """A Card Dispute Merchant Pre-Arbitration Received Visa Network Event object.

    This field will be present in the JSON response if and only if `category` is
    equal to `merchant_prearbitration_received`. Contains the details specific to a
    merchant prearbitration received Visa Card Dispute Network Event, which
    represents that the merchant has issued a prearbitration request in the user's
    favor.
    """

    merchant_prearbitration_timed_out: Optional[object] = None
    """A Card Dispute Merchant Pre-Arbitration Timed Out Visa Network Event object.

    This field will be present in the JSON response if and only if `category` is
    equal to `merchant_prearbitration_timed_out`. Contains the details specific to a
    merchant prearbitration timed out Visa Card Dispute Network Event, which
    represents that the user has timed out responding to the merchant's
    prearbitration request.
    """

    represented: Optional[VisaNetworkEventRepresented] = None
    """A Card Dispute Re-presented Visa Network Event object.

    This field will be present in the JSON response if and only if `category` is
    equal to `represented`. Contains the details specific to a re-presented Visa
    Card Dispute Network Event, which represents that the merchant has declined the
    user's chargeback and has re-presented the payment.
    """

    representment_timed_out: Optional[object] = None
    """A Card Dispute Re-presentment Timed Out Visa Network Event object.

    This field will be present in the JSON response if and only if `category` is
    equal to `representment_timed_out`. Contains the details specific to a
    re-presentment time-out Visa Card Dispute Network Event, which represents that
    the user did not respond to the re-presentment by the merchant within the time
    limit.
    """

    user_prearbitration_accepted: Optional[object] = None
    """A Card Dispute User Pre-Arbitration Accepted Visa Network Event object.

    This field will be present in the JSON response if and only if `category` is
    equal to `user_prearbitration_accepted`. Contains the details specific to a user
    prearbitration accepted Visa Card Dispute Network Event, which represents that
    the merchant has accepted the user's prearbitration request in the user's favor.
    """

    user_prearbitration_declined: Optional[object] = None
    """A Card Dispute User Pre-Arbitration Declined Visa Network Event object.

    This field will be present in the JSON response if and only if `category` is
    equal to `user_prearbitration_declined`. Contains the details specific to a user
    prearbitration declined Visa Card Dispute Network Event, which represents that
    the merchant has declined the user's prearbitration request.
    """

    user_prearbitration_submitted: Optional[object] = None
    """A Card Dispute User Pre-Arbitration Submitted Visa Network Event object.

    This field will be present in the JSON response if and only if `category` is
    equal to `user_prearbitration_submitted`. Contains the details specific to a
    user prearbitration submitted Visa Card Dispute Network Event, which represents
    that the user's request for prearbitration has been submitted to the network.
    """

    user_prearbitration_timed_out: Optional[object] = None
    """A Card Dispute User Pre-Arbitration Timed Out Visa Network Event object.

    This field will be present in the JSON response if and only if `category` is
    equal to `user_prearbitration_timed_out`. Contains the details specific to a
    user prearbitration timed out Visa Card Dispute Network Event, which represents
    that the merchant has timed out responding to the user's prearbitration request.
    """

    user_withdrawal_submitted: Optional[object] = None
    """A Card Dispute User Withdrawal Submitted Visa Network Event object.

    This field will be present in the JSON response if and only if `category` is
    equal to `user_withdrawal_submitted`. Contains the details specific to a user
    withdrawal submitted Visa Card Dispute Network Event, which represents that the
    user's request to withdraw the dispute has been submitted to the network.
    """


class VisaUserSubmissionAttachmentFile(BaseModel):
    file_id: str
    """The ID of the file attached to the Card Dispute."""


class VisaUserSubmissionChargebackAuthorization(BaseModel):
    account_status: Literal["account_closed", "credit_problem", "fraud"]
    """Account status.

    - `account_closed` - Account closed.
    - `credit_problem` - Credit problem.
    - `fraud` - Fraud.
    """


class VisaUserSubmissionChargebackConsumerCanceledMerchandiseCardholderCancellation(BaseModel):
    canceled_at: date
    """Canceled at."""

    canceled_prior_to_ship_date: Literal["canceled_prior_to_ship_date", "not_canceled_prior_to_ship_date"]
    """Canceled prior to ship date.

    - `canceled_prior_to_ship_date` - Canceled prior to ship date.
    - `not_canceled_prior_to_ship_date` - Not canceled prior to ship date.
    """

    cancellation_policy_provided: Literal["not_provided", "provided"]
    """Cancellation policy provided.

    - `not_provided` - Not provided.
    - `provided` - Provided.
    """

    reason: str
    """Reason."""


class VisaUserSubmissionChargebackConsumerCanceledMerchandiseReturnAttempted(BaseModel):
    attempt_explanation: str
    """Attempt explanation."""

    attempt_reason: Literal[
        "merchant_not_responding",
        "no_return_authorization_provided",
        "no_return_instructions",
        "requested_not_to_return",
        "return_not_accepted",
    ]
    """Attempt reason.

    - `merchant_not_responding` - Merchant not responding.
    - `no_return_authorization_provided` - No return authorization provided.
    - `no_return_instructions` - No return instructions.
    - `requested_not_to_return` - Requested not to return.
    - `return_not_accepted` - Return not accepted.
    """

    attempted_at: date
    """Attempted at."""

    merchandise_disposition: str
    """Merchandise disposition."""


class VisaUserSubmissionChargebackConsumerCanceledMerchandiseReturned(BaseModel):
    merchant_received_return_at: Optional[date] = None
    """Merchant received return at."""

    other_explanation: Optional[str] = None
    """Other explanation. Required if and only if the return method is `other`."""

    return_method: Literal["dhl", "face_to_face", "fedex", "other", "postal_service", "ups"]
    """Return method.

    - `dhl` - DHL.
    - `face_to_face` - Face-to-face.
    - `fedex` - FedEx.
    - `other` - Other.
    - `postal_service` - Postal service.
    - `ups` - UPS.
    """

    returned_at: date
    """Returned at."""

    tracking_number: Optional[str] = None
    """Tracking number."""


class VisaUserSubmissionChargebackConsumerCanceledMerchandise(BaseModel):
    cardholder_cancellation: Optional[VisaUserSubmissionChargebackConsumerCanceledMerchandiseCardholderCancellation] = (
        None
    )
    """Cardholder cancellation."""

    merchant_resolution_attempted: Literal["attempted", "prohibited_by_local_law"]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    not_returned: Optional[object] = None
    """Not returned. Present if and only if `return_outcome` is `not_returned`."""

    purchase_explanation: str
    """Purchase explanation."""

    received_or_expected_at: date
    """Received or expected at."""

    return_attempted: Optional[VisaUserSubmissionChargebackConsumerCanceledMerchandiseReturnAttempted] = None
    """Return attempted.

    Present if and only if `return_outcome` is `return_attempted`.
    """

    return_outcome: Literal["not_returned", "returned", "return_attempted"]
    """Return outcome.

    - `not_returned` - Not returned.
    - `returned` - Returned.
    - `return_attempted` - Return attempted.
    """

    returned: Optional[VisaUserSubmissionChargebackConsumerCanceledMerchandiseReturned] = None
    """Returned. Present if and only if `return_outcome` is `returned`."""


class VisaUserSubmissionChargebackConsumerCanceledRecurringTransactionMerchantContactMethods(BaseModel):
    application_name: Optional[str] = None
    """Application name."""

    call_center_phone_number: Optional[str] = None
    """Call center phone number."""

    email_address: Optional[str] = None
    """Email address."""

    in_person_address: Optional[str] = None
    """In person address."""

    mailing_address: Optional[str] = None
    """Mailing address."""

    text_phone_number: Optional[str] = None
    """Text phone number."""


class VisaUserSubmissionChargebackConsumerCanceledRecurringTransaction(BaseModel):
    cancellation_target: Literal["account", "transaction"]
    """Cancellation target.

    - `account` - Account.
    - `transaction` - Transaction.
    """

    merchant_contact_methods: VisaUserSubmissionChargebackConsumerCanceledRecurringTransactionMerchantContactMethods
    """Merchant contact methods."""

    other_form_of_payment_explanation: Optional[str] = None
    """Other form of payment explanation."""

    transaction_or_account_canceled_at: date
    """Transaction or account canceled at."""


class VisaUserSubmissionChargebackConsumerCanceledServicesCardholderCancellation(BaseModel):
    canceled_at: date
    """Canceled at."""

    cancellation_policy_provided: Literal["not_provided", "provided"]
    """Cancellation policy provided.

    - `not_provided` - Not provided.
    - `provided` - Provided.
    """

    reason: str
    """Reason."""


class VisaUserSubmissionChargebackConsumerCanceledServicesGuaranteedReservation(BaseModel):
    explanation: Literal[
        "cardholder_canceled_prior_to_service",
        "cardholder_cancellation_attempt_within_24_hours_of_confirmation",
        "merchant_billed_no_show",
    ]
    """Explanation.

    - `cardholder_canceled_prior_to_service` - Cardholder canceled prior to service.
    - `cardholder_cancellation_attempt_within_24_hours_of_confirmation` - Cardholder
      cancellation attempt within 24 hours of confirmation.
    - `merchant_billed_no_show` - Merchant billed for no-show.
    """


class VisaUserSubmissionChargebackConsumerCanceledServices(BaseModel):
    cardholder_cancellation: VisaUserSubmissionChargebackConsumerCanceledServicesCardholderCancellation
    """Cardholder cancellation."""

    contracted_at: date
    """Contracted at."""

    guaranteed_reservation: Optional[VisaUserSubmissionChargebackConsumerCanceledServicesGuaranteedReservation] = None
    """Guaranteed reservation explanation.

    Present if and only if `service_type` is `guaranteed_reservation`.
    """

    merchant_resolution_attempted: Literal["attempted", "prohibited_by_local_law"]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    other: Optional[object] = None
    """Other service type explanation.

    Present if and only if `service_type` is `other`.
    """

    purchase_explanation: str
    """Purchase explanation."""

    service_type: Literal["guaranteed_reservation", "other", "timeshare"]
    """Service type.

    - `guaranteed_reservation` - Guaranteed reservation.
    - `other` - Other.
    - `timeshare` - Timeshare.
    """

    timeshare: Optional[object] = None
    """Timeshare explanation. Present if and only if `service_type` is `timeshare`."""


class VisaUserSubmissionChargebackConsumerCounterfeitMerchandise(BaseModel):
    counterfeit_explanation: str
    """Counterfeit explanation."""

    disposition_explanation: str
    """Disposition explanation."""

    order_explanation: str
    """Order explanation."""

    received_at: date
    """Received at."""


class VisaUserSubmissionChargebackConsumerCreditNotProcessed(BaseModel):
    canceled_or_returned_at: Optional[date] = None
    """Canceled or returned at."""

    credit_expected_at: Optional[date] = None
    """Credit expected at."""


class VisaUserSubmissionChargebackConsumerDamagedOrDefectiveMerchandiseReturnAttempted(BaseModel):
    attempt_explanation: str
    """Attempt explanation."""

    attempt_reason: Literal[
        "merchant_not_responding",
        "no_return_authorization_provided",
        "no_return_instructions",
        "requested_not_to_return",
        "return_not_accepted",
    ]
    """Attempt reason.

    - `merchant_not_responding` - Merchant not responding.
    - `no_return_authorization_provided` - No return authorization provided.
    - `no_return_instructions` - No return instructions.
    - `requested_not_to_return` - Requested not to return.
    - `return_not_accepted` - Return not accepted.
    """

    attempted_at: date
    """Attempted at."""

    merchandise_disposition: str
    """Merchandise disposition."""


class VisaUserSubmissionChargebackConsumerDamagedOrDefectiveMerchandiseReturned(BaseModel):
    merchant_received_return_at: Optional[date] = None
    """Merchant received return at."""

    other_explanation: Optional[str] = None
    """Other explanation. Required if and only if the return method is `other`."""

    return_method: Literal["dhl", "face_to_face", "fedex", "other", "postal_service", "ups"]
    """Return method.

    - `dhl` - DHL.
    - `face_to_face` - Face-to-face.
    - `fedex` - FedEx.
    - `other` - Other.
    - `postal_service` - Postal service.
    - `ups` - UPS.
    """

    returned_at: date
    """Returned at."""

    tracking_number: Optional[str] = None
    """Tracking number."""


class VisaUserSubmissionChargebackConsumerDamagedOrDefectiveMerchandise(BaseModel):
    merchant_resolution_attempted: Literal["attempted", "prohibited_by_local_law"]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    not_returned: Optional[object] = None
    """Not returned. Present if and only if `return_outcome` is `not_returned`."""

    order_and_issue_explanation: str
    """Order and issue explanation."""

    received_at: date
    """Received at."""

    return_attempted: Optional[VisaUserSubmissionChargebackConsumerDamagedOrDefectiveMerchandiseReturnAttempted] = None
    """Return attempted.

    Present if and only if `return_outcome` is `return_attempted`.
    """

    return_outcome: Literal["not_returned", "returned", "return_attempted"]
    """Return outcome.

    - `not_returned` - Not returned.
    - `returned` - Returned.
    - `return_attempted` - Return attempted.
    """

    returned: Optional[VisaUserSubmissionChargebackConsumerDamagedOrDefectiveMerchandiseReturned] = None
    """Returned. Present if and only if `return_outcome` is `returned`."""


class VisaUserSubmissionChargebackConsumerMerchandiseMisrepresentationReturnAttempted(BaseModel):
    attempt_explanation: str
    """Attempt explanation."""

    attempt_reason: Literal[
        "merchant_not_responding",
        "no_return_authorization_provided",
        "no_return_instructions",
        "requested_not_to_return",
        "return_not_accepted",
    ]
    """Attempt reason.

    - `merchant_not_responding` - Merchant not responding.
    - `no_return_authorization_provided` - No return authorization provided.
    - `no_return_instructions` - No return instructions.
    - `requested_not_to_return` - Requested not to return.
    - `return_not_accepted` - Return not accepted.
    """

    attempted_at: date
    """Attempted at."""

    merchandise_disposition: str
    """Merchandise disposition."""


class VisaUserSubmissionChargebackConsumerMerchandiseMisrepresentationReturned(BaseModel):
    merchant_received_return_at: Optional[date] = None
    """Merchant received return at."""

    other_explanation: Optional[str] = None
    """Other explanation. Required if and only if the return method is `other`."""

    return_method: Literal["dhl", "face_to_face", "fedex", "other", "postal_service", "ups"]
    """Return method.

    - `dhl` - DHL.
    - `face_to_face` - Face-to-face.
    - `fedex` - FedEx.
    - `other` - Other.
    - `postal_service` - Postal service.
    - `ups` - UPS.
    """

    returned_at: date
    """Returned at."""

    tracking_number: Optional[str] = None
    """Tracking number."""


class VisaUserSubmissionChargebackConsumerMerchandiseMisrepresentation(BaseModel):
    merchant_resolution_attempted: Literal["attempted", "prohibited_by_local_law"]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    misrepresentation_explanation: str
    """Misrepresentation explanation."""

    not_returned: Optional[object] = None
    """Not returned. Present if and only if `return_outcome` is `not_returned`."""

    purchase_explanation: str
    """Purchase explanation."""

    received_at: date
    """Received at."""

    return_attempted: Optional[VisaUserSubmissionChargebackConsumerMerchandiseMisrepresentationReturnAttempted] = None
    """Return attempted.

    Present if and only if `return_outcome` is `return_attempted`.
    """

    return_outcome: Literal["not_returned", "returned", "return_attempted"]
    """Return outcome.

    - `not_returned` - Not returned.
    - `returned` - Returned.
    - `return_attempted` - Return attempted.
    """

    returned: Optional[VisaUserSubmissionChargebackConsumerMerchandiseMisrepresentationReturned] = None
    """Returned. Present if and only if `return_outcome` is `returned`."""


class VisaUserSubmissionChargebackConsumerMerchandiseNotAsDescribedReturnAttempted(BaseModel):
    attempt_explanation: str
    """Attempt explanation."""

    attempt_reason: Literal[
        "merchant_not_responding",
        "no_return_authorization_provided",
        "no_return_instructions",
        "requested_not_to_return",
        "return_not_accepted",
    ]
    """Attempt reason.

    - `merchant_not_responding` - Merchant not responding.
    - `no_return_authorization_provided` - No return authorization provided.
    - `no_return_instructions` - No return instructions.
    - `requested_not_to_return` - Requested not to return.
    - `return_not_accepted` - Return not accepted.
    """

    attempted_at: date
    """Attempted at."""

    merchandise_disposition: str
    """Merchandise disposition."""


class VisaUserSubmissionChargebackConsumerMerchandiseNotAsDescribedReturned(BaseModel):
    merchant_received_return_at: Optional[date] = None
    """Merchant received return at."""

    other_explanation: Optional[str] = None
    """Other explanation. Required if and only if the return method is `other`."""

    return_method: Literal["dhl", "face_to_face", "fedex", "other", "postal_service", "ups"]
    """Return method.

    - `dhl` - DHL.
    - `face_to_face` - Face-to-face.
    - `fedex` - FedEx.
    - `other` - Other.
    - `postal_service` - Postal service.
    - `ups` - UPS.
    """

    returned_at: date
    """Returned at."""

    tracking_number: Optional[str] = None
    """Tracking number."""


class VisaUserSubmissionChargebackConsumerMerchandiseNotAsDescribed(BaseModel):
    merchant_resolution_attempted: Literal["attempted", "prohibited_by_local_law"]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    received_at: date
    """Received at."""

    return_attempted: Optional[VisaUserSubmissionChargebackConsumerMerchandiseNotAsDescribedReturnAttempted] = None
    """Return attempted.

    Present if and only if `return_outcome` is `return_attempted`.
    """

    return_outcome: Literal["returned", "return_attempted"]
    """Return outcome.

    - `returned` - Returned.
    - `return_attempted` - Return attempted.
    """

    returned: Optional[VisaUserSubmissionChargebackConsumerMerchandiseNotAsDescribedReturned] = None
    """Returned. Present if and only if `return_outcome` is `returned`."""


class VisaUserSubmissionChargebackConsumerMerchandiseNotReceivedCardholderCancellationPriorToExpectedReceipt(BaseModel):
    canceled_at: date
    """Canceled at."""

    reason: Optional[str] = None
    """Reason."""


class VisaUserSubmissionChargebackConsumerMerchandiseNotReceivedDelayedReturnAttempted(BaseModel):
    attempted_at: date
    """Attempted at."""


class VisaUserSubmissionChargebackConsumerMerchandiseNotReceivedDelayedReturned(BaseModel):
    merchant_received_return_at: date
    """Merchant received return at."""

    returned_at: date
    """Returned at."""


class VisaUserSubmissionChargebackConsumerMerchandiseNotReceivedDelayed(BaseModel):
    explanation: str
    """Explanation."""

    not_returned: Optional[object] = None
    """Not returned. Present if and only if `return_outcome` is `not_returned`."""

    return_attempted: Optional[VisaUserSubmissionChargebackConsumerMerchandiseNotReceivedDelayedReturnAttempted] = None
    """Return attempted.

    Present if and only if `return_outcome` is `return_attempted`.
    """

    return_outcome: Literal["not_returned", "returned", "return_attempted"]
    """Return outcome.

    - `not_returned` - Not returned.
    - `returned` - Returned.
    - `return_attempted` - Return attempted.
    """

    returned: Optional[VisaUserSubmissionChargebackConsumerMerchandiseNotReceivedDelayedReturned] = None
    """Returned. Present if and only if `return_outcome` is `returned`."""


class VisaUserSubmissionChargebackConsumerMerchandiseNotReceivedDeliveredToWrongLocation(BaseModel):
    agreed_location: str
    """Agreed location."""


class VisaUserSubmissionChargebackConsumerMerchandiseNotReceivedMerchantCancellation(BaseModel):
    canceled_at: date
    """Canceled at."""


class VisaUserSubmissionChargebackConsumerMerchandiseNotReceived(BaseModel):
    cancellation_outcome: Literal[
        "cardholder_cancellation_prior_to_expected_receipt", "merchant_cancellation", "no_cancellation"
    ]
    """Cancellation outcome.

    - `cardholder_cancellation_prior_to_expected_receipt` - Cardholder cancellation
      prior to expected receipt.
    - `merchant_cancellation` - Merchant cancellation.
    - `no_cancellation` - No cancellation.
    """

    cardholder_cancellation_prior_to_expected_receipt: Optional[
        VisaUserSubmissionChargebackConsumerMerchandiseNotReceivedCardholderCancellationPriorToExpectedReceipt
    ] = None
    """Cardholder cancellation prior to expected receipt.

    Present if and only if `cancellation_outcome` is
    `cardholder_cancellation_prior_to_expected_receipt`.
    """

    delayed: Optional[VisaUserSubmissionChargebackConsumerMerchandiseNotReceivedDelayed] = None
    """Delayed. Present if and only if `delivery_issue` is `delayed`."""

    delivered_to_wrong_location: Optional[
        VisaUserSubmissionChargebackConsumerMerchandiseNotReceivedDeliveredToWrongLocation
    ] = None
    """Delivered to wrong location.

    Present if and only if `delivery_issue` is `delivered_to_wrong_location`.
    """

    delivery_issue: Literal["delayed", "delivered_to_wrong_location"]
    """Delivery issue.

    - `delayed` - Delayed.
    - `delivered_to_wrong_location` - Delivered to wrong location.
    """

    last_expected_receipt_at: date
    """Last expected receipt at."""

    merchant_cancellation: Optional[VisaUserSubmissionChargebackConsumerMerchandiseNotReceivedMerchantCancellation] = (
        None
    )
    """Merchant cancellation.

    Present if and only if `cancellation_outcome` is `merchant_cancellation`.
    """

    merchant_resolution_attempted: Literal["attempted", "prohibited_by_local_law"]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    no_cancellation: Optional[object] = None
    """No cancellation.

    Present if and only if `cancellation_outcome` is `no_cancellation`.
    """

    purchase_info_and_explanation: str
    """Purchase information and explanation."""


class VisaUserSubmissionChargebackConsumerOriginalCreditTransactionNotAccepted(BaseModel):
    explanation: str
    """Explanation."""

    reason: Literal["prohibited_by_local_laws_or_regulation", "recipient_refused"]
    """Reason.

    - `prohibited_by_local_laws_or_regulation` - Prohibited by local laws or
      regulation.
    - `recipient_refused` - Recipient refused.
    """


class VisaUserSubmissionChargebackConsumerQualityMerchandiseOngoingNegotiations(BaseModel):
    explanation: str
    """
    Explanation of the previous ongoing negotiations between the cardholder and
    merchant.
    """

    issuer_first_notified_at: date
    """Date the cardholder first notified the issuer of the dispute."""

    started_at: date
    """Started at."""


class VisaUserSubmissionChargebackConsumerQualityMerchandiseReturnAttempted(BaseModel):
    attempt_explanation: str
    """Attempt explanation."""

    attempt_reason: Literal[
        "merchant_not_responding",
        "no_return_authorization_provided",
        "no_return_instructions",
        "requested_not_to_return",
        "return_not_accepted",
    ]
    """Attempt reason.

    - `merchant_not_responding` - Merchant not responding.
    - `no_return_authorization_provided` - No return authorization provided.
    - `no_return_instructions` - No return instructions.
    - `requested_not_to_return` - Requested not to return.
    - `return_not_accepted` - Return not accepted.
    """

    attempted_at: date
    """Attempted at."""

    merchandise_disposition: str
    """Merchandise disposition."""


class VisaUserSubmissionChargebackConsumerQualityMerchandiseReturned(BaseModel):
    merchant_received_return_at: Optional[date] = None
    """Merchant received return at."""

    other_explanation: Optional[str] = None
    """Other explanation. Required if and only if the return method is `other`."""

    return_method: Literal["dhl", "face_to_face", "fedex", "other", "postal_service", "ups"]
    """Return method.

    - `dhl` - DHL.
    - `face_to_face` - Face-to-face.
    - `fedex` - FedEx.
    - `other` - Other.
    - `postal_service` - Postal service.
    - `ups` - UPS.
    """

    returned_at: date
    """Returned at."""

    tracking_number: Optional[str] = None
    """Tracking number."""


class VisaUserSubmissionChargebackConsumerQualityMerchandise(BaseModel):
    expected_at: date
    """Expected at."""

    merchant_resolution_attempted: Literal["attempted", "prohibited_by_local_law"]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    not_returned: Optional[object] = None
    """Not returned. Present if and only if `return_outcome` is `not_returned`."""

    ongoing_negotiations: Optional[VisaUserSubmissionChargebackConsumerQualityMerchandiseOngoingNegotiations] = None
    """Ongoing negotiations. Exclude if there is no evidence of ongoing negotiations."""

    purchase_info_and_quality_issue: str
    """Purchase information and quality issue."""

    received_at: date
    """Received at."""

    return_attempted: Optional[VisaUserSubmissionChargebackConsumerQualityMerchandiseReturnAttempted] = None
    """Return attempted.

    Present if and only if `return_outcome` is `return_attempted`.
    """

    return_outcome: Literal["not_returned", "returned", "return_attempted"]
    """Return outcome.

    - `not_returned` - Not returned.
    - `returned` - Returned.
    - `return_attempted` - Return attempted.
    """

    returned: Optional[VisaUserSubmissionChargebackConsumerQualityMerchandiseReturned] = None
    """Returned. Present if and only if `return_outcome` is `returned`."""


class VisaUserSubmissionChargebackConsumerQualityServicesCardholderCancellation(BaseModel):
    accepted_by_merchant: Literal["accepted", "not_accepted"]
    """Accepted by merchant.

    - `accepted` - Accepted.
    - `not_accepted` - Not accepted.
    """

    canceled_at: date
    """Canceled at."""

    reason: str
    """Reason."""


class VisaUserSubmissionChargebackConsumerQualityServicesOngoingNegotiations(BaseModel):
    explanation: str
    """
    Explanation of the previous ongoing negotiations between the cardholder and
    merchant.
    """

    issuer_first_notified_at: date
    """Date the cardholder first notified the issuer of the dispute."""

    started_at: date
    """Started at."""


class VisaUserSubmissionChargebackConsumerQualityServices(BaseModel):
    cardholder_cancellation: VisaUserSubmissionChargebackConsumerQualityServicesCardholderCancellation
    """Cardholder cancellation."""

    cardholder_paid_to_have_work_redone: Optional[
        Literal["did_not_pay_to_have_work_redone", "paid_to_have_work_redone"]
    ] = None
    """Cardholder paid to have work redone.

    - `did_not_pay_to_have_work_redone` - Cardholder did not pay to have work
      redone.
    - `paid_to_have_work_redone` - Cardholder paid to have work redone.
    """

    non_fiat_currency_or_non_fungible_token_related_and_not_matching_description: Literal["not_related", "related"]
    """Non-fiat currency or non-fungible token related and not matching description.

    - `not_related` - Not related.
    - `related` - Related.
    """

    ongoing_negotiations: Optional[VisaUserSubmissionChargebackConsumerQualityServicesOngoingNegotiations] = None
    """Ongoing negotiations. Exclude if there is no evidence of ongoing negotiations."""

    purchase_info_and_quality_issue: str
    """Purchase information and quality issue."""

    restaurant_food_related: Optional[Literal["not_related", "related"]] = None
    """
    Whether the dispute is related to the quality of food from an eating place or
    restaurant. Must be provided when Merchant Category Code (MCC) is 5812, 5813
    or 5814.

    - `not_related` - Not related.
    - `related` - Related.
    """

    services_received_at: date
    """Services received at."""


class VisaUserSubmissionChargebackConsumerServicesMisrepresentationCardholderCancellation(BaseModel):
    accepted_by_merchant: Literal["accepted", "not_accepted"]
    """Accepted by merchant.

    - `accepted` - Accepted.
    - `not_accepted` - Not accepted.
    """

    canceled_at: date
    """Canceled at."""

    reason: str
    """Reason."""


class VisaUserSubmissionChargebackConsumerServicesMisrepresentation(BaseModel):
    cardholder_cancellation: VisaUserSubmissionChargebackConsumerServicesMisrepresentationCardholderCancellation
    """Cardholder cancellation."""

    merchant_resolution_attempted: Literal["attempted", "prohibited_by_local_law"]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    misrepresentation_explanation: str
    """Misrepresentation explanation."""

    purchase_explanation: str
    """Purchase explanation."""

    received_at: date
    """Received at."""


class VisaUserSubmissionChargebackConsumerServicesNotAsDescribedCardholderCancellation(BaseModel):
    accepted_by_merchant: Literal["accepted", "not_accepted"]
    """Accepted by merchant.

    - `accepted` - Accepted.
    - `not_accepted` - Not accepted.
    """

    canceled_at: date
    """Canceled at."""

    reason: str
    """Reason."""


class VisaUserSubmissionChargebackConsumerServicesNotAsDescribed(BaseModel):
    cardholder_cancellation: VisaUserSubmissionChargebackConsumerServicesNotAsDescribedCardholderCancellation
    """Cardholder cancellation."""

    merchant_resolution_attempted: Literal["attempted", "prohibited_by_local_law"]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    received_at: date
    """Received at."""


class VisaUserSubmissionChargebackConsumerServicesNotReceivedCardholderCancellationPriorToExpectedReceipt(BaseModel):
    canceled_at: date
    """Canceled at."""

    reason: Optional[str] = None
    """Reason."""


class VisaUserSubmissionChargebackConsumerServicesNotReceivedMerchantCancellation(BaseModel):
    canceled_at: date
    """Canceled at."""


class VisaUserSubmissionChargebackConsumerServicesNotReceived(BaseModel):
    cancellation_outcome: Literal[
        "cardholder_cancellation_prior_to_expected_receipt", "merchant_cancellation", "no_cancellation"
    ]
    """Cancellation outcome.

    - `cardholder_cancellation_prior_to_expected_receipt` - Cardholder cancellation
      prior to expected receipt.
    - `merchant_cancellation` - Merchant cancellation.
    - `no_cancellation` - No cancellation.
    """

    cardholder_cancellation_prior_to_expected_receipt: Optional[
        VisaUserSubmissionChargebackConsumerServicesNotReceivedCardholderCancellationPriorToExpectedReceipt
    ] = None
    """Cardholder cancellation prior to expected receipt.

    Present if and only if `cancellation_outcome` is
    `cardholder_cancellation_prior_to_expected_receipt`.
    """

    last_expected_receipt_at: date
    """Last expected receipt at."""

    merchant_cancellation: Optional[VisaUserSubmissionChargebackConsumerServicesNotReceivedMerchantCancellation] = None
    """Merchant cancellation.

    Present if and only if `cancellation_outcome` is `merchant_cancellation`.
    """

    merchant_resolution_attempted: Literal["attempted", "prohibited_by_local_law"]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    no_cancellation: Optional[object] = None
    """No cancellation.

    Present if and only if `cancellation_outcome` is `no_cancellation`.
    """

    purchase_info_and_explanation: str
    """Purchase information and explanation."""


class VisaUserSubmissionChargebackFraud(BaseModel):
    fraud_type: Literal[
        "account_or_credentials_takeover",
        "card_not_received_as_issued",
        "fraudulent_application",
        "fraudulent_use_of_account_number",
        "incorrect_processing",
        "issuer_reported_counterfeit",
        "lost",
        "manipulation_of_account_holder",
        "merchant_misrepresentation",
        "miscellaneous",
        "stolen",
    ]
    """Fraud type.

    - `account_or_credentials_takeover` - Account or credentials takeover.
    - `card_not_received_as_issued` - Card not received as issued.
    - `fraudulent_application` - Fraudulent application.
    - `fraudulent_use_of_account_number` - Fraudulent use of account number.
    - `incorrect_processing` - Incorrect processing.
    - `issuer_reported_counterfeit` - Issuer reported counterfeit.
    - `lost` - Lost.
    - `manipulation_of_account_holder` - Manipulation of account holder.
    - `merchant_misrepresentation` - Merchant misrepresentation.
    - `miscellaneous` - Miscellaneous.
    - `stolen` - Stolen.
    """


class VisaUserSubmissionChargebackProcessingErrorDuplicateTransaction(BaseModel):
    other_transaction_id: str
    """Other transaction ID."""


class VisaUserSubmissionChargebackProcessingErrorIncorrectAmount(BaseModel):
    expected_amount: int
    """Expected amount."""


class VisaUserSubmissionChargebackProcessingErrorPaidByOtherMeans(BaseModel):
    other_form_of_payment_evidence: Literal[
        "canceled_check", "card_transaction", "cash_receipt", "other", "statement", "voucher"
    ]
    """Other form of payment evidence.

    - `canceled_check` - Canceled check.
    - `card_transaction` - Card transaction.
    - `cash_receipt` - Cash receipt.
    - `other` - Other.
    - `statement` - Statement.
    - `voucher` - Voucher.
    """

    other_transaction_id: Optional[str] = None
    """Other transaction ID."""


class VisaUserSubmissionChargebackProcessingError(BaseModel):
    duplicate_transaction: Optional[VisaUserSubmissionChargebackProcessingErrorDuplicateTransaction] = None
    """Duplicate transaction.

    Present if and only if `error_reason` is `duplicate_transaction`.
    """

    error_reason: Literal["duplicate_transaction", "incorrect_amount", "paid_by_other_means"]
    """Error reason.

    - `duplicate_transaction` - Duplicate transaction.
    - `incorrect_amount` - Incorrect amount.
    - `paid_by_other_means` - Paid by other means.
    """

    incorrect_amount: Optional[VisaUserSubmissionChargebackProcessingErrorIncorrectAmount] = None
    """Incorrect amount. Present if and only if `error_reason` is `incorrect_amount`."""

    merchant_resolution_attempted: Literal["attempted", "prohibited_by_local_law"]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    paid_by_other_means: Optional[VisaUserSubmissionChargebackProcessingErrorPaidByOtherMeans] = None
    """Paid by other means.

    Present if and only if `error_reason` is `paid_by_other_means`.
    """


class VisaUserSubmissionChargeback(BaseModel):
    authorization: Optional[VisaUserSubmissionChargebackAuthorization] = None
    """Authorization. Present if and only if `category` is `authorization`."""

    category: Literal[
        "authorization",
        "consumer_canceled_merchandise",
        "consumer_canceled_recurring_transaction",
        "consumer_canceled_services",
        "consumer_counterfeit_merchandise",
        "consumer_credit_not_processed",
        "consumer_damaged_or_defective_merchandise",
        "consumer_merchandise_misrepresentation",
        "consumer_merchandise_not_as_described",
        "consumer_merchandise_not_received",
        "consumer_non_receipt_of_cash",
        "consumer_original_credit_transaction_not_accepted",
        "consumer_quality_merchandise",
        "consumer_quality_services",
        "consumer_services_misrepresentation",
        "consumer_services_not_as_described",
        "consumer_services_not_received",
        "fraud",
        "processing_error",
    ]
    """Category.

    - `authorization` - Authorization.
    - `consumer_canceled_merchandise` - Consumer: canceled merchandise.
    - `consumer_canceled_recurring_transaction` - Consumer: canceled recurring
      transaction.
    - `consumer_canceled_services` - Consumer: canceled services.
    - `consumer_counterfeit_merchandise` - Consumer: counterfeit merchandise.
    - `consumer_credit_not_processed` - Consumer: credit not processed.
    - `consumer_damaged_or_defective_merchandise` - Consumer: damaged or defective
      merchandise.
    - `consumer_merchandise_misrepresentation` - Consumer: merchandise
      misrepresentation.
    - `consumer_merchandise_not_as_described` - Consumer: merchandise not as
      described.
    - `consumer_merchandise_not_received` - Consumer: merchandise not received.
    - `consumer_non_receipt_of_cash` - Consumer: non-receipt of cash.
    - `consumer_original_credit_transaction_not_accepted` - Consumer: Original
      Credit Transaction (OCT) not accepted.
    - `consumer_quality_merchandise` - Consumer: merchandise quality issue.
    - `consumer_quality_services` - Consumer: services quality issue.
    - `consumer_services_misrepresentation` - Consumer: services misrepresentation.
    - `consumer_services_not_as_described` - Consumer: services not as described.
    - `consumer_services_not_received` - Consumer: services not received.
    - `fraud` - Fraud.
    - `processing_error` - Processing error.
    """

    consumer_canceled_merchandise: Optional[VisaUserSubmissionChargebackConsumerCanceledMerchandise] = None
    """Canceled merchandise.

    Present if and only if `category` is `consumer_canceled_merchandise`.
    """

    consumer_canceled_recurring_transaction: Optional[
        VisaUserSubmissionChargebackConsumerCanceledRecurringTransaction
    ] = None
    """Canceled recurring transaction.

    Present if and only if `category` is `consumer_canceled_recurring_transaction`.
    """

    consumer_canceled_services: Optional[VisaUserSubmissionChargebackConsumerCanceledServices] = None
    """Canceled services.

    Present if and only if `category` is `consumer_canceled_services`.
    """

    consumer_counterfeit_merchandise: Optional[VisaUserSubmissionChargebackConsumerCounterfeitMerchandise] = None
    """Counterfeit merchandise.

    Present if and only if `category` is `consumer_counterfeit_merchandise`.
    """

    consumer_credit_not_processed: Optional[VisaUserSubmissionChargebackConsumerCreditNotProcessed] = None
    """Credit not processed.

    Present if and only if `category` is `consumer_credit_not_processed`.
    """

    consumer_damaged_or_defective_merchandise: Optional[
        VisaUserSubmissionChargebackConsumerDamagedOrDefectiveMerchandise
    ] = None
    """Damaged or defective merchandise.

    Present if and only if `category` is
    `consumer_damaged_or_defective_merchandise`.
    """

    consumer_merchandise_misrepresentation: Optional[
        VisaUserSubmissionChargebackConsumerMerchandiseMisrepresentation
    ] = None
    """Merchandise misrepresentation.

    Present if and only if `category` is `consumer_merchandise_misrepresentation`.
    """

    consumer_merchandise_not_as_described: Optional[VisaUserSubmissionChargebackConsumerMerchandiseNotAsDescribed] = (
        None
    )
    """Merchandise not as described.

    Present if and only if `category` is `consumer_merchandise_not_as_described`.
    """

    consumer_merchandise_not_received: Optional[VisaUserSubmissionChargebackConsumerMerchandiseNotReceived] = None
    """Merchandise not received.

    Present if and only if `category` is `consumer_merchandise_not_received`.
    """

    consumer_non_receipt_of_cash: Optional[object] = None
    """Non-receipt of cash.

    Present if and only if `category` is `consumer_non_receipt_of_cash`.
    """

    consumer_original_credit_transaction_not_accepted: Optional[
        VisaUserSubmissionChargebackConsumerOriginalCreditTransactionNotAccepted
    ] = None
    """Original Credit Transaction (OCT) not accepted.

    Present if and only if `category` is
    `consumer_original_credit_transaction_not_accepted`.
    """

    consumer_quality_merchandise: Optional[VisaUserSubmissionChargebackConsumerQualityMerchandise] = None
    """Merchandise quality issue.

    Present if and only if `category` is `consumer_quality_merchandise`.
    """

    consumer_quality_services: Optional[VisaUserSubmissionChargebackConsumerQualityServices] = None
    """Services quality issue.

    Present if and only if `category` is `consumer_quality_services`.
    """

    consumer_services_misrepresentation: Optional[VisaUserSubmissionChargebackConsumerServicesMisrepresentation] = None
    """Services misrepresentation.

    Present if and only if `category` is `consumer_services_misrepresentation`.
    """

    consumer_services_not_as_described: Optional[VisaUserSubmissionChargebackConsumerServicesNotAsDescribed] = None
    """Services not as described.

    Present if and only if `category` is `consumer_services_not_as_described`.
    """

    consumer_services_not_received: Optional[VisaUserSubmissionChargebackConsumerServicesNotReceived] = None
    """Services not received.

    Present if and only if `category` is `consumer_services_not_received`.
    """

    fraud: Optional[VisaUserSubmissionChargebackFraud] = None
    """Fraud. Present if and only if `category` is `fraud`."""

    processing_error: Optional[VisaUserSubmissionChargebackProcessingError] = None
    """Processing error. Present if and only if `category` is `processing_error`."""


class VisaUserSubmissionMerchantPrearbitrationDecline(BaseModel):
    reason: str
    """
    The reason the user declined the merchant's request for pre-arbitration in their
    favor.
    """


class VisaUserSubmissionUserPrearbitrationCategoryChange(BaseModel):
    category: Literal[
        "authorization",
        "consumer_canceled_merchandise",
        "consumer_canceled_recurring_transaction",
        "consumer_canceled_services",
        "consumer_counterfeit_merchandise",
        "consumer_credit_not_processed",
        "consumer_damaged_or_defective_merchandise",
        "consumer_merchandise_misrepresentation",
        "consumer_merchandise_not_as_described",
        "consumer_merchandise_not_received",
        "consumer_non_receipt_of_cash",
        "consumer_original_credit_transaction_not_accepted",
        "consumer_quality_merchandise",
        "consumer_quality_services",
        "consumer_services_misrepresentation",
        "consumer_services_not_as_described",
        "consumer_services_not_received",
        "fraud",
        "processing_error",
    ]
    """The category the dispute is being changed to.

    - `authorization` - Authorization.
    - `consumer_canceled_merchandise` - Consumer: canceled merchandise.
    - `consumer_canceled_recurring_transaction` - Consumer: canceled recurring
      transaction.
    - `consumer_canceled_services` - Consumer: canceled services.
    - `consumer_counterfeit_merchandise` - Consumer: counterfeit merchandise.
    - `consumer_credit_not_processed` - Consumer: credit not processed.
    - `consumer_damaged_or_defective_merchandise` - Consumer: damaged or defective
      merchandise.
    - `consumer_merchandise_misrepresentation` - Consumer: merchandise
      misrepresentation.
    - `consumer_merchandise_not_as_described` - Consumer: merchandise not as
      described.
    - `consumer_merchandise_not_received` - Consumer: merchandise not received.
    - `consumer_non_receipt_of_cash` - Consumer: non-receipt of cash.
    - `consumer_original_credit_transaction_not_accepted` - Consumer: Original
      Credit Transaction (OCT) not accepted.
    - `consumer_quality_merchandise` - Consumer: merchandise quality issue.
    - `consumer_quality_services` - Consumer: services quality issue.
    - `consumer_services_misrepresentation` - Consumer: services misrepresentation.
    - `consumer_services_not_as_described` - Consumer: services not as described.
    - `consumer_services_not_received` - Consumer: services not received.
    - `fraud` - Fraud.
    - `processing_error` - Processing error.
    """

    reason: str
    """The reason for the pre-arbitration request."""


class VisaUserSubmissionUserPrearbitration(BaseModel):
    category_change: Optional[VisaUserSubmissionUserPrearbitrationCategoryChange] = None
    """Category change details for the pre-arbitration request, if requested."""

    reason: str
    """The reason for the pre-arbitration request."""


class VisaUserSubmission(BaseModel):
    accepted_at: Optional[datetime] = None
    """
    The date and time at which the Visa Card Dispute User Submission was reviewed
    and accepted.
    """

    amount: Optional[int] = None
    """
    The amount of the dispute if it is different from the amount of a prior user
    submission or the disputed transaction.
    """

    attachment_files: List[VisaUserSubmissionAttachmentFile]
    """The files attached to the Visa Card Dispute User Submission."""

    category: Literal["chargeback", "merchant_prearbitration_decline", "user_prearbitration"]
    """The category of the user submission.

    We may add additional possible values for this enum over time; your application
    should be able to handle such additions gracefully.

    - `chargeback` - Visa Card Dispute Chargeback User Submission Chargeback
      Details: details will be under the `chargeback` object.
    - `merchant_prearbitration_decline` - Visa Card Dispute Merchant Pre-Arbitration
      Decline User Submission: details will be under the
      `merchant_prearbitration_decline` object.
    - `user_prearbitration` - Visa Card Dispute User-Initiated Pre-Arbitration User
      Submission: details will be under the `user_prearbitration` object.
    """

    chargeback: Optional[VisaUserSubmissionChargeback] = None
    """A Visa Card Dispute Chargeback User Submission Chargeback Details object.

    This field will be present in the JSON response if and only if `category` is
    equal to `chargeback`. Contains the details specific to a Visa chargeback User
    Submission for a Card Dispute.
    """

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Visa Card Dispute User Submission was created.
    """

    further_information_requested_at: Optional[datetime] = None
    """
    The date and time at which Increase requested further information from the user
    for the Visa Card Dispute.
    """

    further_information_requested_reason: Optional[str] = None
    """
    The reason for Increase requesting further information from the user for the
    Visa Card Dispute.
    """

    merchant_prearbitration_decline: Optional[VisaUserSubmissionMerchantPrearbitrationDecline] = None
    """A Visa Card Dispute Merchant Pre-Arbitration Decline User Submission object.

    This field will be present in the JSON response if and only if `category` is
    equal to `merchant_prearbitration_decline`. Contains the details specific to a
    merchant prearbitration decline Visa Card Dispute User Submission.
    """

    status: Literal["abandoned", "accepted", "further_information_requested", "pending_reviewing"]
    """The status of the Visa Card Dispute User Submission.

    - `abandoned` - The User Submission was abandoned.
    - `accepted` - The User Submission was accepted.
    - `further_information_requested` - Further information is requested, please
      resubmit with the requested information.
    - `pending_reviewing` - The User Submission is pending review.
    """

    updated_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Visa Card Dispute User Submission was updated.
    """

    user_prearbitration: Optional[VisaUserSubmissionUserPrearbitration] = None
    """A Visa Card Dispute User-Initiated Pre-Arbitration User Submission object.

    This field will be present in the JSON response if and only if `category` is
    equal to `user_prearbitration`. Contains the details specific to a
    user-initiated pre-arbitration Visa Card Dispute User Submission.
    """


class Visa(BaseModel):
    network_events: List[VisaNetworkEvent]
    """The network events for the Card Dispute."""

    required_user_submission_category: Optional[
        Literal["chargeback", "merchant_prearbitration_decline", "user_prearbitration"]
    ] = None
    """
    The category of the currently required user submission if the user wishes to
    proceed with the dispute. Present if and only if status is
    `user_submission_required`. Otherwise, this will be `nil`.

    - `chargeback` - A Chargeback User Submission is required.
    - `merchant_prearbitration_decline` - A Merchant Pre Arbitration Decline User
      Submission is required.
    - `user_prearbitration` - A User Initiated Pre Arbitration User Submission is
      required.
    """

    user_submissions: List[VisaUserSubmission]
    """The user submissions for the Card Dispute."""


class Win(BaseModel):
    won_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Card Dispute was won.
    """


class CardDispute(BaseModel):
    id: str
    """The Card Dispute identifier."""

    amount: int
    """The amount of the dispute."""

    card_id: str
    """The Card that the Card Dispute is associated with."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the Card Dispute was created.
    """

    disputed_transaction_id: str
    """The identifier of the Transaction that was disputed."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    loss: Optional[Loss] = None
    """
    If the Card Dispute's status is `lost`, this will contain details of the lost
    dispute.
    """

    network: Literal["visa", "pulse"]
    """The network that the Card Dispute is associated with.

    - `visa` - Visa: details will be under the `visa` object.
    - `pulse` - Pulse: details will be under the `pulse` object.
    """

    status: Literal[
        "user_submission_required",
        "pending_user_submission_reviewing",
        "pending_user_submission_submitting",
        "pending_user_withdrawal_submitting",
        "pending_response",
        "lost",
        "won",
    ]
    """The status of the Card Dispute.

    - `user_submission_required` - A User Submission is required to continue with
      the Card Dispute.
    - `pending_user_submission_reviewing` - The most recent User Submission is being
      reviewed.
    - `pending_user_submission_submitting` - The most recent User Submission is
      being submitted to the network.
    - `pending_user_withdrawal_submitting` - The user's withdrawal of the Card
      Dispute is being submitted to the network.
    - `pending_response` - The Card Dispute is pending a response from the network.
    - `lost` - The Card Dispute has been lost and funds previously credited from the
      acceptance have been debited.
    - `won` - The Card Dispute has been won and no further action can be taken.
    """

    type: Literal["card_dispute"]
    """A constant representing the object's type.

    For this resource it will always be `card_dispute`.
    """

    user_submission_required_by: Optional[datetime] = None
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which
    the user submission is required by. Present only if status is
    `user_submission_required` and a user submission is required by a certain time.
    Otherwise, this will be `nil`.
    """

    visa: Optional[Visa] = None
    """Card Dispute information for card payments processed over Visa's network.

    This field will be present in the JSON response if and only if `network` is
    equal to `visa`.
    """

    win: Optional[Win] = None
    """
    If the Card Dispute's status is `won`, this will contain details of the won
    dispute.
    """
