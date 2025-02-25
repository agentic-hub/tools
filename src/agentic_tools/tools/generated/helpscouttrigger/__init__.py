# helpScoutTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_helpscouttrigger_tools() -> List[BaseTool]:
    """Get all helpScoutTrigger tools."""
    from . import operations
    return operations.get_tools()
