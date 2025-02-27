# splitOut operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all splitOut operation tools."""
    tools = []
    from .default import SplitoutDefaultTool
    tools.append(SplitoutDefaultTool())
    return tools
