# writeBinaryFile operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all writeBinaryFile operation tools."""
    tools = []
    from .default import WritebinaryfileDefaultTool
    tools.append(WritebinaryfileDefaultTool())
    return tools
