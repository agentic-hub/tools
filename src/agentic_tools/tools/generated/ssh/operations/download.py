from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SshCredentials(BaseModel):
    """Credentials for ssh authentication."""
    ssh_password: Optional[Dict[str, Any]] = Field(None, description="sshPassword")
    ssh_private_key: Optional[Dict[str, Any]] = Field(None, description="sshPrivateKey")

class SshDownloadToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SshCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    binary_property_name: Optional[str] = Field(None, description="Object property name which holds binary data")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="Authentication")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The file path of the file to download. Has to contain the full path including file name.")


class SshDownloadTool(BaseTool):
    name = "ssh_download"
    description = "Tool for ssh download operation - download operation"
    
    def __init__(self, credentials: Optional[SshCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the ssh download operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running ssh download operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running ssh download operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the ssh download operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
