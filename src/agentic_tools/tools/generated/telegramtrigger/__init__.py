# telegramTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_telegramtrigger_tools() -> List[BaseTool]:
    """Get all telegramTrigger tools."""
    from . import operations
    return operations.get_tools()
