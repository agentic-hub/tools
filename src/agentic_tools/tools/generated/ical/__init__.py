# iCal toolkit
from langchain.tools import BaseTool
from typing import List

def get_ical_tools() -> List[BaseTool]:
    """Get all iCal tools."""
    from . import operations
    return operations.get_tools()
