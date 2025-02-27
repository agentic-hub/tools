# crypto operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all crypto operation tools."""
    tools = []
    from .default import CryptoDefaultTool
    tools.append(CryptoDefaultTool())
    return tools
