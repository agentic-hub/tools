# quickChart operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all quickChart operation tools."""
    tools = []
    from .default import QuickchartDefaultTool
    tools.append(QuickchartDefaultTool())
    return tools
