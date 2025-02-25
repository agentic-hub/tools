from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TravisciCredentials(BaseModel):
    """Credentials for travisCi authentication."""
    travis_ci_api: Optional[Dict[str, Any]] = Field(None, description="travisCiApi")

class TravisciTriggerToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[TravisciCredentials] = Field(None, description="Custom credentials for authentication")
    build_id: Optional[str] = Field(None, description="Value uniquely identifying the build")
    slug: Optional[str] = Field(None, description="Same as {ownerName}/{repositoryName}")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    branch: Optional[str] = Field(None, description="Branch requested to be built")
    operation: Optional[str] = Field(None, description="Operation")


class TravisciTriggerTool(BaseTool):
    name = "travisci_trigger"
    description = "Tool for travisCi trigger operation - trigger operation"
    
    def __init__(self, credentials: Optional[TravisciCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the travisCi trigger operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running travisCi trigger operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running travisCi trigger operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the travisCi trigger operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
