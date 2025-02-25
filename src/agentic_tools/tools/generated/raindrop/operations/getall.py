from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RaindropCredentials(BaseModel):
    """Credentials for raindrop authentication."""
    raindrop_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="raindropOAuth2Api")

class RaindropGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[RaindropCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    bookmark_id: Optional[str] = Field(None, description="The ID of the bookmark to delete")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    collection_id: Optional[str] = Field(None, description="The ID of the collection from which to retrieve all bookmarks. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    type: Optional[str] = Field(None, description="Type")


class RaindropGetallTool(BaseTool):
    name = "raindrop_getall"
    description = "Tool for raindrop getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[RaindropCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the raindrop getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running raindrop getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running raindrop getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the raindrop getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
