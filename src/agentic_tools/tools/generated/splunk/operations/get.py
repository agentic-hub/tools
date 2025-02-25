from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SplunkCredentials(BaseModel):
    """Credentials for splunk authentication."""
    splunk_api: Optional[Dict[str, Any]] = Field(None, description="splunkApi")

class SplunkGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SplunkCredentials] = Field(None, description="Custom credentials for authentication")
    search_configuration_id: Optional[str] = Field(None, description="ID of the search configuration to retrieve")
    user_id: Optional[str] = Field(None, description="ID of the user to retrieve")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    search_job_id: Optional[str] = Field(None, description="ID of the search job to retrieve")
    roles: Optional[str] = Field(None, description="roles")
    operation: Optional[str] = Field(None, description="Operation")


class SplunkGetTool(BaseTool):
    name = "splunk_get"
    description = "Tool for splunk get operation - get operation"
    
    def __init__(self, credentials: Optional[SplunkCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the splunk get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running splunk get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running splunk get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the splunk get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
