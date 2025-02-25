from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class UrlscanioCredentials(BaseModel):
    """Credentials for urlScanIo authentication."""
    url_scan_io_api: Optional[Dict[str, Any]] = Field(None, description="urlScanIoApi")

class UrlscanioGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[UrlscanioCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    scan_id: Optional[str] = Field(None, description="ID of the scan to retrieve")
    operation: Optional[str] = Field(None, description="Operation")


class UrlscanioGetTool(BaseTool):
    name = "urlscanio_get"
    description = "Tool for urlScanIo get operation - get operation"
    
    def __init__(self, credentials: Optional[UrlscanioCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the urlScanIo get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running urlScanIo get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running urlScanIo get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the urlScanIo get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
