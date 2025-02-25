from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AutopilotCredentials(BaseModel):
    """Credentials for autopilot authentication."""
    autopilot_api: Optional[Dict[str, Any]] = Field(None, description="autopilotApi")

class AutopilotGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AutopilotCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    contact_id: Optional[str] = Field(None, description="Can be ID or email")
    operation: Optional[str] = Field(None, description="Operation")


class AutopilotGetTool(BaseTool):
    name = "autopilot_get"
    description = "Tool for autopilot get operation - get operation"
    
    def __init__(self, credentials: Optional[AutopilotCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the autopilot get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running autopilot get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running autopilot get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the autopilot get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
