# googleCloudStorage toolkit
from langchain.tools import BaseTool
from typing import List

def get_googlecloudstorage_tools() -> List[BaseTool]:
    """Get all googleCloudStorage tools."""
    from . import operations
    return operations.get_tools()
