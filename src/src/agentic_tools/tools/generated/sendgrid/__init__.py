# sendGrid toolkit
from langchain.tools import BaseTool
from typing import List

def get_sendgrid_tools() -> List[BaseTool]:
    """Get all sendGrid tools."""
    from . import operations
    return operations.get_tools()
