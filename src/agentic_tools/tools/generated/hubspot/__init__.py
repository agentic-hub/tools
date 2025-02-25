# hubspot toolkit
from langchain.tools import BaseTool
from typing import List

def get_hubspot_tools() -> List[BaseTool]:
    """Get all hubspot tools."""
    from . import operations
    return operations.get_tools()
