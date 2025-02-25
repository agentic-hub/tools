# gitlab toolkit
from langchain.tools import BaseTool
from typing import List

def get_gitlab_tools() -> List[BaseTool]:
    """Get all gitlab tools."""
    from . import operations
    return operations.get_tools()
