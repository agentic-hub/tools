# netlify toolkit
from langchain.tools import BaseTool
from typing import List

def get_netlify_tools() -> List[BaseTool]:
    """Get all netlify tools."""
    from . import operations
    return operations.get_tools()
