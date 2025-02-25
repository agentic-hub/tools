# mailjet toolkit
from langchain.tools import BaseTool
from typing import List

def get_mailjet_tools() -> List[BaseTool]:
    """Get all mailjet tools."""
    from . import operations
    return operations.get_tools()
