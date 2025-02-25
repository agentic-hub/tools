from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FlowCredentials(BaseModel):
    """Credentials for flow authentication."""
    flow_api: Optional[Dict[str, Any]] = Field(None, description="flowApi")

class FlowUpdateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[FlowCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    task_id: Optional[str] = Field(None, description="Task ID")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    workspace_id: Optional[str] = Field(None, description="Create resources under the given workspace")
    operation: Optional[str] = Field(None, description="Operation")


class FlowUpdateTool(BaseTool):
    name = "flow_update"
    description = "Tool for flow update operation - update operation"
    
    def __init__(self, credentials: Optional[FlowCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the flow update operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running flow update operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running flow update operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the flow update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
