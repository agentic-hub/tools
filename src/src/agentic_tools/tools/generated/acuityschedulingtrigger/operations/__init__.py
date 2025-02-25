# acuitySchedulingTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all acuitySchedulingTrigger operation tools."""
    tools = []
    from .default import AcuityschedulingtriggerDefaultTool
    tools.append(AcuityschedulingtriggerDefaultTool())
    return tools
