from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class LdapCredentials(BaseModel):
    """Credentials for ldap authentication."""
    ldap: Optional[Dict[str, Any]] = Field(None, description="ldap")

class LdapSearchToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[LdapCredentials] = Field(None, description="Custom credentials for authentication")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    base_dn: Optional[str] = Field(None, description="The distinguished name of the subtree to search in")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    attributes: Optional[Dict[str, Any]] = Field(None, description="Attributes to add to the entry")
    attribute: Optional[str] = Field(None, description="Attribute to search for")
    search_text: Optional[str] = Field(None, description="Text to search for, Use * for a wildcard")
    search_for: Optional[str] = Field(None, description="Directory object class to search for")
    dn: Optional[str] = Field(None, description="The distinguished name of the entry to compare")
    node_debug: Optional[bool] = Field(None, description="Debug")
    operation: Optional[str] = Field(None, description="Operation")
    custom_filter: Optional[str] = Field(None, description="Custom LDAP filter. Escape these chars * ( ) \ with a backslash \"\\".")


class LdapSearchTool(BaseTool):
    name = "ldap_search"
    description = "Tool for ldap search operation - search operation"
    
    def __init__(self, credentials: Optional[LdapCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the ldap search operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running ldap search operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running ldap search operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the ldap search operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
