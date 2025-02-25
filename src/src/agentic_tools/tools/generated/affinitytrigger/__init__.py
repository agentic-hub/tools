# affinityTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_affinitytrigger_tools() -> List[BaseTool]:
    """Get all affinityTrigger tools."""
    from . import operations
    return operations.get_tools()
