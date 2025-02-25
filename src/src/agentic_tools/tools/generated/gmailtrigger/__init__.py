# gmailTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_gmailtrigger_tools() -> List[BaseTool]:
    """Get all gmailTrigger tools."""
    from . import operations
    return operations.get_tools()
