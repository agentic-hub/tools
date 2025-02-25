# humanticAi toolkit
from langchain.tools import BaseTool
from typing import List

def get_humanticai_tools() -> List[BaseTool]:
    """Get all humanticAi tools."""
    from . import operations
    return operations.get_tools()
