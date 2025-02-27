# lingvaNex operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import LingvanexCredentials

def get_tools() -> List[BaseTool]:
    """Get all lingvaNex operation tools."""
    tools = []
    from .translate import LingvanexTranslateTool
    tools.append(LingvanexTranslateTool())
    return tools
