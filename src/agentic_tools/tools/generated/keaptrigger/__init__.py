# keapTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_keaptrigger_tools() -> List[BaseTool]:
    """Get all keapTrigger tools."""
    from . import operations
    return operations.get_tools()
