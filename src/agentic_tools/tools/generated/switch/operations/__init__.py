# switch operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all switch operation tools."""
    tools = []
    from .default import SwitchDefaultTool
    tools.append(SwitchDefaultTool())
    return tools
