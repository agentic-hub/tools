# convertToFile toolkit
from langchain.tools import BaseTool
from typing import List

def get_converttofile_tools() -> List[BaseTool]:
    """Get all convertToFile tools."""
    from . import operations
    return operations.get_tools()
