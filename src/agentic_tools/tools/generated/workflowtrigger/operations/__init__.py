# workflowTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all workflowTrigger operation tools."""
    tools = []
    from .default import WorkflowtriggerDefaultTool
    tools.append(WorkflowtriggerDefaultTool())
    return tools
