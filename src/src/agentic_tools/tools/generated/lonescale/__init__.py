# loneScale toolkit
from langchain.tools import BaseTool
from typing import List

def get_lonescale_tools() -> List[BaseTool]:
    """Get all loneScale tools."""
    from . import operations
    return operations.get_tools()
