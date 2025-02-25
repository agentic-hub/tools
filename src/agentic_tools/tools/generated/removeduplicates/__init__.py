# removeDuplicates toolkit
from langchain.tools import BaseTool
from typing import List

def get_removeduplicates_tools() -> List[BaseTool]:
    """Get all removeDuplicates tools."""
    from . import operations
    return operations.get_tools()
