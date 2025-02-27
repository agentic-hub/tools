# xml operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all xml operation tools."""
    tools = []
    from .default import XmlDefaultTool
    tools.append(XmlDefaultTool())
    return tools
