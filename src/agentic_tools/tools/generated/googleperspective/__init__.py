# googlePerspective toolkit
from langchain.tools import BaseTool
from typing import List

def get_googleperspective_tools() -> List[BaseTool]:
    """Get all googlePerspective tools."""
    from . import operations
    return operations.get_tools()
