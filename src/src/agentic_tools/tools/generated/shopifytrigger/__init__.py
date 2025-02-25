# shopifyTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_shopifytrigger_tools() -> List[BaseTool]:
    """Get all shopifyTrigger tools."""
    from . import operations
    return operations.get_tools()
