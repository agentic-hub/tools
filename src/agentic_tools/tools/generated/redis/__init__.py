# redis toolkit
from langchain.tools import BaseTool
from typing import List

def get_redis_tools() -> List[BaseTool]:
    """Get all redis tools."""
    from . import operations
    return operations.get_tools()
