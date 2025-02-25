# mailcheck toolkit
from langchain.tools import BaseTool
from typing import List

def get_mailcheck_tools() -> List[BaseTool]:
    """Get all mailcheck tools."""
    from . import operations
    return operations.get_tools()
