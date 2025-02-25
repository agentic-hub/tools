# theHive toolkit
from langchain.tools import BaseTool
from typing import List

def get_thehive_tools() -> List[BaseTool]:
    """Get all theHive tools."""
    from . import operations
    return operations.get_tools()
