# postHog toolkit
from langchain.tools import BaseTool
from typing import List

def get_posthog_tools() -> List[BaseTool]:
    """Get all postHog tools."""
    from . import operations
    return operations.get_tools()
