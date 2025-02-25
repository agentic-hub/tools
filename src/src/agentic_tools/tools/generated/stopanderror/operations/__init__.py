# stopAndError operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all stopAndError operation tools."""
    tools = []
    from .default import StopanderrorDefaultTool
    tools.append(StopanderrorDefaultTool())
    return tools
