from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FreshserviceCredentials(BaseModel):
    """Credentials for freshservice authentication."""
    freshservice_api: Optional[Dict[str, Any]] = Field(None, description="freshserviceApi")

class FreshserviceDeleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[FreshserviceCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    release_id: Optional[str] = Field(None, description="ID of the release to delete")
    software_id: Optional[str] = Field(None, description="ID of the software application to delete")
    location_id: Optional[str] = Field(None, description="ID of the location to delete")
    announcement_id: Optional[str] = Field(None, description="ID of the announcement to delete")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email")
    agent_group_id: Optional[str] = Field(None, description="ID of the agent group to delete")
    subject: Optional[str] = Field(None, description="Subject")
    ticket_id: Optional[str] = Field(None, description="ID of the ticket to delete")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    asset_type_id: Optional[str] = Field(None, description="ID of the asset type to delete")
    agent_id: Optional[str] = Field(None, description="ID of the agent to delete")
    requester_id: Optional[str] = Field(None, description="ID of the requester to delete")
    change_id: Optional[str] = Field(None, description="ID of the change to delete")
    problem_id: Optional[str] = Field(None, description="ID of the problem to delete")
    department_id: Optional[str] = Field(None, description="ID of the department to delete")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    planned_end_date: Optional[str] = Field(None, description="Planned End Date")
    first_name: Optional[str] = Field(None, description="First Name")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    status: Optional[str] = Field(None, description="Status")
    priority: Optional[str] = Field(None, description="Priority")
    planned_start_date: Optional[str] = Field(None, description="Planned Start Date")
    requester_group_id: Optional[str] = Field(None, description="ID of the requester group to delete")
    product_id: Optional[str] = Field(None, description="ID of the product to delete")


class FreshserviceDeleteTool(BaseTool):
    name = "freshservice_delete"
    description = "Tool for freshservice delete operation - delete operation"
    
    def __init__(self, credentials: Optional[FreshserviceCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the freshservice delete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running freshservice delete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running freshservice delete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the freshservice delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
