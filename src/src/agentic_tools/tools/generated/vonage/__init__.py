# vonage toolkit
from langchain.tools import BaseTool
from typing import List

def get_vonage_tools() -> List[BaseTool]:
    """Get all vonage tools."""
    from . import operations
    return operations.get_tools()
