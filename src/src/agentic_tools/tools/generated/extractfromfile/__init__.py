# extractFromFile toolkit
from langchain.tools import BaseTool
from typing import List

def get_extractfromfile_tools() -> List[BaseTool]:
    """Get all extractFromFile tools."""
    from . import operations
    return operations.get_tools()
