# workableTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_workabletrigger_tools() -> List[BaseTool]:
    """Get all workableTrigger tools."""
    from . import operations
    return operations.get_tools()
