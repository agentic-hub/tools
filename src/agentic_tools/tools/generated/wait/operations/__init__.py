# wait operations
from typing import List
from langchain.tools import BaseTool
from .. import WaitCredentials

def get_tools() -> List[BaseTool]:
    """Get all wait operation tools."""
    tools = []
    from .default import WaitDefaultTool
    tools.append(WaitDefaultTool())
    return tools
