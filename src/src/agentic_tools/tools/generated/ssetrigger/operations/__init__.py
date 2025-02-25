# sseTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all sseTrigger operation tools."""
    tools = []
    from .default import SsetriggerDefaultTool
    tools.append(SsetriggerDefaultTool())
    return tools
