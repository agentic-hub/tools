# awsSes toolkit
from langchain.tools import BaseTool
from typing import List

def get_awsses_tools() -> List[BaseTool]:
    """Get all awsSes tools."""
    from . import operations
    return operations.get_tools()
