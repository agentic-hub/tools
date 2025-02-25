from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RaindropCredentials(BaseModel):
    """Credentials for raindrop authentication."""
    raindrop_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="raindropOAuth2Api")

class RaindropDeleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[RaindropCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    bookmark_id: Optional[str] = Field(None, description="The ID of the bookmark to delete")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    tags: Optional[str] = Field(None, description="One or more tags to delete. Enter comma-separated values to delete multiple tags.")
    collection_id: Optional[str] = Field(None, description="The ID of the collection to delete")
    operation: Optional[str] = Field(None, description="Operation")


class RaindropDeleteTool(BaseTool):
    name = "raindrop_delete"
    description = "Tool for raindrop delete operation - delete operation"
    
    def __init__(self, credentials: Optional[RaindropCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the raindrop delete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running raindrop delete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running raindrop delete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the raindrop delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
