from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AutopilotCredentials(BaseModel):
    """Credentials for autopilot authentication."""
    autopilot_api: Optional[Dict[str, Any]] = Field(None, description="autopilotApi")

class AutopilotUpsertToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AutopilotCredentials] = Field(None, description="Custom credentials for authentication")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    email: Optional[str] = Field(None, description="Email address of the contact")
    contact_id: Optional[str] = Field(None, description="Can be ID or email")
    operation: Optional[str] = Field(None, description="Operation")


class AutopilotUpsertTool(BaseTool):
    name = "autopilot_upsert"
    description = "Tool for autopilot upsert operation - upsert operation"
    
    def __init__(self, credentials: Optional[AutopilotCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the autopilot upsert operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running autopilot upsert operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running autopilot upsert operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the autopilot upsert operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
