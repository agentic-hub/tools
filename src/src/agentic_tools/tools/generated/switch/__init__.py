# switch toolkit
from langchain.tools import BaseTool
from typing import List

def get_switch_tools() -> List[BaseTool]:
    """Get all switch tools."""
    from . import operations
    return operations.get_tools()
