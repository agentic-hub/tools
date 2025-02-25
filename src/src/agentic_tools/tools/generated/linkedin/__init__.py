# linkedIn toolkit
from langchain.tools import BaseTool
from typing import List

def get_linkedin_tools() -> List[BaseTool]:
    """Get all linkedIn tools."""
    from . import operations
    return operations.get_tools()
