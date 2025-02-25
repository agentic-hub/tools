# wufooTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all wufooTrigger operation tools."""
    tools = []
    from .default import WufootriggerDefaultTool
    tools.append(WufootriggerDefaultTool())
    return tools
