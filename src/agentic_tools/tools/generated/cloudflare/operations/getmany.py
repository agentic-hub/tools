from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CloudflareCredentials(BaseModel):
    """Credentials for cloudflare authentication."""
    cloudflare_api: Optional[Dict[str, Any]] = Field(None, description="cloudflareApi")

class CloudflareGetmanyToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[CloudflareCredentials] = Field(None, description="Custom credentials for authentication")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    zone_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class CloudflareGetmanyTool(BaseTool):
    name = "cloudflare_getmany"
    description = "Tool for cloudflare getMany operation - getMany operation"
    
    def __init__(self, credentials: Optional[CloudflareCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the cloudflare getMany operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running cloudflare getMany operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running cloudflare getMany operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the cloudflare getMany operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
