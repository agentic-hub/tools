# helpScoutTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all helpScoutTrigger operation tools."""
    tools = []
    from .default import HelpscouttriggerDefaultTool
    tools.append(HelpscouttriggerDefaultTool())
    return tools
