# formstackTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_formstacktrigger_tools() -> List[BaseTool]:
    """Get all formstackTrigger tools."""
    from . import operations
    return operations.get_tools()
