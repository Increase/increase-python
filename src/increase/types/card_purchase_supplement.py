# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardPurchaseSupplement", "Invoice", "LineItem"]


class Invoice(BaseModel):
    discount_amount: Optional[int]
    """Discount given to cardholder."""

    discount_currency: Optional[str]
    """The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the discount."""

    discount_treatment_code: Optional[
        Literal[
            "no_invoice_level_discount_provided",
            "tax_calculated_on_post_discount_invoice_total",
            "tax_calculated_on_pre_discount_invoice_total",
        ]
    ]
    """Indicates how the merchant applied the discount.

    - `no_invoice_level_discount_provided` - No invoice level discount provided
    - `tax_calculated_on_post_discount_invoice_total` - Tax calculated on post
      discount invoice total
    - `tax_calculated_on_pre_discount_invoice_total` - Tax calculated on pre
      discount invoice total
    """

    duty_tax_amount: Optional[int]
    """Amount of duty taxes."""

    duty_tax_currency: Optional[str]
    """The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the duty tax."""

    order_date: Optional[date]
    """Date the order was taken."""

    shipping_amount: Optional[int]
    """The shipping cost."""

    shipping_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the shipping
    cost.
    """

    shipping_destination_country_code: Optional[str]
    """Country code of the shipping destination."""

    shipping_destination_postal_code: Optional[str]
    """Postal code of the shipping destination."""

    shipping_source_postal_code: Optional[str]
    """Postal code of the location being shipped from."""

    shipping_tax_amount: Optional[int]
    """Taxes paid for freight and shipping."""

    shipping_tax_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the shipping
    tax.
    """

    shipping_tax_rate: Optional[str]
    """Tax rate for freight and shipping."""

    tax_treatments: Optional[
        Literal[
            "no_tax_applies",
            "net_price_line_item_level",
            "net_price_invoice_level",
            "gross_price_line_item_level",
            "gross_price_invoice_level",
        ]
    ]
    """Indicates how the merchant applied taxes.

    - `no_tax_applies` - No tax applies
    - `net_price_line_item_level` - Net price line item level
    - `net_price_invoice_level` - Net price invoice level
    - `gross_price_line_item_level` - Gross price line item level
    - `gross_price_invoice_level` - Gross price invoice level
    """

    unique_value_added_tax_invoice_reference: Optional[str]
    """Value added tax invoice reference number."""


class LineItem(BaseModel):
    detail_indicator: Optional[Literal["normal", "credit", "payment"]]
    """Indicates the type of line item.

    - `normal` - Normal
    - `credit` - Credit
    - `payment` - Purchase
    """

    discount_amount: Optional[int]
    """Discount amount for this specific line item."""

    discount_currency: Optional[str]
    """The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the discount."""

    discount_treatment_code: Optional[
        Literal[
            "no_line_item_level_discount_provided",
            "tax_calculated_on_post_discount_line_item_total",
            "tax_calculated_on_pre_discount_line_item_total",
        ]
    ]
    """Indicates how the merchant applied the discount for this specific line item.

    - `no_line_item_level_discount_provided` - No line item level discount provided
    - `tax_calculated_on_post_discount_line_item_total` - Tax calculated on post
      discount line item total
    - `tax_calculated_on_pre_discount_line_item_total` - Tax calculated on pre
      discount line item total
    """

    item_commodity_code: Optional[str]
    """Code used to categorize the purchase item."""

    item_descriptor: Optional[str]
    """Description of the purchase item."""

    item_quantity: Optional[str]
    """The number of units of the product being purchased."""

    product_code: Optional[str]
    """Code used to categorize the product being purchased."""

    sales_tax_amount: Optional[int]
    """Sales tax amount for this line item."""

    sales_tax_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the sales tax
    assessed.
    """

    sales_tax_rate: Optional[str]
    """Sales tax rate for this line item."""

    total_amount: Optional[int]
    """Total amount of all line items."""

    total_amount_currency: Optional[str]
    """
    The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the total
    amount.
    """

    unit_cost: Optional[str]
    """Cost of line item per unit of measure, in major units."""

    unit_cost_currency: Optional[str]
    """The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the unit cost."""

    unit_of_measure_code: Optional[str]
    """Code indicating unit of measure (gallons, etc.)."""


class CardPurchaseSupplement(BaseModel):
    id: str
    """The Card Purchase Supplement identifier."""

    card_payment_id: Optional[str]
    """The ID of the Card Payment this transaction belongs to."""

    invoice: Optional[Invoice]
    """Invoice-level information about the payment."""

    line_items: Optional[List[LineItem]]
    """Line item information, such as individual products purchased."""

    transaction_id: str
    """The ID of the transaction."""

    type: Literal["card_purchase_supplement"]
    """A constant representing the object's type.

    For this resource it will always be `card_purchase_supplement`.
    """
