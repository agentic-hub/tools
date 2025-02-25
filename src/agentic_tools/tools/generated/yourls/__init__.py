# yourls toolkit
from langchain.tools import BaseTool
from typing import List

def get_yourls_tools() -> List[BaseTool]:
    """Get all yourls tools."""
    from . import operations
    return operations.get_tools()
