from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TapfiliateCredentials(BaseModel):
    """Credentials for tapfiliate authentication."""
    tapfiliate_api: Optional[Dict[str, Any]] = Field(None, description="tapfiliateApi")

class TapfiliateUpdateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[TapfiliateCredentials] = Field(None, description="Custom credentials for authentication")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    value: Optional[str] = Field(None, description="Value to set for the metadata key")
    program_id: Optional[str] = Field(None, description="The ID of the Program to add the affiliate to. This ID can be found as part of the URL when viewing the program on the platform. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    key: Optional[str] = Field(None, description="Name of the metadata key to update")
    affiliate_id: Optional[str] = Field(None, description="The ID of the affiliate")
    operation: Optional[str] = Field(None, description="Operation")


class TapfiliateUpdateTool(BaseTool):
    name = "tapfiliate_update"
    description = "Tool for tapfiliate update operation - update operation"
    
    def __init__(self, credentials: Optional[TapfiliateCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the tapfiliate update operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running tapfiliate update operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running tapfiliate update operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the tapfiliate update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
