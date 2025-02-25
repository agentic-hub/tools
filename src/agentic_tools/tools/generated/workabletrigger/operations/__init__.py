# workableTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all workableTrigger operation tools."""
    tools = []
    from .default import WorkabletriggerDefaultTool
    tools.append(WorkabletriggerDefaultTool())
    return tools
