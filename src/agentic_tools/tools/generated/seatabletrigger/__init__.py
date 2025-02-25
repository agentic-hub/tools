# seaTableTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_seatabletrigger_tools() -> List[BaseTool]:
    """Get all seaTableTrigger tools."""
    from . import operations
    return operations.get_tools()
