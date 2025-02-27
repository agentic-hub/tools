# dhl operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import DhlCredentials

def get_tools() -> List[BaseTool]:
    """Get all dhl operation tools."""
    tools = []
    from .get import DhlGetTool
    tools.append(DhlGetTool())
    return tools
