# urlScanIo toolkit
from langchain.tools import BaseTool
from typing import List

def get_urlscanio_tools() -> List[BaseTool]:
    """Get all urlScanIo tools."""
    from . import operations
    return operations.get_tools()
