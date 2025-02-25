# dhl operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all dhl operation tools."""
    tools = []
    from .get import DhlGetTool
    tools.append(DhlGetTool())
    return tools
