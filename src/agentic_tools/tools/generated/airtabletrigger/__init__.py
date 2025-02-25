# airtableTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_airtabletrigger_tools() -> List[BaseTool]:
    """Get all airtableTrigger tools."""
    from . import operations
    return operations.get_tools()
