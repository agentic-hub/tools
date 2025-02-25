from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FtpCredentials(BaseModel):
    """Credentials for ftp authentication."""
    ftp: Optional[Dict[str, Any]] = Field(None, description="ftp")
    sftp: Optional[Dict[str, Any]] = Field(None, description="sftp")

class FtpListToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[FtpCredentials] = Field(None, description="Custom credentials for authentication")
    recursive: Optional[bool] = Field(None, description="Whether to return object representing all directories / objects recursively found within SFTP server")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    protocol: Optional[str] = Field(None, description="File transfer protocol")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="Path of directory to list contents of")


class FtpListTool(BaseTool):
    name = "ftp_list"
    description = "Tool for ftp list operation - list operation"
    
    def __init__(self, credentials: Optional[FtpCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the ftp list operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running ftp list operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running ftp list operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the ftp list operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
