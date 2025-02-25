# uplead operations
from typing import List
from langchain.tools import BaseTool
from .. import UpleadCredentials

def get_tools() -> List[BaseTool]:
    """Get all uplead operation tools."""
    tools = []
    from .enrich import UpleadEnrichTool
    tools.append(UpleadEnrichTool())
    from .enrich import UpleadEnrichTool
    tools.append(UpleadEnrichTool())
    return tools
