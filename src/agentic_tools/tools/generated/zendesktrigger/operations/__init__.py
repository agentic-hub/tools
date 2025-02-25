# zendeskTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all zendeskTrigger operation tools."""
    tools = []
    from .default import ZendesktriggerDefaultTool
    tools.append(ZendesktriggerDefaultTool())
    return tools
