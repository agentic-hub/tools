# oneSimpleApi toolkit
from langchain.tools import BaseTool
from typing import List

def get_onesimpleapi_tools() -> List[BaseTool]:
    """Get all oneSimpleApi tools."""
    from . import operations
    return operations.get_tools()
