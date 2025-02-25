from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PaypalCredentials(BaseModel):
    """Credentials for payPal authentication."""
    pay_pal_api: Optional[Dict[str, Any]] = Field(None, description="payPalApi")

class PaypalCancelToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[PaypalCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    payout_item_id: Optional[str] = Field(None, description="The ID of the payout item to cancel")


class PaypalCancelTool(BaseTool):
    name = "paypal_cancel"
    description = "Tool for payPal cancel operation - cancel operation"
    
    def __init__(self, credentials: Optional[PaypalCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the payPal cancel operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running payPal cancel operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running payPal cancel operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the payPal cancel operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
