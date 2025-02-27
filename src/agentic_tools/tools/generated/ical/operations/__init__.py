# iCal operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all iCal operation tools."""
    tools = []
    from .createeventfile import IcalCreateeventfileTool
    tools.append(IcalCreateeventfileTool())
    return tools
