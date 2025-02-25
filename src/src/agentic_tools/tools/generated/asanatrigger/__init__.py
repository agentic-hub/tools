# asanaTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_asanatrigger_tools() -> List[BaseTool]:
    """Get all asanaTrigger tools."""
    from . import operations
    return operations.get_tools()
