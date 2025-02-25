# pipedrive toolkit
from langchain.tools import BaseTool
from typing import List

def get_pipedrive_tools() -> List[BaseTool]:
    """Get all pipedrive tools."""
    from . import operations
    return operations.get_tools()
