# executeWorkflowTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all executeWorkflowTrigger operation tools."""
    tools = []
    from .default import ExecuteworkflowtriggerDefaultTool
    tools.append(ExecuteworkflowtriggerDefaultTool())
    return tools
