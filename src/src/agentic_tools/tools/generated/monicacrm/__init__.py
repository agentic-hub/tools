# monicaCrm toolkit
from langchain.tools import BaseTool
from typing import List

def get_monicacrm_tools() -> List[BaseTool]:
    """Get all monicaCrm tools."""
    from . import operations
    return operations.get_tools()
