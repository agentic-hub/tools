# ftp toolkit
from langchain.tools import BaseTool
from typing import List

def get_ftp_tools() -> List[BaseTool]:
    """Get all ftp tools."""
    from . import operations
    return operations.get_tools()
