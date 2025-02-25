# googleAds toolkit
from langchain.tools import BaseTool
from typing import List

def get_googleads_tools() -> List[BaseTool]:
    """Get all googleAds tools."""
    from . import operations
    return operations.get_tools()
