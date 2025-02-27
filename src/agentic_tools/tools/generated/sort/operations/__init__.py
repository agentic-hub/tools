# sort operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all sort operation tools."""
    tools = []
    from .default import SortDefaultTool
    tools.append(SortDefaultTool())
    return tools
