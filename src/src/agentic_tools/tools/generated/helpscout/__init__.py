# helpScout toolkit
from langchain.tools import BaseTool
from typing import List

def get_helpscout_tools() -> List[BaseTool]:
    """Get all helpScout tools."""
    from . import operations
    return operations.get_tools()
