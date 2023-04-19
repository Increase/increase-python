# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Document"]


class Document(BaseModel):
    category: Literal[
        "anti_money_laundering_policy",
        "anti_money_laundering_procedures",
        "audit_report",
        "background_checks",
        "business_continuity_plan",
        "collections_policy",
        "complaints_policy",
        "complaint_report",
        "compliance_report",
        "compliance_management_system_policy",
        "consumer_protection_policy",
        "corporate_formation_document",
        "credit_monitoring_report",
        "customer_information_program_policy",
        "employee_overview",
        "end_user_terms_of_service",
        "financial_statement",
        "form_1099_int",
        "fraud_prevention_policy",
        "funds_flow_diagram",
        "information_security_policy",
        "insurance_policy",
        "investor_presentation",
        "loan_application_processing_policy",
        "management_biography",
        "marketing_and_advertising_policy",
        "network_security_diagram",
        "onboarding_questionnaire",
        "penetration_test_report",
        "program_risk_assessment",
        "security_audit_report",
        "servicing_policy",
        "transaction_monitoring_report",
        "underwriting_policy",
        "vendor_list",
        "vendor_management_policy",
        "vendor_risk_management_report",
        "volume_forecast",
    ]
    """The type of document."""

    created_at: datetime
    """
    The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the
    Document was created.
    """

    entity_id: Optional[str]
    """The identifier of the Entity the document was generated for."""

    file_id: str
    """The identifier of the File containing the Document's contents."""

    id: str
    """The Document identifier."""

    type: Literal["document"]
    """A constant representing the object's type.

    For this resource it will always be `document`.
    """
