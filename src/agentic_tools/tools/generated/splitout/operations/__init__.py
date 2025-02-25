# splitOut operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all splitOut operation tools."""
    tools = []
    from .default import SplitoutDefaultTool
    tools.append(SplitoutDefaultTool())
    return tools
