from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MicrosoftgraphsecurityCredentials(BaseModel):
    """Credentials for microsoftGraphSecurity authentication."""
    microsoft_graph_security_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="microsoftGraphSecurityOAuth2Api")

class MicrosoftgraphsecurityUpdateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MicrosoftgraphsecurityCredentials] = Field(None, description="Custom credentials for authentication")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    secure_score_control_profile_id: Optional[str] = Field(None, description="ID of the secure score control profile to update")
    provider: Optional[str] = Field(None, description="Name of the provider of the security product or service")
    vendor: Optional[str] = Field(None, description="Name of the vendor of the security product or service")
    operation: Optional[str] = Field(None, description="Operation")


class MicrosoftgraphsecurityUpdateTool(BaseTool):
    name = "microsoftgraphsecurity_update"
    description = "Tool for microsoftGraphSecurity update operation - update operation"
    
    def __init__(self, credentials: Optional[MicrosoftgraphsecurityCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the microsoftGraphSecurity update operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running microsoftGraphSecurity update operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running microsoftGraphSecurity update operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the microsoftGraphSecurity update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
