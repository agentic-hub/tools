# readBinaryFiles operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all readBinaryFiles operation tools."""
    tools = []
    from .default import ReadbinaryfilesDefaultTool
    tools.append(ReadbinaryfilesDefaultTool())
    return tools
