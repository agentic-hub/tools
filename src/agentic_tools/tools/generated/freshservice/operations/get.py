from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FreshserviceCredentials(BaseModel):
    """Credentials for freshservice authentication."""
    freshservice_api: Optional[Dict[str, Any]] = Field(None, description="freshserviceApi")

class FreshserviceGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[FreshserviceCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    release_id: Optional[str] = Field(None, description="ID of the release to retrieve")
    software_id: Optional[str] = Field(None, description="ID of the software application to retrieve")
    location_id: Optional[str] = Field(None, description="ID of the location to retrieve")
    announcement_id: Optional[str] = Field(None, description="ID of the announcement to retrieve")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email")
    agent_group_id: Optional[str] = Field(None, description="ID of the agent group to retrieve")
    subject: Optional[str] = Field(None, description="Subject")
    ticket_id: Optional[str] = Field(None, description="ID of the ticket to retrieve")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    agent_role_id: Optional[str] = Field(None, description="ID of the agent role to retrieve")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    asset_type_id: Optional[str] = Field(None, description="ID of the asset type to retrieve")
    agent_id: Optional[str] = Field(None, description="ID of the agent to retrieve")
    requester_id: Optional[str] = Field(None, description="ID of the requester to retrieve")
    change_id: Optional[str] = Field(None, description="ID of the change to retrieve")
    problem_id: Optional[str] = Field(None, description="ID of the problem to retrieve")
    department_id: Optional[str] = Field(None, description="ID of the department to retrieve")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    planned_end_date: Optional[str] = Field(None, description="Planned End Date")
    first_name: Optional[str] = Field(None, description="First Name")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    status: Optional[str] = Field(None, description="Status")
    priority: Optional[str] = Field(None, description="Priority")
    planned_start_date: Optional[str] = Field(None, description="Planned Start Date")
    requester_group_id: Optional[str] = Field(None, description="ID of the requester group to retrieve")
    product_id: Optional[str] = Field(None, description="ID of the product to retrieve")


class FreshserviceGetTool(BaseTool):
    name = "freshservice_get"
    description = "Tool for freshservice get operation - get operation"
    
    def __init__(self, credentials: Optional[FreshserviceCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the freshservice get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running freshservice get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running freshservice get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the freshservice get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
