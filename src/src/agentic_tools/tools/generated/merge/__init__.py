# merge toolkit
from langchain.tools import BaseTool
from typing import List

def get_merge_tools() -> List[BaseTool]:
    """Get all merge tools."""
    from . import operations
    return operations.get_tools()
