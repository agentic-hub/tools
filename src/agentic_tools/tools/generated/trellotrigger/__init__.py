# trelloTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_trellotrigger_tools() -> List[BaseTool]:
    """Get all trelloTrigger tools."""
    from . import operations
    return operations.get_tools()
