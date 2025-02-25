# onfleetTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all onfleetTrigger operation tools."""
    tools = []
    from .default import OnfleettriggerDefaultTool
    tools.append(OnfleettriggerDefaultTool())
    return tools
