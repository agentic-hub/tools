# npm toolkit
from langchain.tools import BaseTool
from typing import List

def get_npm_tools() -> List[BaseTool]:
    """Get all npm tools."""
    from . import operations
    return operations.get_tools()
