# wiseTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_wisetrigger_tools() -> List[BaseTool]:
    """Get all wiseTrigger tools."""
    from . import operations
    return operations.get_tools()
