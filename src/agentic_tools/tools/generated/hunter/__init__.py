# hunter toolkit
from langchain.tools import BaseTool
from typing import List

def get_hunter_tools() -> List[BaseTool]:
    """Get all hunter tools."""
    from . import operations
    return operations.get_tools()
