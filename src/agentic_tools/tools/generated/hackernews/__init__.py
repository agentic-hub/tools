# hackerNews toolkit
from langchain.tools import BaseTool
from typing import List

def get_hackernews_tools() -> List[BaseTool]:
    """Get all hackerNews tools."""
    from . import operations
    return operations.get_tools()
