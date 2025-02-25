# facebookTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_facebooktrigger_tools() -> List[BaseTool]:
    """Get all facebookTrigger tools."""
    from . import operations
    return operations.get_tools()
