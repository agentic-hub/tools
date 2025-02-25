from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DropcontactCredentials(BaseModel):
    """Credentials for dropcontact authentication."""
    dropcontact_api: Optional[Dict[str, Any]] = Field(None, description="dropcontactApi")

class DropcontactEnrichToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[DropcontactCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    simplify: Optional[bool] = Field(None, description="When off, waits for the contact data before completing. Waiting time can be adjusted with Extend Wait Time option. When on, returns a request_id that can be used later in the Fetch Request operation.")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    email: Optional[str] = Field(None, description="Email")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class DropcontactEnrichTool(BaseTool):
    name = "dropcontact_enrich"
    description = "Tool for dropcontact enrich operation - enrich operation"
    
    def __init__(self, credentials: Optional[DropcontactCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the dropcontact enrich operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running dropcontact enrich operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running dropcontact enrich operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the dropcontact enrich operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
