# splitOut toolkit
from langchain.tools import BaseTool
from typing import List

def get_splitout_tools() -> List[BaseTool]:
    """Get all splitOut tools."""
    from . import operations
    return operations.get_tools()
