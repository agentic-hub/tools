from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AsanaCredentials(BaseModel):
    """Credentials for asana authentication."""
    asana_api: Optional[Dict[str, Any]] = Field(None, description="asanaApi")
    asana_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="asanaOAuth2Api")

class AsanaCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AsanaCredentials] = Field(None, description="Custom credentials for authentication")
    workspace: Optional[str] = Field(None, description="The workspace to create the task in. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    tag: Optional[str] = Field(None, description="The tag that should be added. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    text: Optional[str] = Field(None, description="The plain text of the comment to add")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="The ID of the task to delete")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[str] = Field(None, description="The task to operate on")
    name: Optional[str] = Field(None, description="The name of the subtask to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    project: Optional[str] = Field(None, description="The project where the task will be added. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Other properties to set")
    authentication: Optional[str] = Field(None, description="Authentication")
    team: Optional[str] = Field(None, description="The team this project will be assigned to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    other_properties: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class AsanaCreateTool(BaseTool):
    name = "asana_create"
    description = "Tool for asana create operation - create operation"
    
    def __init__(self, credentials: Optional[AsanaCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the asana create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running asana create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running asana create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the asana create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
