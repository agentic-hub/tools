# convertKitTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_convertkittrigger_tools() -> List[BaseTool]:
    """Get all convertKitTrigger tools."""
    from . import operations
    return operations.get_tools()
