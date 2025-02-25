# localFileTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_localfiletrigger_tools() -> List[BaseTool]:
    """Get all localFileTrigger tools."""
    from . import operations
    return operations.get_tools()
