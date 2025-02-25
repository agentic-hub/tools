# mocean toolkit
from langchain.tools import BaseTool
from typing import List

def get_mocean_tools() -> List[BaseTool]:
    """Get all mocean tools."""
    from . import operations
    return operations.get_tools()
