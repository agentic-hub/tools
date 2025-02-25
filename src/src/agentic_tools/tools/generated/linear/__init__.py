# linear toolkit
from langchain.tools import BaseTool
from typing import List

def get_linear_tools() -> List[BaseTool]:
    """Get all linear tools."""
    from . import operations
    return operations.get_tools()
