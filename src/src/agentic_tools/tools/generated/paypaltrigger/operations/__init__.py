# payPalTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all payPalTrigger operation tools."""
    tools = []
    from .default import PaypaltriggerDefaultTool
    tools.append(PaypaltriggerDefaultTool())
    return tools
