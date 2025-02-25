# readBinaryFiles toolkit
from langchain.tools import BaseTool
from typing import List

def get_readbinaryfiles_tools() -> List[BaseTool]:
    """Get all readBinaryFiles tools."""
    from . import operations
    return operations.get_tools()
