from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StrapiCredentials(BaseModel):
    """Credentials for strapi authentication."""
    strapi_api: Optional[Dict[str, Any]] = Field(None, description="strapiApi")
    strapi_token_api: Optional[Dict[str, Any]] = Field(None, description="strapiTokenApi")

class StrapiCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[StrapiCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    entry_id: Optional[str] = Field(None, description="The ID of the entry to delete")
    content_type: Optional[str] = Field(None, description="Name of the content type")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class StrapiCreateTool(BaseTool):
    name = "strapi_create"
    description = "Tool for strapi create operation - create operation"
    
    def __init__(self, credentials: Optional[StrapiCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the strapi create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running strapi create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running strapi create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the strapi create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
