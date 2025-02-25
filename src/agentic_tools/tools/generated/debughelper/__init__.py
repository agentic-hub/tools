# debugHelper toolkit
from langchain.tools import BaseTool
from typing import List

def get_debughelper_tools() -> List[BaseTool]:
    """Get all debugHelper tools."""
    from . import operations
    return operations.get_tools()
