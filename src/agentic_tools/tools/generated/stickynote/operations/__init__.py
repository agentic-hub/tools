# stickyNote operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all stickyNote operation tools."""
    tools = []
    from .default import StickynoteDefaultTool
    tools.append(StickynoteDefaultTool())
    return tools
