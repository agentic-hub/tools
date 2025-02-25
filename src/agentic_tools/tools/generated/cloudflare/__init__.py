# cloudflare toolkit
from langchain.tools import BaseTool
from typing import List

def get_cloudflare_tools() -> List[BaseTool]:
    """Get all cloudflare tools."""
    from . import operations
    return operations.get_tools()
