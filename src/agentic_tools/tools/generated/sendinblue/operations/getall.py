from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SendinblueCredentials(BaseModel):
    """Credentials for sendInBlue authentication."""
    send_in_blue_api: Optional[Dict[str, Any]] = Field(None, description="sendInBlueApi")

class SendinblueGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SendinblueCredentials] = Field(None, description="Custom credentials for authentication")
    identifier: Optional[str] = Field(None, description="Email (urlencoded) OR ID of the contact OR its SMS attribute value")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email of the sender")
    receipients: Optional[str] = Field(None, description="Receipients")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")


class SendinblueGetallTool(BaseTool):
    name = "sendinblue_getall"
    description = "Tool for sendInBlue getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[SendinblueCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the sendInBlue getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running sendInBlue getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running sendInBlue getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sendInBlue getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
