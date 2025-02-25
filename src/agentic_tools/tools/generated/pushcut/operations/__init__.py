# pushcut operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all pushcut operation tools."""
    tools = []
    from .send import PushcutSendTool
    tools.append(PushcutSendTool())
    return tools
