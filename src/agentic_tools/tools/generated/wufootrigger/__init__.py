# wufooTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_wufootrigger_tools() -> List[BaseTool]:
    """Get all wufooTrigger tools."""
    from . import operations
    return operations.get_tools()
