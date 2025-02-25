# localFileTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all localFileTrigger operation tools."""
    tools = []
    from .default import LocalfiletriggerDefaultTool
    tools.append(LocalfiletriggerDefaultTool())
    return tools
