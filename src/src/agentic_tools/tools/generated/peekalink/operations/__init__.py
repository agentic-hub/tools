# peekalink operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all peekalink operation tools."""
    tools = []
    from .isavailable import PeekalinkIsavailableTool
    tools.append(PeekalinkIsavailableTool())
    from .preview import PeekalinkPreviewTool
    tools.append(PeekalinkPreviewTool())
    return tools
