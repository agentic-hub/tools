from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DemioCredentials(BaseModel):
    """Credentials for demio authentication."""
    demio_api: Optional[Dict[str, Any]] = Field(None, description="demioApi")

class DemioRegisterToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[DemioCredentials] = Field(None, description="Custom credentials for authentication")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    event_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    first_name: Optional[str] = Field(None, description="The registrant's first name")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    email: Optional[str] = Field(None, description="The registrant's email address")
    operation: Optional[str] = Field(None, description="Operation")


class DemioRegisterTool(BaseTool):
    name = "demio_register"
    description = "Tool for demio register operation - register operation"
    
    def __init__(self, credentials: Optional[DemioCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the demio register operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running demio register operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running demio register operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the demio register operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
