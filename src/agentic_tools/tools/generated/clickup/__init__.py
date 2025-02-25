# clickUp toolkit
from langchain.tools import BaseTool
from typing import List

def get_clickup_tools() -> List[BaseTool]:
    """Get all clickUp tools."""
    from . import operations
    return operations.get_tools()
