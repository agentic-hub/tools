# formIoTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_formiotrigger_tools() -> List[BaseTool]:
    """Get all formIoTrigger tools."""
    from . import operations
    return operations.get_tools()
