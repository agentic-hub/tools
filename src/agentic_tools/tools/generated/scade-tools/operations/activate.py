from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Scade-toolsCredentials(BaseModel):
    """Credentials for scade-tools authentication."""
    n8n_api: Optional[Dict[str, Any]] = Field(None, description="n8nApi")

class Scade-toolsActivateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[Scade-toolsCredentials] = Field(None, description="Custom credentials for authentication")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    workflow_id: Optional[Dict[str, Any]] = Field(None, description="Workflow to filter the executions by")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    workflow_object: Optional[str] = Field(None, description="A valid JSON object with required fields: 'name', 'nodes', 'connections' and 'settings'. More information can be found in the <a href=\"https://docs.n8n.io/api/api-reference/#tag/Workflow/paths/~1workflows/post\">documentation</a>.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    credential_type_name: Optional[str] = Field(None, description="The available types depend on nodes installed on the n8n instance. Some built-in types include e.g. 'githubApi', 'notionApi', and 'slackApi'.")
    execution_id: Optional[str] = Field(None, description="Execution ID")
    additional_options: Optional[Dict[str, Any]] = Field(None, description="Additional Options")
    operation: Optional[str] = Field(None, description="Operation")


class Scade-toolsActivateTool(BaseTool):
    name = "scade-tools_activate"
    description = "Tool for scade-tools activate operation - activate operation"
    
    def __init__(self, credentials: Optional[Scade-toolsCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the scade-tools activate operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running scade-tools activate operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running scade-tools activate operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the scade-tools activate operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
