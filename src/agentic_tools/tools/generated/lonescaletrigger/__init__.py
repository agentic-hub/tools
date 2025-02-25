# loneScaleTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_lonescaletrigger_tools() -> List[BaseTool]:
    """Get all loneScaleTrigger tools."""
    from . import operations
    return operations.get_tools()
