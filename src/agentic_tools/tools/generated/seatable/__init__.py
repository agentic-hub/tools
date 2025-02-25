# seaTable toolkit
from langchain.tools import BaseTool
from typing import List

def get_seatable_tools() -> List[BaseTool]:
    """Get all seaTable tools."""
    from . import operations
    return operations.get_tools()
