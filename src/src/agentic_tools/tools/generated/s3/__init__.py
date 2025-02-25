# s3 toolkit
from langchain.tools import BaseTool
from typing import List

def get_s3_tools() -> List[BaseTool]:
    """Get all s3 tools."""
    from . import operations
    return operations.get_tools()
