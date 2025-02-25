# webflowTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all webflowTrigger operation tools."""
    tools = []
    from .default import WebflowtriggerDefaultTool
    tools.append(WebflowtriggerDefaultTool())
    return tools
