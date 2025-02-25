from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GoogledocsCredentials(BaseModel):
    """Credentials for googleDocs authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")
    google_docs_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleDocsOAuth2Api")

class GoogledocsGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GoogledocsCredentials] = Field(None, description="Custom credentials for authentication")
    document_url: Optional[str] = Field(None, description="The ID in the document URL (or just paste the whole URL)")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    operation: Optional[str] = Field(None, description="Operation")


class GoogledocsGetTool(BaseTool):
    name = "googledocs_get"
    description = "Tool for googleDocs get operation - get operation"
    
    def __init__(self, credentials: Optional[GoogledocsCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleDocs get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleDocs get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleDocs get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleDocs get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
