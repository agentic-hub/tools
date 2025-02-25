# netlifyTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_netlifytrigger_tools() -> List[BaseTool]:
    """Get all netlifyTrigger tools."""
    from . import operations
    return operations.get_tools()
