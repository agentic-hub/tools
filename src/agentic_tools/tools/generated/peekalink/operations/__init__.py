# peekalink operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import PeekalinkCredentials

def get_tools() -> List[BaseTool]:
    """Get all peekalink operation tools."""
    tools = []
    from .isavailable import PeekalinkIsavailableTool
    tools.append(PeekalinkIsavailableTool())
    from .preview import PeekalinkPreviewTool
    tools.append(PeekalinkPreviewTool())
    return tools
