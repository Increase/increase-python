# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "CardDisputeCreateParams",
    "AttachmentFile",
    "Visa",
    "VisaAuthorization",
    "VisaConsumerCanceledMerchandise",
    "VisaConsumerCanceledMerchandiseCardholderCancellation",
    "VisaConsumerCanceledMerchandiseReturnAttempted",
    "VisaConsumerCanceledMerchandiseReturned",
    "VisaConsumerCanceledRecurringTransaction",
    "VisaConsumerCanceledRecurringTransactionMerchantContactMethods",
    "VisaConsumerCanceledServices",
    "VisaConsumerCanceledServicesCardholderCancellation",
    "VisaConsumerCanceledServicesGuaranteedReservation",
    "VisaConsumerCounterfeitMerchandise",
    "VisaConsumerCreditNotProcessed",
    "VisaConsumerDamagedOrDefectiveMerchandise",
    "VisaConsumerDamagedOrDefectiveMerchandiseReturnAttempted",
    "VisaConsumerDamagedOrDefectiveMerchandiseReturned",
    "VisaConsumerMerchandiseMisrepresentation",
    "VisaConsumerMerchandiseMisrepresentationReturnAttempted",
    "VisaConsumerMerchandiseMisrepresentationReturned",
    "VisaConsumerMerchandiseNotAsDescribed",
    "VisaConsumerMerchandiseNotAsDescribedReturnAttempted",
    "VisaConsumerMerchandiseNotAsDescribedReturned",
    "VisaConsumerMerchandiseNotReceived",
    "VisaConsumerMerchandiseNotReceivedCardholderCancellationPriorToExpectedReceipt",
    "VisaConsumerMerchandiseNotReceivedDelayed",
    "VisaConsumerMerchandiseNotReceivedDelayedReturnAttempted",
    "VisaConsumerMerchandiseNotReceivedDelayedReturned",
    "VisaConsumerMerchandiseNotReceivedDeliveredToWrongLocation",
    "VisaConsumerMerchandiseNotReceivedMerchantCancellation",
    "VisaConsumerOriginalCreditTransactionNotAccepted",
    "VisaConsumerQualityMerchandise",
    "VisaConsumerQualityMerchandiseOngoingNegotiations",
    "VisaConsumerQualityMerchandiseReturnAttempted",
    "VisaConsumerQualityMerchandiseReturned",
    "VisaConsumerQualityServices",
    "VisaConsumerQualityServicesCardholderCancellation",
    "VisaConsumerQualityServicesOngoingNegotiations",
    "VisaConsumerServicesMisrepresentation",
    "VisaConsumerServicesMisrepresentationCardholderCancellation",
    "VisaConsumerServicesNotAsDescribed",
    "VisaConsumerServicesNotAsDescribedCardholderCancellation",
    "VisaConsumerServicesNotReceived",
    "VisaConsumerServicesNotReceivedCardholderCancellationPriorToExpectedReceipt",
    "VisaConsumerServicesNotReceivedMerchantCancellation",
    "VisaFraud",
    "VisaProcessingError",
    "VisaProcessingErrorDuplicateTransaction",
    "VisaProcessingErrorIncorrectAmount",
    "VisaProcessingErrorPaidByOtherMeans",
]


class CardDisputeCreateParams(TypedDict, total=False):
    disputed_transaction_id: Required[str]
    """The Transaction you wish to dispute.

    This Transaction must have a `source_type` of `card_settlement`.
    """

    network: Required[Literal["visa"]]
    """The network of the disputed transaction.

    Details specific to the network are required under the sub-object with the same
    identifier as the network.

    - `visa` - Visa
    """

    amount: int
    """The monetary amount of the part of the transaction that is being disputed.

    This is optional and will default to the full amount of the transaction if not
    provided. If provided, the amount must be less than or equal to the amount of
    the transaction.
    """

    attachment_files: Iterable[AttachmentFile]
    """The files to be attached to the initial dispute submission."""

    visa: Visa
    """The Visa-specific parameters for the dispute.

    Required if and only if `network` is `visa`.
    """


class AttachmentFile(TypedDict, total=False):
    file_id: Required[str]
    """The ID of the file to be attached.

    The file must have a `purpose` of `card_dispute_attachment`.
    """


class VisaAuthorization(TypedDict, total=False):
    account_status: Required[Literal["account_closed", "credit_problem", "fraud"]]
    """Account status.

    - `account_closed` - Account closed.
    - `credit_problem` - Credit problem.
    - `fraud` - Fraud.
    """


class VisaConsumerCanceledMerchandiseCardholderCancellation(TypedDict, total=False):
    canceled_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Canceled at."""

    canceled_prior_to_ship_date: Required[Literal["canceled_prior_to_ship_date", "not_canceled_prior_to_ship_date"]]
    """Canceled prior to ship date.

    - `canceled_prior_to_ship_date` - Canceled prior to ship date.
    - `not_canceled_prior_to_ship_date` - Not canceled prior to ship date.
    """

    cancellation_policy_provided: Required[Literal["not_provided", "provided"]]
    """Cancellation policy provided.

    - `not_provided` - Not provided.
    - `provided` - Provided.
    """

    reason: Required[str]
    """Reason."""


class VisaConsumerCanceledMerchandiseReturnAttempted(TypedDict, total=False):
    attempt_explanation: Required[str]
    """Attempt explanation."""

    attempt_reason: Required[
        Literal[
            "merchant_not_responding",
            "no_return_authorization_provided",
            "no_return_instructions",
            "requested_not_to_return",
            "return_not_accepted",
        ]
    ]
    """Attempt reason.

    - `merchant_not_responding` - Merchant not responding.
    - `no_return_authorization_provided` - No return authorization provided.
    - `no_return_instructions` - No return instructions.
    - `requested_not_to_return` - Requested not to return.
    - `return_not_accepted` - Return not accepted.
    """

    attempted_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Attempted at."""

    merchandise_disposition: Required[str]
    """Merchandise disposition."""


class VisaConsumerCanceledMerchandiseReturned(TypedDict, total=False):
    return_method: Required[Literal["dhl", "face_to_face", "fedex", "other", "postal_service", "ups"]]
    """Return method.

    - `dhl` - DHL.
    - `face_to_face` - Face-to-face.
    - `fedex` - FedEx.
    - `other` - Other.
    - `postal_service` - Postal service.
    - `ups` - UPS.
    """

    returned_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Returned at."""

    merchant_received_return_at: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Merchant received return at."""

    other_explanation: str
    """Other explanation. Required if and only if the return method is `other`."""

    tracking_number: str
    """Tracking number."""


class VisaConsumerCanceledMerchandise(TypedDict, total=False):
    merchant_resolution_attempted: Required[Literal["attempted", "prohibited_by_local_law"]]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    purchase_explanation: Required[str]
    """Purchase explanation."""

    received_or_expected_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Received or expected at."""

    return_outcome: Required[Literal["not_returned", "returned", "return_attempted"]]
    """Return outcome.

    - `not_returned` - Not returned.
    - `returned` - Returned.
    - `return_attempted` - Return attempted.
    """

    cardholder_cancellation: VisaConsumerCanceledMerchandiseCardholderCancellation
    """Cardholder cancellation."""

    not_returned: object
    """Not returned. Required if and only if `return_outcome` is `not_returned`."""

    return_attempted: VisaConsumerCanceledMerchandiseReturnAttempted
    """Return attempted.

    Required if and only if `return_outcome` is `return_attempted`.
    """

    returned: VisaConsumerCanceledMerchandiseReturned
    """Returned. Required if and only if `return_outcome` is `returned`."""


class VisaConsumerCanceledRecurringTransactionMerchantContactMethods(TypedDict, total=False):
    application_name: str
    """Application name."""

    call_center_phone_number: str
    """Call center phone number."""

    email_address: str
    """Email address."""

    in_person_address: str
    """In person address."""

    mailing_address: str
    """Mailing address."""

    text_phone_number: str
    """Text phone number."""


class VisaConsumerCanceledRecurringTransaction(TypedDict, total=False):
    cancellation_target: Required[Literal["account", "transaction"]]
    """Cancellation target.

    - `account` - Account.
    - `transaction` - Transaction.
    """

    merchant_contact_methods: Required[VisaConsumerCanceledRecurringTransactionMerchantContactMethods]
    """Merchant contact methods."""

    transaction_or_account_canceled_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Transaction or account canceled at."""

    other_form_of_payment_explanation: str
    """Other form of payment explanation."""


class VisaConsumerCanceledServicesCardholderCancellation(TypedDict, total=False):
    canceled_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Canceled at."""

    cancellation_policy_provided: Required[Literal["not_provided", "provided"]]
    """Cancellation policy provided.

    - `not_provided` - Not provided.
    - `provided` - Provided.
    """

    reason: Required[str]
    """Reason."""


class VisaConsumerCanceledServicesGuaranteedReservation(TypedDict, total=False):
    explanation: Required[
        Literal[
            "cardholder_canceled_prior_to_service",
            "cardholder_cancellation_attempt_within_24_hours_of_confirmation",
            "merchant_billed_no_show",
        ]
    ]
    """Explanation.

    - `cardholder_canceled_prior_to_service` - Cardholder canceled prior to service.
    - `cardholder_cancellation_attempt_within_24_hours_of_confirmation` - Cardholder
      cancellation attempt within 24 hours of confirmation.
    - `merchant_billed_no_show` - Merchant billed for no-show.
    """


class VisaConsumerCanceledServices(TypedDict, total=False):
    cardholder_cancellation: Required[VisaConsumerCanceledServicesCardholderCancellation]
    """Cardholder cancellation."""

    contracted_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Contracted at."""

    merchant_resolution_attempted: Required[Literal["attempted", "prohibited_by_local_law"]]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    purchase_explanation: Required[str]
    """Purchase explanation."""

    service_type: Required[Literal["guaranteed_reservation", "other", "timeshare"]]
    """Service type.

    - `guaranteed_reservation` - Guaranteed reservation.
    - `other` - Other.
    - `timeshare` - Timeshare.
    """

    guaranteed_reservation: VisaConsumerCanceledServicesGuaranteedReservation
    """Guaranteed reservation explanation.

    Required if and only if `service_type` is `guaranteed_reservation`.
    """

    other: object
    """Other service type explanation.

    Required if and only if `service_type` is `other`.
    """

    timeshare: object
    """Timeshare explanation. Required if and only if `service_type` is `timeshare`."""


class VisaConsumerCounterfeitMerchandise(TypedDict, total=False):
    counterfeit_explanation: Required[str]
    """Counterfeit explanation."""

    disposition_explanation: Required[str]
    """Disposition explanation."""

    order_explanation: Required[str]
    """Order explanation."""

    received_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Received at."""


class VisaConsumerCreditNotProcessed(TypedDict, total=False):
    canceled_or_returned_at: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Canceled or returned at."""

    credit_expected_at: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Credit expected at."""


class VisaConsumerDamagedOrDefectiveMerchandiseReturnAttempted(TypedDict, total=False):
    attempt_explanation: Required[str]
    """Attempt explanation."""

    attempt_reason: Required[
        Literal[
            "merchant_not_responding",
            "no_return_authorization_provided",
            "no_return_instructions",
            "requested_not_to_return",
            "return_not_accepted",
        ]
    ]
    """Attempt reason.

    - `merchant_not_responding` - Merchant not responding.
    - `no_return_authorization_provided` - No return authorization provided.
    - `no_return_instructions` - No return instructions.
    - `requested_not_to_return` - Requested not to return.
    - `return_not_accepted` - Return not accepted.
    """

    attempted_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Attempted at."""

    merchandise_disposition: Required[str]
    """Merchandise disposition."""


class VisaConsumerDamagedOrDefectiveMerchandiseReturned(TypedDict, total=False):
    return_method: Required[Literal["dhl", "face_to_face", "fedex", "other", "postal_service", "ups"]]
    """Return method.

    - `dhl` - DHL.
    - `face_to_face` - Face-to-face.
    - `fedex` - FedEx.
    - `other` - Other.
    - `postal_service` - Postal service.
    - `ups` - UPS.
    """

    returned_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Returned at."""

    merchant_received_return_at: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Merchant received return at."""

    other_explanation: str
    """Other explanation. Required if and only if the return method is `other`."""

    tracking_number: str
    """Tracking number."""


class VisaConsumerDamagedOrDefectiveMerchandise(TypedDict, total=False):
    merchant_resolution_attempted: Required[Literal["attempted", "prohibited_by_local_law"]]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    order_and_issue_explanation: Required[str]
    """Order and issue explanation."""

    received_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Received at."""

    return_outcome: Required[Literal["not_returned", "returned", "return_attempted"]]
    """Return outcome.

    - `not_returned` - Not returned.
    - `returned` - Returned.
    - `return_attempted` - Return attempted.
    """

    not_returned: object
    """Not returned. Required if and only if `return_outcome` is `not_returned`."""

    return_attempted: VisaConsumerDamagedOrDefectiveMerchandiseReturnAttempted
    """Return attempted.

    Required if and only if `return_outcome` is `return_attempted`.
    """

    returned: VisaConsumerDamagedOrDefectiveMerchandiseReturned
    """Returned. Required if and only if `return_outcome` is `returned`."""


class VisaConsumerMerchandiseMisrepresentationReturnAttempted(TypedDict, total=False):
    attempt_explanation: Required[str]
    """Attempt explanation."""

    attempt_reason: Required[
        Literal[
            "merchant_not_responding",
            "no_return_authorization_provided",
            "no_return_instructions",
            "requested_not_to_return",
            "return_not_accepted",
        ]
    ]
    """Attempt reason.

    - `merchant_not_responding` - Merchant not responding.
    - `no_return_authorization_provided` - No return authorization provided.
    - `no_return_instructions` - No return instructions.
    - `requested_not_to_return` - Requested not to return.
    - `return_not_accepted` - Return not accepted.
    """

    attempted_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Attempted at."""

    merchandise_disposition: Required[str]
    """Merchandise disposition."""


class VisaConsumerMerchandiseMisrepresentationReturned(TypedDict, total=False):
    return_method: Required[Literal["dhl", "face_to_face", "fedex", "other", "postal_service", "ups"]]
    """Return method.

    - `dhl` - DHL.
    - `face_to_face` - Face-to-face.
    - `fedex` - FedEx.
    - `other` - Other.
    - `postal_service` - Postal service.
    - `ups` - UPS.
    """

    returned_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Returned at."""

    merchant_received_return_at: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Merchant received return at."""

    other_explanation: str
    """Other explanation. Required if and only if the return method is `other`."""

    tracking_number: str
    """Tracking number."""


class VisaConsumerMerchandiseMisrepresentation(TypedDict, total=False):
    merchant_resolution_attempted: Required[Literal["attempted", "prohibited_by_local_law"]]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    misrepresentation_explanation: Required[str]
    """Misrepresentation explanation."""

    purchase_explanation: Required[str]
    """Purchase explanation."""

    received_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Received at."""

    return_outcome: Required[Literal["not_returned", "returned", "return_attempted"]]
    """Return outcome.

    - `not_returned` - Not returned.
    - `returned` - Returned.
    - `return_attempted` - Return attempted.
    """

    not_returned: object
    """Not returned. Required if and only if `return_outcome` is `not_returned`."""

    return_attempted: VisaConsumerMerchandiseMisrepresentationReturnAttempted
    """Return attempted.

    Required if and only if `return_outcome` is `return_attempted`.
    """

    returned: VisaConsumerMerchandiseMisrepresentationReturned
    """Returned. Required if and only if `return_outcome` is `returned`."""


class VisaConsumerMerchandiseNotAsDescribedReturnAttempted(TypedDict, total=False):
    attempt_explanation: Required[str]
    """Attempt explanation."""

    attempt_reason: Required[
        Literal[
            "merchant_not_responding",
            "no_return_authorization_provided",
            "no_return_instructions",
            "requested_not_to_return",
            "return_not_accepted",
        ]
    ]
    """Attempt reason.

    - `merchant_not_responding` - Merchant not responding.
    - `no_return_authorization_provided` - No return authorization provided.
    - `no_return_instructions` - No return instructions.
    - `requested_not_to_return` - Requested not to return.
    - `return_not_accepted` - Return not accepted.
    """

    attempted_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Attempted at."""

    merchandise_disposition: Required[str]
    """Merchandise disposition."""


class VisaConsumerMerchandiseNotAsDescribedReturned(TypedDict, total=False):
    return_method: Required[Literal["dhl", "face_to_face", "fedex", "other", "postal_service", "ups"]]
    """Return method.

    - `dhl` - DHL.
    - `face_to_face` - Face-to-face.
    - `fedex` - FedEx.
    - `other` - Other.
    - `postal_service` - Postal service.
    - `ups` - UPS.
    """

    returned_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Returned at."""

    merchant_received_return_at: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Merchant received return at."""

    other_explanation: str
    """Other explanation. Required if and only if the return method is `other`."""

    tracking_number: str
    """Tracking number."""


class VisaConsumerMerchandiseNotAsDescribed(TypedDict, total=False):
    merchant_resolution_attempted: Required[Literal["attempted", "prohibited_by_local_law"]]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    received_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Received at."""

    return_outcome: Required[Literal["returned", "return_attempted"]]
    """Return outcome.

    - `returned` - Returned.
    - `return_attempted` - Return attempted.
    """

    return_attempted: VisaConsumerMerchandiseNotAsDescribedReturnAttempted
    """Return attempted.

    Required if and only if `return_outcome` is `return_attempted`.
    """

    returned: VisaConsumerMerchandiseNotAsDescribedReturned
    """Returned. Required if and only if `return_outcome` is `returned`."""


class VisaConsumerMerchandiseNotReceivedCardholderCancellationPriorToExpectedReceipt(TypedDict, total=False):
    canceled_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Canceled at."""

    reason: str
    """Reason."""


class VisaConsumerMerchandiseNotReceivedDelayedReturnAttempted(TypedDict, total=False):
    attempted_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Attempted at."""


class VisaConsumerMerchandiseNotReceivedDelayedReturned(TypedDict, total=False):
    merchant_received_return_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Merchant received return at."""

    returned_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Returned at."""


class VisaConsumerMerchandiseNotReceivedDelayed(TypedDict, total=False):
    explanation: Required[str]
    """Explanation."""

    return_outcome: Required[Literal["not_returned", "returned", "return_attempted"]]
    """Return outcome.

    - `not_returned` - Not returned.
    - `returned` - Returned.
    - `return_attempted` - Return attempted.
    """

    not_returned: object
    """Not returned. Required if and only if `return_outcome` is `not_returned`."""

    return_attempted: VisaConsumerMerchandiseNotReceivedDelayedReturnAttempted
    """Return attempted.

    Required if and only if `return_outcome` is `return_attempted`.
    """

    returned: VisaConsumerMerchandiseNotReceivedDelayedReturned
    """Returned. Required if and only if `return_outcome` is `returned`."""


class VisaConsumerMerchandiseNotReceivedDeliveredToWrongLocation(TypedDict, total=False):
    agreed_location: Required[str]
    """Agreed location."""


class VisaConsumerMerchandiseNotReceivedMerchantCancellation(TypedDict, total=False):
    canceled_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Canceled at."""


class VisaConsumerMerchandiseNotReceived(TypedDict, total=False):
    cancellation_outcome: Required[
        Literal["cardholder_cancellation_prior_to_expected_receipt", "merchant_cancellation", "no_cancellation"]
    ]
    """Cancellation outcome.

    - `cardholder_cancellation_prior_to_expected_receipt` - Cardholder cancellation
      prior to expected receipt.
    - `merchant_cancellation` - Merchant cancellation.
    - `no_cancellation` - No cancellation.
    """

    delivery_issue: Required[Literal["delayed", "delivered_to_wrong_location"]]
    """Delivery issue.

    - `delayed` - Delayed.
    - `delivered_to_wrong_location` - Delivered to wrong location.
    """

    last_expected_receipt_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Last expected receipt at."""

    merchant_resolution_attempted: Required[Literal["attempted", "prohibited_by_local_law"]]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    purchase_info_and_explanation: Required[str]
    """Purchase information and explanation."""

    cardholder_cancellation_prior_to_expected_receipt: (
        VisaConsumerMerchandiseNotReceivedCardholderCancellationPriorToExpectedReceipt
    )
    """Cardholder cancellation prior to expected receipt.

    Required if and only if `cancellation_outcome` is
    `cardholder_cancellation_prior_to_expected_receipt`.
    """

    delayed: VisaConsumerMerchandiseNotReceivedDelayed
    """Delayed. Required if and only if `delivery_issue` is `delayed`."""

    delivered_to_wrong_location: VisaConsumerMerchandiseNotReceivedDeliveredToWrongLocation
    """Delivered to wrong location.

    Required if and only if `delivery_issue` is `delivered_to_wrong_location`.
    """

    merchant_cancellation: VisaConsumerMerchandiseNotReceivedMerchantCancellation
    """Merchant cancellation.

    Required if and only if `cancellation_outcome` is `merchant_cancellation`.
    """

    no_cancellation: object
    """No cancellation.

    Required if and only if `cancellation_outcome` is `no_cancellation`.
    """


class VisaConsumerOriginalCreditTransactionNotAccepted(TypedDict, total=False):
    explanation: Required[str]
    """Explanation."""

    reason: Required[Literal["prohibited_by_local_laws_or_regulation", "recipient_refused"]]
    """Reason.

    - `prohibited_by_local_laws_or_regulation` - Prohibited by local laws or
      regulation.
    - `recipient_refused` - Recipient refused.
    """


class VisaConsumerQualityMerchandiseOngoingNegotiations(TypedDict, total=False):
    explanation: Required[str]
    """
    Explanation of the previous ongoing negotiations between the cardholder and
    merchant.
    """

    issuer_first_notified_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Date the cardholder first notified the issuer of the dispute."""

    started_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Started at."""


class VisaConsumerQualityMerchandiseReturnAttempted(TypedDict, total=False):
    attempt_explanation: Required[str]
    """Attempt explanation."""

    attempt_reason: Required[
        Literal[
            "merchant_not_responding",
            "no_return_authorization_provided",
            "no_return_instructions",
            "requested_not_to_return",
            "return_not_accepted",
        ]
    ]
    """Attempt reason.

    - `merchant_not_responding` - Merchant not responding.
    - `no_return_authorization_provided` - No return authorization provided.
    - `no_return_instructions` - No return instructions.
    - `requested_not_to_return` - Requested not to return.
    - `return_not_accepted` - Return not accepted.
    """

    attempted_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Attempted at."""

    merchandise_disposition: Required[str]
    """Merchandise disposition."""


class VisaConsumerQualityMerchandiseReturned(TypedDict, total=False):
    return_method: Required[Literal["dhl", "face_to_face", "fedex", "other", "postal_service", "ups"]]
    """Return method.

    - `dhl` - DHL.
    - `face_to_face` - Face-to-face.
    - `fedex` - FedEx.
    - `other` - Other.
    - `postal_service` - Postal service.
    - `ups` - UPS.
    """

    returned_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Returned at."""

    merchant_received_return_at: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Merchant received return at."""

    other_explanation: str
    """Other explanation. Required if and only if the return method is `other`."""

    tracking_number: str
    """Tracking number."""


class VisaConsumerQualityMerchandise(TypedDict, total=False):
    expected_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Expected at."""

    merchant_resolution_attempted: Required[Literal["attempted", "prohibited_by_local_law"]]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    purchase_info_and_quality_issue: Required[str]
    """Purchase information and quality issue."""

    received_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Received at."""

    return_outcome: Required[Literal["not_returned", "returned", "return_attempted"]]
    """Return outcome.

    - `not_returned` - Not returned.
    - `returned` - Returned.
    - `return_attempted` - Return attempted.
    """

    not_returned: object
    """Not returned. Required if and only if `return_outcome` is `not_returned`."""

    ongoing_negotiations: VisaConsumerQualityMerchandiseOngoingNegotiations
    """Ongoing negotiations. Exclude if there is no evidence of ongoing negotiations."""

    return_attempted: VisaConsumerQualityMerchandiseReturnAttempted
    """Return attempted.

    Required if and only if `return_outcome` is `return_attempted`.
    """

    returned: VisaConsumerQualityMerchandiseReturned
    """Returned. Required if and only if `return_outcome` is `returned`."""


class VisaConsumerQualityServicesCardholderCancellation(TypedDict, total=False):
    accepted_by_merchant: Required[Literal["accepted", "not_accepted"]]
    """Accepted by merchant.

    - `accepted` - Accepted.
    - `not_accepted` - Not accepted.
    """

    canceled_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Canceled at."""

    reason: Required[str]
    """Reason."""


class VisaConsumerQualityServicesOngoingNegotiations(TypedDict, total=False):
    explanation: Required[str]
    """
    Explanation of the previous ongoing negotiations between the cardholder and
    merchant.
    """

    issuer_first_notified_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Date the cardholder first notified the issuer of the dispute."""

    started_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Started at."""


class VisaConsumerQualityServices(TypedDict, total=False):
    cardholder_cancellation: Required[VisaConsumerQualityServicesCardholderCancellation]
    """Cardholder cancellation."""

    non_fiat_currency_or_non_fungible_token_related_and_not_matching_description: Required[
        Literal["not_related", "related"]
    ]
    """Non-fiat currency or non-fungible token related and not matching description.

    - `not_related` - Not related.
    - `related` - Related.
    """

    purchase_info_and_quality_issue: Required[str]
    """Purchase information and quality issue."""

    services_received_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Services received at."""

    cardholder_paid_to_have_work_redone: Literal["did_not_pay_to_have_work_redone", "paid_to_have_work_redone"]
    """Cardholder paid to have work redone.

    - `did_not_pay_to_have_work_redone` - Cardholder did not pay to have work
      redone.
    - `paid_to_have_work_redone` - Cardholder paid to have work redone.
    """

    ongoing_negotiations: VisaConsumerQualityServicesOngoingNegotiations
    """Ongoing negotiations. Exclude if there is no evidence of ongoing negotiations."""

    restaurant_food_related: Literal["not_related", "related"]
    """
    Whether the dispute is related to the quality of food from an eating place or
    restaurant. Must be provided when Merchant Category Code (MCC) is 5812, 5813
    or 5814.

    - `not_related` - Not related.
    - `related` - Related.
    """


class VisaConsumerServicesMisrepresentationCardholderCancellation(TypedDict, total=False):
    accepted_by_merchant: Required[Literal["accepted", "not_accepted"]]
    """Accepted by merchant.

    - `accepted` - Accepted.
    - `not_accepted` - Not accepted.
    """

    canceled_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Canceled at."""

    reason: Required[str]
    """Reason."""


class VisaConsumerServicesMisrepresentation(TypedDict, total=False):
    cardholder_cancellation: Required[VisaConsumerServicesMisrepresentationCardholderCancellation]
    """Cardholder cancellation."""

    merchant_resolution_attempted: Required[Literal["attempted", "prohibited_by_local_law"]]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    misrepresentation_explanation: Required[str]
    """Misrepresentation explanation."""

    purchase_explanation: Required[str]
    """Purchase explanation."""

    received_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Received at."""


class VisaConsumerServicesNotAsDescribedCardholderCancellation(TypedDict, total=False):
    accepted_by_merchant: Required[Literal["accepted", "not_accepted"]]
    """Accepted by merchant.

    - `accepted` - Accepted.
    - `not_accepted` - Not accepted.
    """

    canceled_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Canceled at."""

    reason: Required[str]
    """Reason."""


class VisaConsumerServicesNotAsDescribed(TypedDict, total=False):
    cardholder_cancellation: Required[VisaConsumerServicesNotAsDescribedCardholderCancellation]
    """Cardholder cancellation."""

    merchant_resolution_attempted: Required[Literal["attempted", "prohibited_by_local_law"]]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    received_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Received at."""


class VisaConsumerServicesNotReceivedCardholderCancellationPriorToExpectedReceipt(TypedDict, total=False):
    canceled_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Canceled at."""

    reason: str
    """Reason."""


class VisaConsumerServicesNotReceivedMerchantCancellation(TypedDict, total=False):
    canceled_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Canceled at."""


class VisaConsumerServicesNotReceived(TypedDict, total=False):
    cancellation_outcome: Required[
        Literal["cardholder_cancellation_prior_to_expected_receipt", "merchant_cancellation", "no_cancellation"]
    ]
    """Cancellation outcome.

    - `cardholder_cancellation_prior_to_expected_receipt` - Cardholder cancellation
      prior to expected receipt.
    - `merchant_cancellation` - Merchant cancellation.
    - `no_cancellation` - No cancellation.
    """

    last_expected_receipt_at: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Last expected receipt at."""

    merchant_resolution_attempted: Required[Literal["attempted", "prohibited_by_local_law"]]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    purchase_info_and_explanation: Required[str]
    """Purchase information and explanation."""

    cardholder_cancellation_prior_to_expected_receipt: (
        VisaConsumerServicesNotReceivedCardholderCancellationPriorToExpectedReceipt
    )
    """Cardholder cancellation prior to expected receipt.

    Required if and only if `cancellation_outcome` is
    `cardholder_cancellation_prior_to_expected_receipt`.
    """

    merchant_cancellation: VisaConsumerServicesNotReceivedMerchantCancellation
    """Merchant cancellation.

    Required if and only if `cancellation_outcome` is `merchant_cancellation`.
    """

    no_cancellation: object
    """No cancellation.

    Required if and only if `cancellation_outcome` is `no_cancellation`.
    """


class VisaFraud(TypedDict, total=False):
    fraud_type: Required[
        Literal[
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


class VisaProcessingErrorDuplicateTransaction(TypedDict, total=False):
    other_transaction_id: Required[str]
    """Other transaction ID."""


class VisaProcessingErrorIncorrectAmount(TypedDict, total=False):
    expected_amount: Required[int]
    """Expected amount."""


class VisaProcessingErrorPaidByOtherMeans(TypedDict, total=False):
    other_form_of_payment_evidence: Required[
        Literal["canceled_check", "card_transaction", "cash_receipt", "other", "statement", "voucher"]
    ]
    """Other form of payment evidence.

    - `canceled_check` - Canceled check.
    - `card_transaction` - Card transaction.
    - `cash_receipt` - Cash receipt.
    - `other` - Other.
    - `statement` - Statement.
    - `voucher` - Voucher.
    """

    other_transaction_id: str
    """Other transaction ID."""


class VisaProcessingError(TypedDict, total=False):
    error_reason: Required[Literal["duplicate_transaction", "incorrect_amount", "paid_by_other_means"]]
    """Error reason.

    - `duplicate_transaction` - Duplicate transaction.
    - `incorrect_amount` - Incorrect amount.
    - `paid_by_other_means` - Paid by other means.
    """

    merchant_resolution_attempted: Required[Literal["attempted", "prohibited_by_local_law"]]
    """Merchant resolution attempted.

    - `attempted` - Attempted.
    - `prohibited_by_local_law` - Prohibited by local law.
    """

    duplicate_transaction: VisaProcessingErrorDuplicateTransaction
    """Duplicate transaction.

    Required if and only if `error_reason` is `duplicate_transaction`.
    """

    incorrect_amount: VisaProcessingErrorIncorrectAmount
    """Incorrect amount. Required if and only if `error_reason` is `incorrect_amount`."""

    paid_by_other_means: VisaProcessingErrorPaidByOtherMeans
    """Paid by other means.

    Required if and only if `error_reason` is `paid_by_other_means`.
    """


class Visa(TypedDict, total=False):
    category: Required[
        Literal[
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

    authorization: VisaAuthorization
    """Authorization. Required if and only if `category` is `authorization`."""

    consumer_canceled_merchandise: VisaConsumerCanceledMerchandise
    """Canceled merchandise.

    Required if and only if `category` is `consumer_canceled_merchandise`.
    """

    consumer_canceled_recurring_transaction: VisaConsumerCanceledRecurringTransaction
    """Canceled recurring transaction.

    Required if and only if `category` is `consumer_canceled_recurring_transaction`.
    """

    consumer_canceled_services: VisaConsumerCanceledServices
    """Canceled services.

    Required if and only if `category` is `consumer_canceled_services`.
    """

    consumer_counterfeit_merchandise: VisaConsumerCounterfeitMerchandise
    """Counterfeit merchandise.

    Required if and only if `category` is `consumer_counterfeit_merchandise`.
    """

    consumer_credit_not_processed: VisaConsumerCreditNotProcessed
    """Credit not processed.

    Required if and only if `category` is `consumer_credit_not_processed`.
    """

    consumer_damaged_or_defective_merchandise: VisaConsumerDamagedOrDefectiveMerchandise
    """Damaged or defective merchandise.

    Required if and only if `category` is
    `consumer_damaged_or_defective_merchandise`.
    """

    consumer_merchandise_misrepresentation: VisaConsumerMerchandiseMisrepresentation
    """Merchandise misrepresentation.

    Required if and only if `category` is `consumer_merchandise_misrepresentation`.
    """

    consumer_merchandise_not_as_described: VisaConsumerMerchandiseNotAsDescribed
    """Merchandise not as described.

    Required if and only if `category` is `consumer_merchandise_not_as_described`.
    """

    consumer_merchandise_not_received: VisaConsumerMerchandiseNotReceived
    """Merchandise not received.

    Required if and only if `category` is `consumer_merchandise_not_received`.
    """

    consumer_non_receipt_of_cash: object
    """Non-receipt of cash.

    Required if and only if `category` is `consumer_non_receipt_of_cash`.
    """

    consumer_original_credit_transaction_not_accepted: VisaConsumerOriginalCreditTransactionNotAccepted
    """Original Credit Transaction (OCT) not accepted.

    Required if and only if `category` is
    `consumer_original_credit_transaction_not_accepted`.
    """

    consumer_quality_merchandise: VisaConsumerQualityMerchandise
    """Merchandise quality issue.

    Required if and only if `category` is `consumer_quality_merchandise`.
    """

    consumer_quality_services: VisaConsumerQualityServices
    """Services quality issue.

    Required if and only if `category` is `consumer_quality_services`.
    """

    consumer_services_misrepresentation: VisaConsumerServicesMisrepresentation
    """Services misrepresentation.

    Required if and only if `category` is `consumer_services_misrepresentation`.
    """

    consumer_services_not_as_described: VisaConsumerServicesNotAsDescribed
    """Services not as described.

    Required if and only if `category` is `consumer_services_not_as_described`.
    """

    consumer_services_not_received: VisaConsumerServicesNotReceived
    """Services not received.

    Required if and only if `category` is `consumer_services_not_received`.
    """

    fraud: VisaFraud
    """Fraud. Required if and only if `category` is `fraud`."""

    processing_error: VisaProcessingError
    """Processing error. Required if and only if `category` is `processing_error`."""
