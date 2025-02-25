# compression toolkit
from langchain.tools import BaseTool
from typing import List

def get_compression_tools() -> List[BaseTool]:
    """Get all compression tools."""
    from . import operations
    return operations.get_tools()
