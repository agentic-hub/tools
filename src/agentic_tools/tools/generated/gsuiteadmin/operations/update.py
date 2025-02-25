from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GsuiteadminCredentials(BaseModel):
    """Credentials for gSuiteAdmin authentication."""
    g_suite_admin_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="gSuiteAdminOAuth2Api")

class GsuiteadminUpdateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GsuiteadminCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    user_id: Optional[str] = Field(None, description="The value can be the user's primary email address, alias email address, or unique user ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    group_id: Optional[str] = Field(None, description="Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.")
    projection: Optional[str] = Field(None, description="What subset of fields to fetch for this user")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")


class GsuiteadminUpdateTool(BaseTool):
    name = "gsuiteadmin_update"
    description = "Tool for gSuiteAdmin update operation - update operation"
    
    def __init__(self, credentials: Optional[GsuiteadminCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the gSuiteAdmin update operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running gSuiteAdmin update operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running gSuiteAdmin update operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the gSuiteAdmin update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
