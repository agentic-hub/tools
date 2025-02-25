# googleContacts toolkit
from langchain.tools import BaseTool
from typing import List

def get_googlecontacts_tools() -> List[BaseTool]:
    """Get all googleContacts tools."""
    from . import operations
    return operations.get_tools()
