# mocean operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import MoceanCredentials

def get_tools() -> List[BaseTool]:
    """Get all mocean operation tools."""
    tools = []
    from .send import MoceanSendTool
    tools.append(MoceanSendTool())
    return tools
