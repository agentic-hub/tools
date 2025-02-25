from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class LdapCredentials(BaseModel):
    """Credentials for ldap authentication."""
    ldap: Optional[Dict[str, Any]] = Field(None, description="ldap")

class LdapCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[LdapCredentials] = Field(None, description="Custom credentials for authentication")
    attributes: Optional[Dict[str, Any]] = Field(None, description="Attributes to add to the entry")
    dn: Optional[str] = Field(None, description="The distinguished name of the entry to create")
    node_debug: Optional[bool] = Field(None, description="Debug")
    operation: Optional[str] = Field(None, description="Operation")


class LdapCreateTool(BaseTool):
    name = "ldap_create"
    description = "Tool for ldap create operation - create operation"
    
    def __init__(self, credentials: Optional[LdapCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the ldap create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running ldap create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running ldap create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the ldap create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
