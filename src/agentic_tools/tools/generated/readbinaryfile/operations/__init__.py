# readBinaryFile operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all readBinaryFile operation tools."""
    tools = []
    from .default import ReadbinaryfileDefaultTool
    tools.append(ReadbinaryfileDefaultTool())
    return tools
