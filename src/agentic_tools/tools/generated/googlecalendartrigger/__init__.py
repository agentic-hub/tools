# googleCalendarTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_googlecalendartrigger_tools() -> List[BaseTool]:
    """Get all googleCalendarTrigger tools."""
    from . import operations
    return operations.get_tools()
