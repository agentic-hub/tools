# kafkaTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_kafkatrigger_tools() -> List[BaseTool]:
    """Get all kafkaTrigger tools."""
    from . import operations
    return operations.get_tools()
