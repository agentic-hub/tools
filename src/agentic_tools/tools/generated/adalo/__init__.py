# adalo toolkit
from langchain.tools import BaseTool
from typing import List

def get_adalo_tools() -> List[BaseTool]:
    """Get all adalo tools."""
    from . import operations
    return operations.get_tools()
