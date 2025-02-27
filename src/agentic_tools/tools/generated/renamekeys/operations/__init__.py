# renameKeys operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all renameKeys operation tools."""
    tools = []
    from .default import RenamekeysDefaultTool
    tools.append(RenamekeysDefaultTool())
    return tools
