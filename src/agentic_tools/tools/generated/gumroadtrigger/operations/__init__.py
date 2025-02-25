# gumroadTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all gumroadTrigger operation tools."""
    tools = []
    from .default import GumroadtriggerDefaultTool
    tools.append(GumroadtriggerDefaultTool())
    return tools
