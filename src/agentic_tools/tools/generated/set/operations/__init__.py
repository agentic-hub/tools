# set operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all set operation tools."""
    tools = []
    from .default import SetDefaultTool
    tools.append(SetDefaultTool())
    return tools
