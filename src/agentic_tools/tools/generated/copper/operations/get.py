from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CopperCredentials(BaseModel):
    """Credentials for copper authentication."""
    copper_api: Optional[Dict[str, Any]] = Field(None, description="copperApi")

class CopperGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[CopperCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    task_id: Optional[str] = Field(None, description="ID of the task to retrieve")
    opportunity_id: Optional[str] = Field(None, description="ID of the opportunity to retrieve")
    name: Optional[str] = Field(None, description="Name of the company to create")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    project_id: Optional[str] = Field(None, description="ID of the project to retrieve")
    person_id: Optional[str] = Field(None, description="ID of the person to retrieve")
    lead_id: Optional[str] = Field(None, description="ID of the lead to retrieve")
    company_id: Optional[str] = Field(None, description="ID of the company to retrieve")
    operation: Optional[str] = Field(None, description="Operation")
    filter_fields: Optional[Dict[str, Any]] = Field(None, description="Filters")


class CopperGetTool(BaseTool):
    name = "copper_get"
    description = "Tool for copper get operation - get operation"
    
    def __init__(self, credentials: Optional[CopperCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the copper get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running copper get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running copper get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the copper get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
