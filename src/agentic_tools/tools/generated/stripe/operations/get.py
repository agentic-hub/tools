from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StripeGetToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    customerId: Optional[str] = Field(None, description="ID of the customer whose card to retrieve")
    type: Optional[str] = Field(None, description="Whether the coupon discount is a percentage or a fixed amount")
    sourceId: Optional[str] = Field(None, description="ID of the source to retrieve")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    chargeId: Optional[str] = Field(None, description="ID of the charge to retrieve")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    currency: Optional[str] = Field(None, description="Three-letter ISO currency code, e.g. <code>USD</code> or <code>EUR</code>. It must be a <a href=\"https://stripe.com/docs/currencies\">Stripe-supported currency</a>. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    amount: Optional[float] = Field(None, description="Amount in cents to be collected for this charge, e.g. enter <code>100</code> for $1.00")


class StripeGetTool(BaseTool):
    name = "stripe_get"
    description = "Tool for stripe get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the stripe get operation."""
        # Implement the tool logic here
        return f"Running stripe get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the stripe get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
