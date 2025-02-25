from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TaigaCredentials(BaseModel):
    """Credentials for taiga authentication."""
    taiga_api: Optional[Dict[str, Any]] = Field(None, description="taigaApi")

class TaigaGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[TaigaCredentials] = Field(None, description="Custom credentials for authentication")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    task_id: Optional[str] = Field(None, description="ID of the task to delete")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    project_id: Optional[str] = Field(None, description="ID of the project to which the epic belongs. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    subject: Optional[str] = Field(None, description="Subject")
    issue_id: Optional[str] = Field(None, description="ID of the issue to delete")
    operation: Optional[str] = Field(None, description="Operation")
    user_story_id: Optional[str] = Field(None, description="ID of the user story to delete")
    epic_id: Optional[str] = Field(None, description="ID of the epic to delete")


class TaigaGetallTool(BaseTool):
    name = "taiga_getall"
    description = "Tool for taiga getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[TaigaCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the taiga getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running taiga getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running taiga getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the taiga getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
