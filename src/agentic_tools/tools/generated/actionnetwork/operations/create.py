from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ActionnetworkCredentials(BaseModel):
    """Credentials for actionNetwork authentication."""
    action_network_api: Optional[Dict[str, Any]] = Field(None, description="actionNetworkApi")

class ActionnetworkCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ActionnetworkCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email_addresses: Optional[Dict[str, Any]] = Field(None, description="Person’s email addresses")
    signature_id: Optional[str] = Field(None, description="ID of the signature to retrieve")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of the tag to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    tag_id: Optional[str] = Field(None, description="ID of the tag to retrieve")
    person_id: Optional[str] = Field(None, description="ID of the person to create an attendance for")
    petition_id: Optional[str] = Field(None, description="ID of the petition to sign")
    event_id: Optional[str] = Field(None, description="ID of the event to create an attendance for")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    title: Optional[str] = Field(None, description="Title of the event to create")
    origin_system: Optional[str] = Field(None, description="Source where the event originated")


class ActionnetworkCreateTool(BaseTool):
    name = "actionnetwork_create"
    description = "Tool for actionNetwork create operation - create operation"
    
    def __init__(self, credentials: Optional[ActionnetworkCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the actionNetwork create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running actionNetwork create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running actionNetwork create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the actionNetwork create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
