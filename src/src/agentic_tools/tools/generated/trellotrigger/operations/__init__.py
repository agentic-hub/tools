# trelloTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all trelloTrigger operation tools."""
    tools = []
    from .default import TrellotriggerDefaultTool
    tools.append(TrellotriggerDefaultTool())
    return tools
