# uproc toolkit
from langchain.tools import BaseTool
from typing import List

def get_uproc_tools() -> List[BaseTool]:
    """Get all uproc tools."""
    from . import operations
    return operations.get_tools()
