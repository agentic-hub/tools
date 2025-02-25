# seaTableTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all seaTableTrigger operation tools."""
    tools = []
    from .default import SeatabletriggerDefaultTool
    tools.append(SeatabletriggerDefaultTool())
    return tools
