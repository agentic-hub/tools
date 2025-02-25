# respondToWebhook toolkit
from langchain.tools import BaseTool
from typing import List

def get_respondtowebhook_tools() -> List[BaseTool]:
    """Get all respondToWebhook tools."""
    from . import operations
    return operations.get_tools()
