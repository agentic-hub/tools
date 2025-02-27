# code operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all code operation tools."""
    tools = []
    from .default import CodeDefaultTool
    tools.append(CodeDefaultTool())
    return tools
