from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FtpCredentials(BaseModel):
    """Credentials for ftp authentication."""
    ftp: Optional[Dict[str, Any]] = Field(None, description="ftp")
    sftp: Optional[Dict[str, Any]] = Field(None, description="sftp")

class FtpDownloadToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[FtpCredentials] = Field(None, description="Custom credentials for authentication")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    protocol: Optional[str] = Field(None, description="File transfer protocol")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The file path of the file to download. Has to contain the full path.")


class FtpDownloadTool(BaseTool):
    name = "ftp_download"
    description = "Tool for ftp download operation - download operation"
    
    def __init__(self, credentials: Optional[FtpCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the ftp download operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running ftp download operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running ftp download operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the ftp download operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
