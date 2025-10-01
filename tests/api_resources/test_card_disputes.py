# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from increase import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from increase.types import (
    CardDispute,
)
from increase._utils import parse_date, parse_datetime
from increase.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardDisputes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Increase) -> None:
        card_dispute = client.card_disputes.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            network="visa",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Increase) -> None:
        card_dispute = client.card_disputes.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            network="visa",
            amount=100,
            attachment_files=[{"file_id": "file_id"}],
            visa={
                "category": "fraud",
                "authorization": {"account_status": "account_closed"},
                "consumer_canceled_merchandise": {
                    "merchant_resolution_attempted": "attempted",
                    "purchase_explanation": "x",
                    "received_or_expected_at": parse_date("2019-12-27"),
                    "return_outcome": "not_returned",
                    "cardholder_cancellation": {
                        "canceled_at": parse_date("2019-12-27"),
                        "canceled_prior_to_ship_date": "canceled_prior_to_ship_date",
                        "cancellation_policy_provided": "not_provided",
                        "reason": "x",
                    },
                    "not_returned": {},
                    "return_attempted": {
                        "attempt_explanation": "x",
                        "attempt_reason": "merchant_not_responding",
                        "attempted_at": parse_date("2019-12-27"),
                        "merchandise_disposition": "x",
                    },
                    "returned": {
                        "return_method": "dhl",
                        "returned_at": parse_date("2019-12-27"),
                        "merchant_received_return_at": parse_date("2019-12-27"),
                        "other_explanation": "x",
                        "tracking_number": "x",
                    },
                },
                "consumer_canceled_recurring_transaction": {
                    "cancellation_target": "account",
                    "merchant_contact_methods": {
                        "application_name": "x",
                        "call_center_phone_number": "x",
                        "email_address": "x",
                        "in_person_address": "x",
                        "mailing_address": "x",
                        "text_phone_number": "x",
                    },
                    "transaction_or_account_canceled_at": parse_date("2019-12-27"),
                    "other_form_of_payment_explanation": "x",
                },
                "consumer_canceled_services": {
                    "cardholder_cancellation": {
                        "canceled_at": parse_date("2019-12-27"),
                        "cancellation_policy_provided": "not_provided",
                        "reason": "x",
                    },
                    "contracted_at": parse_date("2019-12-27"),
                    "merchant_resolution_attempted": "attempted",
                    "purchase_explanation": "x",
                    "service_type": "guaranteed_reservation",
                    "guaranteed_reservation": {"explanation": "cardholder_canceled_prior_to_service"},
                    "other": {},
                    "timeshare": {},
                },
                "consumer_counterfeit_merchandise": {
                    "counterfeit_explanation": "x",
                    "disposition_explanation": "x",
                    "order_explanation": "x",
                    "received_at": parse_date("2019-12-27"),
                },
                "consumer_credit_not_processed": {
                    "canceled_or_returned_at": parse_date("2019-12-27"),
                    "credit_expected_at": parse_date("2019-12-27"),
                },
                "consumer_damaged_or_defective_merchandise": {
                    "merchant_resolution_attempted": "attempted",
                    "order_and_issue_explanation": "x",
                    "received_at": parse_date("2019-12-27"),
                    "return_outcome": "not_returned",
                    "not_returned": {},
                    "return_attempted": {
                        "attempt_explanation": "x",
                        "attempt_reason": "merchant_not_responding",
                        "attempted_at": parse_date("2019-12-27"),
                        "merchandise_disposition": "x",
                    },
                    "returned": {
                        "return_method": "dhl",
                        "returned_at": parse_date("2019-12-27"),
                        "merchant_received_return_at": parse_date("2019-12-27"),
                        "other_explanation": "x",
                        "tracking_number": "x",
                    },
                },
                "consumer_merchandise_misrepresentation": {
                    "merchant_resolution_attempted": "attempted",
                    "misrepresentation_explanation": "x",
                    "purchase_explanation": "x",
                    "received_at": parse_date("2019-12-27"),
                    "return_outcome": "not_returned",
                    "not_returned": {},
                    "return_attempted": {
                        "attempt_explanation": "x",
                        "attempt_reason": "merchant_not_responding",
                        "attempted_at": parse_date("2019-12-27"),
                        "merchandise_disposition": "x",
                    },
                    "returned": {
                        "return_method": "dhl",
                        "returned_at": parse_date("2019-12-27"),
                        "merchant_received_return_at": parse_date("2019-12-27"),
                        "other_explanation": "x",
                        "tracking_number": "x",
                    },
                },
                "consumer_merchandise_not_as_described": {
                    "merchant_resolution_attempted": "attempted",
                    "received_at": parse_date("2019-12-27"),
                    "return_outcome": "returned",
                    "return_attempted": {
                        "attempt_explanation": "x",
                        "attempt_reason": "merchant_not_responding",
                        "attempted_at": parse_date("2019-12-27"),
                        "merchandise_disposition": "x",
                    },
                    "returned": {
                        "return_method": "dhl",
                        "returned_at": parse_date("2019-12-27"),
                        "merchant_received_return_at": parse_date("2019-12-27"),
                        "other_explanation": "x",
                        "tracking_number": "x",
                    },
                },
                "consumer_merchandise_not_received": {
                    "cancellation_outcome": "cardholder_cancellation_prior_to_expected_receipt",
                    "delivery_issue": "delayed",
                    "last_expected_receipt_at": parse_date("2019-12-27"),
                    "merchant_resolution_attempted": "attempted",
                    "purchase_info_and_explanation": "x",
                    "cardholder_cancellation_prior_to_expected_receipt": {
                        "canceled_at": parse_date("2019-12-27"),
                        "reason": "x",
                    },
                    "delayed": {
                        "explanation": "x",
                        "return_outcome": "not_returned",
                        "not_returned": {},
                        "return_attempted": {"attempted_at": parse_date("2019-12-27")},
                        "returned": {
                            "merchant_received_return_at": parse_date("2019-12-27"),
                            "returned_at": parse_date("2019-12-27"),
                        },
                    },
                    "delivered_to_wrong_location": {"agreed_location": "x"},
                    "merchant_cancellation": {"canceled_at": parse_date("2019-12-27")},
                    "no_cancellation": {},
                },
                "consumer_non_receipt_of_cash": {},
                "consumer_original_credit_transaction_not_accepted": {
                    "explanation": "x",
                    "reason": "prohibited_by_local_laws_or_regulation",
                },
                "consumer_quality_merchandise": {
                    "expected_at": parse_date("2019-12-27"),
                    "merchant_resolution_attempted": "attempted",
                    "purchase_info_and_quality_issue": "x",
                    "received_at": parse_date("2019-12-27"),
                    "return_outcome": "not_returned",
                    "not_returned": {},
                    "ongoing_negotiations": {
                        "explanation": "x",
                        "issuer_first_notified_at": parse_date("2019-12-27"),
                        "started_at": parse_date("2019-12-27"),
                    },
                    "return_attempted": {
                        "attempt_explanation": "x",
                        "attempt_reason": "merchant_not_responding",
                        "attempted_at": parse_date("2019-12-27"),
                        "merchandise_disposition": "x",
                    },
                    "returned": {
                        "return_method": "dhl",
                        "returned_at": parse_date("2019-12-27"),
                        "merchant_received_return_at": parse_date("2019-12-27"),
                        "other_explanation": "x",
                        "tracking_number": "x",
                    },
                },
                "consumer_quality_services": {
                    "cardholder_cancellation": {
                        "accepted_by_merchant": "accepted",
                        "canceled_at": parse_date("2019-12-27"),
                        "reason": "x",
                    },
                    "non_fiat_currency_or_non_fungible_token_related_and_not_matching_description": "not_related",
                    "purchase_info_and_quality_issue": "x",
                    "services_received_at": parse_date("2019-12-27"),
                    "cardholder_paid_to_have_work_redone": "did_not_pay_to_have_work_redone",
                    "ongoing_negotiations": {
                        "explanation": "x",
                        "issuer_first_notified_at": parse_date("2019-12-27"),
                        "started_at": parse_date("2019-12-27"),
                    },
                    "restaurant_food_related": "not_related",
                },
                "consumer_services_misrepresentation": {
                    "cardholder_cancellation": {
                        "accepted_by_merchant": "accepted",
                        "canceled_at": parse_date("2019-12-27"),
                        "reason": "x",
                    },
                    "merchant_resolution_attempted": "attempted",
                    "misrepresentation_explanation": "x",
                    "purchase_explanation": "x",
                    "received_at": parse_date("2019-12-27"),
                },
                "consumer_services_not_as_described": {
                    "cardholder_cancellation": {
                        "accepted_by_merchant": "accepted",
                        "canceled_at": parse_date("2019-12-27"),
                        "reason": "x",
                    },
                    "merchant_resolution_attempted": "attempted",
                    "received_at": parse_date("2019-12-27"),
                },
                "consumer_services_not_received": {
                    "cancellation_outcome": "cardholder_cancellation_prior_to_expected_receipt",
                    "last_expected_receipt_at": parse_date("2019-12-27"),
                    "merchant_resolution_attempted": "attempted",
                    "purchase_info_and_explanation": "x",
                    "cardholder_cancellation_prior_to_expected_receipt": {
                        "canceled_at": parse_date("2019-12-27"),
                        "reason": "x",
                    },
                    "merchant_cancellation": {"canceled_at": parse_date("2019-12-27")},
                    "no_cancellation": {},
                },
                "fraud": {"fraud_type": "account_or_credentials_takeover"},
                "processing_error": {
                    "error_reason": "duplicate_transaction",
                    "merchant_resolution_attempted": "attempted",
                    "duplicate_transaction": {"other_transaction_id": "x"},
                    "incorrect_amount": {"expected_amount": 0},
                    "paid_by_other_means": {
                        "other_form_of_payment_evidence": "canceled_check",
                        "other_transaction_id": "x",
                    },
                },
            },
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Increase) -> None:
        response = client.card_disputes.with_raw_response.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            network="visa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = response.parse()
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Increase) -> None:
        with client.card_disputes.with_streaming_response.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            network="visa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = response.parse()
            assert_matches_type(CardDispute, card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Increase) -> None:
        card_dispute = client.card_disputes.retrieve(
            "card_dispute_h9sc95nbl1cgltpp7men",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Increase) -> None:
        response = client.card_disputes.with_raw_response.retrieve(
            "card_dispute_h9sc95nbl1cgltpp7men",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = response.parse()
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Increase) -> None:
        with client.card_disputes.with_streaming_response.retrieve(
            "card_dispute_h9sc95nbl1cgltpp7men",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = response.parse()
            assert_matches_type(CardDispute, card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_dispute_id` but received ''"):
            client.card_disputes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Increase) -> None:
        card_dispute = client.card_disputes.list()
        assert_matches_type(SyncPage[CardDispute], card_dispute, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Increase) -> None:
        card_dispute = client.card_disputes.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["user_submission_required"]},
        )
        assert_matches_type(SyncPage[CardDispute], card_dispute, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Increase) -> None:
        response = client.card_disputes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = response.parse()
        assert_matches_type(SyncPage[CardDispute], card_dispute, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Increase) -> None:
        with client.card_disputes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = response.parse()
            assert_matches_type(SyncPage[CardDispute], card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_submit_user_submission(self, client: Increase) -> None:
        card_dispute = client.card_disputes.submit_user_submission(
            card_dispute_id="card_dispute_h9sc95nbl1cgltpp7men",
            network="visa",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_method_submit_user_submission_with_all_params(self, client: Increase) -> None:
        card_dispute = client.card_disputes.submit_user_submission(
            card_dispute_id="card_dispute_h9sc95nbl1cgltpp7men",
            network="visa",
            amount=1,
            attachment_files=[{"file_id": "file_id"}],
            visa={
                "category": "merchant_prearbitration_decline",
                "chargeback": {
                    "category": "authorization",
                    "authorization": {"account_status": "account_closed"},
                    "consumer_canceled_merchandise": {
                        "merchant_resolution_attempted": "attempted",
                        "purchase_explanation": "x",
                        "received_or_expected_at": parse_date("2019-12-27"),
                        "return_outcome": "not_returned",
                        "cardholder_cancellation": {
                            "canceled_at": parse_date("2019-12-27"),
                            "canceled_prior_to_ship_date": "canceled_prior_to_ship_date",
                            "cancellation_policy_provided": "not_provided",
                            "reason": "x",
                        },
                        "not_returned": {},
                        "return_attempted": {
                            "attempt_explanation": "x",
                            "attempt_reason": "merchant_not_responding",
                            "attempted_at": parse_date("2019-12-27"),
                            "merchandise_disposition": "x",
                        },
                        "returned": {
                            "return_method": "dhl",
                            "returned_at": parse_date("2019-12-27"),
                            "merchant_received_return_at": parse_date("2019-12-27"),
                            "other_explanation": "x",
                            "tracking_number": "x",
                        },
                    },
                    "consumer_canceled_recurring_transaction": {
                        "cancellation_target": "account",
                        "merchant_contact_methods": {
                            "application_name": "x",
                            "call_center_phone_number": "x",
                            "email_address": "x",
                            "in_person_address": "x",
                            "mailing_address": "x",
                            "text_phone_number": "x",
                        },
                        "transaction_or_account_canceled_at": parse_date("2019-12-27"),
                        "other_form_of_payment_explanation": "x",
                    },
                    "consumer_canceled_services": {
                        "cardholder_cancellation": {
                            "canceled_at": parse_date("2019-12-27"),
                            "cancellation_policy_provided": "not_provided",
                            "reason": "x",
                        },
                        "contracted_at": parse_date("2019-12-27"),
                        "merchant_resolution_attempted": "attempted",
                        "purchase_explanation": "x",
                        "service_type": "guaranteed_reservation",
                        "guaranteed_reservation": {"explanation": "cardholder_canceled_prior_to_service"},
                        "other": {},
                        "timeshare": {},
                    },
                    "consumer_counterfeit_merchandise": {
                        "counterfeit_explanation": "x",
                        "disposition_explanation": "x",
                        "order_explanation": "x",
                        "received_at": parse_date("2019-12-27"),
                    },
                    "consumer_credit_not_processed": {
                        "canceled_or_returned_at": parse_date("2019-12-27"),
                        "credit_expected_at": parse_date("2019-12-27"),
                    },
                    "consumer_damaged_or_defective_merchandise": {
                        "merchant_resolution_attempted": "attempted",
                        "order_and_issue_explanation": "x",
                        "received_at": parse_date("2019-12-27"),
                        "return_outcome": "not_returned",
                        "not_returned": {},
                        "return_attempted": {
                            "attempt_explanation": "x",
                            "attempt_reason": "merchant_not_responding",
                            "attempted_at": parse_date("2019-12-27"),
                            "merchandise_disposition": "x",
                        },
                        "returned": {
                            "return_method": "dhl",
                            "returned_at": parse_date("2019-12-27"),
                            "merchant_received_return_at": parse_date("2019-12-27"),
                            "other_explanation": "x",
                            "tracking_number": "x",
                        },
                    },
                    "consumer_merchandise_misrepresentation": {
                        "merchant_resolution_attempted": "attempted",
                        "misrepresentation_explanation": "x",
                        "purchase_explanation": "x",
                        "received_at": parse_date("2019-12-27"),
                        "return_outcome": "not_returned",
                        "not_returned": {},
                        "return_attempted": {
                            "attempt_explanation": "x",
                            "attempt_reason": "merchant_not_responding",
                            "attempted_at": parse_date("2019-12-27"),
                            "merchandise_disposition": "x",
                        },
                        "returned": {
                            "return_method": "dhl",
                            "returned_at": parse_date("2019-12-27"),
                            "merchant_received_return_at": parse_date("2019-12-27"),
                            "other_explanation": "x",
                            "tracking_number": "x",
                        },
                    },
                    "consumer_merchandise_not_as_described": {
                        "merchant_resolution_attempted": "attempted",
                        "received_at": parse_date("2019-12-27"),
                        "return_outcome": "returned",
                        "return_attempted": {
                            "attempt_explanation": "x",
                            "attempt_reason": "merchant_not_responding",
                            "attempted_at": parse_date("2019-12-27"),
                            "merchandise_disposition": "x",
                        },
                        "returned": {
                            "return_method": "dhl",
                            "returned_at": parse_date("2019-12-27"),
                            "merchant_received_return_at": parse_date("2019-12-27"),
                            "other_explanation": "x",
                            "tracking_number": "x",
                        },
                    },
                    "consumer_merchandise_not_received": {
                        "cancellation_outcome": "cardholder_cancellation_prior_to_expected_receipt",
                        "delivery_issue": "delayed",
                        "last_expected_receipt_at": parse_date("2019-12-27"),
                        "merchant_resolution_attempted": "attempted",
                        "purchase_info_and_explanation": "x",
                        "cardholder_cancellation_prior_to_expected_receipt": {
                            "canceled_at": parse_date("2019-12-27"),
                            "reason": "x",
                        },
                        "delayed": {
                            "explanation": "x",
                            "return_outcome": "not_returned",
                            "not_returned": {},
                            "return_attempted": {"attempted_at": parse_date("2019-12-27")},
                            "returned": {
                                "merchant_received_return_at": parse_date("2019-12-27"),
                                "returned_at": parse_date("2019-12-27"),
                            },
                        },
                        "delivered_to_wrong_location": {"agreed_location": "x"},
                        "merchant_cancellation": {"canceled_at": parse_date("2019-12-27")},
                        "no_cancellation": {},
                    },
                    "consumer_non_receipt_of_cash": {},
                    "consumer_original_credit_transaction_not_accepted": {
                        "explanation": "x",
                        "reason": "prohibited_by_local_laws_or_regulation",
                    },
                    "consumer_quality_merchandise": {
                        "expected_at": parse_date("2019-12-27"),
                        "merchant_resolution_attempted": "attempted",
                        "purchase_info_and_quality_issue": "x",
                        "received_at": parse_date("2019-12-27"),
                        "return_outcome": "not_returned",
                        "not_returned": {},
                        "ongoing_negotiations": {
                            "explanation": "x",
                            "issuer_first_notified_at": parse_date("2019-12-27"),
                            "started_at": parse_date("2019-12-27"),
                        },
                        "return_attempted": {
                            "attempt_explanation": "x",
                            "attempt_reason": "merchant_not_responding",
                            "attempted_at": parse_date("2019-12-27"),
                            "merchandise_disposition": "x",
                        },
                        "returned": {
                            "return_method": "dhl",
                            "returned_at": parse_date("2019-12-27"),
                            "merchant_received_return_at": parse_date("2019-12-27"),
                            "other_explanation": "x",
                            "tracking_number": "x",
                        },
                    },
                    "consumer_quality_services": {
                        "cardholder_cancellation": {
                            "accepted_by_merchant": "accepted",
                            "canceled_at": parse_date("2019-12-27"),
                            "reason": "x",
                        },
                        "non_fiat_currency_or_non_fungible_token_related_and_not_matching_description": "not_related",
                        "purchase_info_and_quality_issue": "x",
                        "services_received_at": parse_date("2019-12-27"),
                        "cardholder_paid_to_have_work_redone": "did_not_pay_to_have_work_redone",
                        "ongoing_negotiations": {
                            "explanation": "x",
                            "issuer_first_notified_at": parse_date("2019-12-27"),
                            "started_at": parse_date("2019-12-27"),
                        },
                        "restaurant_food_related": "not_related",
                    },
                    "consumer_services_misrepresentation": {
                        "cardholder_cancellation": {
                            "accepted_by_merchant": "accepted",
                            "canceled_at": parse_date("2019-12-27"),
                            "reason": "x",
                        },
                        "merchant_resolution_attempted": "attempted",
                        "misrepresentation_explanation": "x",
                        "purchase_explanation": "x",
                        "received_at": parse_date("2019-12-27"),
                    },
                    "consumer_services_not_as_described": {
                        "cardholder_cancellation": {
                            "accepted_by_merchant": "accepted",
                            "canceled_at": parse_date("2019-12-27"),
                            "reason": "x",
                        },
                        "merchant_resolution_attempted": "attempted",
                        "received_at": parse_date("2019-12-27"),
                    },
                    "consumer_services_not_received": {
                        "cancellation_outcome": "cardholder_cancellation_prior_to_expected_receipt",
                        "last_expected_receipt_at": parse_date("2019-12-27"),
                        "merchant_resolution_attempted": "attempted",
                        "purchase_info_and_explanation": "x",
                        "cardholder_cancellation_prior_to_expected_receipt": {
                            "canceled_at": parse_date("2019-12-27"),
                            "reason": "x",
                        },
                        "merchant_cancellation": {"canceled_at": parse_date("2019-12-27")},
                        "no_cancellation": {},
                    },
                    "fraud": {"fraud_type": "account_or_credentials_takeover"},
                    "processing_error": {
                        "error_reason": "duplicate_transaction",
                        "merchant_resolution_attempted": "attempted",
                        "duplicate_transaction": {"other_transaction_id": "x"},
                        "incorrect_amount": {"expected_amount": 0},
                        "paid_by_other_means": {
                            "other_form_of_payment_evidence": "canceled_check",
                            "other_transaction_id": "x",
                        },
                    },
                },
                "merchant_prearbitration_decline": {
                    "reason": "The pre-arbitration received from the merchantdoes not explain how they obtained permission to charge the card."
                },
                "user_prearbitration": {
                    "reason": "x",
                    "category_change": {
                        "category": "authorization",
                        "reason": "x",
                    },
                },
            },
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_raw_response_submit_user_submission(self, client: Increase) -> None:
        response = client.card_disputes.with_raw_response.submit_user_submission(
            card_dispute_id="card_dispute_h9sc95nbl1cgltpp7men",
            network="visa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = response.parse()
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_streaming_response_submit_user_submission(self, client: Increase) -> None:
        with client.card_disputes.with_streaming_response.submit_user_submission(
            card_dispute_id="card_dispute_h9sc95nbl1cgltpp7men",
            network="visa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = response.parse()
            assert_matches_type(CardDispute, card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_submit_user_submission(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_dispute_id` but received ''"):
            client.card_disputes.with_raw_response.submit_user_submission(
                card_dispute_id="",
                network="visa",
            )

    @parametrize
    def test_method_withdraw(self, client: Increase) -> None:
        card_dispute = client.card_disputes.withdraw(
            "card_dispute_h9sc95nbl1cgltpp7men",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_raw_response_withdraw(self, client: Increase) -> None:
        response = client.card_disputes.with_raw_response.withdraw(
            "card_dispute_h9sc95nbl1cgltpp7men",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = response.parse()
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    def test_streaming_response_withdraw(self, client: Increase) -> None:
        with client.card_disputes.with_streaming_response.withdraw(
            "card_dispute_h9sc95nbl1cgltpp7men",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = response.parse()
            assert_matches_type(CardDispute, card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_withdraw(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_dispute_id` but received ''"):
            client.card_disputes.with_raw_response.withdraw(
                "",
            )


class TestAsyncCardDisputes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncIncrease) -> None:
        card_dispute = await async_client.card_disputes.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            network="visa",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIncrease) -> None:
        card_dispute = await async_client.card_disputes.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            network="visa",
            amount=100,
            attachment_files=[{"file_id": "file_id"}],
            visa={
                "category": "fraud",
                "authorization": {"account_status": "account_closed"},
                "consumer_canceled_merchandise": {
                    "merchant_resolution_attempted": "attempted",
                    "purchase_explanation": "x",
                    "received_or_expected_at": parse_date("2019-12-27"),
                    "return_outcome": "not_returned",
                    "cardholder_cancellation": {
                        "canceled_at": parse_date("2019-12-27"),
                        "canceled_prior_to_ship_date": "canceled_prior_to_ship_date",
                        "cancellation_policy_provided": "not_provided",
                        "reason": "x",
                    },
                    "not_returned": {},
                    "return_attempted": {
                        "attempt_explanation": "x",
                        "attempt_reason": "merchant_not_responding",
                        "attempted_at": parse_date("2019-12-27"),
                        "merchandise_disposition": "x",
                    },
                    "returned": {
                        "return_method": "dhl",
                        "returned_at": parse_date("2019-12-27"),
                        "merchant_received_return_at": parse_date("2019-12-27"),
                        "other_explanation": "x",
                        "tracking_number": "x",
                    },
                },
                "consumer_canceled_recurring_transaction": {
                    "cancellation_target": "account",
                    "merchant_contact_methods": {
                        "application_name": "x",
                        "call_center_phone_number": "x",
                        "email_address": "x",
                        "in_person_address": "x",
                        "mailing_address": "x",
                        "text_phone_number": "x",
                    },
                    "transaction_or_account_canceled_at": parse_date("2019-12-27"),
                    "other_form_of_payment_explanation": "x",
                },
                "consumer_canceled_services": {
                    "cardholder_cancellation": {
                        "canceled_at": parse_date("2019-12-27"),
                        "cancellation_policy_provided": "not_provided",
                        "reason": "x",
                    },
                    "contracted_at": parse_date("2019-12-27"),
                    "merchant_resolution_attempted": "attempted",
                    "purchase_explanation": "x",
                    "service_type": "guaranteed_reservation",
                    "guaranteed_reservation": {"explanation": "cardholder_canceled_prior_to_service"},
                    "other": {},
                    "timeshare": {},
                },
                "consumer_counterfeit_merchandise": {
                    "counterfeit_explanation": "x",
                    "disposition_explanation": "x",
                    "order_explanation": "x",
                    "received_at": parse_date("2019-12-27"),
                },
                "consumer_credit_not_processed": {
                    "canceled_or_returned_at": parse_date("2019-12-27"),
                    "credit_expected_at": parse_date("2019-12-27"),
                },
                "consumer_damaged_or_defective_merchandise": {
                    "merchant_resolution_attempted": "attempted",
                    "order_and_issue_explanation": "x",
                    "received_at": parse_date("2019-12-27"),
                    "return_outcome": "not_returned",
                    "not_returned": {},
                    "return_attempted": {
                        "attempt_explanation": "x",
                        "attempt_reason": "merchant_not_responding",
                        "attempted_at": parse_date("2019-12-27"),
                        "merchandise_disposition": "x",
                    },
                    "returned": {
                        "return_method": "dhl",
                        "returned_at": parse_date("2019-12-27"),
                        "merchant_received_return_at": parse_date("2019-12-27"),
                        "other_explanation": "x",
                        "tracking_number": "x",
                    },
                },
                "consumer_merchandise_misrepresentation": {
                    "merchant_resolution_attempted": "attempted",
                    "misrepresentation_explanation": "x",
                    "purchase_explanation": "x",
                    "received_at": parse_date("2019-12-27"),
                    "return_outcome": "not_returned",
                    "not_returned": {},
                    "return_attempted": {
                        "attempt_explanation": "x",
                        "attempt_reason": "merchant_not_responding",
                        "attempted_at": parse_date("2019-12-27"),
                        "merchandise_disposition": "x",
                    },
                    "returned": {
                        "return_method": "dhl",
                        "returned_at": parse_date("2019-12-27"),
                        "merchant_received_return_at": parse_date("2019-12-27"),
                        "other_explanation": "x",
                        "tracking_number": "x",
                    },
                },
                "consumer_merchandise_not_as_described": {
                    "merchant_resolution_attempted": "attempted",
                    "received_at": parse_date("2019-12-27"),
                    "return_outcome": "returned",
                    "return_attempted": {
                        "attempt_explanation": "x",
                        "attempt_reason": "merchant_not_responding",
                        "attempted_at": parse_date("2019-12-27"),
                        "merchandise_disposition": "x",
                    },
                    "returned": {
                        "return_method": "dhl",
                        "returned_at": parse_date("2019-12-27"),
                        "merchant_received_return_at": parse_date("2019-12-27"),
                        "other_explanation": "x",
                        "tracking_number": "x",
                    },
                },
                "consumer_merchandise_not_received": {
                    "cancellation_outcome": "cardholder_cancellation_prior_to_expected_receipt",
                    "delivery_issue": "delayed",
                    "last_expected_receipt_at": parse_date("2019-12-27"),
                    "merchant_resolution_attempted": "attempted",
                    "purchase_info_and_explanation": "x",
                    "cardholder_cancellation_prior_to_expected_receipt": {
                        "canceled_at": parse_date("2019-12-27"),
                        "reason": "x",
                    },
                    "delayed": {
                        "explanation": "x",
                        "return_outcome": "not_returned",
                        "not_returned": {},
                        "return_attempted": {"attempted_at": parse_date("2019-12-27")},
                        "returned": {
                            "merchant_received_return_at": parse_date("2019-12-27"),
                            "returned_at": parse_date("2019-12-27"),
                        },
                    },
                    "delivered_to_wrong_location": {"agreed_location": "x"},
                    "merchant_cancellation": {"canceled_at": parse_date("2019-12-27")},
                    "no_cancellation": {},
                },
                "consumer_non_receipt_of_cash": {},
                "consumer_original_credit_transaction_not_accepted": {
                    "explanation": "x",
                    "reason": "prohibited_by_local_laws_or_regulation",
                },
                "consumer_quality_merchandise": {
                    "expected_at": parse_date("2019-12-27"),
                    "merchant_resolution_attempted": "attempted",
                    "purchase_info_and_quality_issue": "x",
                    "received_at": parse_date("2019-12-27"),
                    "return_outcome": "not_returned",
                    "not_returned": {},
                    "ongoing_negotiations": {
                        "explanation": "x",
                        "issuer_first_notified_at": parse_date("2019-12-27"),
                        "started_at": parse_date("2019-12-27"),
                    },
                    "return_attempted": {
                        "attempt_explanation": "x",
                        "attempt_reason": "merchant_not_responding",
                        "attempted_at": parse_date("2019-12-27"),
                        "merchandise_disposition": "x",
                    },
                    "returned": {
                        "return_method": "dhl",
                        "returned_at": parse_date("2019-12-27"),
                        "merchant_received_return_at": parse_date("2019-12-27"),
                        "other_explanation": "x",
                        "tracking_number": "x",
                    },
                },
                "consumer_quality_services": {
                    "cardholder_cancellation": {
                        "accepted_by_merchant": "accepted",
                        "canceled_at": parse_date("2019-12-27"),
                        "reason": "x",
                    },
                    "non_fiat_currency_or_non_fungible_token_related_and_not_matching_description": "not_related",
                    "purchase_info_and_quality_issue": "x",
                    "services_received_at": parse_date("2019-12-27"),
                    "cardholder_paid_to_have_work_redone": "did_not_pay_to_have_work_redone",
                    "ongoing_negotiations": {
                        "explanation": "x",
                        "issuer_first_notified_at": parse_date("2019-12-27"),
                        "started_at": parse_date("2019-12-27"),
                    },
                    "restaurant_food_related": "not_related",
                },
                "consumer_services_misrepresentation": {
                    "cardholder_cancellation": {
                        "accepted_by_merchant": "accepted",
                        "canceled_at": parse_date("2019-12-27"),
                        "reason": "x",
                    },
                    "merchant_resolution_attempted": "attempted",
                    "misrepresentation_explanation": "x",
                    "purchase_explanation": "x",
                    "received_at": parse_date("2019-12-27"),
                },
                "consumer_services_not_as_described": {
                    "cardholder_cancellation": {
                        "accepted_by_merchant": "accepted",
                        "canceled_at": parse_date("2019-12-27"),
                        "reason": "x",
                    },
                    "merchant_resolution_attempted": "attempted",
                    "received_at": parse_date("2019-12-27"),
                },
                "consumer_services_not_received": {
                    "cancellation_outcome": "cardholder_cancellation_prior_to_expected_receipt",
                    "last_expected_receipt_at": parse_date("2019-12-27"),
                    "merchant_resolution_attempted": "attempted",
                    "purchase_info_and_explanation": "x",
                    "cardholder_cancellation_prior_to_expected_receipt": {
                        "canceled_at": parse_date("2019-12-27"),
                        "reason": "x",
                    },
                    "merchant_cancellation": {"canceled_at": parse_date("2019-12-27")},
                    "no_cancellation": {},
                },
                "fraud": {"fraud_type": "account_or_credentials_takeover"},
                "processing_error": {
                    "error_reason": "duplicate_transaction",
                    "merchant_resolution_attempted": "attempted",
                    "duplicate_transaction": {"other_transaction_id": "x"},
                    "incorrect_amount": {"expected_amount": 0},
                    "paid_by_other_means": {
                        "other_form_of_payment_evidence": "canceled_check",
                        "other_transaction_id": "x",
                    },
                },
            },
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIncrease) -> None:
        response = await async_client.card_disputes.with_raw_response.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            network="visa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = await response.parse()
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIncrease) -> None:
        async with async_client.card_disputes.with_streaming_response.create(
            disputed_transaction_id="transaction_uyrp7fld2ium70oa7oi",
            network="visa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = await response.parse()
            assert_matches_type(CardDispute, card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIncrease) -> None:
        card_dispute = await async_client.card_disputes.retrieve(
            "card_dispute_h9sc95nbl1cgltpp7men",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIncrease) -> None:
        response = await async_client.card_disputes.with_raw_response.retrieve(
            "card_dispute_h9sc95nbl1cgltpp7men",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = await response.parse()
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIncrease) -> None:
        async with async_client.card_disputes.with_streaming_response.retrieve(
            "card_dispute_h9sc95nbl1cgltpp7men",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = await response.parse()
            assert_matches_type(CardDispute, card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_dispute_id` but received ''"):
            await async_client.card_disputes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIncrease) -> None:
        card_dispute = await async_client.card_disputes.list()
        assert_matches_type(AsyncPage[CardDispute], card_dispute, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIncrease) -> None:
        card_dispute = await async_client.card_disputes.list(
            created_at={
                "after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "before": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_after": parse_datetime("2019-12-27T18:11:19.117Z"),
                "on_or_before": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            cursor="cursor",
            idempotency_key="x",
            limit=1,
            status={"in": ["user_submission_required"]},
        )
        assert_matches_type(AsyncPage[CardDispute], card_dispute, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIncrease) -> None:
        response = await async_client.card_disputes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = await response.parse()
        assert_matches_type(AsyncPage[CardDispute], card_dispute, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIncrease) -> None:
        async with async_client.card_disputes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = await response.parse()
            assert_matches_type(AsyncPage[CardDispute], card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_submit_user_submission(self, async_client: AsyncIncrease) -> None:
        card_dispute = await async_client.card_disputes.submit_user_submission(
            card_dispute_id="card_dispute_h9sc95nbl1cgltpp7men",
            network="visa",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_method_submit_user_submission_with_all_params(self, async_client: AsyncIncrease) -> None:
        card_dispute = await async_client.card_disputes.submit_user_submission(
            card_dispute_id="card_dispute_h9sc95nbl1cgltpp7men",
            network="visa",
            amount=1,
            attachment_files=[{"file_id": "file_id"}],
            visa={
                "category": "merchant_prearbitration_decline",
                "chargeback": {
                    "category": "authorization",
                    "authorization": {"account_status": "account_closed"},
                    "consumer_canceled_merchandise": {
                        "merchant_resolution_attempted": "attempted",
                        "purchase_explanation": "x",
                        "received_or_expected_at": parse_date("2019-12-27"),
                        "return_outcome": "not_returned",
                        "cardholder_cancellation": {
                            "canceled_at": parse_date("2019-12-27"),
                            "canceled_prior_to_ship_date": "canceled_prior_to_ship_date",
                            "cancellation_policy_provided": "not_provided",
                            "reason": "x",
                        },
                        "not_returned": {},
                        "return_attempted": {
                            "attempt_explanation": "x",
                            "attempt_reason": "merchant_not_responding",
                            "attempted_at": parse_date("2019-12-27"),
                            "merchandise_disposition": "x",
                        },
                        "returned": {
                            "return_method": "dhl",
                            "returned_at": parse_date("2019-12-27"),
                            "merchant_received_return_at": parse_date("2019-12-27"),
                            "other_explanation": "x",
                            "tracking_number": "x",
                        },
                    },
                    "consumer_canceled_recurring_transaction": {
                        "cancellation_target": "account",
                        "merchant_contact_methods": {
                            "application_name": "x",
                            "call_center_phone_number": "x",
                            "email_address": "x",
                            "in_person_address": "x",
                            "mailing_address": "x",
                            "text_phone_number": "x",
                        },
                        "transaction_or_account_canceled_at": parse_date("2019-12-27"),
                        "other_form_of_payment_explanation": "x",
                    },
                    "consumer_canceled_services": {
                        "cardholder_cancellation": {
                            "canceled_at": parse_date("2019-12-27"),
                            "cancellation_policy_provided": "not_provided",
                            "reason": "x",
                        },
                        "contracted_at": parse_date("2019-12-27"),
                        "merchant_resolution_attempted": "attempted",
                        "purchase_explanation": "x",
                        "service_type": "guaranteed_reservation",
                        "guaranteed_reservation": {"explanation": "cardholder_canceled_prior_to_service"},
                        "other": {},
                        "timeshare": {},
                    },
                    "consumer_counterfeit_merchandise": {
                        "counterfeit_explanation": "x",
                        "disposition_explanation": "x",
                        "order_explanation": "x",
                        "received_at": parse_date("2019-12-27"),
                    },
                    "consumer_credit_not_processed": {
                        "canceled_or_returned_at": parse_date("2019-12-27"),
                        "credit_expected_at": parse_date("2019-12-27"),
                    },
                    "consumer_damaged_or_defective_merchandise": {
                        "merchant_resolution_attempted": "attempted",
                        "order_and_issue_explanation": "x",
                        "received_at": parse_date("2019-12-27"),
                        "return_outcome": "not_returned",
                        "not_returned": {},
                        "return_attempted": {
                            "attempt_explanation": "x",
                            "attempt_reason": "merchant_not_responding",
                            "attempted_at": parse_date("2019-12-27"),
                            "merchandise_disposition": "x",
                        },
                        "returned": {
                            "return_method": "dhl",
                            "returned_at": parse_date("2019-12-27"),
                            "merchant_received_return_at": parse_date("2019-12-27"),
                            "other_explanation": "x",
                            "tracking_number": "x",
                        },
                    },
                    "consumer_merchandise_misrepresentation": {
                        "merchant_resolution_attempted": "attempted",
                        "misrepresentation_explanation": "x",
                        "purchase_explanation": "x",
                        "received_at": parse_date("2019-12-27"),
                        "return_outcome": "not_returned",
                        "not_returned": {},
                        "return_attempted": {
                            "attempt_explanation": "x",
                            "attempt_reason": "merchant_not_responding",
                            "attempted_at": parse_date("2019-12-27"),
                            "merchandise_disposition": "x",
                        },
                        "returned": {
                            "return_method": "dhl",
                            "returned_at": parse_date("2019-12-27"),
                            "merchant_received_return_at": parse_date("2019-12-27"),
                            "other_explanation": "x",
                            "tracking_number": "x",
                        },
                    },
                    "consumer_merchandise_not_as_described": {
                        "merchant_resolution_attempted": "attempted",
                        "received_at": parse_date("2019-12-27"),
                        "return_outcome": "returned",
                        "return_attempted": {
                            "attempt_explanation": "x",
                            "attempt_reason": "merchant_not_responding",
                            "attempted_at": parse_date("2019-12-27"),
                            "merchandise_disposition": "x",
                        },
                        "returned": {
                            "return_method": "dhl",
                            "returned_at": parse_date("2019-12-27"),
                            "merchant_received_return_at": parse_date("2019-12-27"),
                            "other_explanation": "x",
                            "tracking_number": "x",
                        },
                    },
                    "consumer_merchandise_not_received": {
                        "cancellation_outcome": "cardholder_cancellation_prior_to_expected_receipt",
                        "delivery_issue": "delayed",
                        "last_expected_receipt_at": parse_date("2019-12-27"),
                        "merchant_resolution_attempted": "attempted",
                        "purchase_info_and_explanation": "x",
                        "cardholder_cancellation_prior_to_expected_receipt": {
                            "canceled_at": parse_date("2019-12-27"),
                            "reason": "x",
                        },
                        "delayed": {
                            "explanation": "x",
                            "return_outcome": "not_returned",
                            "not_returned": {},
                            "return_attempted": {"attempted_at": parse_date("2019-12-27")},
                            "returned": {
                                "merchant_received_return_at": parse_date("2019-12-27"),
                                "returned_at": parse_date("2019-12-27"),
                            },
                        },
                        "delivered_to_wrong_location": {"agreed_location": "x"},
                        "merchant_cancellation": {"canceled_at": parse_date("2019-12-27")},
                        "no_cancellation": {},
                    },
                    "consumer_non_receipt_of_cash": {},
                    "consumer_original_credit_transaction_not_accepted": {
                        "explanation": "x",
                        "reason": "prohibited_by_local_laws_or_regulation",
                    },
                    "consumer_quality_merchandise": {
                        "expected_at": parse_date("2019-12-27"),
                        "merchant_resolution_attempted": "attempted",
                        "purchase_info_and_quality_issue": "x",
                        "received_at": parse_date("2019-12-27"),
                        "return_outcome": "not_returned",
                        "not_returned": {},
                        "ongoing_negotiations": {
                            "explanation": "x",
                            "issuer_first_notified_at": parse_date("2019-12-27"),
                            "started_at": parse_date("2019-12-27"),
                        },
                        "return_attempted": {
                            "attempt_explanation": "x",
                            "attempt_reason": "merchant_not_responding",
                            "attempted_at": parse_date("2019-12-27"),
                            "merchandise_disposition": "x",
                        },
                        "returned": {
                            "return_method": "dhl",
                            "returned_at": parse_date("2019-12-27"),
                            "merchant_received_return_at": parse_date("2019-12-27"),
                            "other_explanation": "x",
                            "tracking_number": "x",
                        },
                    },
                    "consumer_quality_services": {
                        "cardholder_cancellation": {
                            "accepted_by_merchant": "accepted",
                            "canceled_at": parse_date("2019-12-27"),
                            "reason": "x",
                        },
                        "non_fiat_currency_or_non_fungible_token_related_and_not_matching_description": "not_related",
                        "purchase_info_and_quality_issue": "x",
                        "services_received_at": parse_date("2019-12-27"),
                        "cardholder_paid_to_have_work_redone": "did_not_pay_to_have_work_redone",
                        "ongoing_negotiations": {
                            "explanation": "x",
                            "issuer_first_notified_at": parse_date("2019-12-27"),
                            "started_at": parse_date("2019-12-27"),
                        },
                        "restaurant_food_related": "not_related",
                    },
                    "consumer_services_misrepresentation": {
                        "cardholder_cancellation": {
                            "accepted_by_merchant": "accepted",
                            "canceled_at": parse_date("2019-12-27"),
                            "reason": "x",
                        },
                        "merchant_resolution_attempted": "attempted",
                        "misrepresentation_explanation": "x",
                        "purchase_explanation": "x",
                        "received_at": parse_date("2019-12-27"),
                    },
                    "consumer_services_not_as_described": {
                        "cardholder_cancellation": {
                            "accepted_by_merchant": "accepted",
                            "canceled_at": parse_date("2019-12-27"),
                            "reason": "x",
                        },
                        "merchant_resolution_attempted": "attempted",
                        "received_at": parse_date("2019-12-27"),
                    },
                    "consumer_services_not_received": {
                        "cancellation_outcome": "cardholder_cancellation_prior_to_expected_receipt",
                        "last_expected_receipt_at": parse_date("2019-12-27"),
                        "merchant_resolution_attempted": "attempted",
                        "purchase_info_and_explanation": "x",
                        "cardholder_cancellation_prior_to_expected_receipt": {
                            "canceled_at": parse_date("2019-12-27"),
                            "reason": "x",
                        },
                        "merchant_cancellation": {"canceled_at": parse_date("2019-12-27")},
                        "no_cancellation": {},
                    },
                    "fraud": {"fraud_type": "account_or_credentials_takeover"},
                    "processing_error": {
                        "error_reason": "duplicate_transaction",
                        "merchant_resolution_attempted": "attempted",
                        "duplicate_transaction": {"other_transaction_id": "x"},
                        "incorrect_amount": {"expected_amount": 0},
                        "paid_by_other_means": {
                            "other_form_of_payment_evidence": "canceled_check",
                            "other_transaction_id": "x",
                        },
                    },
                },
                "merchant_prearbitration_decline": {
                    "reason": "The pre-arbitration received from the merchantdoes not explain how they obtained permission to charge the card."
                },
                "user_prearbitration": {
                    "reason": "x",
                    "category_change": {
                        "category": "authorization",
                        "reason": "x",
                    },
                },
            },
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_raw_response_submit_user_submission(self, async_client: AsyncIncrease) -> None:
        response = await async_client.card_disputes.with_raw_response.submit_user_submission(
            card_dispute_id="card_dispute_h9sc95nbl1cgltpp7men",
            network="visa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = await response.parse()
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_streaming_response_submit_user_submission(self, async_client: AsyncIncrease) -> None:
        async with async_client.card_disputes.with_streaming_response.submit_user_submission(
            card_dispute_id="card_dispute_h9sc95nbl1cgltpp7men",
            network="visa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = await response.parse()
            assert_matches_type(CardDispute, card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_submit_user_submission(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_dispute_id` but received ''"):
            await async_client.card_disputes.with_raw_response.submit_user_submission(
                card_dispute_id="",
                network="visa",
            )

    @parametrize
    async def test_method_withdraw(self, async_client: AsyncIncrease) -> None:
        card_dispute = await async_client.card_disputes.withdraw(
            "card_dispute_h9sc95nbl1cgltpp7men",
        )
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_raw_response_withdraw(self, async_client: AsyncIncrease) -> None:
        response = await async_client.card_disputes.with_raw_response.withdraw(
            "card_dispute_h9sc95nbl1cgltpp7men",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_dispute = await response.parse()
        assert_matches_type(CardDispute, card_dispute, path=["response"])

    @parametrize
    async def test_streaming_response_withdraw(self, async_client: AsyncIncrease) -> None:
        async with async_client.card_disputes.with_streaming_response.withdraw(
            "card_dispute_h9sc95nbl1cgltpp7men",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_dispute = await response.parse()
            assert_matches_type(CardDispute, card_dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_withdraw(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_dispute_id` but received ''"):
            await async_client.card_disputes.with_raw_response.withdraw(
                "",
            )
