# postmarkTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_postmarktrigger_tools() -> List[BaseTool]:
    """Get all postmarkTrigger tools."""
    from . import operations
    return operations.get_tools()
