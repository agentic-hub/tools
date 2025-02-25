from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EgoiCredentials(BaseModel):
    """Credentials for egoi authentication."""
    egoi_api: Optional[Dict[str, Any]] = Field(None, description="egoiApi")

class EgoiUpdateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[EgoiCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    list: Optional[str] = Field(None, description="ID of list to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resolve_data: Optional[bool] = Field(None, description="By default the response just includes the contact ID. If this option gets activated, it will resolve the data automatically.")
    resource: Optional[str] = Field(None, description="Resource")
    email: Optional[str] = Field(None, description="Email address for a subscriber")
    contact_id: Optional[str] = Field(None, description="Contact ID of the subscriber")
    operation: Optional[str] = Field(None, description="Operation")


class EgoiUpdateTool(BaseTool):
    name = "egoi_update"
    description = "Tool for egoi update operation - update operation"
    
    def __init__(self, credentials: Optional[EgoiCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the egoi update operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running egoi update operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running egoi update operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the egoi update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
