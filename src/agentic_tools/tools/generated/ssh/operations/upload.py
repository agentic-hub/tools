from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SshCredentials(BaseModel):
    """Credentials for ssh authentication."""
    ssh_password: Optional[Dict[str, Any]] = Field(None, description="sshPassword")
    ssh_private_key: Optional[Dict[str, Any]] = Field(None, description="sshPrivateKey")

class SshUploadToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SshCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="Authentication")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The directory to upload the file to. The name of the file does not need to be specified, it's taken from the binary data file name. To override this behavior, set the parameter \"File Name\" under options.")


class SshUploadTool(BaseTool):
    name = "ssh_upload"
    description = "Tool for ssh upload operation - upload operation"
    
    def __init__(self, credentials: Optional[SshCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the ssh upload operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running ssh upload operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running ssh upload operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the ssh upload operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
