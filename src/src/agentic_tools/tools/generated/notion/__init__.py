# notion toolkit
from langchain.tools import BaseTool
from typing import List

def get_notion_tools() -> List[BaseTool]:
    """Get all notion tools."""
    from . import operations
    return operations.get_tools()
