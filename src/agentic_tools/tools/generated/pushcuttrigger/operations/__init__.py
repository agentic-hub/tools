# pushcutTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all pushcutTrigger operation tools."""
    tools = []
    from .default import PushcuttriggerDefaultTool
    tools.append(PushcuttriggerDefaultTool())
    return tools
