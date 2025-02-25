# xml operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all xml operation tools."""
    tools = []
    from .default import XmlDefaultTool
    tools.append(XmlDefaultTool())
    return tools
