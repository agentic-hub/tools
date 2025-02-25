from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HarvestCredentials(BaseModel):
    """Credentials for harvest authentication."""
    harvest_api: Optional[Dict[str, Any]] = Field(None, description="harvestApi")
    harvest_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="harvestOAuth2Api")

class HarvestCreatebydurationToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[HarvestCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    spent_date: Optional[str] = Field(None, description="The ISO 8601 formatted date the time entry was spent")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="The ID of the client you are retrieving")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    task_id: Optional[str] = Field(None, description="The ID of the task to associate with the time entry")
    name: Optional[str] = Field(None, description="The name of the client")
    client_id: Optional[str] = Field(None, description="The ID of the client associated with this contact")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    first_name: Optional[str] = Field(None, description="The first name of the contact")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    project_id: Optional[str] = Field(None, description="The ID of the project to associate with the time entry")
    authentication: Optional[str] = Field(None, description="Authentication")


class HarvestCreatebydurationTool(BaseTool):
    name = "harvest_createbyduration"
    description = "Tool for harvest createByDuration operation - createByDuration operation"
    
    def __init__(self, credentials: Optional[HarvestCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the harvest createByDuration operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running harvest createByDuration operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running harvest createByDuration operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the harvest createByDuration operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
