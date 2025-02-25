# quickChart toolkit
from langchain.tools import BaseTool
from typing import List

def get_quickchart_tools() -> List[BaseTool]:
    """Get all quickChart tools."""
    from . import operations
    return operations.get_tools()
