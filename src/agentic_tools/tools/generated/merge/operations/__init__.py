# merge operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all merge operation tools."""
    tools = []
    from .default import MergeDefaultTool
    tools.append(MergeDefaultTool())
    return tools
