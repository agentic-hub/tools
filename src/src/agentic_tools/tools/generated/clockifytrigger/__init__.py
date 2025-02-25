# clockifyTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_clockifytrigger_tools() -> List[BaseTool]:
    """Get all clockifyTrigger tools."""
    from . import operations
    return operations.get_tools()
