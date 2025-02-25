# discord toolkit
from langchain.tools import BaseTool
from typing import List

def get_discord_tools() -> List[BaseTool]:
    """Get all discord tools."""
    from . import operations
    return operations.get_tools()
