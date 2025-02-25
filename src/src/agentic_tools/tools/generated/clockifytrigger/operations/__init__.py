# clockifyTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all clockifyTrigger operation tools."""
    tools = []
    from .default import ClockifytriggerDefaultTool
    tools.append(ClockifytriggerDefaultTool())
    return tools
