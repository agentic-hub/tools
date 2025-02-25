# emeliaTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_emeliatrigger_tools() -> List[BaseTool]:
    """Get all emeliaTrigger tools."""
    from . import operations
    return operations.get_tools()
