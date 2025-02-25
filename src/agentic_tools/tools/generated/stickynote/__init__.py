# stickyNote toolkit
from langchain.tools import BaseTool
from typing import List

def get_stickynote_tools() -> List[BaseTool]:
    """Get all stickyNote tools."""
    from . import operations
    return operations.get_tools()
