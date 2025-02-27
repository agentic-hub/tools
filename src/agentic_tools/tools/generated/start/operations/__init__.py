# start operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all start operation tools."""
    tools = []
    from .default import StartDefaultTool
    tools.append(StartDefaultTool())
    return tools
