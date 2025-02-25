# iCal operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all iCal operation tools."""
    tools = []
    from .createeventfile import IcalCreateeventfileTool
    tools.append(IcalCreateeventfileTool())
    return tools
