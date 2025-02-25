from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GoogletasksCredentials(BaseModel):
    """Credentials for googleTasks authentication."""
    google_tasks_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleTasksOAuth2Api")

class GoogletasksGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GoogletasksCredentials] = Field(None, description="Custom credentials for authentication")
    task_id: Optional[str] = Field(None, description="Task ID")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    task: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class GoogletasksGetTool(BaseTool):
    name = "googletasks_get"
    description = "Tool for googleTasks get operation - get operation"
    
    def __init__(self, credentials: Optional[GoogletasksCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleTasks get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleTasks get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleTasks get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleTasks get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
