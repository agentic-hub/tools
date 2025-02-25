from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ChargebeeCredentials(BaseModel):
    """Credentials for chargebee authentication."""
    chargebee_api: Optional[Dict[str, Any]] = Field(None, description="chargebeeApi")

class ChargebeePdfurlToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ChargebeeCredentials] = Field(None, description="Custom credentials for authentication")
    invoice_id: Optional[str] = Field(None, description="The ID of the invoice to get")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    subscription_id: Optional[str] = Field(None, description="The ID of the subscription to cancel")


class ChargebeePdfurlTool(BaseTool):
    name = "chargebee_pdfurl"
    description = "Tool for chargebee pdfUrl operation - pdfUrl operation"
    
    def __init__(self, credentials: Optional[ChargebeeCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the chargebee pdfUrl operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running chargebee pdfUrl operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running chargebee pdfUrl operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the chargebee pdfUrl operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
