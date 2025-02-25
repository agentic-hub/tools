# goToWebinar toolkit
from langchain.tools import BaseTool
from typing import List

def get_gotowebinar_tools() -> List[BaseTool]:
    """Get all goToWebinar tools."""
    from . import operations
    return operations.get_tools()
