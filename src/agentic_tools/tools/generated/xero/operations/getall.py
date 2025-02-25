from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class XeroCredentials(BaseModel):
    """Credentials for xero authentication."""
    xero_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="xeroOAuth2Api")

class XeroGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[XeroCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    invoice_id: Optional[str] = Field(None, description="Invoice ID")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    organization_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    operation: Optional[str] = Field(None, description="Operation")


class XeroGetallTool(BaseTool):
    name = "xero_getall"
    description = "Tool for xero getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[XeroCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the xero getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running xero getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running xero getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the xero getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
