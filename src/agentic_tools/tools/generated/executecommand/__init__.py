# executeCommand toolkit
from langchain.tools import BaseTool
from typing import List

def get_executecommand_tools() -> List[BaseTool]:
    """Get all executeCommand tools."""
    from . import operations
    return operations.get_tools()
