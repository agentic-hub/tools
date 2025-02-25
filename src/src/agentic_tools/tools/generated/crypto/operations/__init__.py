# crypto operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all crypto operation tools."""
    tools = []
    from .default import CryptoDefaultTool
    tools.append(CryptoDefaultTool())
    return tools
