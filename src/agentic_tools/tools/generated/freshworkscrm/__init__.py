# freshworksCrm toolkit
from langchain.tools import BaseTool
from typing import List

def get_freshworkscrm_tools() -> List[BaseTool]:
    """Get all freshworksCrm tools."""
    from . import operations
    return operations.get_tools()
