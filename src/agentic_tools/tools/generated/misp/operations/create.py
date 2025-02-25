from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MispCredentials(BaseModel):
    """Credentials for misp authentication."""
    misp_api: Optional[Dict[str, Any]] = Field(None, description="mispApi")

class MispCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MispCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    information: Optional[str] = Field(None, description="Information on the event - max 65535 characters")
    type: Optional[str] = Field(None, description="Type")
    org_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    feed_id: Optional[str] = Field(None, description="UUID or numeric ID of the feed")
    user_id: Optional[str] = Field(None, description="Numeric ID of the user")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    role_id: Optional[str] = Field(None, description="Role IDs are available in the MISP dashboard at /roles/index")
    value: Optional[str] = Field(None, description="Value")
    email: Optional[str] = Field(None, description="Email")
    organisation_id: Optional[str] = Field(None, description="UUID or numeric ID of the organisation")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    tag_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    attribute_id: Optional[str] = Field(None, description="UUID or numeric ID of the attribute")
    url: Optional[str] = Field(None, description="URL")
    galaxy_id: Optional[str] = Field(None, description="UUID or numeric ID of the galaxy")
    event_id: Optional[str] = Field(None, description="UUID of the event to attach the attribute to")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    provider: Optional[str] = Field(None, description="Provider")


class MispCreateTool(BaseTool):
    name = "misp_create"
    description = "Tool for misp create operation - create operation"
    
    def __init__(self, credentials: Optional[MispCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the misp create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running misp create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running misp create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the misp create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
