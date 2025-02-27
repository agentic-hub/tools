from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import StripeCredentials

class StripeCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    expiration_month: Optional[str] = Field(None, description="Number of the month when the card will expire")
    customer_id: Optional[str] = Field(None, description="ID of the customer to be associated with this charge")
    cvc: Optional[str] = Field(None, description="Security code printed on the back of the card")
    percent_off: Optional[float] = Field(None, description="Percentage to apply with the coupon")
    type: Optional[str] = Field(None, description="Whether the coupon discount is a percentage or a fixed amount")
    source_id: Optional[str] = Field(None, description="ID of the source to retrieve")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    charge_id: Optional[str] = Field(None, description="ID of the charge to retrieve")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Full name or business name of the customer to create")
    number: Optional[str] = Field(None, description="Card Number")
    amount_off: Optional[float] = Field(None, description="Amount in cents to subtract from an invoice total, e.g. enter <code>100</code> for $1.00")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    currency: Optional[str] = Field(None, description="Three-letter ISO currency code, e.g. <code>USD</code> or <code>EUR</code>. It must be a <a href=\"https://stripe.com/docs/currencies\">Stripe-supported currency</a>. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    source: Optional[str] = Field(None, description="ID of the customer's payment source to be charged")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    amount: Optional[float] = Field(None, description="Amount in cents to be collected for this charge, e.g. enter <code>100</code> for $1.00")
    expiration_year: Optional[str] = Field(None, description="Year when the card will expire")
    duration: Optional[str] = Field(None, description="How long the discount will be in effect")


class StripeCreateTool(BaseTool):
    name: str = "stripe_create"
    connector_id: str = "nodes-base.stripe"
    description: str = "Tool for stripe create operation - create operation"
    args_schema: type[BaseModel] | None = StripeCreateToolInput
    credentials: Optional[StripeCredentials] = None
