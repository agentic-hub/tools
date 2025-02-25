# lingvaNex operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all lingvaNex operation tools."""
    tools = []
    from .translate import LingvanexTranslateTool
    tools.append(LingvanexTranslateTool())
    return tools
