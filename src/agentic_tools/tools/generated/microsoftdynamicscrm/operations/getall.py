from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MicrosoftdynamicscrmCredentials(BaseModel):
    """Credentials for microsoftDynamicsCrm authentication."""
    microsoft_dynamics_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="microsoftDynamicsOAuth2Api")

class MicrosoftdynamicscrmGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MicrosoftdynamicscrmCredentials] = Field(None, description="Custom credentials for authentication")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class MicrosoftdynamicscrmGetallTool(BaseTool):
    name = "microsoftdynamicscrm_getall"
    description = "Tool for microsoftDynamicsCrm getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[MicrosoftdynamicscrmCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the microsoftDynamicsCrm getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running microsoftDynamicsCrm getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running microsoftDynamicsCrm getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the microsoftDynamicsCrm getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
