# redisTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_redistrigger_tools() -> List[BaseTool]:
    """Get all redisTrigger tools."""
    from . import operations
    return operations.get_tools()
