# function operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all function operation tools."""
    tools = []
    from .default import FunctionDefaultTool
    tools.append(FunctionDefaultTool())
    return tools
