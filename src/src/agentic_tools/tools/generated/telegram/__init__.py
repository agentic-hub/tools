# telegram toolkit
from langchain.tools import BaseTool
from typing import List

def get_telegram_tools() -> List[BaseTool]:
    """Get all telegram tools."""
    from . import operations
    return operations.get_tools()
