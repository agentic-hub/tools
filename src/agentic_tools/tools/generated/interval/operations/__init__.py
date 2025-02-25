# interval operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all interval operation tools."""
    tools = []
    from .default import IntervalDefaultTool
    tools.append(IntervalDefaultTool())
    return tools
