# mongoDb toolkit
from langchain.tools import BaseTool
from typing import List

def get_mongodb_tools() -> List[BaseTool]:
    """Get all mongoDb tools."""
    from . import operations
    return operations.get_tools()
