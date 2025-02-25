# calTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all calTrigger operation tools."""
    tools = []
    from .default import CaltriggerDefaultTool
    tools.append(CaltriggerDefaultTool())
    return tools
