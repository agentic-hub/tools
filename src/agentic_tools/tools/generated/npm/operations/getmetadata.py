from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class NpmCredentials(BaseModel):
    """Credentials for npm authentication."""
    npm_api: Optional[Dict[str, Any]] = Field(None, description="npmApi")

class NpmGetmetadataToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[NpmCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    package_name: Optional[str] = Field(None, description="Package Name")
    operation: Optional[str] = Field(None, description="Operation")
    package_version: Optional[str] = Field(None, description="Package Version")


class NpmGetmetadataTool(BaseTool):
    name = "npm_getmetadata"
    description = "Tool for npm getMetadata operation - getMetadata operation"
    
    def __init__(self, credentials: Optional[NpmCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the npm getMetadata operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running npm getMetadata operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running npm getMetadata operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the npm getMetadata operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
