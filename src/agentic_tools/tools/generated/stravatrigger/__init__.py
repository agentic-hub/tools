# stravaTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_stravatrigger_tools() -> List[BaseTool]:
    """Get all stravaTrigger tools."""
    from . import operations
    return operations.get_tools()
