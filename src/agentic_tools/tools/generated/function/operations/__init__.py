# function operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all function operation tools."""
    tools = []
    from .default import FunctionDefaultTool
    tools.append(FunctionDefaultTool())
    return tools
