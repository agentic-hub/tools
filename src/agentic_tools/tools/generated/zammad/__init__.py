# zammad toolkit
from langchain.tools import BaseTool
from typing import List

def get_zammad_tools() -> List[BaseTool]:
    """Get all zammad tools."""
    from . import operations
    return operations.get_tools()
