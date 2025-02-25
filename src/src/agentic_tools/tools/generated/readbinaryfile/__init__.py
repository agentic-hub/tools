# readBinaryFile toolkit
from langchain.tools import BaseTool
from typing import List

def get_readbinaryfile_tools() -> List[BaseTool]:
    """Get all readBinaryFile tools."""
    from . import operations
    return operations.get_tools()
