from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AutopilotCredentials(BaseModel):
    """Credentials for autopilot authentication."""
    autopilot_api: Optional[Dict[str, Any]] = Field(None, description="autopilotApi")

class AutopilotGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AutopilotCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[str] = Field(None, description="ID of the list to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    contact_id: Optional[str] = Field(None, description="Can be ID or email")
    operation: Optional[str] = Field(None, description="Operation")


class AutopilotGetallTool(BaseTool):
    name = "autopilot_getall"
    description = "Tool for autopilot getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[AutopilotCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the autopilot getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running autopilot getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running autopilot getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the autopilot getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
