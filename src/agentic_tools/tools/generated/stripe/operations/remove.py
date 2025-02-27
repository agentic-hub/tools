from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import StripeCredentials

class StripeRemoveToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    customer_id: Optional[str] = Field(None, description="ID of the customer whose card to remove")
    type: Optional[str] = Field(None, description="Whether the coupon discount is a percentage or a fixed amount")
    source_id: Optional[str] = Field(None, description="ID of the source to retrieve")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    charge_id: Optional[str] = Field(None, description="ID of the charge to retrieve")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    currency: Optional[str] = Field(None, description="Three-letter ISO currency code, e.g. <code>USD</code> or <code>EUR</code>. It must be a <a href=\"https://stripe.com/docs/currencies\">Stripe-supported currency</a>. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    card_id: Optional[str] = Field(None, description="ID of the card to remove")
    amount: Optional[float] = Field(None, description="Amount in cents to be collected for this charge, e.g. enter <code>100</code> for $1.00")


class StripeRemoveTool(BaseTool):
    name: str = "stripe_remove"
    description: str = "Tool for stripe remove operation - remove operation"
    args_schema: type[BaseModel] | None = StripeRemoveToolInput
    credentials: Optional[StripeCredentials] = None
