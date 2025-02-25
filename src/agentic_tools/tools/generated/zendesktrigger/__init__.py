# zendeskTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_zendesktrigger_tools() -> List[BaseTool]:
    """Get all zendeskTrigger tools."""
    from . import operations
    return operations.get_tools()
