# ldap toolkit
from langchain.tools import BaseTool
from typing import List

def get_ldap_tools() -> List[BaseTool]:
    """Get all ldap tools."""
    from . import operations
    return operations.get_tools()
