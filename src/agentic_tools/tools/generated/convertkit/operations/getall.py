from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ConvertkitCredentials(BaseModel):
    """Credentials for convertKit authentication."""
    convert_kit_api: Optional[Dict[str, Any]] = Field(None, description="convertKitApi")

class ConvertkitGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ConvertkitCredentials] = Field(None, description="Custom credentials for authentication")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Receive only active subscribers or cancelled subscribers")
    tag_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    email: Optional[str] = Field(None, description="The subscriber's email address")
    id: Optional[str] = Field(None, description="The ID of your custom field")
    operation: Optional[str] = Field(None, description="Operation")


class ConvertkitGetallTool(BaseTool):
    name = "convertkit_getall"
    description = "Tool for convertKit getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[ConvertkitCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the convertKit getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running convertKit getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running convertKit getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the convertKit getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
