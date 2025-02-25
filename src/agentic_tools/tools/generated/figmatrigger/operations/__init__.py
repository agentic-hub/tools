# figmaTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all figmaTrigger operation tools."""
    tools = []
    from .default import FigmatriggerDefaultTool
    tools.append(FigmatriggerDefaultTool())
    return tools
