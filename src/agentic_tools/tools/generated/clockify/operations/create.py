from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ClockifyCredentials(BaseModel):
    """Credentials for clockify authentication."""
    clockify_api: Optional[Dict[str, Any]] = Field(None, description="clockifyApi")

class ClockifyCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ClockifyCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    task_id: Optional[str] = Field(None, description="ID of task to delete")
    name: Optional[str] = Field(None, description="Name of client being created")
    start: Optional[str] = Field(None, description="Start")
    client_id: Optional[str] = Field(None, description="Client ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    tag_id: Optional[str] = Field(None, description="Tag ID")
    project_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    workspace_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")
    time_entry_id: Optional[str] = Field(None, description="Time Entry ID")


class ClockifyCreateTool(BaseTool):
    name = "clockify_create"
    description = "Tool for clockify create operation - create operation"
    
    def __init__(self, credentials: Optional[ClockifyCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the clockify create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running clockify create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running clockify create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the clockify create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
