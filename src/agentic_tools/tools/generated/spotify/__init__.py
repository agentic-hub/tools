# spotify toolkit
from langchain.tools import BaseTool
from typing import List

def get_spotify_tools() -> List[BaseTool]:
    """Get all spotify tools."""
    from . import operations
    return operations.get_tools()
