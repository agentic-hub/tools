# wekan toolkit
from langchain.tools import BaseTool
from typing import List

def get_wekan_tools() -> List[BaseTool]:
    """Get all wekan tools."""
    from . import operations
    return operations.get_tools()
