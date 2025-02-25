from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglebooksCredentials(BaseModel):
    """Credentials for googleBooks authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")
    google_books_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleBooksOAuth2Api")

class GooglebooksGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GooglebooksCredentials] = Field(None, description="Custom credentials for authentication")
    user_id: Optional[str] = Field(None, description="ID of user")
    resource: Optional[str] = Field(None, description="Resource")
    my_library: Optional[bool] = Field(None, description="My Library")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    search_query: Optional[str] = Field(None, description="Full-text search query string")
    authentication: Optional[str] = Field(None, description="Authentication")
    shelf_id: Optional[str] = Field(None, description="ID of the bookshelf")
    operation: Optional[str] = Field(None, description="Operation")


class GooglebooksGetallTool(BaseTool):
    name = "googlebooks_getall"
    description = "Tool for googleBooks getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[GooglebooksCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleBooks getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleBooks getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleBooks getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleBooks getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
