# calTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_caltrigger_tools() -> List[BaseTool]:
    """Get all calTrigger tools."""
    from . import operations
    return operations.get_tools()
