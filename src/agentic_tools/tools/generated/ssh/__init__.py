# ssh toolkit
from langchain.tools import BaseTool
from typing import List

def get_ssh_tools() -> List[BaseTool]:
    """Get all ssh tools."""
    from . import operations
    return operations.get_tools()
