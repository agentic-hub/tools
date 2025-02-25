# zendesk toolkit
from langchain.tools import BaseTool
from typing import List

def get_zendesk_tools() -> List[BaseTool]:
    """Get all zendesk tools."""
    from . import operations
    return operations.get_tools()
