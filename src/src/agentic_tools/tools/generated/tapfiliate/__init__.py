# tapfiliate toolkit
from langchain.tools import BaseTool
from typing import List

def get_tapfiliate_tools() -> List[BaseTool]:
    """Get all tapfiliate tools."""
    from . import operations
    return operations.get_tools()
