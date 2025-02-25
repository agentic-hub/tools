# googleBooks toolkit
from langchain.tools import BaseTool
from typing import List

def get_googlebooks_tools() -> List[BaseTool]:
    """Get all googleBooks tools."""
    from . import operations
    return operations.get_tools()
