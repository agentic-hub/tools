from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StripeCredentials(BaseModel):
    """Credentials for stripe authentication."""
    stripe_api: Optional[Dict[str, Any]] = Field(None, description="stripeApi")

class StripeGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[StripeCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    customer_id: Optional[str] = Field(None, description="ID of the customer whose card to retrieve")
    type: Optional[str] = Field(None, description="Whether the coupon discount is a percentage or a fixed amount")
    source_id: Optional[str] = Field(None, description="ID of the source to retrieve")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    charge_id: Optional[str] = Field(None, description="ID of the charge to retrieve")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    currency: Optional[str] = Field(None, description="Three-letter ISO currency code, e.g. <code>USD</code> or <code>EUR</code>. It must be a <a href=\"https://stripe.com/docs/currencies\">Stripe-supported currency</a>. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    amount: Optional[float] = Field(None, description="Amount in cents to be collected for this charge, e.g. enter <code>100</code> for $1.00")


class StripeGetTool(BaseTool):
    name = "stripe_get"
    description = "Tool for stripe get operation - get operation"
    
    def __init__(self, credentials: Optional[StripeCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the stripe get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running stripe get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running stripe get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the stripe get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
