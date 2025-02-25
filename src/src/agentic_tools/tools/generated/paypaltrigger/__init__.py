# payPalTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_paypaltrigger_tools() -> List[BaseTool]:
    """Get all payPalTrigger tools."""
    from . import operations
    return operations.get_tools()
