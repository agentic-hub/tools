# errorTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_errortrigger_tools() -> List[BaseTool]:
    """Get all errorTrigger tools."""
    from . import operations
    return operations.get_tools()
