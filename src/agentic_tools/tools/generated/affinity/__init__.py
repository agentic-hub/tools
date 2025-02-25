# affinity toolkit
from langchain.tools import BaseTool
from typing import List

def get_affinity_tools() -> List[BaseTool]:
    """Get all affinity tools."""
    from . import operations
    return operations.get_tools()
