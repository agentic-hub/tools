# egoi toolkit
from langchain.tools import BaseTool
from typing import List

def get_egoi_tools() -> List[BaseTool]:
    """Get all egoi tools."""
    from . import operations
    return operations.get_tools()
