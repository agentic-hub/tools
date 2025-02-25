# sseTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_ssetrigger_tools() -> List[BaseTool]:
    """Get all sseTrigger tools."""
    from . import operations
    return operations.get_tools()
