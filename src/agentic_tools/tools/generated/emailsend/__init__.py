# emailSend toolkit
from langchain.tools import BaseTool
from typing import List

def get_emailsend_tools() -> List[BaseTool]:
    """Get all emailSend tools."""
    from . import operations
    return operations.get_tools()
