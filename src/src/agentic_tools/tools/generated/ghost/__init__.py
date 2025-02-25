# ghost toolkit
from langchain.tools import BaseTool
from typing import List

def get_ghost_tools() -> List[BaseTool]:
    """Get all ghost tools."""
    from . import operations
    return operations.get_tools()
