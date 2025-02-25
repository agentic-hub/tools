# facebookLeadAdsTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_facebookleadadstrigger_tools() -> List[BaseTool]:
    """Get all facebookLeadAdsTrigger tools."""
    from . import operations
    return operations.get_tools()
