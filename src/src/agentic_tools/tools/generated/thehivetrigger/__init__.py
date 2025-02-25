# theHiveTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_thehivetrigger_tools() -> List[BaseTool]:
    """Get all theHiveTrigger tools."""
    from . import operations
    return operations.get_tools()
