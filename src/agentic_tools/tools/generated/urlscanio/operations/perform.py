from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class UrlscanioCredentials(BaseModel):
    """Credentials for urlScanIo authentication."""
    url_scan_io_api: Optional[Dict[str, Any]] = Field(None, description="urlScanIoApi")

class UrlscanioPerformToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[UrlscanioCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    url: Optional[str] = Field(None, description="URL to scan")
    operation: Optional[str] = Field(None, description="Operation")


class UrlscanioPerformTool(BaseTool):
    name = "urlscanio_perform"
    description = "Tool for urlScanIo perform operation - perform operation"
    
    def __init__(self, credentials: Optional[UrlscanioCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the urlScanIo perform operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running urlScanIo perform operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running urlScanIo perform operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the urlScanIo perform operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
