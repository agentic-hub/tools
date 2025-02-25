# manualTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all manualTrigger operation tools."""
    tools = []
    from .default import ManualtriggerDefaultTool
    tools.append(ManualtriggerDefaultTool())
    return tools
