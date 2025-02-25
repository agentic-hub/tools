from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MauticCredentials(BaseModel):
    """Credentials for mautic authentication."""
    mautic_api: Optional[Dict[str, Any]] = Field(None, description="mauticApi")
    mautic_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="mauticOAuth2Api")

class MauticCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MauticCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    position: Optional[str] = Field(None, description="Position")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    company: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    body_json: Optional[str] = Field(None, description="Contact parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    last_name: Optional[str] = Field(None, description="Last Name")
    email: Optional[str] = Field(None, description="Email address of the contact")
    company_id: Optional[str] = Field(None, description="The ID of the company to update")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The name of the company to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    first_name: Optional[str] = Field(None, description="First Name")
    action: Optional[str] = Field(None, description="Action")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    title: Optional[str] = Field(None, description="Title")


class MauticCreateTool(BaseTool):
    name = "mautic_create"
    description = "Tool for mautic create operation - create operation"
    
    def __init__(self, credentials: Optional[MauticCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the mautic create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running mautic create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running mautic create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mautic create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
