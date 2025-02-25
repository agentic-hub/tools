# togglTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_toggltrigger_tools() -> List[BaseTool]:
    """Get all togglTrigger tools."""
    from . import operations
    return operations.get_tools()
