# autopilotTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all autopilotTrigger operation tools."""
    tools = []
    from .default import AutopilottriggerDefaultTool
    tools.append(AutopilottriggerDefaultTool())
    return tools
