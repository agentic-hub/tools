# if operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all if operation tools."""
    tools = []
    from .default import IfDefaultTool
    tools.append(IfDefaultTool())
    return tools
