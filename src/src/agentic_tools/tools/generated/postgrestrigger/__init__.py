# postgresTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_postgrestrigger_tools() -> List[BaseTool]:
    """Get all postgresTrigger tools."""
    from . import operations
    return operations.get_tools()
