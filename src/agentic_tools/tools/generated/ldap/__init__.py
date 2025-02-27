# ldap toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_ldap_tools() -> List[BaseTool]:
    """Get all ldap tools."""
    from . import operations
    return operations.get_tools()

class LdapCredentials(BaseModel):
    """Credentials for ldap authentication."""
    ldap: Optional[Dict[str, Any]] = Field(None, description="ldap")

class LdapToolkit(AgenticHubToolkit):
    """Toolkit for interacting with ldap."""

    def __init__(self, credentials: Optional[LdapCredentials] = None):
        """Initialize the ldap toolkit with optional credentials.

        Args:
            credentials: LdapCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all ldap tools with the configured credentials."""
        from . import operations
        return self.get_tools_from_operations(operations)
        # Apply credentials to each tool if provided
        if self.credentials:
            for tool in tools:
                # Set credentials on each tool instance
                tool.credentials = self.credentials
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all ldap tools with default credentials."""
        return get_ldap_tools()
