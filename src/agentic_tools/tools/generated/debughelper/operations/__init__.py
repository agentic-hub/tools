# debugHelper operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all debugHelper operation tools."""
    tools = []
    from .default import DebughelperDefaultTool
    tools.append(DebughelperDefaultTool())
    return tools
