# nextCloud toolkit
from langchain.tools import BaseTool
from typing import List

def get_nextcloud_tools() -> List[BaseTool]:
    """Get all nextCloud tools."""
    from . import operations
    return operations.get_tools()
