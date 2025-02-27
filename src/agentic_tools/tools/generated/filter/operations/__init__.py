# filter operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all filter operation tools."""
    tools = []
    from .default import FilterDefaultTool
    tools.append(FilterDefaultTool())
    return tools
