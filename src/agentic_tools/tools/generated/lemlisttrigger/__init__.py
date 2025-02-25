# lemlistTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_lemlisttrigger_tools() -> List[BaseTool]:
    """Get all lemlistTrigger tools."""
    from . import operations
    return operations.get_tools()
