from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class LinearCredentials(BaseModel):
    """Credentials for linear authentication."""
    linear_api: Optional[Dict[str, Any]] = Field(None, description="linearApi")
    linear_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="linearOAuth2Api")

class LinearCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[LinearCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    team_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    authentication: Optional[str] = Field(None, description="Authentication")
    title: Optional[str] = Field(None, description="Title")
    issue_id: Optional[str] = Field(None, description="Issue ID")
    operation: Optional[str] = Field(None, description="Operation")


class LinearCreateTool(BaseTool):
    name = "linear_create"
    description = "Tool for linear create operation - create operation"
    
    def __init__(self, credentials: Optional[LinearCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the linear create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running linear create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running linear create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the linear create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
