# bitbucketTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_bitbuckettrigger_tools() -> List[BaseTool]:
    """Get all bitbucketTrigger tools."""
    from . import operations
    return operations.get_tools()
