# linearTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all linearTrigger operation tools."""
    tools = []
    from .default import LineartriggerDefaultTool
    tools.append(LineartriggerDefaultTool())
    return tools
