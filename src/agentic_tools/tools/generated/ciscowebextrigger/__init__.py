# ciscoWebexTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_ciscowebextrigger_tools() -> List[BaseTool]:
    """Get all ciscoWebexTrigger tools."""
    from . import operations
    return operations.get_tools()
