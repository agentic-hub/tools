# pushcut operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import PushcutCredentials

def get_tools() -> List[BaseTool]:
    """Get all pushcut operation tools."""
    tools = []
    from .send import PushcutSendTool
    tools.append(PushcutSendTool())
    return tools
