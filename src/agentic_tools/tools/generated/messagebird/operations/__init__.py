# messageBird operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import MessagebirdCredentials

def get_tools() -> List[BaseTool]:
    """Get all messageBird operation tools."""
    tools = []
    from .send import MessagebirdSendTool
    tools.append(MessagebirdSendTool())
    from .get import MessagebirdGetTool
    tools.append(MessagebirdGetTool())
    return tools
