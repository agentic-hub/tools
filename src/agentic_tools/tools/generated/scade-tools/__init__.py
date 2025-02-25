# scade-tools toolkit
from langchain.tools import BaseTool
from typing import List

def get_scade-tools_tools() -> List[BaseTool]:
    """Get all scade-tools tools."""
    from . import operations
    return operations.get_tools()
