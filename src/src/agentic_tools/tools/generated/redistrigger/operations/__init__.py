# redisTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all redisTrigger operation tools."""
    tools = []
    from .default import RedistriggerDefaultTool
    tools.append(RedistriggerDefaultTool())
    return tools
