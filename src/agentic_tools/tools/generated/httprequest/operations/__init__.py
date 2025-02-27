# httpRequest operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all httpRequest operation tools."""
    tools = []
    from .default import HttprequestDefaultTool
    tools.append(HttprequestDefaultTool())
    return tools
