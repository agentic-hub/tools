# renameKeys toolkit
from langchain.tools import BaseTool
from typing import List

def get_renamekeys_tools() -> List[BaseTool]:
    """Get all renameKeys tools."""
    from . import operations
    return operations.get_tools()
