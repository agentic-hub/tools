# removeDuplicates operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all removeDuplicates operation tools."""
    tools = []
    from .default import RemoveduplicatesDefaultTool
    tools.append(RemoveduplicatesDefaultTool())
    return tools
