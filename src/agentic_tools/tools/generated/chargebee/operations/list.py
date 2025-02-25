from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ChargebeeCredentials(BaseModel):
    """Credentials for chargebee authentication."""
    chargebee_api: Optional[Dict[str, Any]] = Field(None, description="chargebeeApi")

class ChargebeeListToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ChargebeeCredentials] = Field(None, description="Custom credentials for authentication")
    max_results: Optional[float] = Field(None, description="Max. amount of results to return(< 100).")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filter for invoices")
    subscription_id: Optional[str] = Field(None, description="The ID of the subscription to cancel")


class ChargebeeListTool(BaseTool):
    name = "chargebee_list"
    description = "Tool for chargebee list operation - list operation"
    
    def __init__(self, credentials: Optional[ChargebeeCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the chargebee list operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running chargebee list operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running chargebee list operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the chargebee list operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
