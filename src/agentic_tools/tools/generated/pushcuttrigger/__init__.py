# pushcutTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_pushcuttrigger_tools() -> List[BaseTool]:
    """Get all pushcutTrigger tools."""
    from . import operations
    return operations.get_tools()
