# spontit toolkit
from langchain.tools import BaseTool
from typing import List

def get_spontit_tools() -> List[BaseTool]:
    """Get all spontit tools."""
    from . import operations
    return operations.get_tools()
