# totp toolkit
from langchain.tools import BaseTool
from typing import List

def get_totp_tools() -> List[BaseTool]:
    """Get all totp tools."""
    from . import operations
    return operations.get_tools()
