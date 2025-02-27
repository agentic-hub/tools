# interval operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all interval operation tools."""
    tools = []
    from .default import IntervalDefaultTool
    tools.append(IntervalDefaultTool())
    return tools
