# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CardPurchaseSupplementCreateParams", "Invoice", "LineItem"]


class CardPurchaseSupplementCreateParams(TypedDict, total=False):
    transaction_id: Required[str]
    """The identifier of the Transaction to create a Card Purchase Supplement for.

    The Transaction must have a source of type `card_settlement`.
    """

    invoice: Invoice
    """Invoice-level information about the payment."""

    line_items: Iterable[LineItem]
    """Line item information, such as individual products purchased."""


class Invoice(TypedDict, total=False):
    """Invoice-level information about the payment."""

    discount_amount: int
    """Discount given to cardholder."""

    duty_tax_amount: int
    """Amount of duty taxes."""

    order_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Date the order was taken."""

    shipping_amount: int
    """The shipping cost."""

    shipping_destination_country_code: str
    """Country code of the shipping destination."""

    shipping_destination_postal_code: str
    """Postal code of the shipping destination."""

    shipping_source_postal_code: str
    """Postal code of the location being shipped from."""

    shipping_tax_amount: int
    """Taxes paid for freight and shipping."""

    shipping_tax_rate: str
    """Tax rate for freight and shipping."""

    unique_value_added_tax_invoice_reference: str
    """Value added tax invoice reference number."""


class LineItem(TypedDict, total=False):
    discount_amount: int
    """Discount amount for this specific line item."""

    item_commodity_code: str
    """Code used to categorize the purchase item."""

    item_descriptor: str
    """Description of the purchase item."""

    item_quantity: str
    """The number of units of the product being purchased."""

    product_code: str
    """Code used to categorize the product being purchased."""

    sales_tax_amount: int
    """Sales tax amount for this line item."""

    sales_tax_rate: str
    """Sales tax rate for this line item."""

    total_amount: int
    """Total amount of all line items."""

    unit_cost: str
    """Cost of line item per unit of measure, in major units."""

    unit_of_measure_code: str
    """Code indicating unit of measure (gallons, etc.)."""
