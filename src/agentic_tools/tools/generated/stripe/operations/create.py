from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StripeCreateToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    expirationMonth: Optional[str] = Field(None, description="Number of the month when the card will expire")
    customerId: Optional[str] = Field(None, description="ID of the customer to be associated with this charge")
    cvc: Optional[str] = Field(None, description="Security code printed on the back of the card")
    percentOff: Optional[float] = Field(None, description="Percentage to apply with the coupon")
    type: Optional[str] = Field(None, description="Whether the coupon discount is a percentage or a fixed amount")
    sourceId: Optional[str] = Field(None, description="ID of the source to retrieve")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    chargeId: Optional[str] = Field(None, description="ID of the charge to retrieve")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Full name or business name of the customer to create")
    number: Optional[str] = Field(None, description="Card Number")
    amountOff: Optional[float] = Field(None, description="Amount in cents to subtract from an invoice total, e.g. enter <code>100</code> for $1.00")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    currency: Optional[str] = Field(None, description="Three-letter ISO currency code, e.g. <code>USD</code> or <code>EUR</code>. It must be a <a href=\"https://stripe.com/docs/currencies\">Stripe-supported currency</a>. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    source: Optional[str] = Field(None, description="ID of the customer's payment source to be charged")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    amount: Optional[float] = Field(None, description="Amount in cents to be collected for this charge, e.g. enter <code>100</code> for $1.00")
    expirationYear: Optional[str] = Field(None, description="Year when the card will expire")
    duration: Optional[str] = Field(None, description="How long the discount will be in effect")


class StripeCreateTool(BaseTool):
    name = "stripe_create"
    description = "Tool for stripe create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the stripe create operation."""
        # Implement the tool logic here
        return f"Running stripe create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the stripe create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
