# pipedriveTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_pipedrivetrigger_tools() -> List[BaseTool]:
    """Get all pipedriveTrigger tools."""
    from . import operations
    return operations.get_tools()
