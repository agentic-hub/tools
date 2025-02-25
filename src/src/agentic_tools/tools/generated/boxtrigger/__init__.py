# boxTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_boxtrigger_tools() -> List[BaseTool]:
    """Get all boxTrigger tools."""
    from . import operations
    return operations.get_tools()
