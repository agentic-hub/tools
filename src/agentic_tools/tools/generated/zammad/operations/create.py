from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ZammadCredentials(BaseModel):
    """Credentials for zammad authentication."""
    zammad_basic_auth_api: Optional[Dict[str, Any]] = Field(None, description="zammadBasicAuthApi")
    zammad_token_auth_api: Optional[Dict[str, Any]] = Field(None, description="zammadTokenAuthApi")

class ZammadCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ZammadCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    article: Optional[Dict[str, Any]] = Field(None, description="Article")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="Group to update. Specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    customer: Optional[str] = Field(None, description="Email address of the customer concerned in the ticket to create. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    lastname: Optional[str] = Field(None, description="Last Name")
    name: Optional[str] = Field(None, description="Group Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    group: Optional[str] = Field(None, description="Group that will own the ticket to create. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    firstname: Optional[str] = Field(None, description="First Name")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    title: Optional[str] = Field(None, description="Title of the ticket to create")


class ZammadCreateTool(BaseTool):
    name = "zammad_create"
    description = "Tool for zammad create operation - create operation"
    
    def __init__(self, credentials: Optional[ZammadCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the zammad create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running zammad create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running zammad create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the zammad create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
