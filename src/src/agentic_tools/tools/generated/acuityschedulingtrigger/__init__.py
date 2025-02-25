# acuitySchedulingTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_acuityschedulingtrigger_tools() -> List[BaseTool]:
    """Get all acuitySchedulingTrigger tools."""
    from . import operations
    return operations.get_tools()
