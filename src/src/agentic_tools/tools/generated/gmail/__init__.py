# gmail toolkit
from langchain.tools import BaseTool
from typing import List

def get_gmail_tools() -> List[BaseTool]:
    """Get all gmail tools."""
    from . import operations
    return operations.get_tools()
