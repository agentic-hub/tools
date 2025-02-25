# intercom toolkit
from langchain.tools import BaseTool
from typing import List

def get_intercom_tools() -> List[BaseTool]:
    """Get all intercom tools."""
    from . import operations
    return operations.get_tools()
