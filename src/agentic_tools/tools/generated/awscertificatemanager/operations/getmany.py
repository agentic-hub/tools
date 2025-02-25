from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwscertificatemanagerCredentials(BaseModel):
    """Credentials for awsCertificateManager authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwscertificatemanagerGetmanyToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AwscertificatemanagerCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class AwscertificatemanagerGetmanyTool(BaseTool):
    name = "awscertificatemanager_getmany"
    description = "Tool for awsCertificateManager getMany operation - getMany operation"
    
    def __init__(self, credentials: Optional[AwscertificatemanagerCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the awsCertificateManager getMany operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running awsCertificateManager getMany operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running awsCertificateManager getMany operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsCertificateManager getMany operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
