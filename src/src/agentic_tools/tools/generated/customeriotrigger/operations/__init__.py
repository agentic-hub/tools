# customerIoTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all customerIoTrigger operation tools."""
    tools = []
    from .default import CustomeriotriggerDefaultTool
    tools.append(CustomeriotriggerDefaultTool())
    return tools
