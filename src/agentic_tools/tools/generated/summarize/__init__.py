# summarize toolkit
from langchain.tools import BaseTool
from typing import List

def get_summarize_tools() -> List[BaseTool]:
    """Get all summarize tools."""
    from . import operations
    return operations.get_tools()
