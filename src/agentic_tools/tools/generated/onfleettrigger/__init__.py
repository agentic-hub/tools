# onfleetTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_onfleettrigger_tools() -> List[BaseTool]:
    """Get all onfleetTrigger tools."""
    from . import operations
    return operations.get_tools()
