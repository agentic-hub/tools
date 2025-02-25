# freshservice toolkit
from langchain.tools import BaseTool
from typing import List

def get_freshservice_tools() -> List[BaseTool]:
    """Get all freshservice tools."""
    from . import operations
    return operations.get_tools()
