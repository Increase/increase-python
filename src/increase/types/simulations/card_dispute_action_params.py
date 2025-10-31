# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "CardDisputeActionParams",
    "Visa",
    "VisaAcceptChargeback",
    "VisaAcceptUserSubmission",
    "VisaDeclineUserPrearbitration",
    "VisaReceiveMerchantPrearbitration",
    "VisaRepresent",
    "VisaRequestFurtherInformation",
    "VisaTimeOutChargeback",
    "VisaTimeOutMerchantPrearbitration",
    "VisaTimeOutRepresentment",
    "VisaTimeOutUserPrearbitration",
]


class CardDisputeActionParams(TypedDict, total=False):
    network: Required[Literal["visa"]]
    """The network of the Card Dispute.

    Details specific to the network are required under the sub-object with the same
    identifier as the network.

    - `visa` - Visa
    """

    visa: Visa
    """The Visa-specific parameters for the taking action on the dispute.

    Required if and only if `network` is `visa`.
    """


class VisaAcceptChargeback(TypedDict, total=False):
    pass


class VisaAcceptUserSubmission(TypedDict, total=False):
    pass


class VisaDeclineUserPrearbitration(TypedDict, total=False):
    pass


class VisaReceiveMerchantPrearbitration(TypedDict, total=False):
    pass


class VisaRepresent(TypedDict, total=False):
    pass


class VisaRequestFurtherInformation(TypedDict, total=False):
    reason: Required[str]
    """The reason for requesting further information from the user."""


class VisaTimeOutChargeback(TypedDict, total=False):
    pass


class VisaTimeOutMerchantPrearbitration(TypedDict, total=False):
    pass


class VisaTimeOutRepresentment(TypedDict, total=False):
    pass


class VisaTimeOutUserPrearbitration(TypedDict, total=False):
    pass


class Visa(TypedDict, total=False):
    action: Required[
        Literal[
            "accept_chargeback",
            "accept_user_submission",
            "decline_user_prearbitration",
            "receive_merchant_prearbitration",
            "represent",
            "request_further_information",
            "time_out_chargeback",
            "time_out_merchant_prearbitration",
            "time_out_representment",
            "time_out_user_prearbitration",
        ]
    ]
    """The action to take.

    Details specific to the action are required under the sub-object with the same
    identifier as the action.

    - `accept_chargeback` - Simulate the merchant accepting the chargeback. This
      will move the dispute to a `won` state.
    - `accept_user_submission` - Accept the user's submission and transmit it to the
      network. This will move the dispute to a `pending_response` state.
    - `decline_user_prearbitration` - Simulate the merchant declining the user's
      pre-arbitration. This will move the dispute to a `lost` state.
    - `receive_merchant_prearbitration` - Simulate the merchant issuing
      pre-arbitration. This will move the dispute to a `user_submission_required`
      state.
    - `represent` - Simulate the merchant re-presenting the dispute. This will move
      the dispute to a `user_submission_required` state.
    - `request_further_information` - Simulate further information being requested
      from the user. This will move the dispute to a `user_submission_required`
      state.
    - `time_out_chargeback` - Simulate the merchant timing out responding to the
      chargeback. This will move the dispute to a `won` state.
    - `time_out_merchant_prearbitration` - Simulate the user timing out responding
      to a merchant pre-arbitration. This will move the dispute to a `lost` state.
    - `time_out_representment` - Simulate the user timing out responding to a
      merchant re-presentment. This will move the dispute to a `lost` state.
    - `time_out_user_prearbitration` - Simulate the merchant timing out responding
      to a user pre-arbitration. This will move the dispute to a `win` state.
    """

    accept_chargeback: VisaAcceptChargeback
    """The parameters for accepting the chargeback.

    Required if and only if `action` is `accept_chargeback`.
    """

    accept_user_submission: VisaAcceptUserSubmission
    """The parameters for accepting the user submission.

    Required if and only if `action` is `accept_user_submission`.
    """

    decline_user_prearbitration: VisaDeclineUserPrearbitration
    """The parameters for declining the prearbitration.

    Required if and only if `action` is `decline_user_prearbitration`.
    """

    receive_merchant_prearbitration: VisaReceiveMerchantPrearbitration
    """The parameters for receiving the prearbitration.

    Required if and only if `action` is `receive_merchant_prearbitration`.
    """

    represent: VisaRepresent
    """The parameters for re-presenting the dispute.

    Required if and only if `action` is `represent`.
    """

    request_further_information: VisaRequestFurtherInformation
    """The parameters for requesting further information from the user.

    Required if and only if `action` is `request_further_information`.
    """

    time_out_chargeback: VisaTimeOutChargeback
    """The parameters for timing out the chargeback.

    Required if and only if `action` is `time_out_chargeback`.
    """

    time_out_merchant_prearbitration: VisaTimeOutMerchantPrearbitration
    """The parameters for timing out the merchant prearbitration.

    Required if and only if `action` is `time_out_merchant_prearbitration`.
    """

    time_out_representment: VisaTimeOutRepresentment
    """The parameters for timing out the re-presentment.

    Required if and only if `action` is `time_out_representment`.
    """

    time_out_user_prearbitration: VisaTimeOutUserPrearbitration
    """The parameters for timing out the user prearbitration.

    Required if and only if `action` is `time_out_user_prearbitration`.
    """
