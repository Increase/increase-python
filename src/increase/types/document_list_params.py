# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentListParams", "Category", "CreatedAt"]


class DocumentListParams(TypedDict, total=False):
    category: Category

    created_at: CreatedAt

    cursor: str
    """Return the page of entries after this one."""

    entity_id: str
    """Filter Documents to ones belonging to the specified Entity."""

    limit: int
    """Limit the size of the list that is returned.

    The default (and maximum) is 100 objects.
    """


_CategoryReservedKeywords = TypedDict(
    "_CategoryReservedKeywords",
    {
        "in": List[
            Literal[
                "account_opening_disclosures",
                "anti_money_laundering_policy",
                "anti_money_laundering_procedures",
                "audit_report",
                "background_checks",
                "business_continuity_plan",
                "collections_policy",
                "complaints_policy",
                "complaint_report",
                "compliance_report",
                "compliance_staffing_plan",
                "compliance_management_system_policy",
                "consumer_privacy_notice",
                "consumer_protection_policy",
                "corporate_formation_document",
                "credit_monitoring_report",
                "customer_information_program_policy",
                "electronic_funds_tranfer_act_policy",
                "employee_overview",
                "end_user_terms_of_service",
                "e_sign_policy",
                "financial_statement",
                "form_1099_int",
                "fraud_prevention_policy",
                "funds_availability_policy",
                "funds_availability_disclosure",
                "funds_flow_diagram",
                "gramm_leach_bliley_act_policy",
                "information_security_policy",
                "insurance_policy",
                "investor_presentation",
                "loan_application_processing_policy",
                "management_biography",
                "marketing_and_advertising_policy",
                "network_security_diagram",
                "onboarding_questionnaire",
                "penetration_test_report",
                "platform_compliance_metrics_submission",
                "consumer_platform_compliance_metrics_submission",
                "program_risk_assessment",
                "security_audit_report",
                "servicing_policy",
                "transaction_monitoring_report",
                "truth_in_savings_act_policy",
                "underwriting_policy",
                "vendor_list",
                "vendor_management_policy",
                "vendor_risk_management_report",
                "volume_forecast",
            ]
        ],
    },
    total=False,
)


class Category(_CategoryReservedKeywords, total=False):
    pass


class CreatedAt(TypedDict, total=False):
    after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    timestamp.
    """

    before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    timestamp.
    """

    on_or_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results on or after this
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp.
    """

    on_or_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Return results on or before this
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp.
    """
