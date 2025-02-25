from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CloudflareCredentials(BaseModel):
    """Credentials for cloudflare authentication."""
    cloudflare_api: Optional[Dict[str, Any]] = Field(None, description="cloudflareApi")

class CloudflareUploadToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[CloudflareCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    private_key: Optional[str] = Field(None, description="Private Key")
    zone_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    certificate: Optional[str] = Field(None, description="The zone's leaf certificate")
    operation: Optional[str] = Field(None, description="Operation")


class CloudflareUploadTool(BaseTool):
    name = "cloudflare_upload"
    description = "Tool for cloudflare upload operation - upload operation"
    
    def __init__(self, credentials: Optional[CloudflareCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the cloudflare upload operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running cloudflare upload operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running cloudflare upload operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the cloudflare upload operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
