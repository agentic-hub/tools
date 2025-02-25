# hubspotTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_hubspottrigger_tools() -> List[BaseTool]:
    """Get all hubspotTrigger tools."""
    from . import operations
    return operations.get_tools()
