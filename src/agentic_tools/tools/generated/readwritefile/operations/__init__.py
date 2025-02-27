# readWriteFile operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all readWriteFile operation tools."""
    tools = []
    from .read import ReadwritefileReadTool
    tools.append(ReadwritefileReadTool())
    from .write import ReadwritefileWriteTool
    tools.append(ReadwritefileWriteTool())
    return tools
