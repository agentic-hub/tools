# webflowTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_webflowtrigger_tools() -> List[BaseTool]:
    """Get all webflowTrigger tools."""
    from . import operations
    return operations.get_tools()
