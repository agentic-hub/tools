from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TodoistCredentials(BaseModel):
    """Credentials for todoist authentication."""
    todoist_api: Optional[Dict[str, Any]] = Field(None, description="todoistApi")
    todoist_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="todoistOAuth2Api")

class TodoistCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[TodoistCredentials] = Field(None, description="Custom credentials for authentication")
    content: Optional[str] = Field(None, description="Task content")
    resource: Optional[str] = Field(None, description="Resource")
    project: Optional[str] = Field(None, description="ID")
    authentication: Optional[str] = Field(None, description="Authentication")
    options: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    labels: Optional[str] = Field(None, description="labels")
    operation: Optional[str] = Field(None, description="Operation")


class TodoistCreateTool(BaseTool):
    name = "todoist_create"
    description = "Tool for todoist create operation - create operation"
    
    def __init__(self, credentials: Optional[TodoistCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the todoist create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running todoist create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running todoist create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the todoist create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
