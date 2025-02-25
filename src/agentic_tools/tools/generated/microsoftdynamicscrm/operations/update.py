from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MicrosoftdynamicscrmCredentials(BaseModel):
    """Credentials for microsoftDynamicsCrm authentication."""
    microsoft_dynamics_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="microsoftDynamicsOAuth2Api")

class MicrosoftdynamicscrmUpdateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MicrosoftdynamicscrmCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[str] = Field(None, description="Account ID")


class MicrosoftdynamicscrmUpdateTool(BaseTool):
    name = "microsoftdynamicscrm_update"
    description = "Tool for microsoftDynamicsCrm update operation - update operation"
    
    def __init__(self, credentials: Optional[MicrosoftdynamicscrmCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the microsoftDynamicsCrm update operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running microsoftDynamicsCrm update operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running microsoftDynamicsCrm update operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the microsoftDynamicsCrm update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
