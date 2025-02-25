# contentful toolkit
from langchain.tools import BaseTool
from typing import List

def get_contentful_tools() -> List[BaseTool]:
    """Get all contentful tools."""
    from . import operations
    return operations.get_tools()
