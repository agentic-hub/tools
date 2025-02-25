from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TodoistCredentials(BaseModel):
    """Credentials for todoist authentication."""
    todoist_api: Optional[Dict[str, Any]] = Field(None, description="todoistApi")
    todoist_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="todoistOAuth2Api")

class TodoistCloseToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[TodoistCredentials] = Field(None, description="Custom credentials for authentication")
    task_id: Optional[str] = Field(None, description="Task ID")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    labels: Optional[str] = Field(None, description="labels")
    operation: Optional[str] = Field(None, description="Operation")


class TodoistCloseTool(BaseTool):
    name = "todoist_close"
    description = "Tool for todoist close operation - close operation"
    
    def __init__(self, credentials: Optional[TodoistCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the todoist close operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running todoist close operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running todoist close operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the todoist close operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
