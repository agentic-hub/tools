# readPDF operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all readPDF operation tools."""
    tools = []
    from .default import ReadpdfDefaultTool
    tools.append(ReadpdfDefaultTool())
    return tools
