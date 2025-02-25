# readPDF operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all readPDF operation tools."""
    tools = []
    from .default import ReadpdfDefaultTool
    tools.append(ReadpdfDefaultTool())
    return tools
