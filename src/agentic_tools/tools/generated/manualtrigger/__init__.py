# manualTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_manualtrigger_tools() -> List[BaseTool]:
    """Get all manualTrigger tools."""
    from . import operations
    return operations.get_tools()
