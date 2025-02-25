# gSuiteAdmin toolkit
from langchain.tools import BaseTool
from typing import List

def get_gsuiteadmin_tools() -> List[BaseTool]:
    """Get all gSuiteAdmin tools."""
    from . import operations
    return operations.get_tools()
