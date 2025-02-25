# filemaker toolkit
from langchain.tools import BaseTool
from typing import List

def get_filemaker_tools() -> List[BaseTool]:
    """Get all filemaker tools."""
    from . import operations
    return operations.get_tools()
