from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MindeeCredentials(BaseModel):
    """Credentials for mindee authentication."""
    mindee_receipt_api: Optional[Dict[str, Any]] = Field(None, description="mindeeReceiptApi")
    mindee_invoice_api: Optional[Dict[str, Any]] = Field(None, description="mindeeInvoiceApi")

class MindeePredictToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MindeeCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    api_version: Optional[str] = Field(None, description="Which Mindee API Version to use")
    raw_data: Optional[bool] = Field(None, description="Whether to return the data exactly in the way it got received from the API")
    operation: Optional[str] = Field(None, description="Operation")


class MindeePredictTool(BaseTool):
    name = "mindee_predict"
    description = "Tool for mindee predict operation - predict operation"
    
    def __init__(self, credentials: Optional[MindeeCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the mindee predict operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running mindee predict operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running mindee predict operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mindee predict operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
