# uproc operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import UprocCredentials

def get_tools() -> List[BaseTool]:
    """Get all uproc operation tools."""
    tools = []
    from .default import UprocDefaultTool
    tools.append(UprocDefaultTool())
    return tools
