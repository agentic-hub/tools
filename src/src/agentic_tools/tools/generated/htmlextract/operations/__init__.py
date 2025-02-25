# htmlExtract operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all htmlExtract operation tools."""
    tools = []
    from .default import HtmlextractDefaultTool
    tools.append(HtmlextractDefaultTool())
    return tools
