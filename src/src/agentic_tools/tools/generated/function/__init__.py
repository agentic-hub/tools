# function toolkit
from langchain.tools import BaseTool
from typing import List

def get_function_tools() -> List[BaseTool]:
    """Get all function tools."""
    from . import operations
    return operations.get_tools()
