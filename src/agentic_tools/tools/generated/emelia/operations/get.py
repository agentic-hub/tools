from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EmeliaCredentials(BaseModel):
    """Credentials for emelia authentication."""
    emelia_api: Optional[Dict[str, Any]] = Field(None, description="emeliaApi")

class EmeliaGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[EmeliaCredentials] = Field(None, description="Custom credentials for authentication")
    contact_email: Optional[str] = Field(None, description="The email of the contact to add to the campaign")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    campaign_id: Optional[str] = Field(None, description="The ID of the campaign to retrieve")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    campaign_name: Optional[str] = Field(None, description="The name of the campaign to create")
    operation: Optional[str] = Field(None, description="Operation")


class EmeliaGetTool(BaseTool):
    name = "emelia_get"
    description = "Tool for emelia get operation - get operation"
    
    def __init__(self, credentials: Optional[EmeliaCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the emelia get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running emelia get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running emelia get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the emelia get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
