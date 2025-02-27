# readBinaryFiles operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all readBinaryFiles operation tools."""
    tools = []
    from .default import ReadbinaryfilesDefaultTool
    tools.append(ReadbinaryfilesDefaultTool())
    return tools
