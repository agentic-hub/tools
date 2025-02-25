# set operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all set operation tools."""
    tools = []
    from .default import SetDefaultTool
    tools.append(SetDefaultTool())
    return tools
