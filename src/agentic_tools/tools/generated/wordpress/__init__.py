# wordpress toolkit
from langchain.tools import BaseTool
from typing import List

def get_wordpress_tools() -> List[BaseTool]:
    """Get all wordpress tools."""
    from . import operations
    return operations.get_tools()
