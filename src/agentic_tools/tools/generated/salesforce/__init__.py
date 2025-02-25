# salesforce toolkit
from langchain.tools import BaseTool
from typing import List

def get_salesforce_tools() -> List[BaseTool]:
    """Get all salesforce tools."""
    from . import operations
    return operations.get_tools()
