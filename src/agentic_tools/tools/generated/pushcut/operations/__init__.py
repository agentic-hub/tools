# pushcut operations
from typing import List
from langchain.tools import BaseTool
from .. import PushcutCredentials

def get_tools() -> List[BaseTool]:
    """Get all pushcut operation tools."""
    tools = []
    from .send import PushcutSendTool
    tools.append(PushcutSendTool())
    return tools
