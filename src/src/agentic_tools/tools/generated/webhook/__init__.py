# webhook toolkit
from langchain.tools import BaseTool
from typing import List

def get_webhook_tools() -> List[BaseTool]:
    """Get all webhook tools."""
    from . import operations
    return operations.get_tools()
