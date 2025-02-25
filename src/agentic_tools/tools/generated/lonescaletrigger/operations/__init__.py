# loneScaleTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all loneScaleTrigger operation tools."""
    tools = []
    from .default import LonescaletriggerDefaultTool
    tools.append(LonescaletriggerDefaultTool())
    return tools
