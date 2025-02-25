from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ZendeskCredentials(BaseModel):
    """Credentials for zendesk authentication."""
    zendesk_api: Optional[Dict[str, Any]] = Field(None, description="zendeskApi")
    zendesk_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="zendeskOAuth2Api")

class ZendeskUpdateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ZendeskCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="Ticket ID")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The user's name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    update_fields_json: Optional[str] = Field(None, description="Object of values to update as described <a href=\"https://developer.zendesk.com/rest_api/docs/support/tickets\">here</a>")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")


class ZendeskUpdateTool(BaseTool):
    name = "zendesk_update"
    description = "Tool for zendesk update operation - update operation"
    
    def __init__(self, credentials: Optional[ZendeskCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the zendesk update operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running zendesk update operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running zendesk update operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the zendesk update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
