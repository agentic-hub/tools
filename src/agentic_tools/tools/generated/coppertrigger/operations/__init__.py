# copperTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all copperTrigger operation tools."""
    tools = []
    from .default import CoppertriggerDefaultTool
    tools.append(CoppertriggerDefaultTool())
    return tools
