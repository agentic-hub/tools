# uplead operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import UpleadCredentials

def get_tools() -> List[BaseTool]:
    """Get all uplead operation tools."""
    tools = []
    from .enrich import UpleadEnrichTool
    tools.append(UpleadEnrichTool())
    from .enrich import UpleadEnrichTool
    tools.append(UpleadEnrichTool())
    return tools
