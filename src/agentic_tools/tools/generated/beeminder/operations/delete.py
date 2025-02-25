from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class BeeminderCredentials(BaseModel):
    """Credentials for beeminder authentication."""
    beeminder_api: Optional[Dict[str, Any]] = Field(None, description="beeminderApi")

class BeeminderDeleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[BeeminderCredentials] = Field(None, description="Custom credentials for authentication")
    goal_name: Optional[str] = Field(None, description="The name of the goal. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    datapoint_id: Optional[str] = Field(None, description="Datapoint ID")
    operation: Optional[str] = Field(None, description="Operation")


class BeeminderDeleteTool(BaseTool):
    name = "beeminder_delete"
    description = "Tool for beeminder delete operation - delete operation"
    
    def __init__(self, credentials: Optional[BeeminderCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the beeminder delete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running beeminder delete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running beeminder delete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the beeminder delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
