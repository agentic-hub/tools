# keapTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all keapTrigger operation tools."""
    tools = []
    from .default import KeaptriggerDefaultTool
    tools.append(KeaptriggerDefaultTool())
    return tools
