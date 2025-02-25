# agileCrm toolkit
from langchain.tools import BaseTool
from typing import List

def get_agilecrm_tools() -> List[BaseTool]:
    """Get all agileCrm tools."""
    from . import operations
    return operations.get_tools()
