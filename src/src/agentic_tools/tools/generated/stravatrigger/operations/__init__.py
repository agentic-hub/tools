# stravaTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all stravaTrigger operation tools."""
    tools = []
    from .default import StravatriggerDefaultTool
    tools.append(StravatriggerDefaultTool())
    return tools
