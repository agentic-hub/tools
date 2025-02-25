# phantombuster toolkit
from langchain.tools import BaseTool
from typing import List

def get_phantombuster_tools() -> List[BaseTool]:
    """Get all phantombuster tools."""
    from . import operations
    return operations.get_tools()
