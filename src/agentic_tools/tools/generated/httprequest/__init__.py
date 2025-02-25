# httpRequest toolkit
from langchain.tools import BaseTool
from typing import List

def get_httprequest_tools() -> List[BaseTool]:
    """Get all httpRequest tools."""
    from . import operations
    return operations.get_tools()
