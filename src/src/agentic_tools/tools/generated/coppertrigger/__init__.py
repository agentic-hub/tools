# copperTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_coppertrigger_tools() -> List[BaseTool]:
    """Get all copperTrigger tools."""
    from . import operations
    return operations.get_tools()
