# readBinaryFile operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all readBinaryFile operation tools."""
    tools = []
    from .default import ReadbinaryfileDefaultTool
    tools.append(ReadbinaryfileDefaultTool())
    return tools
