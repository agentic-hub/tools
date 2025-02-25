# quickbase toolkit
from langchain.tools import BaseTool
from typing import List

def get_quickbase_tools() -> List[BaseTool]:
    """Get all quickbase tools."""
    from . import operations
    return operations.get_tools()
