# clickUpTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all clickUpTrigger operation tools."""
    tools = []
    from .default import ClickuptriggerDefaultTool
    tools.append(ClickuptriggerDefaultTool())
    return tools
