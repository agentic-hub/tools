# switch operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all switch operation tools."""
    tools = []
    from .default import SwitchDefaultTool
    tools.append(SwitchDefaultTool())
    return tools
