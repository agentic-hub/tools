# getResponse toolkit
from langchain.tools import BaseTool
from typing import List

def get_getresponse_tools() -> List[BaseTool]:
    """Get all getResponse tools."""
    from . import operations
    return operations.get_tools()
