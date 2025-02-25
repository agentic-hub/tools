# jotFormTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_jotformtrigger_tools() -> List[BaseTool]:
    """Get all jotFormTrigger tools."""
    from . import operations
    return operations.get_tools()
