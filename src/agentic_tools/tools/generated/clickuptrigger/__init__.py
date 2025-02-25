# clickUpTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_clickuptrigger_tools() -> List[BaseTool]:
    """Get all clickUpTrigger tools."""
    from . import operations
    return operations.get_tools()
