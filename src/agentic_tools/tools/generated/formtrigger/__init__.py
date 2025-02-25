# formTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_formtrigger_tools() -> List[BaseTool]:
    """Get all formTrigger tools."""
    from . import operations
    return operations.get_tools()
