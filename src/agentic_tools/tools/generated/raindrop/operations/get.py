from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RaindropCredentials(BaseModel):
    """Credentials for raindrop authentication."""
    raindrop_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="raindropOAuth2Api")

class RaindropGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[RaindropCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    bookmark_id: Optional[str] = Field(None, description="The ID of the bookmark to retrieve")
    user_id: Optional[str] = Field(None, description="The ID of the user to retrieve")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    self: Optional[bool] = Field(None, description="Whether to return details on the logged-in user")
    collection_id: Optional[str] = Field(None, description="The ID of the collection to retrieve")
    operation: Optional[str] = Field(None, description="Operation")


class RaindropGetTool(BaseTool):
    name = "raindrop_get"
    description = "Tool for raindrop get operation - get operation"
    
    def __init__(self, credentials: Optional[RaindropCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the raindrop get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running raindrop get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running raindrop get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the raindrop get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
