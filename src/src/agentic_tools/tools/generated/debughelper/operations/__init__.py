# debugHelper operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all debugHelper operation tools."""
    tools = []
    from .default import DebughelperDefaultTool
    tools.append(DebughelperDefaultTool())
    return tools
