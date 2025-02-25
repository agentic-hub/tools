# segment toolkit
from langchain.tools import BaseTool
from typing import List

def get_segment_tools() -> List[BaseTool]:
    """Get all segment tools."""
    from . import operations
    return operations.get_tools()
