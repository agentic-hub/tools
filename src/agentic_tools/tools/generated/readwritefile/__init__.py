# readWriteFile toolkit
from langchain.tools import BaseTool
from typing import List

def get_readwritefile_tools() -> List[BaseTool]:
    """Get all readWriteFile tools."""
    from . import operations
    return operations.get_tools()
