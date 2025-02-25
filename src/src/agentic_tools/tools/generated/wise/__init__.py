# wise toolkit
from langchain.tools import BaseTool
from typing import List

def get_wise_tools() -> List[BaseTool]:
    """Get all wise tools."""
    from . import operations
    return operations.get_tools()
