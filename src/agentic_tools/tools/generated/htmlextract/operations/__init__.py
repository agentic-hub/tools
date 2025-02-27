# htmlExtract operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all htmlExtract operation tools."""
    tools = []
    from .default import HtmlextractDefaultTool
    tools.append(HtmlextractDefaultTool())
    return tools
