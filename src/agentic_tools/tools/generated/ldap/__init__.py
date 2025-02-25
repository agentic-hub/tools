# ldap toolkit
from langchain.tools import BaseTool
from typing import List

def get_ldap_tools() -> List[BaseTool]:
    """Get all ldap tools."""
    from . import operations
    return operations.get_tools()

class LdapToolkit:
    """Toolkit for interacting with ldap."""

    def __init__(self):
        """Initialize the ldap toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all ldap tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all ldap tools with default credentials."""
        return get_ldap_tools()
