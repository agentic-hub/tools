from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RundeckCredentials(BaseModel):
    """Credentials for rundeck authentication."""
    rundeck_api: Optional[Dict[str, Any]] = Field(None, description="rundeckApi")

class RundeckGetmetadataToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[RundeckCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    jobid: Optional[str] = Field(None, description="The job ID to get metadata off")
    operation: Optional[str] = Field(None, description="Operation")


class RundeckGetmetadataTool(BaseTool):
    name = "rundeck_getmetadata"
    description = "Tool for rundeck getMetadata operation - getMetadata operation"
    
    def __init__(self, credentials: Optional[RundeckCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the rundeck getMetadata operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running rundeck getMetadata operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running rundeck getMetadata operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the rundeck getMetadata operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
