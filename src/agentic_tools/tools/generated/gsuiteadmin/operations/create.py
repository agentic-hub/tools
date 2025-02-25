from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GsuiteadminCredentials(BaseModel):
    """Credentials for gSuiteAdmin authentication."""
    g_suite_admin_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="gSuiteAdminOAuth2Api")

class GsuiteadminCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GsuiteadminCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    make_admin: Optional[bool] = Field(None, description="Whether to make a user a super administrator")
    user_id: Optional[str] = Field(None, description="The value can be the user's primary email address, alias email address, or unique user ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    last_name: Optional[str] = Field(None, description="Last Name")
    email: Optional[str] = Field(None, description="The group's email address. If your account has multiple domains, select the appropriate domain for the email address. The email must be unique")
    password: Optional[str] = Field(None, description="Stores the password for the user account. A minimum of 8 characters is required. The maximum length is 100 characters.")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    username: Optional[str] = Field(None, description="The username that will be set to the user. Example: If you domain is example.com and you set the username to jhon then the user's final email address will be jhon@example.com.")
    group_id: Optional[str] = Field(None, description="Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID.")
    domain: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    projection: Optional[str] = Field(None, description="What subset of fields to fetch for this user")
    first_name: Optional[str] = Field(None, description="First Name")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")


class GsuiteadminCreateTool(BaseTool):
    name = "gsuiteadmin_create"
    description = "Tool for gSuiteAdmin create operation - create operation"
    
    def __init__(self, credentials: Optional[GsuiteadminCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the gSuiteAdmin create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running gSuiteAdmin create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running gSuiteAdmin create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the gSuiteAdmin create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
