# uplead toolkit
from langchain.tools import BaseTool
from typing import List

def get_uplead_tools() -> List[BaseTool]:
    """Get all uplead tools."""
    from . import operations
    return operations.get_tools()
