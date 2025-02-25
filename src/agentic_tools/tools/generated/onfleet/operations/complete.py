from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OnfleetCredentials(BaseModel):
    """Credentials for onfleet authentication."""
    onfleet_api: Optional[Dict[str, Any]] = Field(None, description="onfleetApi")

class OnfleetCompleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[OnfleetCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    teams: Optional[str] = Field(None, description="teams")
    workers: Optional[str] = Field(None, description="workers")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    success: Optional[bool] = Field(None, description="Whether the task's completion was successful")
    id: Optional[str] = Field(None, description="The ID of the admin object for lookup")
    phone: Optional[str] = Field(None, description="The phone of the recipient for lookup")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The administrator's name")
    managers: Optional[str] = Field(None, description="managers")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    destination: Optional[Dict[str, Any]] = Field(None, description="Destination")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="The resource to perform operations on")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class OnfleetCompleteTool(BaseTool):
    name = "onfleet_complete"
    description = "Tool for onfleet complete operation - complete operation"
    
    def __init__(self, credentials: Optional[OnfleetCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the onfleet complete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running onfleet complete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running onfleet complete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the onfleet complete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
