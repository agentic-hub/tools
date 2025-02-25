# mailjetTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_mailjettrigger_tools() -> List[BaseTool]:
    """Get all mailjetTrigger tools."""
    from . import operations
    return operations.get_tools()
