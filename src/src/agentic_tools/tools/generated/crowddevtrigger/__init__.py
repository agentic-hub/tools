# crowdDevTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_crowddevtrigger_tools() -> List[BaseTool]:
    """Get all crowdDevTrigger tools."""
    from . import operations
    return operations.get_tools()
