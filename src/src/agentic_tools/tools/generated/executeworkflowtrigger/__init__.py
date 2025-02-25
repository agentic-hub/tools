# executeWorkflowTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_executeworkflowtrigger_tools() -> List[BaseTool]:
    """Get all executeWorkflowTrigger tools."""
    from . import operations
    return operations.get_tools()
