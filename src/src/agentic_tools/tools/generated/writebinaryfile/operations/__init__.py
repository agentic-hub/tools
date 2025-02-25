# writeBinaryFile operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all writeBinaryFile operation tools."""
    tools = []
    from .default import WritebinaryfileDefaultTool
    tools.append(WritebinaryfileDefaultTool())
    return tools
