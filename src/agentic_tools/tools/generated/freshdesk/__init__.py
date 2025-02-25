# freshdesk toolkit
from langchain.tools import BaseTool
from typing import List

def get_freshdesk_tools() -> List[BaseTool]:
    """Get all freshdesk tools."""
    from . import operations
    return operations.get_tools()
