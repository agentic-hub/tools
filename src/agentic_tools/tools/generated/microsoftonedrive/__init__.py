# microsoftOneDrive toolkit
from langchain.tools import BaseTool
from typing import List

def get_microsoftonedrive_tools() -> List[BaseTool]:
    """Get all microsoftOneDrive tools."""
    from . import operations
    return operations.get_tools()
