# reddit toolkit
from langchain.tools import BaseTool
from typing import List

def get_reddit_tools() -> List[BaseTool]:
    """Get all reddit tools."""
    from . import operations
    return operations.get_tools()
