# microsoftOutlook toolkit
from langchain.tools import BaseTool
from typing import List

def get_microsoftoutlook_tools() -> List[BaseTool]:
    """Get all microsoftOutlook tools."""
    from . import operations
    return operations.get_tools()
