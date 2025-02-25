from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ZammadCredentials(BaseModel):
    """Credentials for zammad authentication."""
    zammad_basic_auth_api: Optional[Dict[str, Any]] = Field(None, description="zammadBasicAuthApi")
    zammad_token_auth_api: Optional[Dict[str, Any]] = Field(None, description="zammadTokenAuthApi")

class ZammadGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ZammadCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="Group to retrieve. Specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Group Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")


class ZammadGetTool(BaseTool):
    name = "zammad_get"
    description = "Tool for zammad get operation - get operation"
    
    def __init__(self, credentials: Optional[ZammadCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the zammad get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running zammad get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running zammad get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the zammad get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
