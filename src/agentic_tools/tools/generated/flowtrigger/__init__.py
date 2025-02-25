# flowTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_flowtrigger_tools() -> List[BaseTool]:
    """Get all flowTrigger tools."""
    from . import operations
    return operations.get_tools()
