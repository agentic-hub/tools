# flowTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all flowTrigger operation tools."""
    tools = []
    from .default import FlowtriggerDefaultTool
    tools.append(FlowtriggerDefaultTool())
    return tools
