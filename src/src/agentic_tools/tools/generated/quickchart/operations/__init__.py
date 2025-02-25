# quickChart operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all quickChart operation tools."""
    tools = []
    from .default import QuickchartDefaultTool
    tools.append(QuickchartDefaultTool())
    return tools
