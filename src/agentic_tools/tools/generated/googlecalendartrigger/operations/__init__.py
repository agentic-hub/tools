# googleCalendarTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all googleCalendarTrigger operation tools."""
    tools = []
    from .default import GooglecalendartriggerDefaultTool
    tools.append(GooglecalendartriggerDefaultTool())
    return tools
