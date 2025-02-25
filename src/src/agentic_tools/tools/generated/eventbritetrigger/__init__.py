# eventbriteTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_eventbritetrigger_tools() -> List[BaseTool]:
    """Get all eventbriteTrigger tools."""
    from . import operations
    return operations.get_tools()
