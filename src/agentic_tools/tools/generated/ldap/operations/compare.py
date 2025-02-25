from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class LdapCredentials(BaseModel):
    """Credentials for ldap authentication."""
    ldap: Optional[Dict[str, Any]] = Field(None, description="ldap")

class LdapCompareToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[LdapCredentials] = Field(None, description="Custom credentials for authentication")
    value: Optional[str] = Field(None, description="The value to compare")
    attributes: Optional[Dict[str, Any]] = Field(None, description="Attributes to add to the entry")
    id: Optional[str] = Field(None, description="The ID of the attribute to compare")
    dn: Optional[str] = Field(None, description="The distinguished name of the entry to compare")
    node_debug: Optional[bool] = Field(None, description="Debug")
    operation: Optional[str] = Field(None, description="Operation")


class LdapCompareTool(BaseTool):
    name = "ldap_compare"
    description = "Tool for ldap compare operation - compare operation"
    
    def __init__(self, credentials: Optional[LdapCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the ldap compare operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running ldap compare operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running ldap compare operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the ldap compare operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
