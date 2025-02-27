# yourls operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import YourlsCredentials

def get_tools() -> List[BaseTool]:
    """Get all yourls operation tools."""
    tools = []
    from .expand import YourlsExpandTool
    tools.append(YourlsExpandTool())
    from .shorten import YourlsShortenTool
    tools.append(YourlsShortenTool())
    from .stats import YourlsStatsTool
    tools.append(YourlsStatsTool())
    return tools
