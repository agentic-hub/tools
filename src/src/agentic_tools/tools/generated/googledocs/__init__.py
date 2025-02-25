# googleDocs toolkit
from langchain.tools import BaseTool
from typing import List

def get_googledocs_tools() -> List[BaseTool]:
    """Get all googleDocs tools."""
    from . import operations
    return operations.get_tools()
