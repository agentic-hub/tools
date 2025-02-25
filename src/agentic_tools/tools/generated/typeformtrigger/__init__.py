# typeformTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_typeformtrigger_tools() -> List[BaseTool]:
    """Get all typeformTrigger tools."""
    from . import operations
    return operations.get_tools()
