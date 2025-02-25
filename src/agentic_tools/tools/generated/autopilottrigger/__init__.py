# autopilotTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_autopilottrigger_tools() -> List[BaseTool]:
    """Get all autopilotTrigger tools."""
    from . import operations
    return operations.get_tools()
