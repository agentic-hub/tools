# mautic toolkit
from langchain.tools import BaseTool
from typing import List

def get_mautic_tools() -> List[BaseTool]:
    """Get all mautic tools."""
    from . import operations
    return operations.get_tools()
