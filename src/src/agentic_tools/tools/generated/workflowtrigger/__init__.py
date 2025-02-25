# workflowTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_workflowtrigger_tools() -> List[BaseTool]:
    """Get all workflowTrigger tools."""
    from . import operations
    return operations.get_tools()
